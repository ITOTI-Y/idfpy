"""idfpy command-line interface."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from typer import Option, Typer

app = Typer(name='idfpy', help='EnergyPlus IDF toolkit')


@app.command()
def codegen(
    schema: Annotated[
        Path, Option('--schema', '-s', help='Path to Energy+.schema.epJSON')
    ],
    output: Annotated[
        Path, Option('--output', '-o', help='Output directory for generated models')
    ] = Path('idfpy/models'),
) -> None:
    """Generate Pydantic models from EnergyPlus schema."""
    from idfpy.codegen import ModelGenerator, SchemaParser

    parser = SchemaParser(schema_path=schema)
    specs = parser.parse()
    schema_version = parser.get_version()
    generator = ModelGenerator(output_dir=output)
    generator.generate_all(specs, schema_version=schema_version)


@app.command()
def run(
    idf: Annotated[Path, Option('--idf', '-i', help='Path to IDF file')],
    weather: Annotated[
        Path, Option('--weather', '-w', help='Path to EPW weather file')
    ],
    output: Annotated[
        Path | None, Option('--output', '-o', help='Output directory')
    ] = None,
) -> None:
    """Run EnergyPlus simulation."""
    from idfpy.sim import simulate

    result = simulate(idf, weather=weather, output_dir=output)
    raise SystemExit(result.return_code)
