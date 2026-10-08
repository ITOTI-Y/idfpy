"""Build the versioned documentation site, one copy per EnergyPlus release.

Guides, API pages and site configuration come from the current checkout.
Each ``release/ep-X.Y.Z`` branch only contributes its generated
``idfpy`` package, from which the object reference of that version is built.
The result is a static tree for GitHub Pages::

    <out>/26.2/   <out>/26.1/   ...   <out>/latest/   <out>/versions.json
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Any, Final

import typer
import yaml

ROOT: Final = Path(__file__).resolve().parents[2]
REFERENCE_DIR: Final = ROOT / 'docs' / 'reference'
BUILD_CONFIG: Final = ROOT / '.zensical-build.yml'
REFERENCE_SECTION: Final = 'Object reference'

app = typer.Typer(add_completion=False)


@dataclass(frozen=True)
class Release:
    ref: str
    ep_version: str

    @property
    def short(self) -> str:
        return '.'.join(self.ep_version.split('.')[:2])

    @property
    def key(self) -> tuple[int, ...]:
        return tuple(int(part) for part in self.ep_version.split('.'))


def git(*args: str) -> bytes:
    return subprocess.run(
        ['git', *args], cwd=ROOT, check=True, capture_output=True
    ).stdout


def find_releases(remote: str) -> list[Release]:
    refs = git(
        'for-each-ref',
        '--format=%(refname:short)',
        f'refs/remotes/{remote}/release/ep-*',
    ).decode()
    releases = [
        Release(ref, match.group(1))
        for ref in refs.split()
        if (match := re.fullmatch(rf'{remote}/release/ep-(\d+\.\d+\.\d+)', ref))
    ]
    return sorted(releases, key=lambda r: r.key, reverse=True)


def extract_package(release: Release, dest: Path) -> str:
    """Extract the release's ``idfpy`` package and return its idfpy version."""
    archive = git('archive', '--format=tar', release.ref, 'idfpy')
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(dest, filter='data')
    pyproject = tomllib.loads(git('show', f'{release.ref}:pyproject.toml').decode())
    return pyproject['project']['version']


def site_config(base_url: str, release: Release) -> dict[str, Any]:
    with (ROOT / 'zensical.toml').open('rb') as f:
        project = tomllib.load(f)['project']
    project['site_url'] = f'{base_url.rstrip("/")}/{release.short}/'

    pages = []
    for page in sorted(REFERENCE_DIR.glob('*.md')):
        if page.name == 'index.md':
            continue
        lines = page.read_text(encoding='utf-8').splitlines()
        title = next(line for line in lines if line.startswith('# ')).removeprefix('# ')
        pages.append((title, f'reference/{page.name}'))
    section = next(entry for entry in project['nav'] if REFERENCE_SECTION in entry)
    section[REFERENCE_SECTION] = ['reference/index.md'] + [
        {title: path} for title, path in sorted(pages)
    ]
    return project


def build_release(release: Release, schema: Path, base_url: str, dest: Path) -> None:
    with tempfile.TemporaryDirectory(prefix='idfpy-docs-') as tmp:
        idfpy_version = extract_package(release, Path(tmp))
        subprocess.run(
            [
                sys.executable,
                str(ROOT / 'scripts' / 'docs' / 'gen_reference.py'),
                '--schema',
                str(schema),
                '--ep-version',
                release.short,
                '--idfpy-version',
                idfpy_version,
                '--out',
                str(REFERENCE_DIR),
            ],
            cwd=ROOT,
            check=True,
            env={**os.environ, 'PYTHONPATH': tmp},
        )

    BUILD_CONFIG.write_text(
        yaml.safe_dump(site_config(base_url, release), sort_keys=False),
        encoding='utf-8',
    )
    try:
        subprocess.run(
            [
                sys.executable,
                '-m',
                'zensical',
                'build',
                '--clean',
                '-f',
                str(BUILD_CONFIG),
            ],
            cwd=ROOT,
            check=True,
        )
    finally:
        BUILD_CONFIG.unlink()
    shutil.move(ROOT / 'site', dest)


def redirect_page(target: str) -> str:
    return (
        '<!doctype html><meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0; url={target}">'
        f'<link rel="canonical" href="{target}">'
        f'<a href="{target}">Redirecting to {target}</a>'
    )


@app.command()
def main(
    schema_pattern: Annotated[
        str,
        typer.Option(
            help='Schema path with a {version} placeholder, e.g. schemas/{version}/Energy+.schema.epJSON'
        ),
    ],
    versions: Annotated[
        list[str] | None,
        typer.Option(
            '--version',
            help='EnergyPlus version to build, e.g. 26.2.0; repeatable. Default: every release branch',
        ),
    ] = None,
    out: Annotated[
        Path, typer.Option(help='Output directory, replaced on each run')
    ] = ROOT / '_site',
    base_url: Annotated[
        str, typer.Option(help='Public URL of the site root')
    ] = 'https://itoti-y.github.io/idfpy/',
    remote: Annotated[
        str, typer.Option(help='Git remote holding the release branches')
    ] = 'origin',
) -> None:
    """Build every requested EnergyPlus version and the version switcher data."""
    releases = find_releases(remote)
    if versions:
        missing = set(versions) - {r.ep_version for r in releases}
        if missing:
            raise typer.BadParameter(f'no release branch for {sorted(missing)}')
        releases = [r for r in releases if r.ep_version in versions]
    # Sites are keyed by major.minor, so an EnergyPlus patch branch such as
    # release/ep-26.2.1 supersedes release/ep-26.2.0 instead of colliding.
    newest_per_line = {r.short: r for r in sorted(releases, key=lambda r: r.key)}
    releases = sorted(newest_per_line.values(), key=lambda r: r.key, reverse=True)
    if not releases:
        raise typer.BadParameter(
            f'no {remote}/release/ep-* branches found; run git fetch'
        )

    schemas = {r: Path(schema_pattern.format(version=r.ep_version)) for r in releases}
    if absent := [str(path) for path in schemas.values() if not path.is_file()]:
        raise typer.BadParameter(f'schema files not found: {absent}')

    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    for release in releases:
        typer.echo(f'== EnergyPlus {release.ep_version} from {release.ref}')
        build_release(release, schemas[release], base_url, out / release.short)

    newest = releases[0].short
    shutil.copytree(out / newest, out / 'latest')
    versions_json = [
        {
            'version': r.short,
            'title': f'EnergyPlus {r.short}',
            'aliases': ['latest'] if r.short == newest else [],
        }
        for r in releases
    ]
    (out / 'versions.json').write_text(
        json.dumps(versions_json, indent=2), encoding='utf-8'
    )
    (out / 'index.html').write_text(redirect_page(f'{newest}/'), encoding='utf-8')
    typer.echo(f'Site with {len(releases)} versions written to {out}')


if __name__ == '__main__':
    app()
