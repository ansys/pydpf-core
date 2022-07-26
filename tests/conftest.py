"""This runs at the init of the pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a session fixture
"""
import os
import functools

import psutil
import pytest

import ansys.dpf.core.server_types
from ansys.dpf import core
from ansys.dpf.core import examples
from ansys.dpf.core import path_utilities
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.check_version import meets_version, get_server_version
from ansys.dpf.gate.load_api import _try_use_gatebin
import warnings

ACCEPTABLE_FAILURE_RATE = 0

core.settings.disable_off_screen_rendering()
# currently running dpf on docker.  Used for testing on CI
running_docker = ansys.dpf.core.server_types.RUNNING_DOCKER["use_docker"]

local_test_repo = False

if os.name == "posix":
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context

if running_docker:
    if local_test_repo:
        core.server_types.RUNNING_DOCKER["args"] += (
            ' -v "'
            f'{os.environ.get("AWP_UNIT_TEST_FILES", False)}'
            ':/tmp/test_files"'
        )


@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    if os.name == "posix":
        # accept ACCEPTABLE_FAILURE_RATE percent of failure on Linux
        if exitstatus != pytest.ExitCode.TESTS_FAILED:
            return
        failure_rate = (100.0 * session.testsfailed) / session.testscollected
        if failure_rate <= ACCEPTABLE_FAILURE_RATE:
            session.exitstatus = 0
    else:
        return exitstatus


def resolve_test_file(basename, additional_path="", is_in_examples=None):
    """Resolves a test file's full path based on the base name and the
    environment.

    Normally returns local path unless server is running on docker and
    this repository has been mapped to the docker image at /dpf.
    """
    if local_test_repo is False:
        if is_in_examples:
            return getattr(examples, is_in_examples)
        else:
            # otherwise, assume file is local
            test_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "tests"
            )
            test_files_path = os.path.join(test_path, "testfiles")
            filename = os.path.join(test_files_path, additional_path, basename)
            if not os.path.isfile(filename):
                raise FileNotFoundError(
                    f"Unable to locate {basename} at {test_files_path}"
                )
            return filename
    elif os.environ.get("AWP_UNIT_TEST_FILES", False):
        if running_docker:
            return path_utilities.join(
                "/tmp/test_files", "python", additional_path, basename
            )
        test_files_path = os.path.join(os.environ["AWP_UNIT_TEST_FILES"], "python")
        filename = os.path.join(
            test_files_path, os.path.join(additional_path, basename)
        )
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Unable to locate {basename} at {test_files_path}")
        return filename


@pytest.fixture()
def allkindofcomplexity():
    """Resolve the path of the "allKindOfComplexity.rst" result file."""
    return examples.download_all_kinds_of_complexity()


@pytest.fixture()
def simple_bar():
    """Resolve the path of the "ASimpleBar.rst" result file."""
    return resolve_test_file("ASimpleBar.rst", "", "simple_bar")


@pytest.fixture()
def velocity_acceleration():
    """Resolve the path of the "velocity_acceleration.rst" result file."""
    return resolve_test_file("velocity_acceleration.rst", "rst_operators")


@pytest.fixture()
def cyclic_lin_rst():
    """Resolve the path of the "cyclic/file.rst" result file."""
    return resolve_test_file("file.rst", "cyclic")


@pytest.fixture()
def cyclic_ds():
    """Resolve the path of the "cyclic/ds.dat" result file."""
    return resolve_test_file("ds.dat", "cyclic")


@pytest.fixture()
def fields_container_csv():
    """Resolve the path of the "csvToField/fields_container.csv" result file."""
    return resolve_test_file("fields_container.csv", "csvToField")


@pytest.fixture()
def simple_rst():
    """Resolve the path of the "rst_operators/simpleModel.rst" result file."""
    return resolve_test_file("simpleModel.rst", "rst_operators")


@pytest.fixture()
def multishells():
    """Resolve the path of the "rst_operators/multishells.rst" result file."""
    return resolve_test_file("model_with_ns.rst", "", "multishells_rst")


@pytest.fixture()
def complex_model():
    """Resolve the path of the "complex/fileComplex.rst" result file."""
    return resolve_test_file("complex.rst", "", "complex_rst")


@pytest.fixture()
def plate_msup():
    """Resolve the path of the "msup/plate1.rst" result file.

    Originally:
    UnitTestDataFiles/DataProcessing/expansion/msup/Transient/plate1/file.rst
    """
    return resolve_test_file("msup_transient_plate1.rst", "", "msup_transient")


@pytest.fixture()
def model_with_ns():
    """Resolve the path of the "model_with_ns.rst" result file."""
    return resolve_test_file("model_with_ns.rst", "", "multishells_rst")


@pytest.fixture()
def cff_data_sources():
    """Create a data sources with a cas and a dat file of fluent"""
    ds = core.DataSources()
    files = examples.download_fluent_files()
    ds.set_result_file_path(files["cas"], "cas")
    ds.add_file_path(files["dat"], "dat")
    return ds


@pytest.fixture()
def d3plot():
    """Resolve the path of the "d3plot/d3plot" result file."""
    return resolve_test_file("d3plot", "d3plot")


@pytest.fixture()
def engineering_data_sources():
    """Resolve the path of the "model_with_ns.rst" result file."""
    ds = core.DataSources(resolve_test_file("file.rst", "engineeringData"))
    ds.add_file_path(
        resolve_test_file("MatML.xml", "engineeringData"), "EngineeringData"
    )
    ds.add_file_path(resolve_test_file("ds.dat", "engineeringData"), "dat")
    return ds


SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 = meets_version(
    get_server_version(core._global_server()), "4.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0 = meets_version(
    get_server_version(core._global_server()), "3.0"
)

IS_USING_GATEBIN = _try_use_gatebin()


def raises_for_servers_version_under(version):
    """Launch the test normally if the server version is equal or higher than the "version"
    parameter. Else it makes sure that the test fails by raising a "DpfVersionNotSupported"
    error.
    """

    def decorator(func):
        @pytest.mark.xfail(
            not meets_version(get_server_version(core._global_server()), version),
            reason=f"Requires server version greater than or equal to {version}",
            raises=core.errors.DpfVersionNotSupported,
        )
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    return decorator


if SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0:

    @pytest.fixture(
        scope="session",
        params=[
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
            ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
        ],
        ids=["ansys-grpc-dpf", "gRPC CLayer", "in Process CLayer"],
    )
    def server_type(request):
        server = core.start_local_server(config=request.param, as_global=False)
        if request.param == ServerConfig(
            protocol=CommunicationProtocols.gRPC, legacy=False
        ):
            core.settings.get_runtime_client_config(server).cache_enabled = False
        return server

    @pytest.fixture(
        scope="session",
        params=[
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ],
        ids=[
            "ansys-grpc-dpf",
            "gRPC CLayer",
        ],
    )
    def server_type_remote_process(request):
        server = core.start_local_server(config=request.param, as_global=False)
        if request.param == ServerConfig(
            protocol=CommunicationProtocols.gRPC, legacy=False
        ):
            core.settings.get_runtime_client_config(server).cache_enabled = True
        return server

    @pytest.fixture(
        scope="session",
        params=[
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ],
        ids=["ansys-grpc-dpf config", "gRPC CLayer config"],
    )
    def remote_config_server_type(request):
        return request.param

    @pytest.fixture(
        scope="session",
        params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)],
        ids=[
            "ansys-grpc-dpf",
        ],
    )
    def server_type_legacy_grpc(request):
        return core.start_local_server(config=request.param, as_global=False)

else:

    @pytest.fixture(scope="session")
    def server_type():
        return core._global_server()

    @pytest.fixture(
        scope="session",
        params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)],
        ids=[
            "ansys-grpc-dpf",
        ],
    )
    def server_type_remote_process(request):
        return core._global_server()

    @pytest.fixture(
        scope="session",
        params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)],
        ids=[
            "ansys-grpc-dpf",
        ],
    )
    def remote_config_server_type(request):
        return request.param

    @pytest.fixture(scope="session")
    def server_type_legacy_grpc(request):
        return core._global_server()


@pytest.fixture(
    scope="session",
    params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)],
    ids=[
        "gRPC CLayer",
    ],
)
def server_clayer_remote_process(request):
    server = core.start_local_server(config=request.param, as_global=False)
    if request.param == ServerConfig(
        protocol=CommunicationProtocols.gRPC, legacy=False
    ):
        client = core.settings.get_runtime_client_config(server)
        client.cache_enabled = True
    return server


@pytest.fixture(
    scope="session",
    params=[
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ServerConfig(protocol=None, legacy=False),
    ],
    ids=["gRPC CLayer", "in Process CLayer"],
)
def server_clayer(request):
    server = core.start_local_server(config=request.param, as_global=False)
    if request.param == ServerConfig(
        protocol=CommunicationProtocols.gRPC, legacy=False
    ):
        core.settings.get_runtime_client_config(server).cache_enabled = False
    return server


class LocalServers:
    def __init__(self):
        self._local_servers = []
        self._max_iter = 3

    def __getitem__(self, item):
        if len(self._local_servers) <= item:
            while len(self._local_servers) <= item:
                self._local_servers.append(core.start_local_server(as_global=False))
        try:
            self._local_servers[item].info
            return self._local_servers[item]
        except:
            for iter in range(0, self._max_iter):
                try:
                    self._local_servers[item] = core.start_local_server(as_global=False)
                    self._local_servers[item].info
                    break
                except:
                    pass
            return self._local_servers[item]

    def clear(self):
        self._local_servers = []


local_servers = LocalServers()


@pytest.fixture()
def local_server():
    return local_servers[0]


@pytest.fixture(autouse=False)
def count_servers(request):
    """Count servers once we are finished."""

    def count_servers():
        num_dpf_exe = 0
        for proc in psutil.process_iter():
            if proc.name() == "Ans.Dpf.Grpc.exe":
                num_dpf_exe += 1
        warnings.warn(UserWarning(f"Number of servers running: {num_dpf_exe}"))
        # assert num_dpf_exe == 1

    request.addfinalizer(count_servers)
