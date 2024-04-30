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
from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols
from ansys.dpf.core.check_version import meets_version, get_server_version
from ansys.dpf.gate.load_api import _try_use_gatebin
import warnings

ACCEPTABLE_FAILURE_RATE = 0

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
    ansys.dpf.core.server_types.RUNNING_DOCKER.mounted_volumes[
        _get_test_files_directory()
    ] = "/tmp/test_files"


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
    if is_in_examples:
        return examples.find_files(getattr(examples, is_in_examples))
    else:
        test_files_path = _get_test_files_directory()
        filename = os.path.join(test_files_path, additional_path, basename)
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Unable to locate {basename} at {test_files_path}")
    return examples.find_files(filename)


@pytest.fixture()
def testfiles_dir():
    """Return the path of the testfiles directory."""
    return _get_test_files_directory()


@pytest.fixture()
def allkindofcomplexity():
    """Resolve the path of the "allKindOfComplexity.rst" result file."""
    return examples.download_all_kinds_of_complexity()


@pytest.fixture()
def simple_bar():
    """Resolve the path of the "ASimpleBar.rst" result file."""
    return examples.find_simple_bar()


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
    return examples.find_multishells_rst()


@pytest.fixture()
def complex_model():
    """Resolve the path of the "complex/fileComplex.rst" result file."""
    return examples.find_complex_rst()


@pytest.fixture()
def plate_msup():
    """Resolve the path of the "msup/plate1.rst" result file.

    Originally:
    UnitTestDataFiles/DataProcessing/expansion/msup/Transient/plate1/file.rst
    """
    return examples.find_msup_transient()


@pytest.fixture()
def model_with_ns():
    """Resolve the path of the "model_with_ns.rst" result file."""
    return examples.find_multishells_rst()


@pytest.fixture()
def fluent_multi_species():
    """Return a function which creates a data sources
    with a cas and a dat file of fluent multi-species case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_fluent_multi_species(server=server)
        ds.set_result_file_path(files["cas"], "cas")
        ds.add_file_path(files["dat"], "dat")
        return ds

    return return_ds


@pytest.fixture()
def d3plot_files():
    """Resolve the path of the "d3plot/d3plot" result file."""
    return [
        resolve_test_file("d3plot", "d3plot"),
        resolve_test_file("file.actunits", "d3plot"),
    ]


@pytest.fixture()
def d3plot_beam():
    """Resolve the path of the "d3plot_beam/d3plot" result file."""
    return examples.download_d3plot_beam()[0]


@pytest.fixture()
def binout_matsum():
    """Resolve the path of the "binout/binout_matsum" result file."""
    return examples.download_binout_matsum()


@pytest.fixture()
def binout_glstat():
    """Resolve the path of the "binout/binout_glstat" result file."""
    return examples.download_binout_glstat()


@pytest.fixture()
def engineering_data_sources():
    """Resolve the path of the "model_with_ns.rst" result file."""
    ds = core.DataSources(resolve_test_file("file.rst", "engineeringData"))
    ds.add_file_path(resolve_test_file("MatML.xml", "engineeringData"), "EngineeringData")
    ds.add_file_path(resolve_test_file("ds.dat", "engineeringData"), "dat")
    return ds


@pytest.fixture()
def cyclic_multistage():
    """Resolve the path of the "msup/plate1.rst" result file.

    Originally:
    UnitTestDataFiles/DataProcessing/expansion/msup/Transient/plate1/file.rst
    """
    return examples.download_multi_stage_cyclic_result()


@pytest.fixture()
def fluent_axial_comp():
    """Return a function which creates a data sources
    with a cas and a dat file of fluent axial compressor case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_fluent_axial_comp(server=server)
        ds.set_result_file_path(files["cas"][0], "cas")
        ds.add_file_path(files["dat"][0], "dat")
        return ds

    return return_ds


@pytest.fixture()
def fluent_mixing_elbow_steady_state():
    """Return a function which creates a data sources
    with a cas and a dat file of fluent mixing elbow steady-state case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_fluent_mixing_elbow_steady_state(server=server)
        ds.set_result_file_path(files["cas"][0], "cas")
        ds.add_file_path(files["dat"][0], "dat")
        return ds

    return return_ds


@pytest.fixture()
def fluent_mixing_elbow_transient():
    """Return a function which creates a data sources
    with a cas and a dat file of fluent mixing elbow transient case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_fluent_mixing_elbow_transient(server=server)
        ds.set_result_file_path(files["cas"][0], "cas")
        ds.add_file_path(files["dat"][0], "dat")
        return ds

    return return_ds


@pytest.fixture()
def fluent_multiphase():
    """Return a function which creates a data sources
    with a cas and a dat file of fluent multiphase case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_fluent_multi_phase(server=server)
        ds.set_result_file_path(files["cas"], "cas")
        ds.add_file_path(files["dat"], "dat")
        return ds

    return return_ds


@pytest.fixture()
def cfx_heating_coil():
    """Return a function which creates a data sources
    with a cas and a dat file of CFX heating coil case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_cfx_heating_coil(server=server)
        ds.set_result_file_path(files["cas"], "cas")
        ds.add_file_path(files["dat"], "dat")
        return ds

    return return_ds


@pytest.fixture()
def cfx_mixing_elbow():
    """Return a function which creates a data sources
    with a cas and a dat file of CFX mixing elbow case."""

    def return_ds(server=None):
        ds = core.DataSources(server=server)
        files = examples.download_cfx_mixing_elbow(server=server)
        ds.set_result_file_path(files["cas"], "cas")
        ds.add_file_path(files["dat"], "dat")
        return ds

    return return_ds

SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_1 = meets_version(
    get_server_version(core._global_server()), "8.1"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0 = meets_version(
    get_server_version(core._global_server()), "8.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_1 = meets_version(
    get_server_version(core._global_server()), "7.1"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0 = meets_version(
    get_server_version(core._global_server()), "7.0"
)
SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_2 = meets_version(
    get_server_version(core._global_server()), "6.2"
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


IS_USING_GATEBIN = _try_use_gatebin()


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


configsserver_type, config_namesserver_type = remove_none_available_config(
    [
        # ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
    ],
    [
        # "ansys-grpc-dpf",
        "gRPC CLayer", "in Process CLayer"],
)


@pytest.fixture(
    scope="package",
    params=configsserver_type,
    ids=config_namesserver_type,
)
def server_type(request):
    if core.global_server().config == request.param and os.name != "posix":
        return core.global_server()
    server = core.start_local_server(config=request.param, as_global=False)
    return server


(
    configs_server_type_remote_process,
    config_names_server_type_remote_process,
) = remove_none_available_config(
    [
        # ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True),
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
    ],
    [
        # "ansys-grpc-dpf",
        "gRPC CLayer"],
)


@pytest.fixture(
    scope="package",
    params=configs_server_type_remote_process,
    ids=config_names_server_type_remote_process,
)
def server_type_remote_process(request):
    if core.global_server().config == request.param and os.name != "posix":
        return core.global_server()
    server = core.start_local_server(config=request.param, as_global=False)
    return server


@pytest.fixture(
    scope="package",
    params=configs_server_type_remote_process,
    ids=config_names_server_type_remote_process,
)
def remote_config_server_type(request):
    return request.param


@pytest.fixture(
    scope="package",
    params=configsserver_type,
    ids=config_namesserver_type,
)
def config_server_type(request):
    return request.param


(
    configs_server_type_legacy_grpc,
    config_names_server_type_legacy_grpc,
) = remove_none_available_config(
    [ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)],
    ["ansys-grpc-dpf"],
)


@pytest.fixture(
    scope="package",
    params=configs_server_type_legacy_grpc,
    ids=config_names_server_type_legacy_grpc,
)
def server_type_legacy_grpc(request):
    if core.global_server().config == request.param and os.name != "posix":
        return core.global_server()
    return core.start_local_server(config=request.param, as_global=False)


@pytest.fixture(
    scope="package",
    params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)],
    ids=[
        "gRPC CLayer",
    ],
)
def server_clayer_remote_process(request):
    if core.global_server().config == request.param and os.name != "posix":
        return core.global_server()
    server = core.start_local_server(config=request.param, as_global=False)
    return server


configs_server_clayer, config_names_server_clayer = remove_none_available_config(
    [
        ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
        ServerConfig(protocol=None, legacy=False),
    ],
    ["gRPC CLayer", "in Process CLayer"],
)


@pytest.fixture(
    scope="package",
    params=configs_server_clayer,
    ids=config_names_server_clayer,
)
def server_clayer(request):
    if core.global_server().config == request.param and os.name != "posix":
        return core.global_server()
    server = core.start_local_server(config=request.param, as_global=False)
    return server


@pytest.fixture
def server_in_process():
    if (
        not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0
        or ansys.dpf.core.server_types.RUNNING_DOCKER.use_docker
    ):
        pytest.skip("InProcess unavailable for Ansys <222")
    else:
        return core.start_local_server(
            config=core.AvailableServerConfigs.InProcessServer, as_global=False
        )


@pytest.fixture()
def restore_awp_root():
    ver_to_check = core._version.server_to_ansys_version[str(core.global_server().version)]
    ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
    awp_root_name = "AWP_ROOT" + ver_to_check
    awp_root_save = os.environ.get(awp_root_name, None)
    yield
    # restore awp_root
    if awp_root_save:
        os.environ[awp_root_name] = awp_root_save


class LocalServers:
    def __init__(self):
        self._local_servers = []
        self._max_iter = 3

    def __getitem__(self, item):
        if not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0:
            conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
        else:
            conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
        if len(self._local_servers) <= item:
            while len(self._local_servers) <= item:
                self._local_servers.append(core.start_local_server(as_global=False, config=conf))
        try:
            self._local_servers[item].info
            return self._local_servers[item]
        except:
            for iter in range(0, self._max_iter):
                try:
                    self._local_servers[item] = core.start_local_server(
                        as_global=False, config=conf
                    )
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
