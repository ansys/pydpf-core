"""This runs at the init of the pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a session fixture
"""
import os

import pytest
from ansys.dpf import core
from ansys.dpf.core import examples

core.settings.disable_off_screen_rendering()

# currently running dpf on docker.  Used for testing on CI
running_docker = os.environ.get("DPF_DOCKER", False)

local_test_repo = True

if os.name == "posix":
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context


def resolve_test_file(basename, additional_path="", is_in_examples=None):
    """Resolves a test file's full path based on the base name and the
    environment.

    Normally returns local path unless server is running on docker and
    this repository has been mapped to the docker image at /dpf.
    """
    if running_docker:
        # assumes repository root is mounted at '/dpf'
        test_files_path = "/dpf/tests/testfiles"
        return os.path.join(test_files_path, additional_path, basename)
    elif local_test_repo is False:
        if is_in_examples:
            return getattr(examples, is_in_examples)
        else:
            # otherwise, assume file is local
            test_path = os.path.dirname(os.path.abspath(__file__))
            test_files_path = os.path.join(test_path, "testfiles")
            filename = os.path.join(test_files_path, additional_path, basename)
            if not os.path.isfile(filename):
                raise FileNotFoundError(
                    f"Unable to locate {basename} at {test_files_path}"
                )
            return filename
    elif os.environ.get("AWP_UNIT_TEST_FILES", False):
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

local_servers = [core.start_local_server(as_global=False),core.start_local_server(as_global=False),core.start_local_server(as_global=False)]
local_server =local_servers[0]


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def close_servers():
        core.server.shutdown_all_session_servers()
        try:
            local_server.shutdown()
        except:
            pass

    request.addfinalizer(close_servers)
