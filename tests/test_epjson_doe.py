"""Test epJSON conversion with DOE reference building IDF files.

Uses ASHRAE901_OfficeMedium_STD2019_Denver.idf as a complex real-world test case.
Validates: load IDF → save epJSON → load epJSON → run EnergyPlus simulation.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from idfpy import IDF

EP_DIR = Path('/usr/local/EnergyPlus-25-1-0')
DOE_IDF = EP_DIR / 'ExampleFiles' / 'ASHRAE901_OfficeMedium_STD2019_Denver.idf'
WEATHER = EP_DIR / 'WeatherData' / 'USA_CO_Golden-NREL.724666_TMY3.epw'


@pytest.fixture
def doe_idf() -> IDF:
    return IDF.load(DOE_IDF)


@pytest.mark.skipif(not DOE_IDF.exists(), reason='DOE IDF file not found')
class TestDOEepJSON:
    def test_load_doe_idf(self, doe_idf: IDF):
        """DOE IDF should load with a significant number of objects."""
        assert len(doe_idf) > 100
        assert doe_idf.has('Building', 'OfficeMedium')
        # Should have zones, surfaces, HVAC components
        zones = doe_idf.all_of_type('Zone')
        assert len(zones) > 0
        print(f'Loaded {len(doe_idf)} objects, {len(zones)} zones')

    def test_to_dict_structure(self, doe_idf: IDF):
        """to_dict should produce valid epJSON structure."""
        d = doe_idf.to_dict()

        assert isinstance(d, dict)
        assert 'Building' in d
        assert 'OfficeMedium' in d['Building']

        # Verify name is not in fields
        for obj_type, objects in d.items():
            for obj_name, fields in objects.items():
                assert 'name' not in fields, (
                    f"{obj_type}/{obj_name} still has 'name' in fields"
                )

        # Verify extensible fields (surfaces with vertices)
        if 'BuildingSurface:Detailed' in d:
            for _surf_name, surf_fields in d['BuildingSurface:Detailed'].items():
                if 'vertices' in surf_fields:
                    verts = surf_fields['vertices']
                    assert isinstance(verts, list)
                    assert len(verts) > 0
                    assert 'vertex_x_coordinate' in verts[0]
                    break

    def test_epjson_roundtrip_object_count(self, doe_idf: IDF):
        """Roundtrip through to_dict/from_dict should preserve object count."""
        d = doe_idf.to_dict()
        loaded = IDF.from_dict(d)

        original_count = len(doe_idf)
        roundtrip_count = len(loaded)
        print(f'Original: {original_count}, Roundtrip: {roundtrip_count}')
        assert roundtrip_count == original_count

    def test_epjson_save_load_file(self, doe_idf: IDF, tmp_path: Path):
        """Save as .epjson file, load back, verify object count."""
        epjson_path = tmp_path / 'OfficeMedium.epjson'
        doe_idf.save(epjson_path, output_type='epjson')

        assert epjson_path.exists()
        data = json.loads(epjson_path.read_text())
        assert 'Building' in data

        loaded = IDF.load(epjson_path)
        assert len(loaded) == len(doe_idf)
        assert loaded.has('Building', 'OfficeMedium')

    def test_epjson_field_values_preserved(self, doe_idf: IDF):
        """Key field values should survive roundtrip."""
        d = doe_idf.to_dict()
        loaded = IDF.from_dict(d)

        # Building fields
        orig_building = doe_idf.get('Building', 'OfficeMedium')
        rt_building = loaded.get('Building', 'OfficeMedium')
        assert rt_building is not None
        assert orig_building.north_axis == rt_building.north_axis  # ty: ignore[unresolved-attribute]
        assert orig_building.terrain == rt_building.terrain  # ty: ignore[unresolved-attribute]

        # Zone fields
        orig_zones = doe_idf.all_of_type('Zone')
        rt_zones = loaded.all_of_type('Zone')
        for name in orig_zones:
            assert name in rt_zones, f"Zone '{name}' missing after roundtrip"

    @pytest.mark.skipif(not WEATHER.exists(), reason='Weather file not found')
    def test_epjson_simulation(self, doe_idf: IDF, tmp_path: Path):
        """Run EnergyPlus simulation with converted epJSON file."""
        epjson_path = tmp_path / 'OfficeMedium.epjson'
        doe_idf.save(epjson_path, output_type='epjson')

        output_dir = tmp_path / 'output'
        output_dir.mkdir()

        result = subprocess.run(
            [
                'energyplus',
                '-w',
                str(WEATHER),
                '-d',
                str(output_dir),
                str(epjson_path),
            ],
            capture_output=True,
            text=True,
            timeout=600,
        )

        # Print output for debugging
        if result.returncode != 0:
            print('=== STDOUT ===')
            print(result.stdout[-3000:] if len(result.stdout)
                  > 3000 else result.stdout)
            print('=== STDERR ===')
            print(result.stderr[-3000:] if len(result.stderr)
                  > 3000 else result.stderr)

            # Check error file for details
            err_file = output_dir / 'eplusout.err'
            if err_file.exists():
                print('=== eplusout.err (last 50 lines) ===')
                lines = err_file.read_text().splitlines()
                print('\n'.join(lines[-50:]))

        assert result.returncode == 0, (
            f'EnergyPlus failed with code {result.returncode}'
        )

        # Verify key output files exist
        assert (output_dir / 'eplusout.end').exists()
        end_content = (output_dir / 'eplusout.end').read_text()
        assert 'EnergyPlus Completed Successfully' in end_content
