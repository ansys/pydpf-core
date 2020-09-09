"""Launch a persistent local DPF service to be shared in pytest as a sesson fixture"""
import pytest
import pyvista as pv

from ansys import dpf

# enable off_screen plotting to avoid test interruption
pv.OFF_SCREEN = True


# This runs one at the init of the pytest session
if not dpf.has_local_server():
    dpf.start_local_server()

# @pytest.fixture(scope='session'):
# def dpf_server()

