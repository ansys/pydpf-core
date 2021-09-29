from ansys.dpf.core import Model
from ansys.dpf.core import check_version
from ansys.dpf.core import errors as dpf_errors
import pytest


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


def test_version_tuple():
    t1 = "2.0.0"
    t1_check = 2, 0, 0
    t1_get = check_version.version_tuple(t1)
    assert t1_get == t1_check
    t2 = "2.0"
    t2_check = 2, 0, 0
    t2_get = check_version.version_tuple(t2)
    assert t2_get == t2_check


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
