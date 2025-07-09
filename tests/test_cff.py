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

from ansys.dpf import core as dpf
import conftest


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_cff_model(server_type, fluent_multi_species):
    ds = fluent_multi_species(server_type)
    model = dpf.Model(ds, server=server_type)
    assert "Fluid" in str(model)
    assert model is not None
    mesh = model.metadata.meshed_region
    assert "faces" in str(mesh)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_results_cfx(cfx_heating_coil, server_type):
    model = dpf.Model(cfx_heating_coil(server=server_type), server=server_type)
    # print(model)
    result_names = [
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
    for result_name in result_names:
        result_op = getattr(model.results, result_name)()
        result = result_op.eval()
        assert isinstance(result, dpf.FieldsContainer)
        result_op.connect(1000, {"phase": 2})
        result = result_op.eval()
        assert isinstance(result, dpf.FieldsContainer)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_results_fluent(fluent_mixing_elbow_steady_state, server_type):
    model = dpf.Model(fluent_mixing_elbow_steady_state(server=server_type), server=server_type)
    # print(model)
    result_names = [
        "epsilon",
        "enthalpy",
        "turbulent_kinetic_energy",
        "mach_number",
        "mass_flow_rate",
        "dynamic_viscosity",
        "turbulent_viscosity",
        "static_pressure",
        "surface_heat_rate",
        "density",
        "temperature",
        "velocity",
        "y_plus",
    ]
    for result_name in result_names:
        result_op = getattr(model.results, result_name)()
        result = result_op.eval()
        assert isinstance(result, dpf.FieldsContainer)
        result_op.connect(1000, {"phase": 1})
        result = result_op.eval()
        assert isinstance(result, dpf.FieldsContainer)
