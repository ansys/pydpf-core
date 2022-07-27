import os

import pytest
import psutil
import subprocess
import sys
import io
from ansys.dpf import core
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0, DPF_SERVER_TYPE


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


server_configs = (
    [
        core.AvailableServerConfigs.InProcessServer,
        core.AvailableServerConfigs.GrpcServer,
        core.AvailableServerConfigs.LegacyGrpcServer,
    ]
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
    else [core.AvailableServerConfigs.LegacyGrpcServer]
)

server_configs_names = (
    [
        "InProcessServer",
        "GrpcServer",
        "LegacyGrpcServer",
    ]
    if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
    else ["LegacyGrpcServer"]
)


@pytest.mark.parametrize(
    "server_config", server_configs, ids=server_configs_names, scope="class"
)
class TestServerConfigs:
    @pytest.fixture(scope="class", autouse=True)
    def cleanup(self, request):
        """Cleanup a testing directory once we are finished."""

        def reset_server():
            core.SERVER = None

        request.addfinalizer(reset_server)

    @pytest.mark.skipif(
        not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
        reason="Ans.Dpf.Grpc.bat and .sh need AWP_ROOT221 for 221 install",
    )
    def test_start_local_custom_ansys_path(self, server_config):
        path = os.environ["AWP_ROOT" + str(core._version.__ansys_version__)]
        try:
            os.unsetenv("AWP_ROOT" + str(core._version.__ansys_version__))
        except:
            del os.environ["AWP_ROOT" + str(core._version.__ansys_version__)]
        try:
            server = core.start_local_server(
                ansys_path=path,
                use_docker_by_default=False,
                config=server_config,
                as_global=True,
            )
            assert isinstance(server.os, str)
            if server_config != core.AvailableServerConfigs.InProcessServer:
                p = psutil.Process(server.info["server_process_id"])
                assert path in p.cwd()
            os.environ[
                "AWP_ROOT" + str(core._version.__ansys_version__)
            ] = path
        except Exception as e:
            os.environ[
                "AWP_ROOT" + str(core._version.__ansys_version__)
            ] = path
            raise e

    def test_start_local_no_ansys_path(self, server_config):
        server = core.start_local_server(
            use_docker_by_default=False, config=server_config, as_global=False
        )
        assert isinstance(server.os, str)
        if server_config != core.AvailableServerConfigs.InProcessServer:
            p = psutil.Process(server.info["server_process_id"])
            ver_to_check = core._version.server_to_ansys_version[str(server.version)]
            ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
            assert (
                os.environ["AWP_ROOT" + ver_to_check]
                in p.cwd()
            )

    @pytest.mark.skipif(
        not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
        reason="Ans.Dpf.Grpc.bat and .sh need AWP_ROOT221 for 221 install",
    )
    def test_start_local_ansys_path_environment_variable(self, server_config):
        awp_root = os.environ[
            "AWP_ROOT" + str(core._version.__ansys_version__)
        ]
        try:
            os.environ["ANSYS_DPF_PATH"] = awp_root
            try:
                os.unsetenv("AWP_ROOT" + str(core._version.__ansys_version__))
            except:
                del os.environ[
                    "AWP_ROOT" + str(core._version.__ansys_version__)
                ]
            server = core.start_local_server(
                use_docker_by_default=False, config=server_config
            )
            assert isinstance(server.os, str)
            os.environ[
                "AWP_ROOT" + str(core._version.__ansys_version__)
            ] = awp_root
            try:
                os.unsetenv("ANSYS_DPF_PATH")
            except:
                del os.environ["ANSYS_DPF_PATH"]

        except Exception as e:
            os.environ[
                "AWP_ROOT" + str(core._version.__ansys_version__)
            ] = awp_root
            try:
                os.unsetenv("ANSYS_DPF_PATH")
            except:
                del os.environ["ANSYS_DPF_PATH"]
            raise e

    def test_start_local_wrong_ansys_path(self, server_config):
        if server_config != core.AvailableServerConfigs.InProcessServer:

            def test_start_local_wrong_ansys_path(self, server_config):
                with pytest.raises(NotADirectoryError):
                    core.start_local_server(
                        ansys_path="test/",
                        use_docker_by_default=False,
                        config=server_config,
                        as_global=False,
                    )

        # the test for in process should be done in another process because if dataProcessingCore
        # is already loaded, no error will be raised
        else:
            process = subprocess.Popen(
                [
                    sys.executable,
                    "-c",
                    "from ansys.dpf import core\n"
                    "try:\n"
                    "    core.start_local_server(ansys_path='test/', use_docker_by_default=False,"
                    "config=core.server_factory.AvailableServerConfigs.InProcessServer,"
                    " as_global=False)\n"
                    "except NotADirectoryError:\n"
                    "    exit()\n"
                    "raise Exception('should have raised NotADirectoryError')\n",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            errors = ""
            for line in io.TextIOWrapper(process.stderr, encoding="utf-8"):
                errors += line
            if process.returncode is not None:
                raise Exception(errors)


def test_start_local_failed_executable():
    from ansys.dpf.core.misc import get_ansys_path
    from pathlib import Path

    with pytest.raises(FileNotFoundError):
        path = Path(get_ansys_path()).parent.absolute()
        core.start_local_server(ansys_path=path)


def test_server_ip(server_type_remote_process):
    assert server_type_remote_process.ip is not None
    assert server_type_remote_process.port is not None
    assert server_type_remote_process.version is not None
    assert server_type_remote_process.info["server_process_id"] is not None
    assert server_type_remote_process.info["server_ip"] is not None
    assert server_type_remote_process.info["server_port"] is not None
    assert server_type_remote_process.info["server_version"] is not None


@pytest.mark.skipif(DPF_SERVER_TYPE is not None,
                    reason="This test is for a run with default server type")
def test_start_with_dpf_server_type_env():
    dpf_server_type_str = "DPF_SERVER_TYPE"
    try_serv_type = os.environ.get(dpf_server_type_str, None)
    if try_serv_type:
        raise Exception("Fixture is not correctly working")  # a specific case is already set to run the unit tests
    else:
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0:
            # test for v222 and higher
            os.environ[dpf_server_type_str] = "GRPC"
            my_serv = core.start_local_server(as_global=False)
            assert isinstance(my_serv, core.server_types.GrpcServer)

            os.environ[dpf_server_type_str] = "LEGACYGRPC"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)

            os.environ[dpf_server_type_str] = "bla"
            with pytest.raises(NotImplementedError):
                my_serv_3 = core.start_local_server(as_global=False)

            del os.environ[dpf_server_type_str]
        else:
            # test for v221 and lower
            os.environ[dpf_server_type_str] = "GRPC"
            my_serv = core.start_local_server(as_global=False)
            assert isinstance(my_serv, core.server_types.LegacyGrpcServer)

            os.environ[dpf_server_type_str] = "LEGACYGRPC"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)

            os.environ[dpf_server_type_str] = "bla"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)

            del os.environ[dpf_server_type_str]
