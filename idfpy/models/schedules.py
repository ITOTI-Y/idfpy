"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Schedules
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    DayScheduleNamesRef,
    ScheduleTypeLimitsNamesRef,
    WeekScheduleNamesRef,
)


class ScheduleCompactDataItem(IDFBaseModel):
    """Nested object type for array items."""
    field: float | str | None = Field(default=None)


class ScheduleDayIntervalDataItem(IDFBaseModel):
    """Nested object type for array items."""
    time: str | None = Field(default=None, json_schema_extra={'units': 'hh:mm', 'note': '"until" includes the time entered.'})
    value_until_time: float | None = Field(default=None)


class ScheduleDayListExtensionsItem(IDFBaseModel):
    """Nested object type for array items."""
    value: float | None = Field(default=0.0)


class ScheduleWeekCompactDataItem(IDFBaseModel):
    """Nested object type for array items."""
    daytype_list: str = Field(..., json_schema_extra={'note': '"For" is an optional prefix/start of the For fields. Choices can be combined on single line if separated by spaces. i.e. "Holiday Weekends" Should have a space after For, if it is included. i.e. "F...'})
    schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})


class ScheduleYearScheduleWeeksItem(IDFBaseModel):
    """Nested object type for array items."""
    schedule_week_name: WeekScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['WeekScheduleNames']})
    start_month: int = Field(..., ge=1, le=12)
    start_day: int = Field(..., ge=1, le=31)
    end_month: int = Field(..., ge=1, le=12)
    end_day: int = Field(..., ge=1, le=31)



class ScheduleCompact(IDFBaseModel):
    """Irregular object. Does not follow the usual definition for fields. Fields
A3... are: Through: Date For: Applicable days (ref: Schedule:Week:Compact)
Interpolate: Average/Linear/No (ref: Schedule:Day:Interval) -- optional, if
not used will be \"No\" Until: <Time> (ref: Schedule:Day:Interval) <numeric
value> words \"Through\",\"For\",\"Interpolate\",\"Until\" must be included."""

    _idf_object_type: ClassVar[str] = "Schedule:Compact"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    data: list[ScheduleCompactDataItem] | None = Field(default=None)


class ScheduleConstant(IDFBaseModel):
    """Constant hourly value for entire year."""

    _idf_object_type: ClassVar[str] = "Schedule:Constant"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    hourly_value: float | None = Field(default=0.0)


class ScheduleDayHourly(IDFBaseModel):
    """A Schedule:Day:Hourly contains 24 values for each hour of the day."""

    _idf_object_type: ClassVar[str] = "Schedule:Day:Hourly"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    hour_1: float | None = Field(default=0.0)
    hour_2: float | None = Field(default=0.0)
    hour_3: float | None = Field(default=0.0)
    hour_4: float | None = Field(default=0.0)
    hour_5: float | None = Field(default=0.0)
    hour_6: float | None = Field(default=0.0)
    hour_7: float | None = Field(default=0.0)
    hour_8: float | None = Field(default=0.0)
    hour_9: float | None = Field(default=0.0)
    hour_10: float | None = Field(default=0.0)
    hour_11: float | None = Field(default=0.0)
    hour_12: float | None = Field(default=0.0)
    hour_13: float | None = Field(default=0.0)
    hour_14: float | None = Field(default=0.0)
    hour_15: float | None = Field(default=0.0)
    hour_16: float | None = Field(default=0.0)
    hour_17: float | None = Field(default=0.0)
    hour_18: float | None = Field(default=0.0)
    hour_19: float | None = Field(default=0.0)
    hour_20: float | None = Field(default=0.0)
    hour_21: float | None = Field(default=0.0)
    hour_22: float | None = Field(default=0.0)
    hour_23: float | None = Field(default=0.0)
    hour_24: float | None = Field(default=0.0)


class ScheduleDayInterval(IDFBaseModel):
    """A Schedule:Day:Interval contains a full day of values with specified end
times for each value Currently, is set up to allow for 10 minute intervals
for an entire day."""

    _idf_object_type: ClassVar[str] = "Schedule:Day:Interval"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    interpolate_to_timestep: Literal['', 'Average', 'Linear', 'No'] | None = Field(default='No', json_schema_extra={'note': 'when the interval does not match the user specified timestep a Average choice will average between the intervals request (to timestep resolution. A No choice will use the interval value at the simu...'})
    data: list[ScheduleDayIntervalDataItem] | None = Field(default=None)


class ScheduleDayList(IDFBaseModel):
    """Schedule:Day:List will allow the user to list 24 hours worth of values,
which can be sub-hourly in nature."""

    _idf_object_type: ClassVar[str] = "Schedule:Day:List"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    interpolate_to_timestep: Literal['', 'Average', 'Linear', 'No'] | None = Field(default='No', json_schema_extra={'note': 'when the interval does not match the user specified timestep a "Average" choice will average between the intervals request (to timestep resolution. A "No" choice will use the interval value at the ...'})
    minutes_per_item: int | None = Field(default=None, ge=1, le=60, json_schema_extra={'note': 'Must be evenly divisible into 60'})
    extensions: list[ScheduleDayListExtensionsItem] | None = Field(default=None)


class ScheduleFile(IDFBaseModel):
    """A Schedule:File points to a text computer file that has 8760-8784 hours of
data."""

    _idf_object_type: ClassVar[str] = "Schedule:File"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    file_name: str = Field(...)
    column_number: int = Field(..., ge=1)
    rows_to_skip_at_top: int = Field(..., ge=0)
    number_of_hours_of_data: float | None = Field(default=8760.0, ge=8760.0, le=8784.0, json_schema_extra={'note': '8760 hours does not account for leap years, 8784 does. should be either 8760 or 8784'})
    column_separator: Literal['', 'Comma', 'Semicolon', 'Space', 'Tab'] | None = Field(default='Comma')
    interpolate_to_timestep: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to timestep resolution. a "No" choice will use the interval value at the simu...'})
    minutes_per_item: int | None = Field(default=60, ge=1, le=60, json_schema_extra={'note': 'Must be evenly divisible into 60'})
    adjust_schedule_for_daylight_savings: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': '"No" means do not include Daylight Savings Time in the schedule, instead, use the schedule directly from the Schedule:File csv (default) "Yes" means include Daylight Savings Time to the schedule'})


class ScheduleFileShading(IDFBaseModel):
    """A Schedule:File:Shading points to a CSV file that has 8760-8784 hours of
sunlit fraction data for all or some of the exterior surfaces."""

    _idf_object_type: ClassVar[str] = "Schedule:File:Shading"
    file_name: str = Field(..., json_schema_extra={'note': 'The name of the file that writes all shading data.'})


class ScheduleTypeLimits(IDFBaseModel):
    """ScheduleTypeLimits specifies the data types and limits for the values
contained in schedules"""

    _idf_object_type: ClassVar[str] = "ScheduleTypeLimits"
    name: str = Field(..., json_schema_extra={'note': 'used to validate schedule types in various schedule objects'})
    lower_limit_value: float | None = Field(default=None, json_schema_extra={'note': 'lower limit (real or integer) for the Schedule Type. e.g. if fraction, this is 0.0'})
    upper_limit_value: float | None = Field(default=None, json_schema_extra={'note': 'upper limit (real or integer) for the Schedule Type. e.g. if fraction, this is 1.0'})
    numeric_type: Literal['Continuous', 'Discrete'] | None = Field(default=None, json_schema_extra={'note': 'Numeric type is either Continuous (all numbers within the min and max are valid or Discrete (only integer numbers between min and max are valid. (Could also allow REAL and INTEGER to mean the same ...'})
    unit_type: Literal['', 'ActivityLevel', 'Angle', 'Availability', 'Capacity', 'Control', 'ConvectionCoefficient', 'DeltaTemperature', 'Dimensionless', 'Mode', 'Percent', 'Power', 'PrecipitationRate', 'Temperature', 'Velocity'] | None = Field(default='Dimensionless', json_schema_extra={'note': 'Temperature (C or F) DeltaTemperature (C or F) PrecipitationRate (m/hr or ft/hr) Angle (degrees) Convection Coefficient (W/m2-K or Btu/sqft-hr-F) Activity Level (W/person) Velocity (m/s or ft/min) ...'})


class ScheduleWeekCompact(IDFBaseModel):
    """Compact definition for Schedule:Day:List"""

    _idf_object_type: ClassVar[str] = "Schedule:Week:Compact"
    name: str = Field(...)
    data: list[ScheduleWeekCompactDataItem] | None = Field(default=None)


class ScheduleWeekDaily(IDFBaseModel):
    """A Schedule:Week:Daily contains 12 Schedule:Day:Hourly objects, one for each
day type."""

    _idf_object_type: ClassVar[str] = "Schedule:Week:Daily"
    name: str = Field(...)
    sunday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    monday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    tuesday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    wednesday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    thursday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    friday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    saturday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    holiday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    summerdesignday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    winterdesignday_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    customday1_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})
    customday2_schedule_day_name: DayScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['DayScheduleNames']})


class ScheduleYear(IDFBaseModel):
    """A Schedule:Year contains from 1 to 52 week schedules"""

    _idf_object_type: ClassVar[str] = "Schedule:Year"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    schedule_weeks: list[ScheduleYearScheduleWeeksItem] | None = Field(default=None)

