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

import os
from pathlib import Path

import pytest
import psutil
import subprocess
import sys
import io
from ansys.dpf import core
from conftest import (
    SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    configsserver_type,
    config_namesserver_type,
    running_docker,
)


@pytest.mark.skipif(running_docker, reason="Run to fix on internal side")
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


@pytest.mark.parametrize(
    "server_config", configsserver_type, ids=config_namesserver_type, scope="class"
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
        ver_to_check = core._version.server_to_ansys_version[str(core.global_server().version)]
        ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
        awp_root_name = "AWP_ROOT" + ver_to_check
        path = os.environ.get(awp_root_name, None)
        if path:
            try:
                os.unsetenv(awp_root_name)
            except:
                del os.environ[awp_root_name]
            try:
                server = core.start_local_server(
                    ansys_path=path,
                    config=server_config,
                    as_global=True,
                )
                assert isinstance(server.os, str)
                if (
                    server_config != core.AvailableServerConfigs.InProcessServer
                    and not running_docker
                ):
                    p = psutil.Process(server.info["server_process_id"])
                    assert path in p.cwd()
                if path:
                    os.environ[awp_root_name] = path
            except Exception as e:
                if path:
                    os.environ[awp_root_name] = path
                raise e
        else:
            pytest.skip(awp_root_name + " is not set")

    @pytest.mark.skipif(running_docker, reason="AWP ROOT is not set with Docker")
    def test_start_local_no_ansys_path(self, server_config):
        server = core.start_local_server(
            use_docker_by_default=False, config=server_config, as_global=False
        )
        assert isinstance(server.os, str)
        if server_config != core.AvailableServerConfigs.InProcessServer:
            p = psutil.Process(server.info["server_process_id"])
            ver_to_check = core._version.server_to_ansys_version[str(server.version)]
            ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
            if os.environ.get("AWP_ROOT" + ver_to_check, None) is not None:
                assert os.environ["AWP_ROOT" + ver_to_check] in p.cwd()

    @pytest.mark.skipif(
        not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
        reason="Ans.Dpf.Grpc.bat and .sh need AWP_ROOT221 for 221 install",
    )
    def test_start_local_ansys_path_environment_variable(self, server_config):
        ver_to_check = core._version.server_to_ansys_version[str(core.SERVER.version)]
        ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
        awp_root_name = "AWP_ROOT" + ver_to_check
        awp_root = os.environ.get(awp_root_name, None)
        try:
            if awp_root:
                os.environ["ANSYS_DPF_PATH"] = awp_root
                try:
                    os.unsetenv(awp_root_name)
                except:
                    del os.environ[awp_root_name]
            server = core.start_local_server(config=server_config)
            assert isinstance(server.os, str)
            if awp_root:
                os.environ[awp_root_name] = awp_root
            try:
                os.unsetenv("ANSYS_DPF_PATH")
            except:
                del os.environ["ANSYS_DPF_PATH"]

        except Exception as e:
            if awp_root_name and awp_root:
                os.environ[awp_root_name] = awp_root
            if "ANSYS_DPF_PATH" in os.environ.keys():
                try:
                    os.unsetenv("ANSYS_DPF_PATH")
                except:
                    del os.environ["ANSYS_DPF_PATH"]
                raise e

    @pytest.mark.skipif(running_docker, reason="Not made to work on docker")
    def test_start_local_wrong_ansys_path(self, server_config):
        if server_config != core.AvailableServerConfigs.InProcessServer:
            try:
                core.start_local_server(
                    ansys_path="test/",
                    use_docker_by_default=False,
                    config=server_config,
                    as_global=False,
                )
                raise AssertionError("didn't raise NotADirectoryError nor ModuleNotFoundError")
            except NotADirectoryError:
                pass
            except ModuleNotFoundError:
                pass

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
            with io.TextIOWrapper(process.stderr, encoding="utf-8") as log_err:
                for line in log_err:
                    errors += line
                if process.returncode is not None:
                    raise Exception(errors)

    @pytest.mark.skipif(running_docker, reason="Not made to work on docker")
    def test_launch_server_full_path(self, server_config):
        ansys_path = core.misc.get_ansys_path()
        if os.name == "nt":
            path = Path(ansys_path) / "aisol" / "bin" / "winx64"
        else:
            if server_config.protocol == core.server_factory.CommunicationProtocols.InProcess:
                path = Path(ansys_path) / "aisol" / "dll" / "linx64"
            elif (
                server_config.protocol == core.server_factory.CommunicationProtocols.gRPC
                and server_config.legacy is False
            ):
                # full path is not working because DPFClientAPI and
                # Ans.Dpf.Grpc.sh reside in two different folders
                return
            else:
                path = Path(ansys_path) / "aisol" / "bin" / "linx64"

        # print("trying to launch on ", path)
        # print(os.listdir(path))
        server = core.start_local_server(
            as_global=False, ansys_path=str(path), config=server_config
        )
        assert "server_port" in server.info


@pytest.mark.skipif(running_docker, reason="Not made to work on docker")
def test_start_local_failed_executable(remote_config_server_type):
    from ansys.dpf.core.misc import get_ansys_path
    from pathlib import Path

    with pytest.raises(FileNotFoundError):
        path = Path(get_ansys_path()).parent.absolute()
        core.start_local_server(ansys_path=str(path), config=remote_config_server_type)


@pytest.mark.skipif(not running_docker, reason="Checks docker start server")
def test_start_docker_without_awp_root(restore_awp_root, server_clayer_remote_process):
    ver_to_check = core._version.server_to_ansys_version[str(server_clayer_remote_process.version)]
    ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
    awp_root_name = "AWP_ROOT" + ver_to_check
    # delete awp_root
    if os.environ.get(awp_root_name, None):
        del os.environ[awp_root_name]

    serv = core.start_local_server(as_global=False)

    assert serv.ip is not None


def test_server_ip(server_type_remote_process):
    assert server_type_remote_process.ip is not None
    assert server_type_remote_process.port is not None
    assert server_type_remote_process.version is not None
    assert server_type_remote_process.info["server_process_id"] is not None
    assert server_type_remote_process.info["server_ip"] is not None
    assert server_type_remote_process.info["server_port"] is not None
    assert server_type_remote_process.info["server_version"] is not None


@pytest.mark.skipif(
    os.environ.get("DPF_SERVER_TYPE", None) is None,
    reason="This test is for a run with default server type",
)
def test_start_with_dpf_server_type_env():
    dpf_server_type_str = "DPF_SERVER_TYPE"
    try_serv_type = os.environ.get(dpf_server_type_str, None)
    if try_serv_type:
        raise Exception(
            "Fixture is not correctly working"
        )  # a specific case is already set to run the unit tests
    else:
        if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 and not running_docker:
            # test for v222 and higher
            os.environ[dpf_server_type_str] = "GRPC"
            my_serv = core.start_local_server(as_global=False)
            assert isinstance(my_serv, core.server_types.GrpcServer)
            my_serv.shutdown()

            os.environ[dpf_server_type_str] = "LEGACYGRPC"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)
            my_serv_2.shutdown()

            os.environ[dpf_server_type_str] = "INPROCESS"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.InProcessServer)

            os.environ[dpf_server_type_str] = "bla"
            with pytest.raises(NotImplementedError):
                my_serv_3 = core.start_local_server(as_global=False)

            del os.environ[dpf_server_type_str]
        elif running_docker:
            # test for v221 and lower
            os.environ[dpf_server_type_str] = "GRPC"
            my_serv = core.start_local_server(as_global=False)
            assert isinstance(my_serv, core.server_types.GrpcServer)
            my_serv.shutdown()

            os.environ[dpf_server_type_str] = "LEGACYGRPC"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)
            my_serv_2.shutdown()

            del os.environ[dpf_server_type_str]
        else:
            # test for v221 and lower
            os.environ[dpf_server_type_str] = "GRPC"
            my_serv = core.start_local_server(as_global=False)
            assert isinstance(my_serv, core.server_types.LegacyGrpcServer)
            my_serv.shutdown()

            os.environ[dpf_server_type_str] = "LEGACYGRPC"
            my_serv_2 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_2, core.server_types.LegacyGrpcServer)
            my_serv_2.shutdown()

            os.environ[dpf_server_type_str] = "bla"
            my_serv_3 = core.start_local_server(as_global=False)
            assert isinstance(my_serv_3, core.server_types.LegacyGrpcServer)
            my_serv_3.shutdown()

            del os.environ[dpf_server_type_str]
