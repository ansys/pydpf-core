# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
settings.

Customize the behavior of the module.
"""

from ansys.dpf.core import core, misc
from ansys.dpf.core.misc import module_exists
from ansys.dpf.core.server import set_server_configuration  # noqa: F401
from ansys.dpf.core.server_context import set_default_server_context  # noqa: F401
from ansys.dpf.core.server_factory import ServerConfig  # noqa: F401
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
)


def disable_off_screen_rendering() -> None:
    """No pop up windows appears to plot data with ``matplotlib`` or ``pyvista``."""
    # enable matplotlib off_screen plotting to avoid test interruption
    if module_exists("matplotlib"):
        import matplotlib as mpl

        mpl.use("Agg")

    # enable off_screen plotting to avoid test interruption
    if module_exists("pyvista"):
        import pyvista as pv

        pv.OFF_SCREEN = True


def set_default_pyvista_config():
    """Set default pyvista configuration."""
    # Configure PyVista's ``rcParams`` for dpf
    if module_exists("pyvista"):
        import pyvista as pv

        pv.global_theme.interactive = True
        pv.global_theme.cmap = "jet"
        pv.global_theme.font.family = "courier"
        pv.global_theme.title = "DPF"


def bypass_pv_opengl_osmesa_crash():
    """Bypass pyvista opengl osmesa crash."""
    if module_exists("pyvista"):
        import pyvista as pv

        pv.global_theme.lighting = False


def disable_interpreter_properties_evaluation() -> bool:
    """Disable property evaluation on tab key press if the jedi module is installed.

    If ``jedi`` module is installed (autocompletion module for most of IDEs), disables the
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
    """Set upload chunk size."""
    misc.DEFAULT_FILE_CHUNK_SIZE = num_bytes


def set_dynamic_available_results_capability(value) -> None:
    """Disable evaluation and dynamic creation of result properties when creating a "Model.

    Disables the evaluation of the available results and
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
    from ansys.dpf.core.common import _common_progress_bar, _progress_bar_is_available
    from ansys.dpf.core.misc import DEFAULT_FILE_CHUNK_SIZE
    from ansys.dpf.gate import settings

    settings.forward_settings(
        DEFAULT_FILE_CHUNK_SIZE,
        _common_progress_bar if _progress_bar_is_available() else None,
    )


def get_runtime_client_config(server=None):
    """Get the runtime configuration information of Ans.Dpf.GrpcClient binary.

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
    from ansys.dpf import core as root
    from ansys.dpf.core.runtime_config import RuntimeClientConfig

    if server is None:
        server = root.SERVER
    if server is not None and server.has_client():
        _api = server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        _api.init_data_processing_environment(server)  # creates stub when gRPC
        data_tree_tmp = _api.data_processing_get_client_config_as_data_tree()
        config_to_return = RuntimeClientConfig(data_tree=data_tree_tmp, server=server)
    else:
        if misc.RUNTIME_CLIENT_CONFIG is None:
            from ansys.dpf.gate import misc as gate_misc

            misc.RUNTIME_CLIENT_CONFIG = gate_misc.client_config()
        config_to_return = misc.RUNTIME_CLIENT_CONFIG
    return config_to_return


def get_runtime_core_config(server=None):
    """Get the runtime configuration information of Ans.Dpf.GrpcClient binary.

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
