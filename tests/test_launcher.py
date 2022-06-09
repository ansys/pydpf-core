import os
import pytest

from ansys.dpf import core
# from ansys.dpf.core.misc import is_ubuntu
from ansys.dpf.core.check_version import meets_version, get_server_version

# ansys_path = core.misc.find_ansys()

# invalid_version = None
# if ansys_path is not None:
#     try:
#         invalid_version = int(ansys_path[-3:]) < 211
#     except:
#         invalid_version = True

# # skip unless ansys v212 is installed
# if ansys_path is None or invalid_version or is_ubuntu():
#     pytestmark = pytest.mark.skip("Requires local install of ANSYS 2021R2")


SERVER_VERSION_HIGHER_THAN_2_0 = meets_version(get_server_version(core._global_server()), "2.0")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0,
                    reason='Requires server version at least 2.0')
def test_start_local():
    if not core.SERVER:
        core.start_local_server()
    starting_server = id(core.SERVER)
    n_init = len(core._server_instances)
    core.start_local_server(as_global=False, ansys_path=core.SERVER.ansys_path)
    assert len(core._server_instances) == n_init + 1
    core._server_instances[-1]().shutdown()

    # ensure global channel didn't change
    assert starting_server == id(core.SERVER)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0,
                    reason='Requires server version at least 2.0')
def test_start_local_failed():
    with pytest.raises(NotADirectoryError):
        core.start_local_server(ansys_path="", use_docker_by_default=False)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0,
                    reason='Requires server version at least 2.0')
def test_start_local_failed_executable():
    from ansys.dpf.core._version import __ansys_version__
    from ansys.dpf.core.server import find_ansys
    from pathlib import Path
    with pytest.raises(FileNotFoundError):
        path = Path(os.environ.get("AWP_ROOT" + __ansys_version__,
                                   find_ansys())).parent.absolute()
        core.start_local_server(ansys_path=path)


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_2_0,
                    reason='Requires server version at least 2.0')
def test_server_ip():
    assert core.SERVER.ip is not None
    assert core.SERVER.port is not None
    assert core.SERVER.version is not None
    assert core.SERVER.info["server_process_id"] is not None
    assert core.SERVER.info["server_ip"] is not None
    assert core.SERVER.info["server_port"] is not None
    assert core.SERVER.info["server_version"] is not None
