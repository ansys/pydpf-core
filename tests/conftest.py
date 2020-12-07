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


@pytest.fixture()
def allkindofcomplexity():
    """Path of the result allKindOfComplexity.rst result file

    Normally returns local path unless server is running on docker and
    this repository has been mapped to the docker image at /dpf.

    """
    if running_docker:
        # assumes repository root is mounted at '/dpf'
        test_path = '/dpf'
    else:
        test_path = os.path.dirname(os.path.abspath(__file__))

    test_files_path = os.path.join(test_path, 'testfiles')
    return os.path.join(test_files_path, 'allKindOfComplexity.rst')
