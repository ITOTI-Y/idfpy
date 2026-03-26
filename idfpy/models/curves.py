"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Performance Curves
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel


class CurveBicubic(IDFBaseModel):
    """Cubic curve with two independent variables. Input consists of the curve
    name, the ten coefficients, and the minimum and maximum values for each of
    the independent variables. Optional inputs for curve minimum and maximum may
    be used to limit the output of the performance curve. curve = C1 + C2*x +
    C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 + C8*y**3 + C9*x**2*y +
    C10*x*y**2"""

    _idf_object_type: ClassVar[str] = 'Curve:Bicubic'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_y: float = Field(...)
    coefficient5_y_2: float = Field(...)
    coefficient6_x_y: float = Field(...)
    coefficient7_x_3: float = Field(...)
    coefficient8_y_3: float = Field(...)
    coefficient9_x_2_y: float = Field(...)
    coefficient10_x_y_2: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveBiquadratic(IDFBaseModel):
    """Quadratic curve with two independent variables. Input consists of the curve
    name, the six coefficients, and min and max values for each of the
    independent variables. Optional inputs for curve minimum and maximum may be
    used to limit the output of the performance curve. curve = C1 + C2*x +
    C3*x**2 + C4*y + C5*y**2 + C6*x*y"""

    _idf_object_type: ClassVar[str] = 'Curve:Biquadratic'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_y: float = Field(...)
    coefficient5_y_2: float = Field(...)
    coefficient6_x_y: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveChillerPartLoadWithLift(IDFBaseModel):
    """This chiller part-load performance curve has three independent variables.
    Input consists of the curve name, the twelve coefficients, and the maximum
    and minimum valid independent variable values. Optional inputs for the curve
    minimum and maximum may be used to limit the output of the performance
    curve. curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 +
    C8*y**3 + C9*x**2*y + C10*x*y**2 + C11*x**2*y**2 + C12*z*y**3 x = dT* =
    normalized fractional Lift = dT / dTref y = PLR = part load ratio (cooling
    load/steady state capacity) z = Tdev* = normalized Tdev = Tdev / dTref
    Where: dT = Lift = Leaving Condenser Water Temperature - Leaving Chilled
    Water Temperature dTref = dT at the reference condition Tdev = Leaving
    Chilled Water Temperature - Reference Chilled Water Temperature"""

    _idf_object_type: ClassVar[str] = 'Curve:ChillerPartLoadWithLift'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    coefficient4_c4: float = Field(...)
    coefficient5_c5: float = Field(...)
    coefficient6_c6: float = Field(...)
    coefficient7_c7: float = Field(...)
    coefficient8_c8: float = Field(...)
    coefficient9_c9: float = Field(...)
    coefficient10_c10: float = Field(...)
    coefficient11_c11: float = Field(...)
    coefficient12_c12: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_value_of_z: float = Field(...)
    maximum_value_of_z: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    input_unit_type_for_y: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    input_unit_type_for_z: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveCubic(IDFBaseModel):
    """Cubic curve with one independent variable. Input for a cubic curve consists
    of the curve name, the 4 coefficients, and the maximum and minimum valid
    independent variable values. Optional inputs for curve minimum and maximum
    may be used to limit the output of the performance curve. curve = C1 + C2*x
    + C3*x**2 + C4*x**3"""

    _idf_object_type: ClassVar[str] = 'Curve:Cubic'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_x_3: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveCubicLinear(IDFBaseModel):
    """Cubic-linear curve with two independent variables. Input consists of the
    curve name, the six coefficients, and min and max values for each of the
    independent variables. Optional inputs for curve minimum and maximum may be
    used to limit the output of the performance curve. curve = (C1 + C2*x +
    C3*x**2 + C4*x**3) + (C5 + C6*x)*y"""

    _idf_object_type: ClassVar[str] = 'Curve:CubicLinear'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_x_3: float = Field(...)
    coefficient5_y: float = Field(...)
    coefficient6_x_y: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless', 'Temperature'] | None = Field(
        default='Dimensionless'
    )
    input_unit_type_for_y: Literal['', 'Dimensionless', 'Temperature'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveDoubleExponentialDecay(IDFBaseModel):
    """Double exponential decay curve with one independent variable. Input consists
    of the curve name, the five coefficients, and the maximum and minimum valid
    independent variable values. Optional inputs for the curve minimum and
    maximum may be used to limit the output of the performance curve. curve =
    C1+C2*exp(C3*x)+C4*exp(C5*x)"""

    _idf_object_type: ClassVar[str] = 'Curve:DoubleExponentialDecay'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    coefficient4_c4: float = Field(...)
    coefficient5_c5: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveExponent(IDFBaseModel):
    """Exponent curve with one independent variable. Input for a exponent curve
    consists of the curve name, the 3 coefficients, and the maximum and minimum
    valid independent variable values. Optional inputs for curve minimum and
    maximum may be used to limit the output of the performance curve. curve = C1
    + C2*x**C3 The independent variable x is raised to the C3 power, multiplied
    by C2, and C1 is added to the result."""

    _idf_object_type: ClassVar[str] = 'Curve:Exponent'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_constant: float = Field(...)
    coefficient3_constant: float = Field(...)
    minimum_value_of_x: float = Field(
        ...,
        json_schema_extra={
            'note': 'Specify the minimum value of the independent variable x allowed'
        },
    )
    maximum_value_of_x: float = Field(
        ...,
        json_schema_extra={
            'note': 'Specify the maximum value of the independent variable x allowed'
        },
    )
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveExponentialDecay(IDFBaseModel):
    """Exponential decay curve with one independent variable. Input consists of the
    curve name, the three coefficients, and the maximum and minimum valid
    independent variable values. Optional inputs for the curve minimum and
    maximum may be used to limit the output of the performance curve. curve =
    C1+C2*exp(C3*x)"""

    _idf_object_type: ClassVar[str] = 'Curve:ExponentialDecay'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveExponentialSkewNormal(IDFBaseModel):
    """Exponential-modified skew normal curve with one independent variable. Input
    consists of the curve name, the four coefficients, and the maximum and
    minimum valid independent variable values. Optional inputs for the curve
    minimum and maximum may be used to limit the output of the performance
    curve. curve = see Input Output Reference"""

    _idf_object_type: ClassVar[str] = 'Curve:ExponentialSkewNormal'
    name: str = Field(
        ..., json_schema_extra={'note': 'See InputOut Reference for curve description'}
    )
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    coefficient4_c4: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveFanPressureRise(IDFBaseModel):
    """Special curve type with two independent variables. Input for the fan total
    pressure rise curve consists of the curve name, the four coefficients, and
    the maximum and minimum valid independent variable values. Optional inputs
    for the curve minimum and maximum may be used to limit the output of the
    performance curve. curve = C1*Qfan**2+C2*Qfan+C3*Qfan*(Psm-Po)**0.5+C4*(Psm-
    Po) Po assumed to be zero See InputOut Reference for curve details"""

    _idf_object_type: ClassVar[str] = 'Curve:FanPressureRise'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    coefficient4_c4: float = Field(...)
    minimum_value_of_qfan: float = Field(..., json_schema_extra={'units': 'm3/s'})
    maximum_value_of_qfan: float = Field(..., json_schema_extra={'units': 'm3/s'})
    minimum_value_of_psm: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_value_of_psm: float = Field(..., json_schema_extra={'units': 'Pa'})
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Specify the minimum value calculated by this curve object',
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Specify the maximum value calculated by this curve object',
        },
    )


class CurveFunctionalPressureDrop(IDFBaseModel):
    """Sets up curve information for minor loss and/or friction calculations in
    plant pressure simulations Expression: DeltaP = {K + f*(L/D)} * (rho * V^2)
    / 2"""

    _idf_object_type: ClassVar[str] = 'Curve:Functional:PressureDrop'
    name: str = Field(...)
    diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': '"D" in above expression, used to also calculate local velocity',
        },
    )
    minor_loss_coefficient: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={'units': 'dimensionless', 'note': '"K" in above expression'},
    )
    length: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': '"L" in above expression'},
    )
    roughness: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This will be used to calculate "f" from Moody-chart approximations',
        },
    )
    fixed_friction_factor: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'note': 'Optional way to set a constant value for "f", instead of using internal Moody-chart approximations'
        },
    )


class CurveLinear(IDFBaseModel):
    """Linear curve with one independent variable. Input for the linear curve
    consists of a curve name, the two coefficients, and the maximum and minimum
    valid independent variable values. Optional inputs for curve minimum and
    maximum may be used to limit the output of the performance curve. curve = C1
    + C2*x"""

    _idf_object_type: ClassVar[str] = 'Curve:Linear'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Pressure',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveQuadLinear(IDFBaseModel):
    """Linear curve with four independent variables. Input for the linear curve
    consists of a curve name, the two coefficients, and the maximum and minimum
    valid independent variable values. Optional inputs for curve minimum and
    maximum may be used to limit the output of the performance curve. curve = C1
    + C2*w + C3*x + C4*y + C5*z"""

    _idf_object_type: ClassVar[str] = 'Curve:QuadLinear'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_w: float = Field(...)
    coefficient3_x: float = Field(...)
    coefficient4_y: float = Field(...)
    coefficient5_z: float = Field(...)
    minimum_value_of_w: float = Field(...)
    maximum_value_of_w: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_value_of_z: float = Field(...)
    maximum_value_of_z: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_w: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_z: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')


class CurveQuadratic(IDFBaseModel):
    """Quadratic curve with one independent variable. Input for a quadratic curve
    consists of the curve name, the three coefficients, and the maximum and
    minimum valid independent variable values. Optional inputs for curve minimum
    and maximum may be used to limit the output of the performance curve. curve
    = C1 + C2*x + C3*x**2"""

    _idf_object_type: ClassVar[str] = 'Curve:Quadratic'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveQuadraticLinear(IDFBaseModel):
    """Quadratic-linear curve with two independent variables. Input consists of the
    curve name, the six coefficients, and min and max values for each of the
    independent variables. Optional inputs for curve minimum and maximum may be
    used to limit the output of the performance curve. curve = (C1 + C2*x +
    C3*x**2) + (C4 + C5*x + C6*x**2)*y"""

    _idf_object_type: ClassVar[str] = 'Curve:QuadraticLinear'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_y: float = Field(...)
    coefficient5_x_y: float = Field(...)
    coefficient6_x_2_y: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveQuartic(IDFBaseModel):
    """Quartic (fourth order polynomial) curve with one independent variable. Input
    for a Quartic curve consists of the curve name, the five coefficients, and
    the maximum and minimum valid independent variable values. Optional inputs
    for curve minimum and maximum may be used to limit the output of the
    performance curve. curve = C1 + C2*x + C3*x**2 + C4*x**3 + C5*x**4"""

    _idf_object_type: ClassVar[str] = 'Curve:Quartic'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_x: float = Field(...)
    coefficient3_x_2: float = Field(...)
    coefficient4_x_3: float = Field(...)
    coefficient5_x_4: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveQuintLinear(IDFBaseModel):
    """Linear curve with five independent variables. Input for the linear curve
    consists of a curve name, the two coefficients, and the maximum and minimum
    valid independent variable values. Optional inputs for curve minimum and
    maximum may be used to limit the output of the performance curve. curve = C1
    + C2*v + C3*w + C4*x + C5*y + C6*z"""

    _idf_object_type: ClassVar[str] = 'Curve:QuintLinear'
    name: str = Field(...)
    coefficient1_constant: float = Field(...)
    coefficient2_v: float = Field(...)
    coefficient3_w: float = Field(...)
    coefficient4_x: float = Field(...)
    coefficient5_y: float = Field(...)
    coefficient6_z: float = Field(...)
    minimum_value_of_v: float = Field(...)
    maximum_value_of_v: float = Field(...)
    minimum_value_of_w: float = Field(...)
    maximum_value_of_w: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_value_of_y: float = Field(...)
    maximum_value_of_y: float = Field(...)
    minimum_value_of_z: float = Field(...)
    maximum_value_of_z: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_v: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_w: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_z: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
            'VolumetricFlowPerPower',
        ]
        | None
    ) = Field(default='Dimensionless')


class CurveRectangularHyperbola1(IDFBaseModel):
    """Rectangular hyperbola type 1 curve with one independent variable. Input
    consists of the curve name, the three coefficients, and the maximum and
    minimum valid independent variable values. Optional inputs for the curve
    minimum and maximum may be used to limit the output of the performance
    curve. curve = ((C1*x)/(C2+x))+C3"""

    _idf_object_type: ClassVar[str] = 'Curve:RectangularHyperbola1'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveRectangularHyperbola2(IDFBaseModel):
    """Rectangular hyperbola type 2 curve with one independent variable. Input
    consists of the curve name, the three coefficients, and the maximum and
    minimum valid independent variable values. Optional inputs for the curve
    minimum and maximum may be used to limit the output of the performance
    curve. curve = ((C1*x)/(C2+x))+(C3*x)"""

    _idf_object_type: ClassVar[str] = 'Curve:RectangularHyperbola2'
    name: str = Field(...)
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveSigmoid(IDFBaseModel):
    """Sigmoid curve with one independent variable. Input consists of the curve
    name, the five coefficients, and the maximum and minimum valid independent
    variable values. Optional inputs for the curve minimum and maximum may be
    used to limit the output of the performance curve. curve =
    C1+C2/[1+exp((C3-x)/C4)]**C5"""

    _idf_object_type: ClassVar[str] = 'Curve:Sigmoid'
    name: str = Field(
        ..., json_schema_extra={'note': 'See InputOut Reference for curve description'}
    )
    coefficient1_c1: float = Field(...)
    coefficient2_c2: float = Field(...)
    coefficient3_c3: float = Field(...)
    coefficient4_c4: float = Field(...)
    coefficient5_c5: float = Field(...)
    minimum_value_of_x: float = Field(...)
    maximum_value_of_x: float = Field(...)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: Literal['', 'Dimensionless'] | None = Field(
        default='Dimensionless'
    )
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')


class CurveTriquadratic(IDFBaseModel):
    """Quadratic curve with three independent variables. Input consists of the
    curve name, the twenty seven coefficients, and min and max values for each
    of the independent variables. Optional inputs for curve minimum and maximum
    may be used to limit the output of the performance curve. curve = a0 +
    a1*x**2 + a2*x + a3*y**2 + a4*y + a5*z**2 + a6*z + a7*x**2*y**2 + a8*x*y +
    a9*x*y**2 + a10*x**2*y + a11*x**2*z**2 + a12*x*z + a13*x*z**2 + a14*x**2*z +
    a15*y**2*z**2 + a16*y*z + a17*y*z**2 + a18*y**2*z + a19*x**2*y**2*z**2 +
    a20*x**2*y**2*z + a21*x**2*y*z**2 + a22*x*y**2*z**2 + a23*x**2*y*z +
    a24*x*y**2*z + a25*x*y*z**2 +a26*x*y*z"""

    _idf_object_type: ClassVar[str] = 'Curve:Triquadratic'
    name: str = Field(...)
    coefficient1_constant: float | None = Field(default=None)
    coefficient2_x_2: float | None = Field(default=None)
    coefficient3_x: float | None = Field(default=None)
    coefficient4_y_2: float | None = Field(default=None)
    coefficient5_y: float | None = Field(default=None)
    coefficient6_z_2: float | None = Field(default=None)
    coefficient7_z: float | None = Field(default=None)
    coefficient8_x_2_y_2: float | None = Field(default=None)
    coefficient9_x_y: float | None = Field(default=None)
    coefficient10_x_y_2: float | None = Field(default=None)
    coefficient11_x_2_y: float | None = Field(default=None)
    coefficient12_x_2_z_2: float | None = Field(default=None)
    coefficient13_x_z: float | None = Field(default=None)
    coefficient14_x_z_2: float | None = Field(default=None)
    coefficient15_x_2_z: float | None = Field(default=None)
    coefficient16_y_2_z_2: float | None = Field(default=None)
    coefficient17_y_z: float | None = Field(default=None)
    coefficient18_y_z_2: float | None = Field(default=None)
    coefficient19_y_2_z: float | None = Field(default=None)
    coefficient20_x_2_y_2_z_2: float | None = Field(default=None)
    coefficient21_x_2_y_2_z: float | None = Field(default=None)
    coefficient22_x_2_y_z_2: float | None = Field(default=None)
    coefficient23_x_y_2_z_2: float | None = Field(default=None)
    coefficient24_x_2_y_z: float | None = Field(default=None)
    coefficient25_x_y_2_z: float | None = Field(default=None)
    coefficient26_x_y_z_2: float | None = Field(default=None)
    coefficient27_x_y_z: float | None = Field(default=None)
    minimum_value_of_x: float | None = Field(default=None)
    maximum_value_of_x: float | None = Field(default=None)
    minimum_value_of_y: float | None = Field(default=None)
    maximum_value_of_y: float | None = Field(default=None)
    minimum_value_of_z: float | None = Field(default=None)
    maximum_value_of_z: float | None = Field(default=None)
    minimum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the minimum value calculated by this curve object'
        },
    )
    maximum_curve_output: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specify the maximum value calculated by this curve object'
        },
    )
    input_unit_type_for_x: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_y: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    input_unit_type_for_z: (
        Literal[
            '',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')
