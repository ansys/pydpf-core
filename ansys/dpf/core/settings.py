
"""
settings
========
Customize the behavior of the module.
"""
import os
import re

from ansys.dpf.core.misc import module_exists
from ansys.dpf.core import misc
from ansys.dpf.core.server import set_server_configuration  # noqa: F401
from ansys.dpf.core.server_factory import ServerConfig  # noqa: F401
from ansys.dpf.core import core


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


def bypass_pv_opengl_osmesa_crash():
    if module_exists("pyvista"):
        import pyvista as pv

        def get_lighting():
            """Get lighting configuration.

            Disable lighting when using OSMesa on Windows. See:
            https://github.com/pyvista/pyvista/issues/3185

            """
            pl = pv.Plotter(notebook=False, off_screen=True)
            pl.add_mesh(pv.Sphere())
            pl.show(auto_close=False)
            gpu_info = pl.ren_win.ReportCapabilities()
            pl.close()

            regex = re.compile("OpenGL version string:(.+)\n")
            version = regex.findall(gpu_info)[0]
            return not(os.name == 'nt' and 'Mesa' in version)

        pv.global_theme.lighting = get_lighting()


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


def set_upload_chunk_size(num_bytes=misc.DEFAULT_FILE_CHUNK_SIZE) -> None:
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


def _forward_to_gate():
    from ansys.dpf.gate import settings
    from ansys.dpf.core.misc import DEFAULT_FILE_CHUNK_SIZE
    from ansys.dpf.core.common import _common_progress_bar, _progress_bar_is_available
    settings.forward_settings(
        DEFAULT_FILE_CHUNK_SIZE, _common_progress_bar if _progress_bar_is_available() else None)


def get_runtime_client_config(server=None):
    """Get the runtime configuration information of Ans.Dpf.GrpcClient
    binary.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Notes
    -----
    Available from 4.0 server version. Can only be used for
    a gRPC communication protocol using DPF CLayer.

    Returns
    -------
    runtime_config : RuntimeClientConfig
        RuntimeClientConfig object that can be used to interact
        with Ans.Dpf.GrpcClient configuration.

    """
    base = core.BaseService(server, load_operators=False)
    return base.get_runtime_client_config()


def get_runtime_core_config(server=None):
    """Get the runtime configuration information of Ans.Dpf.GrpcClient
    binary.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Notes
    -----
    Available from 4.0 server version.

    Returns
    -------
    core_config : RuntimeCoreConfig
        RuntimeCoreConfig object that can be used to interact
        with DataProcessingCore configuration.

    """
    base = core.BaseService(server, load_operators=False)
    return base.get_runtime_core_config()
