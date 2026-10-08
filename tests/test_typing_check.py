"""Type checking fixture — verified by ty/pyright"""

from typing import assert_type

from idfpy.models import (
    Building,
    Construction,
    Lights,
    Material,
    RunPeriod,
    Zone,
    get_model_class,
)
from idfpy.models._ref_targets import MaterialNameTarget, ScheduleNamesTarget

b: Building = Building()
z: Zone = Zone(name='Z1')
rp: RunPeriod = RunPeriod(
    name='Annual',
    begin_month=1,
    begin_day_of_month=1,
    end_month=12,
    end_day_of_month=31,
)
cls = get_model_class('Zone')


def _nav_targets(construction: Construction, lights: Lights) -> None:
    """Navigation properties keep concrete types beyond five target classes."""
    layers = construction.layers
    assert_type(layers, list[MaterialNameTarget])
    if isinstance(layers[0], Material):
        assert_type(layers[0].thickness, float)
    assert_type(lights.schedule, ScheduleNamesTarget | None)
