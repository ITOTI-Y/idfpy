"""Type checking fixture — verified by ty/pyright"""

from idfpy.models import Building, RunPeriod, Zone, get_model_class

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
