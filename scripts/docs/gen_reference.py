"""Generate the EnergyPlus object reference pages of the documentation site.

Run this script with the target release branch's ``idfpy`` package first on
``PYTHONPATH``. The epJSON schema supplies IDD field names and untruncated
notes; the runtime registries of that package supply the module grouping and
the cross-object references, so every page matches the models users install.
"""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path
from typing import Annotated, Any, Final

import typer

import idfpy.models
from idfpy.codegen import SchemaParser
from idfpy.codegen.field_parser import _UNSET, FieldSpec
from idfpy.codegen.schema_parser import ObjectSpec
from idfpy.models import CLASS_NAME_REGISTRY
from idfpy.models._ref_meta import REF_CONSUMERS, REF_GROUP_PROVIDERS
from idfpy.models.simulation import Version

IO_REFERENCE_URL: Final = 'https://bigladdersoftware.com/epx/docs/'
MAX_TARGET_LINKS: Final = 12
SUMMARY_LENGTH: Final = 110

app = typer.Typer(add_completion=False)


def anchor(object_type: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', object_type.lower()).strip('-')


def cell(text: object) -> str:
    """Escape free text from the schema for a single Markdown table cell."""
    escaped = (
        str(text)
        .replace('\\', '\\\\')
        .replace('|', '\\|')
        .replace('*', '\\*')
        .replace('[', '\\[')
        .replace(']', '\\]')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
    )
    return ' '.join(escaped.split())


def code(value: object) -> str:
    return f'`{str(value).replace("`", "")}`'


def first_sentence(text: str | None) -> str:
    if not text:
        return ''
    flat = ' '.join(text.split())
    sentence = re.split(r'(?<=[.!?])\s', flat, maxsplit=1)[0]
    if len(sentence) > SUMMARY_LENGTH:
        sentence = sentence[:SUMMARY_LENGTH].rsplit(' ', 1)[0] + ' …'
    return cell(sentence)


def owner_object_type(class_name: str) -> str | None:
    """Map a model or nested item class name to its EnergyPlus object type."""
    if class_name in CLASS_NAME_REGISTRY:
        return CLASS_NAME_REGISTRY[class_name]
    owners = [name for name in CLASS_NAME_REGISTRY if class_name.startswith(name)]
    return CLASS_NAME_REGISTRY[max(owners, key=len)] if owners else None


class Reference:
    """Cross-page links between object types of one EnergyPlus version."""

    def __init__(self, specs: dict[str, ObjectSpec]) -> None:
        self.page_of = {
            name: getattr(idfpy.models, spec.class_name).__module__.rpartition('.')[2]
            for name, spec in specs.items()
        }
        self.consumers: dict[str, set[str]] = defaultdict(set)
        for class_name, fields in REF_CONSUMERS.items():
            consumer = owner_object_type(class_name)
            if consumer is None:
                continue
            for groups in fields.values():
                for group in groups:
                    self.consumers[group].add(consumer)

    def link(self, object_type: str, from_page: str) -> str:
        page = self.page_of.get(object_type)
        if page is None:
            return code(object_type)
        target = '' if page == from_page else f'{page}.md'
        return f'[{object_type}]({target}#{anchor(object_type)})'

    def links(self, object_types: Iterable[str], from_page: str) -> str:
        ordered = sorted(object_types)
        shown = ', '.join(self.link(t, from_page) for t in ordered[:MAX_TARGET_LINKS])
        hidden = len(ordered) - MAX_TARGET_LINKS
        return f'{shown} and {hidden} more' if hidden > 0 else shown


def field_type(spec: FieldSpec) -> str:
    if spec.enum_values:
        return 'choice'
    if spec.object_list:
        return 'reference'
    if spec.anyof_specs:
        kinds = [
            ' or '.join(code(v) for v in alt.enum_values if v != '')
            if alt.enum_values
            else alt.field_type
            for alt in spec.anyof_specs
        ]
        return ' or '.join(k for k in kinds if k)
    if spec.field_type == 'array':
        return 'list'
    return spec.field_type


def value_range(spec: FieldSpec) -> str:
    bounds = [
        (spec.minimum, '≥'),
        (spec.exclusive_minimum, '>'),
        (spec.maximum, '≤'),
        (spec.exclusive_maximum, '<'),
    ]
    return ', '.join(f'{op} {value:g}' for value, op in bounds if value is not None)


def field_details(spec: FieldSpec, ref: Reference, page: str) -> str:
    parts: list[str] = []
    if spec.note:
        parts.append(cell(spec.note))
    if spec.enum_values:
        parts.append('One of ' + ', '.join(code(v) for v in spec.enum_values if v))
    if spec.object_list:
        targets = {
            t for group in spec.object_list for t in REF_GROUP_PROVIDERS.get(group, ())
        }
        parts.append('Names a ' + ref.links(targets, page))
    if bounds := value_range(spec):
        parts.append(f'Range: {bounds}')
    if spec.items_spec and spec.items_spec.nested_fields:
        items = ', '.join(
            code(item.python_name) + (f' ({cell(item.units)})' if item.units else '')
            for item in spec.items_spec.nested_fields
        )
        parts.append(f'Each item: {items}')
    return '<br>'.join(parts)


def field_rows(
    obj: ObjectSpec, idd_names: dict[str, Any], ref: Reference, page: str
) -> list[str]:
    rows = [
        '| Field | Type | Default | Details |',
        '|---|---|---|---|',
    ]
    for spec in obj.fields:
        # <wbr> lets long snake_case names wrap at underscores in narrow tables.
        label = f'<code>{spec.python_name.replace("_", "_<wbr>")}</code>'
        idd_name = idd_names.get(spec.name, {}).get('field_name')
        if idd_name:
            label += f'<br><span class="idf-idd">{cell(idd_name)}</span>'
        if spec.required:
            label += ' <span class="idf-req">required</span>'
        kind = field_type(spec)
        if spec.units:
            kind += f'<br><span class="idf-unit">{cell(spec.units)}</span>'
        default = '' if spec.default is _UNSET else code(spec.default)
        rows.append(
            f'| {label} | {kind} | {default} | {field_details(spec, ref, page)} |'
        )
    return rows


def object_section(
    obj: ObjectSpec, raw: dict[str, Any], ref: Reference, page: str
) -> list[str]:
    badges = []
    if obj.is_singleton:
        badges.append('<span class="idf-badge">unique</span>')
    if obj.extensible_size:
        badges.append('<span class="idf-badge">extensible</span>')
    lines = [
        f'## {obj.name} {{ #{anchor(obj.name)} }}',
        '',
        f'`from idfpy.models import {obj.class_name}` {" ".join(badges)}'.rstrip(),
        '',
    ]
    if obj.memo:
        lines += [cell(obj.memo), '']
    idd_names = raw[obj.name].get('legacy_idd', {}).get('field_info', {})
    lines += [*field_rows(obj, idd_names, ref, page), '']

    provided = {group for spec in obj.fields for group in (spec.reference or [])}
    users = {t for group in provided for t in ref.consumers.get(group, ())}
    if users:
        lines += [
            f'??? info "Referenced by {len(users)} object types"',
            '',
            '    ' + ', '.join(ref.link(t, page) for t in sorted(users)),
            '',
        ]
    return lines


def page_title(objects: list[ObjectSpec], module: str) -> str:
    groups = {obj.group for obj in objects}
    if len(groups) == 1:
        return groups.pop()
    return 'Miscellaneous' if module == 'misc' else module.replace('_', ' ').title()


def render_page(
    module: str,
    objects: list[ObjectSpec],
    raw: dict[str, Any],
    ref: Reference,
    ep_version: str,
) -> str:
    title = page_title(objects, module)
    groups = sorted({obj.group for obj in objects})
    # The summary table replaces the right-hand table of contents, which leaves
    # the field tables the full content width.
    lines = [
        '---',
        'hide:',
        '  - toc',
        '---',
        '',
        f'# {title}',
        '',
        f'{len(objects)} object types from `idfpy.models.{module}` · EnergyPlus {ep_version}'
        + (f' · groups: {", ".join(groups)}' if len(groups) > 1 else ''),
        '',
        '| Object | Summary |',
        '|---|---|',
        *(
            f'| [{obj.name}](#{anchor(obj.name)}) | {first_sentence(obj.memo)} |'
            for obj in objects
        ),
        '',
    ]
    for obj in objects:
        lines += object_section(obj, raw, ref, module)
    return '\n'.join(lines)


def render_index(
    pages: list[tuple[str, str, list[ObjectSpec]]], ep_version: str, idfpy_version: str
) -> str:
    total = sum(len(objects) for _, _, objects in pages)
    lines = [
        '# Object reference',
        '',
        f'All {total} EnergyPlus {ep_version} object types modelled by '
        f'idfpy {idfpy_version}, grouped as in `idfpy.models`.',
        '',
        '!!! tip "Reading the tables"',
        '',
        '    The **Field** column shows the Python attribute name with the original '
        'IDD field name below it; **Type** shows units below the type. Values you '
        'assign are validated against the **Type** and **Details** columns. For the full engineering '
        'description of each field see the official EnergyPlus '
        f'[Input Output Reference]({IO_REFERENCE_URL}).',
        '',
        '| Page | Object types |',
        '|---|---|',
        *(
            f'| [{title}]({module}.md) | {len(objects)} |'
            for module, title, objects in pages
        ),
        '',
    ]
    return '\n'.join(lines)


@app.command()
def main(
    schema: Annotated[
        Path, typer.Option(help='Energy+.schema.epJSON of the target version')
    ],
    ep_version: Annotated[str, typer.Option(help='EnergyPlus version, e.g. 26.2')],
    idfpy_version: Annotated[
        str, typer.Option(help='idfpy release built from the branch')
    ],
    out: Annotated[Path, typer.Option(help='Output directory, replaced on each run')],
) -> None:
    """Write one Markdown page per idfpy.models module plus an index page."""
    model_version = Version.model_fields['version_identifier'].default
    if model_version != ep_version:
        raise typer.BadParameter(
            f'idfpy on PYTHONPATH models EnergyPlus {model_version}, not {ep_version}'
        )

    specs = SchemaParser(schema_path=schema).parse()
    raw = json.loads(schema.read_text(encoding='utf-8'))['properties']
    ref = Reference(specs)

    by_module: dict[str, list[ObjectSpec]] = defaultdict(list)
    for name in sorted(specs):
        by_module[ref.page_of[name]].append(specs[name])

    pages = sorted(
        (
            (module, page_title(objects, module), objects)
            for module, objects in by_module.items()
        ),
        key=lambda page: page[1],
    )
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    for module, _, objects in pages:
        (out / f'{module}.md').write_text(
            render_page(module, objects, raw, ref, ep_version), encoding='utf-8'
        )
    (out / 'index.md').write_text(
        render_index(pages, ep_version, idfpy_version), encoding='utf-8'
    )
    typer.echo(
        f'EnergyPlus {ep_version}: {len(specs)} objects on {len(pages)} pages -> {out}'
    )


if __name__ == '__main__':
    app()
