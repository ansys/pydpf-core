"""
Python DPF plugins utilities
============================

Contains the utilities specific to installing and using Python DPF plugins.
"""
import os.path
import importlib.metadata as importlib_metadata

import ansys.dpf.core as dpf
from ansys.dpf.core import server as server_module


def load_plugin_on_server(plugin, server=None, symbol="load_operators"):
    """Load a DPF Python plugin on the global or given DPF server.

        Parameters
    ----------
    plugin:
        DPF Python plugin to load.
    server:
        DPF server to load the plugin onto.
    symbol:
        Name of the function recording the operators in the plugin.
    """
    server = server_module.get_or_create_server(server)
    plugin_name = plugin.split("-")[-1]
    tmp_folder = dpf.make_tmp_dir_server(server=server)

    # Get the path to the plugin from the package installation
    if len([p for p in importlib_metadata.files(plugin) if "__init__.py" in str(p)]) > 0:
        file_path = [p for p in importlib_metadata.files(plugin) if "__init__.py" in str(p)][0]
        plugin_path = str(os.path.dirname(file_path.locate()))
        # For some reason the "locate()" function returns a path with src doubled
        plugin_path = plugin_path.replace("src"+os.path.sep+"src", "src")
    elif len([p for p in importlib_metadata.files(plugin) if ".pth" in str(p)]) > 0:
        path_file = [p for p in importlib_metadata.files(plugin) if ".pth" in str(p)][0].locate()
        with open(path_file, "r") as file:
            plugin_path = file.readline()[:-1]
        plugin_path = os.path.join(plugin_path, "ansys", "dpf", "plugins", plugin_name)
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
        os.path.join(plugin_path, os.pardir),
        specific_extension=".xml",
        server=server,
    )

    # Load the plugin on the server
    dpf.load_library(
        filename=target_plugin_path,
        name=f"py_{plugin_name}",
        symbol=symbol,
        server=server,
    )
