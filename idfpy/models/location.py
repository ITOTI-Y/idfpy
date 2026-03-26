"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Location and Climate
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    DayScheduleNamesRef,
    MaterialNameRef,
    OSCMNamesRef,
    RunPeriodsAndDesignDaysRef,
    ScheduleNamesRef,
    SpectrumDataNamesRef,
    UndisturbedGroundTempModelsRef,
)


class SiteSpectrumDataExtensionsItem(IDFBaseModel):
    """Nested object type for array items."""

    wavelength: float | None = Field(
        default=None, json_schema_extra={'units': 'micron'}
    )
    spectrum: float | None = Field(default=None)


class RoofIrrigation(IDFBaseModel):
    """Used to describe the amount of irrigation on the ecoroof surface over the
    course of the simulation runperiod."""

    _idf_object_type: ClassVar[str] = 'RoofIrrigation'
    irrigation_model_type: Literal['Schedule', 'SmartSchedule'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'SmartSchedule will not allow irrigation when soil is already moist. Current threshold set at 30% of saturation.'
        },
    )
    irrigation_rate_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values in meters of water per hour values should be non-negative',
        },
    )
    irrigation_maximum_saturation_threshold: float | None = Field(
        default=40.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Used with SmartSchedule to set the saturation level at which no irrigation is allowed.',
        },
    )


class RunPeriod(IDFBaseModel):
    """Specify a range of dates and other parameters for a simulation. Multiple run
    periods may be input, but they may not overlap."""

    _idf_object_type: ClassVar[str] = 'RunPeriod'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'descriptive name (used in reporting mainly) Cannot be not blank and must be unique'
        },
    )
    begin_month: int = Field(..., ge=1, le=12)
    begin_day_of_month: int = Field(..., ge=1, le=31)
    begin_year: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Start year of the simulation, if this field is specified it must agree with the Day of Week for Start Day If this field is blank, the year will be selected to match the weekday, which is Sunday if ...'
        },
    )
    end_month: int = Field(..., ge=1, le=12)
    end_day_of_month: int = Field(..., ge=1, le=31)
    end_year: float | None = Field(
        default=None, json_schema_extra={'note': 'end year of simulation, if specified'}
    )
    day_of_week_for_start_day: (
        Literal[
            'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': '=[Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday]; If no year is input, this field will default to Sunday If a year is input and this field is blank, the correct weekday is determined'
        },
    )
    use_weather_file_holidays_and_special_days: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If yes or blank, use holidays as specified on Weatherfile. If no, do not use the holidays specified on the Weatherfile. Note: You can still specify holidays/special days using the RunPeriodControl:...'
        },
    )
    use_weather_file_daylight_saving_period: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If yes or blank, use daylight saving period as specified on Weatherfile. If no, do not use the daylight saving period as specified on the Weatherfile.'
        },
    )
    apply_weekend_holiday_rule: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'if yes and single day holiday falls on weekend, "holiday" occurs on following Monday'
        },
    )
    use_weather_file_rain_indicators: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes'
    )
    use_weather_file_snow_indicators: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes'
    )
    treat_weather_as_actual: Literal['', 'No', 'Yes'] | None = Field(default='No')
    first_hour_interpolation_starting_values: Literal['', 'Hour1', 'Hour24'] | None = (
        Field(
            default='Hour24',
            json_schema_extra={
                'note': 'When the weather data timestep is longer than the simulation timestep, weather data is interpolated. For the first hour of the simulation, this field specifies which values from the first day of th...'
            },
        )
    )


class RunPeriodControlDaylightSavingTime(IDFBaseModel):
    """This object sets up the daylight saving time period for any RunPeriod.
    Ignores any daylight saving time period on the weather file and uses this
    definition. These are not used with SizingPeriod:DesignDay objects. Use with
    SizingPeriod:WeatherFileDays object can be controlled in that object."""

    _idf_object_type: ClassVar[str] = 'RunPeriodControl:DaylightSavingTime'
    start_date: str = Field(...)
    end_date: str = Field(
        ...,
        json_schema_extra={
            'note': 'Dates can be several formats: <number>/<number>  (month/day) <number> <Month> <Month> <number> <Nth> <Weekday> in <Month> Last <WeekDay> in <Month> <Month> can be January, February, March, April, M...'
        },
    )


class RunPeriodControlSpecialDays(IDFBaseModel):
    """This object sets up holidays/special days to be used during weather file run
    periods. (These are not used with SizingPeriod:* objects.) Depending on the
    value in the run period, days on the weather file may also be used. However,
    the weather file specification will take precedence over any specification
    shown here. (No error message on duplicate days or overlapping days)."""

    _idf_object_type: ClassVar[str] = 'RunPeriodControl:SpecialDays'
    name: str = Field(...)
    start_date: str = Field(
        ...,
        json_schema_extra={
            'note': 'Dates can be several formats: <number>/<number>  (month/day) <number> <Month> <Month> <number> <Nth> <Weekday> in <Month) Last <WeekDay> in <Month> <Month> can be January, February, March, April, M...'
        },
    )
    duration: float | None = Field(
        default=1.0, ge=1.0, le=366.0, json_schema_extra={'units': 'days'}
    )
    special_day_type: (
        Literal[
            '',
            'CustomDay1',
            'CustomDay2',
            'Holiday',
            'SummerDesignDay',
            'WinterDesignDay',
        ]
        | None
    ) = Field(
        default='Holiday',
        json_schema_extra={
            'note': 'Special Day Type selects the schedules appropriate for each day so labeled'
        },
    )


class SiteGroundDomainBasement(IDFBaseModel):
    """Ground-coupled basement model for simulating basements or other underground
    zones."""

    _idf_object_type: ClassVar[str] = 'Site:GroundDomain:Basement'
    name: str = Field(...)
    ground_domain_depth: float | None = Field(
        default=10.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'The depth from ground surface to the deep ground boundary of the domain.',
        },
    )
    aspect_ratio: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'This defines the height to width ratio of the basement zone.'
        },
    )
    perimeter_offset: float | None = Field(
        default=5.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'The distance from the basement wall edge to the edge of the ground domain',
        },
    )
    soil_thermal_conductivity: float | None = Field(
        default=1.5, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float | None = Field(
        default=2800.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    soil_specific_heat: float | None = Field(
        default=850.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    soil_moisture_content_volume_fraction: float | None = Field(
        default=30.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    soil_moisture_content_volume_fraction_at_saturation: float | None = Field(
        default=50.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    undisturbed_ground_temperature_model_type: Literal[
        'Site:GroundTemperature:Undisturbed:FiniteDifference',
        'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
        'Site:GroundTemperature:Undisturbed:Xing',
    ] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(
        ..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']}
    )
    evapotranspiration_ground_cover_parameter: float | None = Field(
        default=0.4,
        ge=0.0,
        le=1.5,
        json_schema_extra={
            'note': 'This specifies the ground cover effects during evapotranspiration calculations. The value roughly represents the following cases: = 0   : concrete or other solid, non-permeable ground surface mater...'
        },
    )
    basement_floor_boundary_condition_model_name: OSCMNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OSCMNames']}
    )
    horizontal_insulation: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field specifies the presence of insulation beneath the basement floor.'
        },
    )
    horizontal_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    horizontal_insulation_extents: Literal['', 'Full', 'Perimeter'] | None = Field(
        default='Full',
        json_schema_extra={
            'note': 'This field specifies whether the horizontal insulation fully insulates the surface or is perimeter only insulation'
        },
    )
    perimeter_horizontal_insulation_width: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Width of horizontal perimeter insulation measured from foundation wall inside surface.',
        },
    )
    basement_wall_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'Depth measured from ground surface.'},
    )
    basement_wall_boundary_condition_model_name: OSCMNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OSCMNames']}
    )
    vertical_insulation: Literal['', 'No', 'Yes'] | None = Field(default='No')
    basement_wall_vertical_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    vertical_insulation_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Depth measured from the ground surface.',
        },
    )
    simulation_timestep: Literal['', 'Hourly', 'Timestep'] | None = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'This field specifies the basement domain simulation interval.'
        },
    )
    mesh_density_parameter: int | None = Field(default=4, ge=2)


class SiteGroundDomainSlab(IDFBaseModel):
    """Ground-coupled slab model for on-grade and in-grade cases with or without
    insulation."""

    _idf_object_type: ClassVar[str] = 'Site:GroundDomain:Slab'
    name: str = Field(...)
    ground_domain_depth: float | None = Field(
        default=10.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    aspect_ratio: float | None = Field(default=1.0)
    perimeter_offset: float | None = Field(
        default=5.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    soil_thermal_conductivity: float | None = Field(
        default=1.5, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float | None = Field(
        default=2800.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    soil_specific_heat: float | None = Field(
        default=850.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    soil_moisture_content_volume_fraction: float | None = Field(
        default=30.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    soil_moisture_content_volume_fraction_at_saturation: float | None = Field(
        default=50.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    undisturbed_ground_temperature_model_type: Literal[
        'Site:GroundTemperature:Undisturbed:FiniteDifference',
        'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
        'Site:GroundTemperature:Undisturbed:Xing',
    ] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(
        ..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']}
    )
    evapotranspiration_ground_cover_parameter: float | None = Field(
        default=0.4,
        ge=0.0,
        le=1.5,
        json_schema_extra={
            'note': 'This specifies the ground cover effects during evapotranspiration calculations. The value roughly represents the following cases: = 0   : concrete or other solid, non-permeable ground surface mater...'
        },
    )
    slab_boundary_condition_model_name: OSCMNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OSCMNames']}
    )
    slab_location: Literal['InGrade', 'OnGrade'] = Field(
        ...,
        json_schema_extra={
            'note': 'This field specifies whether the slab is located "in-grade" or "on-grade"'
        },
    )
    slab_material_name: MaterialNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MaterialName'],
            'note': 'Only applicable for the in-grade case',
        },
    )
    horizontal_insulation: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field specifies the presence of insulation beneath the slab. Only required for in-grade case.'
        },
    )
    horizontal_insulation_material_name: MaterialNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MaterialName'],
            'note': 'This field specifies the horizontal insulation material.',
        },
    )
    horizontal_insulation_extents: Literal['', 'Full', 'Perimeter'] | None = Field(
        default='Full',
        json_schema_extra={
            'note': 'This field specifies whether the horizontal insulation fully insulates the surface or is perimeter only insulation'
        },
    )
    perimeter_insulation_width: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field specifies the width of the underfloor perimeter insulation',
        },
    )
    vertical_insulation: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field specifies the presence of vertical insulation at the slab edge.'
        },
    )
    vertical_insulation_material_name: MaterialNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MaterialName'],
            'note': 'This field specifies the vertical insulation material.',
        },
    )
    vertical_insulation_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Only used when including vertical insulation This field specifies the depth of the vertical insulation',
        },
    )
    simulation_timestep: Literal['', 'Hourly', 'Timestep'] | None = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'This field specifies the ground domain simulation timestep.'
        },
    )
    geometric_mesh_coefficient: float | None = Field(default=1.6, ge=1.0, le=2.0)
    mesh_density_parameter: int | None = Field(default=6, ge=4)


class SiteGroundReflectance(IDFBaseModel):
    """Specifies the ground reflectance values used to calculate ground reflected
    solar. The ground reflectance can be further modified when snow is on the
    ground by Site:GroundReflectance:SnowModifier."""

    _idf_object_type: ClassVar[str] = 'Site:GroundReflectance'
    january_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    february_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    march_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    april_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    may_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    june_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    july_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    august_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    september_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    october_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    november_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    december_ground_reflectance: float | None = Field(
        default=0.2, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )


class SiteGroundReflectanceSnowModifier(IDFBaseModel):
    """Specifies ground reflectance multipliers when snow resident on the ground.
    These multipliers are applied to the \"normal\" ground reflectances
    specified in Site:GroundReflectance."""

    _idf_object_type: ClassVar[str] = 'Site:GroundReflectance:SnowModifier'
    ground_reflected_solar_modifier: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'note': 'Value for modifying the "normal" ground reflectance when Snow is on ground when calculating the "Ground Reflected Solar Radiation Value" a value of 1.0 here uses the "normal" ground reflectance Gro...'
        },
    )
    daylighting_ground_reflected_solar_modifier: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'note': 'Value for modifying the "normal" daylighting ground reflectance when Snow is on ground when calculating the "Ground Reflected Solar Radiation Value" a value of 1.0 here uses the "normal" ground ref...'
        },
    )


class SiteGroundTemperatureBuildingSurface(IDFBaseModel):
    """These temperatures are specifically for those surfaces that have the outside
    environment of \"Ground\". Documentation about what values these should be
    is located in the Auxiliary programs document (Ground Heat Transfer) as well
    as the InputOutput Reference. CAUTION - Do not use the \"undisturbed\"
    ground temperatures from the weather data. These values are too extreme for
    the soil under a conditioned building. For best results, use the Slab or
    Basement program to calculate custom monthly average ground temperatures
    (see Auxiliary Programs). For typical commercial buildings in the USA, a
    reasonable default value is 2C less than the average indoor space
    temperature."""

    _idf_object_type: ClassVar[str] = 'Site:GroundTemperature:BuildingSurface'
    january_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    february_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    march_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    april_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    may_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    june_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    july_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    august_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    september_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    october_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    november_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )
    december_ground_temperature: float | None = Field(
        default=18.0, json_schema_extra={'units': 'C'}
    )


class SiteGroundTemperatureDeep(IDFBaseModel):
    """These temperatures are specifically for the ground heat exchangers that
    would use \"deep\" (3-4 m depth) ground temperatures for their heat source.
    They are not used in other models."""

    _idf_object_type: ClassVar[str] = 'Site:GroundTemperature:Deep'
    january_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    february_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    march_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    april_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    may_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    june_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    july_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    august_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    september_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    october_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    november_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )
    december_deep_ground_temperature: float | None = Field(
        default=16.0, json_schema_extra={'units': 'C'}
    )


class SiteGroundTemperatureFCfactorMethod(IDFBaseModel):
    """These temperatures are specifically for underground walls and ground floors
    defined with the C-factor and F-factor methods, and should be close to the
    monthly average outdoor air temperature delayed by 3 months for the
    location."""

    _idf_object_type: ClassVar[str] = 'Site:GroundTemperature:FCfactorMethod'
    january_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    february_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    march_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    april_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    may_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    june_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    july_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    august_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    september_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    october_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    november_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    december_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )


class SiteGroundTemperatureShallow(IDFBaseModel):
    """These temperatures are specifically for the Surface Ground Heat Exchanger
    and should probably be close to the average outdoor air temperature for the
    location. They are not used in other models."""

    _idf_object_type: ClassVar[str] = 'Site:GroundTemperature:Shallow'
    january_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    february_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    march_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    april_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    may_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    june_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    july_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    august_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    september_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    october_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    november_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )
    december_surface_ground_temperature: float | None = Field(
        default=13.0, json_schema_extra={'units': 'C'}
    )


class SiteGroundTemperatureUndisturbedFiniteDifference(IDFBaseModel):
    """Undisturbed ground temperature object using a detailed finite difference 1-D
    model"""

    _idf_object_type: ClassVar[str] = (
        'Site:GroundTemperature:Undisturbed:FiniteDifference'
    )
    name: str = Field(...)
    soil_thermal_conductivity: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    soil_moisture_content_volume_fraction: float | None = Field(
        default=30.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    soil_moisture_content_volume_fraction_at_saturation: float | None = Field(
        default=50.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    evapotranspiration_ground_cover_parameter: float | None = Field(
        default=0.4,
        ge=0.0,
        le=1.5,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This specifies the ground cover effects during evapotranspiration calculations. The value roughly represents the following cases: = 0   : concrete or other solid, non-permeable ground surface mater...',
        },
    )


class SiteGroundTemperatureUndisturbedKusudaAchenbach(IDFBaseModel):
    """Undisturbed ground temperature object using the Kusuda-Achenbach 1965
    correlation."""

    _idf_object_type: ClassVar[str] = (
        'Site:GroundTemperature:Undisturbed:KusudaAchenbach'
    )
    name: str = Field(...)
    soil_thermal_conductivity: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    average_soil_surface_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Annual average surface temperature If left blank the Site:GroundTemperature:Shallow object must be included in the input The soil temperature, amplitude, and phase shift must all be included or omi...',
        },
    )
    average_amplitude_of_surface_temperature: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Annual average surface temperature variation from average. If left blank the Site:GroundTemperature:Shallow object must be included in the input The soil temperature, amplitude, and phase shift mus...',
        },
    )
    phase_shift_of_minimum_surface_temperature: float | None = Field(
        default=None,
        ge=0.0,
        lt=365.0,
        json_schema_extra={
            'units': 'days',
            'note': 'The phase shift of minimum surface temperature, or the day of the year when the minimum surface temperature occurs. If left blank the Site:GroundTemperature:Shallow object must be included in the i...',
        },
    )


class SiteGroundTemperatureUndisturbedXing(IDFBaseModel):
    """Undisturbed ground temperature object using the Xing 2014 2 harmonic
    parameter model."""

    _idf_object_type: ClassVar[str] = 'Site:GroundTemperature:Undisturbed:Xing'
    name: str = Field(...)
    soil_thermal_conductivity: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    average_soil_surface_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    soil_surface_temperature_amplitude_1: float = Field(
        ..., json_schema_extra={'units': 'deltaC'}
    )
    soil_surface_temperature_amplitude_2: float = Field(
        ..., json_schema_extra={'units': 'deltaC'}
    )
    phase_shift_of_temperature_amplitude_1: float = Field(
        ..., lt=365.0, json_schema_extra={'units': 'days'}
    )
    phase_shift_of_temperature_amplitude_2: float = Field(
        ..., lt=365.0, json_schema_extra={'units': 'days'}
    )


class SiteHeightVariation(IDFBaseModel):
    """This object is used if the user requires advanced control over height-
    dependent variations in wind speed and temperature. When this object is not
    present, the default model for temperature dependence on height is used, and
    the wind speed is modeled according to the Terrain field of the BUILDING
    object."""

    _idf_object_type: ClassVar[str] = 'Site:HeightVariation'
    wind_speed_profile_exponent: float | None = Field(
        default=0.22,
        ge=0.0,
        json_schema_extra={
            'note': 'Set to zero for no wind speed dependence on height.'
        },
    )
    wind_speed_profile_boundary_layer_thickness: float | None = Field(
        default=370.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    air_temperature_gradient_coefficient: float | None = Field(
        default=0.0065,
        ge=0.0,
        json_schema_extra={
            'units': 'K/m',
            'note': 'Set to zero for no air temperature dependence on height.',
        },
    )


class SiteLocation(IDFBaseModel):
    """Specifies the building's location. Only one location is allowed. Weather
    data file location, if it exists, will override this object."""

    _idf_object_type: ClassVar[str] = 'Site:Location'
    name: str = Field(...)
    latitude: float | None = Field(
        default=0.0,
        ge=-90.0,
        le=90.0,
        json_schema_extra={
            'units': 'deg',
            'note': '+ is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)',
        },
    )
    longitude: float | None = Field(
        default=0.0,
        ge=-180.0,
        le=180.0,
        json_schema_extra={
            'units': 'deg',
            'note': '- is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)',
        },
    )
    time_zone: float | None = Field(
        default=0.0,
        ge=-12.0,
        le=14.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'basic these limits on the WorldTimeZone Map (2003) Time relative to GMT. Decimal hours.',
        },
    )
    elevation: float | None = Field(
        default=0.0, ge=-300.0, lt=8900.0, json_schema_extra={'units': 'm'}
    )
    keep_site_location_information: Literal['', 'No', 'Yes'] | None = Field(
        default='No'
    )


class SitePrecipitation(IDFBaseModel):
    """Used to describe the amount of water precipitation at the building site.
    Precipitation includes both rain and the equivalent water content of snow."""

    _idf_object_type: ClassVar[str] = 'Site:Precipitation'
    precipitation_model_type: Literal['ScheduleAndDesignLevel'] | None = Field(
        default=None
    )
    design_level_for_total_annual_precipitation: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm/yr',
            'note': 'meters of water per year used for design level',
        },
    )
    precipitation_rates_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values in meters of water per hour values should be non-negative',
        },
    )
    average_total_annual_precipitation: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm/yr',
            'note': 'meters of water per year from average weather statistics',
        },
    )


class SiteSolarAndVisibleSpectrum(IDFBaseModel):
    """If this object is omitted, the default solar and visible spectrum data will
    be used."""

    _idf_object_type: ClassVar[str] = 'Site:SolarAndVisibleSpectrum'
    name: str = Field(...)
    spectrum_data_method: Literal['', 'Default', 'UserDefined'] | None = Field(
        default='Default',
        json_schema_extra={
            'note': 'The method specifies which of the solar and visible spectrum data to use in the calculations. Choices: Default - existing hard-wired spectrum data in EnergyPlus. UserDefined - user specified spectr...'
        },
    )
    solar_spectrum_data_object_name: SpectrumDataNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['SpectrumDataNames']}
    )
    visible_spectrum_data_object_name: SpectrumDataNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['SpectrumDataNames']}
    )


class SiteSpectrumData(IDFBaseModel):
    """Spectrum Data Type is followed by up to 107 sets of normal-incidence
    measured values of [wavelength, spectrum] for wavelengths covering the solar
    (0.25 to 2.5 microns) or visible spectrum (0.38 to 0.78 microns)"""

    _idf_object_type: ClassVar[str] = 'Site:SpectrumData'
    name: str = Field(...)
    spectrum_data_type: Literal['Solar', 'Visible'] = Field(...)
    wavelength: float | None = Field(
        default=None, json_schema_extra={'units': 'micron'}
    )
    spectrum: float | None = Field(default=None)
    wavelength_1: float | None = Field(
        default=None, json_schema_extra={'units': 'micron'}
    )
    spectrum_2: float | None = Field(default=None)
    extensions: list[SiteSpectrumDataExtensionsItem] | None = Field(default=None)


class SiteVariableLocation(IDFBaseModel):
    """Captures the scheduling of a moving/reorienting building, or more likely a
    vessel"""

    _idf_object_type: ClassVar[str] = 'Site:VariableLocation'
    name: str = Field(...)
    building_location_latitude_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of a schedule that defines the latitude of the building at any time. If not entered, the latitude defined in the Site:Location, or the default latitude, will be used for the entirety of th...',
        },
    )
    building_location_longitude_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of a schedule that defines the longitude of the building at any time. If not entered, the longitude defined in the Site:Location, or the default longitude, will be used for the entirety of...',
        },
    )
    building_location_orientation_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of a schedule that defines the orientation of the building at any time. This orientation is based on a change from the original orientation. -- NEED TO REFINE THIS If not entered, the orig...',
        },
    )


class SiteWaterMainsTemperature(IDFBaseModel):
    """Used to calculate water mains temperatures delivered by underground water
    main pipes. Water mains temperatures are a function of outdoor climate
    conditions and vary with time of year."""

    _idf_object_type: ClassVar[str] = 'Site:WaterMainsTemperature'
    calculation_method: (
        Literal['', 'Correlation', 'CorrelationFromWeatherFile', 'Schedule'] | None
    ) = Field(
        default='CorrelationFromWeatherFile',
        json_schema_extra={
            'note': 'If calculation method is CorrelationFromWeatherFile, the two numeric input fields are ignored. Instead, EnergyPlus calculates them from weather file.'
        },
    )
    temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    annual_average_outdoor_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'If calculation method is CorrelationFromWeatherFile or Schedule, this input field is ignored.',
        },
    )
    maximum_difference_in_monthly_average_outdoor_air_temperatures: float | None = (
        Field(
            default=None,
            ge=0.0,
            json_schema_extra={
                'units': 'deltaC',
                'note': 'If calculation method is CorrelationFromWeatherFile or Schedule, this input field is ignored.',
            },
        )
    )
    temperature_multiplier: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'If calculation method is Schedule, this input field is ignored.',
        },
    )
    temperature_offset: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'If calculation method is Schedule, this input field is ignored.',
        },
    )


class SiteWeatherStation(IDFBaseModel):
    """This object should only be used for non-standard weather data. Standard
    weather data such as TMY2, IWEC, and ASHRAE design day data are all measured
    at the default conditions and do not require this object."""

    _idf_object_type: ClassVar[str] = 'Site:WeatherStation'
    wind_sensor_height_above_ground: float | None = Field(
        default=10.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    wind_speed_profile_exponent: float | None = Field(default=0.14, ge=0.0)
    wind_speed_profile_boundary_layer_thickness: float | None = Field(
        default=270.0, ge=0.0, json_schema_extra={'units': 'm'}
    )
    air_temperature_sensor_height_above_ground: float | None = Field(
        default=1.5, ge=0.0, json_schema_extra={'units': 'm'}
    )


class SizingPeriodDesignDay(IDFBaseModel):
    """The design day object creates the parameters for the program to create the
    24 hour weather profile that can be used for sizing as well as running to
    test the other simulation parameters. Parameters in this include a date
    (month and day), a day type (which uses the appropriate schedules for either
    sizing or simple tests), min/max temperatures, wind speeds, and solar
    radiation values."""

    _idf_object_type: ClassVar[str] = 'SizingPeriod:DesignDay'
    name: str = Field(...)
    month: int = Field(..., ge=1, le=12)
    day_of_month: int = Field(
        ..., ge=1, le=31, json_schema_extra={'note': 'must be valid for Month field'}
    )
    day_type: Literal[
        'CustomDay1',
        'CustomDay2',
        'Friday',
        'Holiday',
        'Monday',
        'Saturday',
        'SummerDesignDay',
        'Sunday',
        'Thursday',
        'Tuesday',
        'Wednesday',
        'WinterDesignDay',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Day Type selects the schedules appropriate for this design day'
        },
    )
    maximum_dry_bulb_temperature: float | None = Field(
        default=None,
        ge=-90.0,
        le=70.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is required when field "Dry-Bulb Temperature Range Modifier Type" is not "TemperatureProfileSchedule".',
        },
    )
    daily_dry_bulb_temperature_range: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Must still produce appropriate maximum dry-bulb (within range) This field is not needed if Dry-Bulb Temperature Range Modifier Type is "delta".',
        },
    )
    dry_bulb_temperature_range_modifier_type: (
        Literal[
            '',
            'DefaultMultipliers',
            'DifferenceSchedule',
            'MultiplierSchedule',
            'TemperatureProfileSchedule',
        ]
        | None
    ) = Field(
        default='DefaultMultipliers',
        json_schema_extra={
            'note': 'Type of modifier to the dry-bulb temperature calculated for the timestep'
        },
    )
    dry_bulb_temperature_range_modifier_day_schedule_name: (
        DayScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DayScheduleNames'],
            'note': 'Only used when previous field is "MultiplierSchedule", "DifferenceSchedule" or "TemperatureProfileSchedule". For type "MultiplierSchedule"  the hour/time interval values should specify the fraction...',
        },
    )
    humidity_condition_type: (
        Literal[
            '',
            'DewPoint',
            'Enthalpy',
            'HumidityRatio',
            'RelativeHumiditySchedule',
            'WetBulb',
            'WetBulbProfileDefaultMultipliers',
            'WetBulbProfileDifferenceSchedule',
            'WetBulbProfileMultiplierSchedule',
        ]
        | None
    ) = Field(
        default='WetBulb',
        json_schema_extra={
            'note': 'values/schedules indicated here and in subsequent fields create the humidity values in the 24 hour design day conditions profile.'
        },
    )
    wetbulb_or_dewpoint_at_maximum_dry_bulb: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Wetbulb or dewpoint temperature coincident with the maximum temperature. Required only if field Humidity Condition Type is "Wetbulb", "Dewpoint", "WetBulbProfileMultiplierSchedule", "WetBulbProfile...',
        },
    )
    humidity_condition_day_schedule_name: DayScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DayScheduleNames'],
            'note': 'Only used when Humidity Condition Type is "RelativeHumiditySchedule", "WetBulbProfileMultiplierSchedule", or "WetBulbProfileDifferenceSchedule" For type "RelativeHumiditySchedule", the hour/time in...',
        },
    )
    humidity_ratio_at_maximum_dry_bulb: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Humidity ratio coincident with the maximum temperature (constant humidity ratio throughout day). Required only if field Humidity Condition Type is "HumidityRatio".',
        },
    )
    enthalpy_at_maximum_dry_bulb: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Enthalpy coincident with the maximum temperature. Required only if field Humidity Condition Type is "Enthalpy".',
        },
    )
    daily_wet_bulb_temperature_range: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Required only if Humidity Condition Type = "WetbulbProfileMultiplierSchedule" or "WetBulbProfileDefaultMultipliers"',
        },
    )
    barometric_pressure: float | None = Field(
        default=None,
        ge=31000.0,
        le=120000.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'This field\'s value is also checked against the calculated "standard barometric pressure" for the location. If out of range (>10%) or blank, then is replaced by standard value.',
        },
    )
    wind_speed: float = Field(..., ge=0.0, le=40.0, json_schema_extra={'units': 'm/s'})
    wind_direction: float = Field(
        ...,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'North=0.0 East=90.0 0 and 360 are the same direction.',
        },
    )
    rain_indicator: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Yes is raining (all day), No is not raining'},
    )
    snow_indicator: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Yes is Snow on Ground, No is no Snow on Ground'},
    )
    daylight_saving_time_indicator: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Yes -- use schedules modified for Daylight Saving Time Schedules. No - do not use schedules modified for Daylight Saving Time Schedules'
        },
    )
    solar_model_indicator: (
        Literal[
            '', 'ASHRAEClearSky', 'ASHRAETau', 'ASHRAETau2017', 'Schedule', 'ZhangHuang'
        ]
        | None
    ) = Field(default='ASHRAEClearSky')
    beam_solar_day_schedule_name: DayScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DayScheduleNames'],
            'note': 'if Solar Model Indicator = Schedule, then beam schedule name (for day)',
        },
    )
    diffuse_solar_day_schedule_name: DayScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DayScheduleNames'],
            'note': 'if Solar Model Indicator = Schedule, then diffuse schedule name (for day)',
        },
    )
    ashrae_clear_sky_optical_depth_for_beam_irradiance_taub: float | None = Field(
        default=0.0,
        validation_alias='ashrae_clear_sky_optical_depth_for_beam_irradiance_taub_',
        ge=0.0,
        le=1.2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Required if Solar Model Indicator = ASHRAETau or ASHRAETau2017 ASHRAETau2017 solar model can be used with 2013 and 2017 HOF matching taub',
        },
    )
    ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud: float | None = Field(
        default=0.0,
        validation_alias='ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud_',
        ge=0.0,
        le=3.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Required if Solar Model Indicator = ASHRAETau or ASHRAETau2017 ASHRAETau2017 solar model can be used with 2013 and 2017 HOF matching taud',
        },
    )
    sky_clearness: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.2,
        json_schema_extra={
            'note': 'Used if Sky Model Indicator = ASHRAEClearSky or ZhangHuang 0.0 is totally unclear, 1.0 is totally clear'
        },
    )
    maximum_number_warmup_days: int | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If used this design day will be run with a custom limit on the maximum number of days that are repeated for warmup. Limiting the number of warmup days can improve run time.'
        },
    )
    begin_environment_reset_mode: (
        Literal['', 'FullResetAtBeginEnvironment', 'SuppressAllBeginEnvironmentResets']
        | None
    ) = Field(
        default='FullResetAtBeginEnvironment',
        json_schema_extra={
            'note': 'If used this can control if you want the thermal history to be reset at the beginning of the design day. When using a series of similar design days, this field can be used to retain warmup state fr...'
        },
    )


class SizingPeriodWeatherFileConditionType(IDFBaseModel):
    """Use a weather file period for design sizing calculations. EPW weather files
    are created with typical and extreme periods created heuristically from the
    weather file data. For more details on these periods, see AuxiliaryPrograms
    document."""

    _idf_object_type: ClassVar[str] = 'SizingPeriod:WeatherFileConditionType'
    name: str = Field(
        ..., json_schema_extra={'note': 'user supplied name for reporting'}
    )
    period_selection: Literal[
        'AutumnTypical',
        'DrySeason',
        'NoDrySeason',
        'NoDrySeasonMax',
        'NoDrySeasonMin',
        'NoWetSeason',
        'NoWetSeasonMax',
        'NoWetSeasonMin',
        'SpringTypical',
        'SummerExtreme',
        'SummerTypical',
        'TropicalCold',
        'TropicalHot',
        'WetSeason',
        'WinterExtreme',
        'WinterTypical',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Following is a list of all possible types of Extreme and Typical periods that might be identified in the Weather File. Not all possible types are available for all weather files.'
        },
    )
    day_of_week_for_start_day: (
        Literal[
            '',
            'CustomDay1',
            'CustomDay2',
            'Friday',
            'Monday',
            'Saturday',
            'SummerDesignDay',
            'Sunday',
            'Thursday',
            'Tuesday',
            'Wednesday',
            'WinterDesignDay',
        ]
        | None
    ) = Field(
        default='Monday',
        json_schema_extra={
            'note': '=[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay| |CustomDay1|CustomDay2]; if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will ...'
        },
    )
    use_weather_file_daylight_saving_period: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If yes or blank, use daylight saving period as specified on Weatherfile. If no, do not use the daylight saving period as specified on the Weatherfile.'
        },
    )
    use_weather_file_rain_and_snow_indicators: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes'
    )


class SizingPeriodWeatherFileDays(IDFBaseModel):
    """Use a weather file period for design sizing calculations."""

    _idf_object_type: ClassVar[str] = 'SizingPeriod:WeatherFileDays'
    name: str = Field(
        ..., json_schema_extra={'note': 'user supplied name for reporting'}
    )
    begin_month: int = Field(..., ge=1, le=12)
    begin_day_of_month: int = Field(..., ge=1, le=31)
    end_month: int = Field(..., ge=1, le=12)
    end_day_of_month: int = Field(..., ge=1, le=31)
    day_of_week_for_start_day: (
        Literal[
            '',
            'CustomDay1',
            'CustomDay2',
            'Friday',
            'Monday',
            'Saturday',
            'SummerDesignDay',
            'Sunday',
            'Thursday',
            'Tuesday',
            'Wednesday',
            'WinterDesignDay',
        ]
        | None
    ) = Field(
        default='Monday',
        json_schema_extra={
            'note': '=[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay| |CustomDay1|CustomDay2]; if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will ...'
        },
    )
    use_weather_file_daylight_saving_period: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If yes or blank, use daylight saving period as specified on Weatherfile. If no, do not use the daylight saving period as specified on the Weatherfile.'
        },
    )
    use_weather_file_rain_and_snow_indicators: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes'
    )


class WeatherPropertySkyTemperature(IDFBaseModel):
    """This object is used to override internal sky temperature calculations."""

    _idf_object_type: ClassVar[str] = 'WeatherProperty:SkyTemperature'
    name: RunPeriodsAndDesignDaysRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RunPeriodsAndDesignDays'],
            'note': 'blank in this field will apply to all run periods (that is, all objects= SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod otherwise, this name must match one of the ...',
        },
    )
    calculation_type: (
        Literal[
            '',
            'BerdahlMartin',
            'Brunt',
            'ClarkAllen',
            'DifferenceScheduleDewPointValue',
            'DifferenceScheduleDryBulbValue',
            'Idso',
            'ScheduleValue',
        ]
        | None
    ) = Field(
        default='ClarkAllen',
        json_schema_extra={
            'note': 'The field indicates that the sky temperature will be imported from external schedules or calculated by alternative methods other than default.'
        },
    )
    schedule_name: (DayScheduleNamesRef | ScheduleNamesRef) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DayScheduleNames', 'ScheduleNames'],
            'note': 'if name matches a SizingPeriod:DesignDay, put in a day schedule of this name if name is for a SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod, put in a full year sc...',
        },
    )
    use_weather_file_horizontal_ir: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If yes or blank, use Horizontal IR values from weather file when present, otherwise use the specified sky model. If no, always use the specified sky model and ignore the horizontal IR values from t...'
        },
    )
