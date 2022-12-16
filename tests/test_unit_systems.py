import pytest
import conftest
from ansys.dpf import core as dpf
from ansys.dpf.core import errors as dpf_errors

@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='unit systems where not supported before 0.6')
def test_predefined_unit_systems():
    # Test ids of the predefined ones
    assert dpf.unit_systems.SI.id == 0
    assert dpf.unit_systems.ansys_cgs.id == 1
    assert dpf.unit_systems.ansys_nmm.id == 2
    assert dpf.unit_systems.ansys_cust.id == 12
    assert dpf.unit_systems.ansys_bin.id == 4
    assert dpf.unit_systems.ansys_umks.id == 9
    assert dpf.unit_systems.ansys_knms.id == 15
    assert dpf.unit_systems.solver_mks.id == 11
    assert dpf.unit_systems.solver_cgs.id == 5
    assert dpf.unit_systems.solver_nmm.id == 6
    assert dpf.unit_systems.solver_bft.id == 7
    assert dpf.unit_systems.solver_bin.id == 8
    assert dpf.unit_systems.solver_umks.id == 10
    assert dpf.unit_systems.solver_knms.id == 16
    assert dpf.unit_systems.undefined.id == -1


@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='unit systems where not supported before 0.6')
def test_unit_system_api():
    # Create custom units from id
    my_mks = dpf.UnitSystem("mks", id=11)
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

    # unit_names not used
    with pytest.raises(dpf_errors.InvalidTypeError) as e:
        wrong_us = dpf.UnitSystem("throw_1", "m;kg;K;rad;C;s")
        assert "id" in e

    # id and unit_names used at the same time
    with pytest.raises(Exception) as e:
        wrong_us = dpf.UnitSystem("throw_2", id = 1, unit_names = "m;kg;K;rad;C;s")
        assert "id and unit_names are mutually exclusionary, but one of them should be provided." in e

    # incomplete unit system
    with pytest.raises(Exception) as e:
        wrong_us = dpf.UnitSystem("throw_3", unit_names="in;kg")
        assert "Some of the basic Units are not present in the UnitSystem definition" in e

    # wrong separator in unit system
    with pytest.raises(Exception) as e:
        wrong_us = dpf.UnitSystem("throw_4", unit_names="in,kg,h,C,degF,deg")
        assert "Unit strings must be seperated by semicolons" in e

    # incorrect unit strings
    with pytest.raises(Exception) as e:
        wrong_us = dpf.UnitSystem("throw_4", unit_names="asd;awe")
        assert "\"asd\" is not a valid unit." in e
