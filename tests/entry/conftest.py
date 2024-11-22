# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

"""This runs at the init of the pytest session for Entry tests.

Must be run separately from the other tests.

Launch or connect to a persistent local Entry DPF server to be shared in
pytest as a session fixture
"""

import os
import functools
import pytest

os.environ["ANSYS_DPF_SERVER_CONTEXT"] = "ENTRY"  # MANDATORY

import ansys.dpf.core.server_types
from ansys.dpf import core
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.check_version import meets_version, get_server_version


core.set_default_server_context(core.AvailableServerContexts.entry)  # MANDATORY

core.settings.disable_off_screen_rendering()
os.environ["PYVISTA_OFF_SCREEN"] = "true"
core.settings.bypass_pv_opengl_osmesa_crash()
os.environ["MPLBACKEND"] = "Agg"
# currently running dpf on docker.  Used for testing on CI
DPF_SERVER_TYPE = os.environ.get("DPF_SERVER_TYPE", None)
running_docker = ansys.dpf.core.server_types.RUNNING_DOCKER.use_docker
local_test_repo = False


def _get_test_files_directory():
    if local_test_repo is False:
        test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(test_path, os.pardir, "tests", "testfiles")
    else:
        return os.path.join(os.environ["AWP_UNIT_TEST_FILES"], "python")


if os.name == "posix":
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context

if running_docker:
    ansys.dpf.core.server_types.RUNNING_DOCKER.mounted_volumes[_get_test_files_directory()] = (
        "/tmp/test_files"
    )

SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_1 = meets_version(
    get_server_version(core._global_server()), "8.1"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0 = meets_version(
    get_server_version(core._global_server()), "8.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1 = meets_version(
    get_server_version(core._global_server()), "6.1"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0 = meets_version(
    get_server_version(core._global_server()), "6.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0 = meets_version(
    get_server_version(core._global_server()), "5.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 = meets_version(
    get_server_version(core._global_server()), "4.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0 = meets_version(
    get_server_version(core._global_server()), "3.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_2_0 = meets_version(
    get_server_version(core._global_server()), "2.1"
)


def raises_for_servers_version_under(version):
    """Launch the test normally if the server version is equal or higher than the "version"
    parameter. Else it makes sure that the test fails by raising a "DpfVersionNotSupported"
    error.
    """

    def decorator(func):
        @pytest.mark.xfail(
            not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0
            if version == "3.0"
            else not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
            if version == "4.0"
            else not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0
            if version == "5.0"
            else not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0
            if version == "6.0"
            else True,
            reason=f"Requires server version greater than or equal to {version}",
            raises=core.errors.DpfVersionNotSupported,
        )
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    return decorator


def remove_none_available_config(configs, config_names):
    configs_out = []
    config_names_out = []
    if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0:
        for conf, conf_name in zip(configs, config_names):
            if conf == core.AvailableServerConfigs.LegacyGrpcServer:
                configs_out.append(conf)
                config_names_out.append(conf_name)
    elif running_docker:
        for conf, conf_name in zip(configs, config_names):
            if conf != core.AvailableServerConfigs.InProcessServer:
                configs_out.append(conf)
                config_names_out.append(conf_name)

    else:
        configs_out = configs
        config_names_out = config_names

    return configs_out, config_names_out


(
    configs_server_type_remote_process,
    config_names_server_type_remote_process,
) = remove_none_available_config(
    [
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
    ],
    ["ansys-grpc-dpf", "gRPC CLayer"],
)


@pytest.fixture(
    scope="package",
    params=configs_server_type_remote_process,
    ids=config_names_server_type_remote_process,
)
def remote_config_server_type(request):
    return request.param


@pytest.fixture(autouse=False, scope="function")
def restore_accept_la_env(request):
    """Restores env ANSYS_DPF_ACCEPT_LA."""

    init_val = os.environ.get("ANSYS_DPF_ACCEPT_LA", None)

    def revert():
        if init_val:
            os.environ["ANSYS_DPF_ACCEPT_LA"] = init_val

    request.addfinalizer(revert)
