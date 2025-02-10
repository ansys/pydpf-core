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
Python DPF plugins utilities.

Contains the utilities specific to installing and using Python DPF plugins.

"""

import os.path
from pathlib import Path

try:
    import importlib.metadata as importlib_metadata
except ImportError:  # Python < 3.10 (backport)
    import importlib_metadata as importlib_metadata

import ansys.dpf.core as dpf
from ansys.dpf.core import server as server_module


def load_plugin_on_server(plugin, server=None, symbol="load_operators", generate_operators=False):
    """Load a DPF Python plugin on the global or given DPF server.

    Parameters
    ----------
    plugin:
        DPF Python plugin to load.
    server:
        DPF server to load the plugin onto.
    symbol:
        Name of the function recording the operators in the plugin.
    generate_operators:
        Whether to generate the Python code for the operators in the plugin.

    """
    server = server_module.get_or_create_server(server)
    plugin_name = plugin.split("-")[-1]
    tmp_folder = dpf.make_tmp_dir_server(server=server)

    # Get the path to the plugin from the package installation
    if len([p for p in importlib_metadata.files(plugin) if "__init__.py" in str(p)]) > 0:
        file_path = [p for p in importlib_metadata.files(plugin) if "__init__.py" in str(p)][0]
        plugin_path = str(file_path.locate().parent)
        # For some reason the "locate()" function returns a path with src doubled
        plugin_path = Path(plugin_path.replace("src" + os.path.sep + "src", "src"))
    elif len([p for p in importlib_metadata.files(plugin) if ".pth" in str(p)]) > 0:
        path_file = [p for p in importlib_metadata.files(plugin) if ".pth" in str(p)][0].locate()
        with path_file.open("r") as file:
            plugin_path = Path(file.readline()[:-1])
        plugin_path = plugin_path / "ansys" / "dpf" / "plugins" / plugin_name
    else:
        raise ModuleNotFoundError(f"Could not locate files for plugin {plugin}")

    target_plugin_path = dpf.path_utilities.join(tmp_folder, "ansys", "dpf", "plugins", plugin_name)
    target_xml_path = dpf.path_utilities.join(tmp_folder, "ansys", "dpf", "plugins")

    # Upload python files
    _ = dpf.upload_files_in_folder(
        target_plugin_path,
        plugin_path,
        specific_extension=".py",
        server=server,
    )

    # upload zip files (site-packages)
    _ = dpf.upload_files_in_folder(
        target_plugin_path,
        plugin_path,
        specific_extension=".zip",
        server=server,
    )

    # Upload xml file for the plugin
    _ = dpf.upload_files_in_folder(
        target_xml_path,
        plugin_path.parent,
        specific_extension=".xml",
        server=server,
    )

    # Load the plugin on the server
    dpf.load_library(
        filename=target_plugin_path,
        name=f"py_{plugin_name}",
        symbol=symbol,
        server=server,
        generate_operators=generate_operators,
    )
