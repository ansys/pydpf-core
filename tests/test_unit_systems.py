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
from ansys.dpf.core import errors as dpf_errors
import conftest


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1,
    reason="Unit systems where not supported before 6.1.",
)
def test_predefined_unit_systems():
    # Test IDs of the predefined ones
    assert dpf.unit_systems.solver_mks.ID == 11
    assert dpf.unit_systems.solver_cgs.ID == 5
    assert dpf.unit_systems.solver_nmm.ID == 6
    assert dpf.unit_systems.solver_bft.ID == 7
    assert dpf.unit_systems.solver_bin.ID == 8
    assert dpf.unit_systems.solver_umks.ID == 10
    assert dpf.unit_systems.solver_knms.ID == 16
    assert dpf.unit_systems.undefined.ID == -1

    assert dpf.unit_systems.solver_mks.name == "solver_mks"
    assert dpf.unit_systems.solver_cgs.name == "solver_cgs"
    assert dpf.unit_systems.solver_nmm.name == "solver_nmm"
    assert dpf.unit_systems.solver_bft.name == "solver_bft"
    assert dpf.unit_systems.solver_bin.name == "solver_bin"
    assert dpf.unit_systems.solver_umks.name == "solver_umks"
    assert dpf.unit_systems.solver_knms.name == "solver_knms"
    assert dpf.unit_systems.undefined.name == "undefined"


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1,
    reason="Unit systems where not supported before 6.1.",
)
def test_unit_system_api():
    # Create custom units from ID
    my_mks = dpf.UnitSystem("mks", ID=11)
    mks_units = my_mks.unit_names.split(";")
    assert "m" in mks_units
    assert "kg" in mks_units
    assert "s" in mks_units
    assert "degC" in mks_units
    assert "C" in mks_units
    assert "rad" in mks_units

    # Create custom units from UnitSystem
    my_mks = dpf.UnitSystem("mks", unit_names="m;kg;degC;rad;C;s")
    mks_units = my_mks.unit_names.split(";")
    assert "m" in mks_units
    assert "kg" in mks_units
    assert "s" in mks_units
    assert "degC" in mks_units
    assert "C" in mks_units
    assert "rad" in mks_units

    # name is not a string
    with pytest.raises(dpf_errors.InvalidTypeError) as e:
        dpf.UnitSystem(1, ID=2)
        assert "str" in e

    # unit_names not used
    with pytest.raises(dpf_errors.InvalidTypeError) as e:
        dpf.UnitSystem("throw_1", "m;kg;K;rad;C;s")
        assert "ID" in e

    # ID and unit_names used at the same time
    with pytest.raises(Exception) as e:
        dpf.UnitSystem("throw_2", ID=1, unit_names="m;kg;K;rad;C;s")
        assert (
            "ID and unit_names are mutually exclusionary, but one of them should be provided." in e
        )

    # incomplete unit system
    with pytest.raises(Exception) as e:
        dpf.UnitSystem("throw_3", unit_names="in;kg")
        assert "Some of the basic Units are not present in the UnitSystem definition" in e

    # wrong separator in unit system
    with pytest.raises(Exception) as e:
        dpf.UnitSystem("throw_4", unit_names="in,kg,h,C,degF,deg")
        assert "Unit strings must be separated by semicolons" in e

    # incorrect unit strings
    with pytest.raises(Exception) as e:
        dpf.UnitSystem("throw_5", unit_names="asd;awe")
        assert '"asd" is not a valid unit.' in e

    # unit_names is not a string
    with pytest.raises(dpf_errors.InvalidTypeError) as e:
        dpf.UnitSystem("throw_6", unit_names=1)
        assert "str" in e
