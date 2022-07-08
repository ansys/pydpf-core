import os
import pytest
from ansys.dpf import core


def test_start_local():
    if not core.SERVER:
        core.start_local_server()
    starting_server = id(core.SERVER)
    n_init = len(core._server_instances)
    server = core.start_local_server(as_global=False)
    assert len(core._server_instances) == n_init + 1
    server.shutdown()
    # ensure global channel didn't change
    assert starting_server == id(core.SERVER)


def test_start_local_failed():
    with pytest.raises(NotADirectoryError):
        core.start_local_server(ansys_path="test/", use_docker_by_default=False)


def test_start_local_failed_executable():
    from ansys.dpf.core._version import __ansys_version__
    from ansys.dpf.core.server import find_ansys
    from pathlib import Path
    with pytest.raises(FileNotFoundError):
        path = Path(os.environ.get("AWP_ROOT" + __ansys_version__,
                                   find_ansys())).parent.absolute()
        core.start_local_server(ansys_path=path)


def test_server_ip(server_type_remote_process):
    assert server_type_remote_process.ip != None
    assert server_type_remote_process.port != None
    assert server_type_remote_process.version != None
    assert server_type_remote_process.info["server_process_id"] != None
    assert server_type_remote_process.info["server_ip"] != None
    assert server_type_remote_process.info["server_port"] != None
    assert server_type_remote_process.info["server_version"] != None

