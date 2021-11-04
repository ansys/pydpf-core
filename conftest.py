"""This runs at the init of the pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a session fixture
"""
import pytest
from ansys.dpf import core
from ansys.dpf.core.misc import module_exists

# enable matplotlib off_screen plotting to avoid test interruption

if module_exists("matplotlib"):
    import matplotlib as mpl

    mpl.use("Agg")


# enable off_screen plotting to avoid test interruption

@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def close_servers():
        core.server.shutdown_all_session_servers()

    request.addfinalizer(close_servers)

core.settings.disable_off_screen_rendering()
