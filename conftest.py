"""This runs at the init of the doctest pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a session fixture
"""
from doctest import OutputChecker
from unittest import mock

import pytest

from ansys.dpf import core
from ansys.dpf.core.misc import module_exists

# enable matplotlib off_screen plotting to avoid test interruption

if module_exists("matplotlib"):
    import matplotlib as mpl

    mpl.use("Agg")


# enable off_screen plotting to avoid test interruption
core.settings.disable_off_screen_rendering()
core.settings.bypass_pv_opengl_osmesa_crash()


class DPFOutputChecker(OutputChecker):
    def check_output(self, want: str, got: str, optionflags: int) -> bool:
        feature_str = "Feature not supported. Upgrade the server to"
        if feature_str in got:
            want = got
        return OutputChecker.check_output(self, want, got, optionflags)


@pytest.fixture(autouse=True)
def accept_upgrade_error():
    with mock.patch("doctest.OutputChecker", DPFOutputChecker):
        yield
