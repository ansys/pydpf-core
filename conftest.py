"""This runs at the init of the doctest pytest session

Launch or connect to a persistent local DPF service to be shared in
pytest as a session fixture
"""
from ansys.dpf import core
from ansys.dpf.core.misc import module_exists

# enable matplotlib off_screen plotting to avoid test interruption

if module_exists("matplotlib"):
    import matplotlib as mpl

    mpl.use("Agg")


# enable off_screen plotting to avoid test interruption
core.settings.disable_off_screen_rendering()
core.settings.bypass_pv_opengl_osmesa_crash()
