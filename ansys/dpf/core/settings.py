
"""
settings
========
Customize the behavior of the module.
"""

from ansys.dpf.core.misc import module_exists
from ansys.dpf.core import misc
from ansys.dpf.core.server import set_server_configuration
from dpf.core.server_factory import ServerConfig


def disable_off_screen_rendering() -> None:
    """No pop up windows appears to plot data with ``matplotlib`` or ``pyvista``"""
    # enable matplotlib off_screen plotting to avoid test interruption
    if module_exists("matplotlib"):
        import matplotlib as mpl

        mpl.use("Agg")

    # enable off_screen plotting to avoid test interruption
    if module_exists("pyvista"):
        import pyvista as pv

        pv.OFF_SCREEN = True


def set_default_pyvista_config():
    # Configure PyVista's ``rcParams`` for dpf
    if module_exists("pyvista"):
        import pyvista as pv

        pv.rcParams["interactive"] = True
        pv.rcParams["cmap"] = "jet"
        pv.rcParams["font"]["family"] = "courier"
        pv.rcParams["title"] = "DPF"


def disable_interpreter_properties_evaluation() -> bool:
    """If ``jedi`` module is installed (autocompletion module for most of IDEs), disables the
    property evaluation when tab key is pressed.

    To use in Jupyter Notebook if autocompletion becomes slow.

    Returns
    -------
    bool
        Whether disabling the capability has been possible.
    """
    if module_exists("jedi"):
        import jedi
        jedi.Interpreter._allow_descriptor_getattr_default = False
        return True
    return False


def set_upload_chunk_size(num_bytes = misc.DEFAULT_FILE_CHUNK_SIZE) -> None:
    misc.DEFAULT_FILE_CHUNK_SIZE = num_bytes


def set_dynamic_available_results_capability(value) -> None:
    """Disables the evaluation of the available results and
    the dynamic creation of the results properties when a ''Model'' is created.

    Parameters
    ----------
    value :  bool
        With ''True'', models will dynamically generate results properties

    Examples
    --------

    >>> from ansys.dpf import core as dpf
    >>> dpf.settings.set_dynamic_available_results_capability(False)
    >>> dpf.settings.set_dynamic_available_results_capability(True)

    """
    misc.DYNAMIC_RESULTS = value
