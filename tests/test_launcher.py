import pytest

from ansys.dpf import core
from ansys.dpf.core.misc import is_ubuntu

ansys_path = core.misc.find_ansys()

invalid_version = None
if ansys_path is not None:
    try:
        invalid_version = int(ansys_path[-3:]) < 211
    except:
        invalid_version = True

# skip unless ansys v212 is installed
if ansys_path is None or invalid_version or is_ubuntu():
    pytestmark = pytest.mark.skip("Requires local install of ANSYS 2021R2")


def test_start_local():
    if not core.SERVER:
        core.start_local_server()
    starting_server = id(core.SERVER)
    n_init = len(core._server_instances)
    server = core.start_local_server(as_global=False, ansys_path=core.SERVER.ansys_path)
    assert len(core._server_instances) == n_init + 1
    core._server_instances[-1]().shutdown()

    # ensure global channel didn't change
    assert starting_server == id(core.SERVER)


def test_start_local_failed():
    with pytest.raises(NotADirectoryError):
        core.start_local_server(ansys_path="test/", use_docker_by_default=False)


def test_server_ip(server_type_remote_process):
    assert server_type_remote_process.ip != None
    assert server_type_remote_process.port != None
    assert server_type_remote_process.version != None

    assert server_type_remote_process.info["server_process_id"] != None
    assert server_type_remote_process.info["server_ip"] != None
    assert server_type_remote_process.info["server_port"] != None
    assert server_type_remote_process.info["server_version"] != None
