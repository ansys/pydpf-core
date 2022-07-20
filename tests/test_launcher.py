import os
import time

import pytest
import psutil
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


server_configs = [
    core.AvailableServerConfigs.InProcessServer,
    core.AvailableServerConfigs.GrpcServer,
    core.AvailableServerConfigs.LegacyGrpcServer
]

server_configs_names = ["InProcessServer",
                        "GrpcServer",
                        "LegacyGrpcServer",
                        ]


@pytest.mark.parametrize("server_config", server_configs, ids=server_configs_names, scope="class")
class TestServerConfigs:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""

        def reset_server():
            core.SERVER = None

        request.addfinalizer(reset_server)

    def test_start_local_wrong_ansys_path(self, server_config):
        with pytest.raises(NotADirectoryError):
            core.start_local_server(ansys_path="test/", use_docker_by_default=False,
                                    config=server_config, as_global=False)

    def test_start_local_custom_ansys_path(self, server_config):
        path = os.environ["AWP_ROOT" + str(core._version.__ansys_version__)]
        os.unsetenv("AWP_ROOT" + str(core._version.__ansys_version__))
        try:
            server = core.start_local_server(ansys_path=path, use_docker_by_default=False,
                                             config=server_config, as_global=True)
            assert isinstance(server.os, str)
            if server_config != core.AvailableServerConfigs.InProcessServer:
                p = psutil.Process(server.info["server_process_id"])
                assert path in p.cwd()
            os.environ["AWP_ROOT" + str(core._version.__ansys_version__)] = path
        except Exception as e:
            os.environ["AWP_ROOT" + str(core._version.__ansys_version__)] = path
            raise e

    def test_start_local_no_ansys_path(self, server_config):
        server = core.start_local_server(use_docker_by_default=False,
                                         config=server_config, as_global=False)
        assert isinstance(server.os, str)
        if server_config != core.AvailableServerConfigs.InProcessServer:
            p = psutil.Process(server.info["server_process_id"])
            assert os.environ["AWP_ROOT" + str(core._version.__ansys_version__)] in p.cwd()

    def test_start_local_ansys_path_environement_variable(self, server_config):
        awp_root = os.environ["AWP_ROOT" + str(core._version.__ansys_version__)]
        try:
            os.environ["ANSYS_DPF_PATH"] = awp_root
            os.unsetenv("AWP_ROOT" + str(core._version.__ansys_version__))
            server = core.start_local_server(use_docker_by_default=False,
                                             config=server_config)
            assert isinstance(server.os, str)
            os.environ["AWP_ROOT" + str(core._version.__ansys_version__)] = awp_root
            os.unsetenv("ANSYS_DPF_PATH")

        except Exception as e:
            os.environ["AWP_ROOT" + str(core._version.__ansys_version__)] = awp_root
            os.unsetenv("ANSYS_DPF_PATH")
            raise e


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
