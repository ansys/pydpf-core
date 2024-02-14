import pytest

from ansys.dpf.core import Model
from ansys.dpf.core import check_version
from ansys.dpf.core import errors as dpf_errors

from ansys.dpf.gate.load_api import _find_outdated_ansys_version


def test_get_server_version(multishells):
    model = Model(multishells)
    server = model._server
    # version without specifying server
    version_blank = check_version.get_server_version()
    assert isinstance(version_blank, str)
    v_blank = float(version_blank)
    assert v_blank >= 2.0
    # version specifying sever
    version = check_version.get_server_version(server)
    assert isinstance(version, str)
    v = float(version)
    assert v >= 2.0


def test_check_server_version_dpfserver(multishells):
    # this test is working because the server version format is "MAJOR.MINOR".
    # It can be adapted if this is evolving.
    model = Model(multishells)
    server = model._server
    v = check_version.get_server_version()
    split = v.split(".")
    l = 2
    assert len(split) == l
    server.check_version(v)
    v_with_patch = v + ".0"
    server.check_version(v_with_patch)
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        n = len(split[l - 1])
        v_up = v[0:n] + "1"
        server.check_version(v_up)
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        v_up_patch = v + ".1"
        server.check_version(v_up_patch)


def test_check_server_version_checkversion(multishells):
    # this test is working because the server version format is "MAJOR.MINOR".
    # It can be adapted if this is evolving.
    model = Model(multishells)
    server = model._server
    v = check_version.get_server_version()
    split = v.split(".")
    l = 2
    assert len(split) == l
    check_version.server_meet_version_and_raise(v, server)
    v_with_patch = v + ".0"
    check_version.server_meet_version_and_raise(v_with_patch, server)
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        n = len(split[l - 1])
        v_up = v[0:n] + "1"
        check_version.server_meet_version_and_raise(v_up, server)
    with pytest.raises(dpf_errors.DpfVersionNotSupported):
        v_up_patch = v + ".1"
        check_version.server_meet_version_and_raise(v_up_patch, server)


def test_meets_version():
    # first is server version, second is version to meet
    assert check_version.meets_version("1.32.0", "1.31.0")
    assert check_version.meets_version("1.32.1", "1.32.0")
    assert check_version.meets_version("1.32.0", "1.32.0")
    assert check_version.meets_version("1.32", "1.32")
    assert check_version.meets_version("1.32", "1.31")
    assert check_version.meets_version("1.32", "1.31.0")
    assert check_version.meets_version("1.32.0", "1.31")
    assert check_version.meets_version("1.32.0", "1.31.1")
    assert not check_version.meets_version("1.31.0", "1.32")
    assert not check_version.meets_version("1.31.0", "1.32.0")
    assert not check_version.meets_version("1.31.1", "1.32")
    assert not check_version.meets_version("1.31.1", "1.32.1")
    assert not check_version.meets_version("1.31", "1.32")
    assert not check_version.meets_version("1.31.0", "1.31.1")


def test_find_outdated_ansys_version():
    arg1 = "v3RG bla v21a ghldv3EF"
    arg2 = "v3RG bla v212 ghldv3EF"
    arg3 = "v3RG bla v222 ghldv3EF"
    arg4 = "v3RGldv3"
    arg5 = "v"
    arg6 = "a"
    arg7 = "blav221hlof"
    assert _find_outdated_ansys_version(arg1) == False
    assert _find_outdated_ansys_version(arg2) == True
    assert _find_outdated_ansys_version(arg3) == False
    assert _find_outdated_ansys_version(arg4) == False
    assert _find_outdated_ansys_version(arg5) == False
    assert _find_outdated_ansys_version(arg6) == False
    assert _find_outdated_ansys_version(arg7) == True


def test_version():
    from ansys.dpf.core._version import server_to_ansys_version

    assert server_to_ansys_version["1.0"] == "2021R1"
    assert server_to_ansys_version["2099.9"] == "2099R9"
