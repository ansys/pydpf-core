"""This runs at the init of the pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a sesson fixture
"""
import os

import pytest
import pyvista as pv

from ansys.dpf import core

# enable off_screen plotting to avoid test interruption
pv.OFF_SCREEN = True


# currently running dpf on docker.  Used for testing on CI
running_docker = os.environ.get('DPF_DOCKER', False)


def resolve_test_file(basename):
    """Resolves a test file's full path based on the base name and the enviornment.

    Normally returns local path unless server is running on docker and
    this repository has been mapped to the docker image at /dpf.

    """
    if running_docker:
        # assumes repository root is mounted at '/dpf'
        test_files_path = '/dpf/tests/testfiles'
        return os.path.join(test_files_path, basename)
    else:
        # otherwise, assume file is local
        test_path = os.path.dirname(os.path.abspath(__file__))
        test_files_path = os.path.join(test_path, 'testfiles')
        filename = os.path.join(test_files_path, basename)
        if not os.path.isfile(filename):
            raise FileNotFoundError(f'Unable to locate {basename} at {test_files_path}')
        return filename


@pytest.fixture()
def allkindofcomplexity():
    """Path of the "allKindOfComplexity.rst" result file."""
    return resolve_test_file('allKindOfComplexity.rst')


@pytest.fixture()
def simple_bar():
    """Path of the "ASimpleBar.rst" result file."""
    return resolve_test_file('ASimpleBar.rst')


@pytest.fixture(scope="session", autouse=True)
def load_operators(request):
    """This loads all the operators on initialization"""
    model = core.Model(resolve_test_file('ASimpleBar.rst'))
