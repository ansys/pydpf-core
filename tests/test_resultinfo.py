# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest

from ansys import dpf
from ansys.dpf.core import Model, examples
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_11_0,
)

if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0:
    mechanical = "mechanical"
else:
    mechanical = "mecanic"  # codespell:ignore mecanic


@pytest.fixture()
def model(velocity_acceleration, server_type):
    return dpf.core.Model(velocity_acceleration, server=server_type)


def test_get_resultinfo_no_model(velocity_acceleration, server_type):
    dataSource = dpf.core.DataSources(velocity_acceleration, server=server_type)
    dataSource.set_result_file_path(velocity_acceleration)
    op = dpf.core.Operator("mapdl::rst::ResultInfoProvider", server=server_type)
    op.connect(4, dataSource)
    res = op.get_output(0, dpf.core.types.result_info)
    assert res.analysis_type == "static"

    if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1:
        assert res.n_results == 14
    else:
        available_results_names = []
        for result in res.available_results:
            available_results_names.append(result.name)
        expected_results = [
            "displacement",
            "velocity",
            "acceleration",
            "reaction_force",
            "stress",
            "elemental_volume",
            "stiffness_matrix_energy",
            "artificial_hourglass_energy",
            "thermal_dissipation_energy",
            "kinetic_energy",
            "co_energy",
            "incremental_energy",
            "elastic_strain",
            "element_orientations",
            "structural_temperature",
        ]
        for result in expected_results:
            assert result in available_results_names

    assert "m, kg, N, s, V, A" in res.unit_system
    assert res.physics_type == mechanical


def test_get_resultinfo(model):
    res = model.metadata.result_info
    assert res.analysis_type == "static"
    if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1:
        assert res.n_results == 14
    else:
        available_results_names = []
        for result in res.available_results:
            available_results_names.append(result.name)
        expected_results = [
            "displacement",
            "velocity",
            "acceleration",
            "reaction_force",
            "stress",
            "elemental_volume",
            "stiffness_matrix_energy",
            "artificial_hourglass_energy",
            "thermal_dissipation_energy",
            "kinetic_energy",
            "co_energy",
            "incremental_energy",
            "elastic_strain",
            "element_orientations",
            "structural_temperature",
        ]
        for result in expected_results:
            assert result in available_results_names

    assert "m, kg, N, s, V, A" in res.unit_system
    assert res.physics_type == mechanical
    assert "Static analysis" in str(res)


def test_get_resultinfo_2(simple_bar, server_type):
    model = Model(simple_bar, server=server_type)
    res = model.metadata.result_info
    assert res.unit_system_name == "MKS: m, kg, N, s, V, A, degC"
    assert res.solver_version == "19.3"
    assert res.solver_date == 20181005
    assert res.solver_time == 170340
    assert res.user_name == "afaure"
    assert res.job_name == "file_Static22_0"
    assert res.product_name == "FULL"
    assert "unsaved_project--Static" in res.main_title
    assert res.cyclic_support is None


def test_byitem_resultinfo(model):
    res = model.metadata.result_info
    assert res["stress"] is not None
    assert res[0] is not None


def test_get_result_resultinfo_from_index(model):
    res = model.metadata.result_info[2]
    assert res.name == "acceleration"
    assert res.n_components == 3
    assert res.dimensionality == "vector"
    assert res.homogeneity == "acceleration"
    assert res.unit == "m/s^2"
    assert res.name == "acceleration"
    assert res.qualifiers == []


def test_print_result_info(model):
    str(model.metadata.result_info)


def test_repr_available_results_list(model):
    ar = model.metadata.result_info.available_results
    assert type(ar) is list
    assert all([type(r) is dpf.core.result_info.available_result.AvailableResult for r in ar])
    assert dpf.core.result_info.available_result.AvailableResult.__name__ in str(ar)


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available with CFF starting 7.0"
)
def test_print_available_result_with_qualifiers(cfx_heating_coil, server_type):
    model = Model(cfx_heating_coil(server=server_type), server=server_type)
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0:
        ref = """DPF Result
----------
specific_heat
Operator name: "CP"
Number of components: 1
Dimensionality: scalar
Homogeneity: specific_heat
Units: J/kg*dK^-1
Location: Nodal
Available qualifier labels:"""  # noqa: E501
    else:
        ref = """DPF Result
----------
specific_heat
Operator name: "CP"
Number of components: 1
Dimensionality: scalar
Homogeneity: specific_heat
Units: J/kg*K^-1
Location: Nodal
Available qualifier labels:"""  # noqa: E501
    ref2 = "'phase': 2"
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0:
        ref3 = "'zone': 11"
    else:
        ref3 = "'zone': 5"
    ar = model.metadata.result_info.available_results[0]
    got = str(ar)
    assert ref in got
    assert ref2 in got
    assert ref3 in got
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0:
        assert len(ar.qualifier_combinations) == 18
    else:
        assert len(ar.qualifier_combinations) == 20


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available with CFF starting 7.0"
)
def test_print_result_info_with_qualifiers(cfx_heating_coil, server_type):
    model = Model(cfx_heating_coil(server=server_type), server=server_type)
    available_results_names = []
    for result in model.metadata.result_info.available_results:
        available_results_names.append(result.name)

    expected_results = [
        "specific_heat",
        "epsilon",
        "enthalpy",
        "turbulent_kinetic_energy",
        "thermal_conductivity",
        "dynamic_viscosity",
        "turbulent_viscosity",
        "static_pressure",
        "total_pressure",
        "density",
        "entropy",
        "temperature",
        "total_temperature",
        "velocity",
    ]
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_11_0:
        expected_results.append("aspect_ratio")
        expected_results.append("static_enthalpy_beta")
        expected_results.append("velocity_u_beta")
        expected_results.append("velocity_v_beta")
        expected_results.append("velocity_w_beta")
        expected_results.append("courant_number")
        expected_results.append("volume_of_finite_volumes")
        expected_results.append("volume_porosity")
        expected_results.append("static_enthalpy_gradient")
        expected_results.append("pressure_gradient")
        expected_results.append("velocity_u_gradient")
        expected_results.append("velocity_v_gradient")
        expected_results.append("velocity_w_gradient")
        expected_results.append("mesh_expansion_factor")
        expected_results.append("orthogonality_angle")
        expected_results.append("absolute_pressure")
        expected_results.append("specific_heat_capacity_at_constant_volume")
        expected_results.append("specific_volume")
        expected_results.append("shear_strain_rate")
        expected_results.append("turbulence_eddy_frequency")

    for result in expected_results:
        assert result in available_results_names


@pytest.mark.skipif(True, reason="Used to test memory leaks")
def test_result_info_memory_leaks(model):
    import gc

    for i in range(1000):
        gc.collect()
        metadata = model.metadata
        res = metadata.result_info
        # Still leaking, but maybe from the Operator.connect
        # in Metadata._load_result_info()
        u = res.unit_system_name
        c = res.cyclic_support
        # v = res.solver_version
        # date = res.solver_date
        # time = res.solver_time
        # na = res.user_name
        # j = res.job_name
        # n = res.product_name
        # t = res.main_title


def test_create_result_info(server_type):
    from ansys.dpf.core.available_result import Homogeneity

    if not server_type.has_client():
        result_info = dpf.core.ResultInfo(
            analysis_type=dpf.core.result_info.analysis_types.static,
            physics_type=dpf.core.result_info.physics_types.mechanical,
            server=server_type,
        )
        result_info.add_result(
            operator_name="operator_name",
            scripting_name="scripting_name",
            homogeneity=Homogeneity.temperature,
            location=dpf.core.locations.nodal,
            nature=dpf.core.natures.scalar,
            dimensions=None,
            description="description",
        )
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
            ref = """Static analysis
Unit system: Undefined
Physics Type: Mechanical
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        elif SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0:
            ref = """Static analysis
Unit system: 
Physics Type: Mechanical
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        else:
            ref = """Static analysis
Unit system: 
Physics Type: Mecanic
Available results:
     -  scripting_name: Nodal Scripting Name
"""
        assert str(result_info) == ref
        with pytest.raises(ValueError, match="requires"):
            _ = dpf.core.ResultInfo()
    else:
        with pytest.raises(NotImplementedError, match="Cannot create a new ResultInfo via gRPC."):
            _ = dpf.core.ResultInfo(
                analysis_type=dpf.core.result_info.analysis_types.static,
                physics_type=dpf.core.result_info.physics_types.mechanical,
                server=server_type,
            )


def test_result_info_add_result(model):
    from ansys.dpf.core.available_result import Homogeneity

    res = model.metadata.result_info
    if not model._server.has_client():
        res.add_result(
            operator_name="operator_name",
            scripting_name="scripting_name",
            homogeneity=Homogeneity.temperature,
            location=dpf.core.locations.nodal,
            nature=dpf.core.natures.scalar,
            dimensions=None,
            description="description",
        )
    else:
        with pytest.raises(
            NotImplementedError, match="Cannot add a result to a ResultInfo via gRPC."
        ):
            res.add_result(
                operator_name="operator_name",
                scripting_name="scripting_name",
                homogeneity=Homogeneity.temperature,
                location=dpf.core.locations.nodal,
                nature=dpf.core.natures.scalar,
                dimensions=None,
                description="description",
            )


@pytest.mark.skipif(
    not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0, reason="Available for servers >=8.0"
)
def test_scripting_name():
    model = Model(examples.download_all_kinds_of_complexity_modal())
    scripting_names = [res.name for res in model.metadata.result_info]
    assert "nmisc" in scripting_names
    assert "smisc" in scripting_names
