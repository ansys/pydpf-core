# noqa: D400
"""
.. _ref_python_operators_with_deps:

Create a plug-in package that has third-party dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a Python plug-in package with
third-party dependencies. You should be familiar with these
examples before proceeding with this more advanced one:

- :ref:`ref_wrapping_numpy_capabilities`
- :ref:`ref_python_plugin_package`

This plug-in contains an operator whose implementation depends on a
third-party Python module named `gltf <https://pypi.org/project/gltf/>`_.
This operator takes a path, a mesh, and a 3D vector field as inputs
and then exports the mesh and the norm of the 3D vector field to a GLTF
file at the given path.

.. note::
    This example requires DPF 4.0 (Ansys 2022R2) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Create the plug-in package
# --------------------------
# Each operator implementation derives from the
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase` class
# and a call to the :py:func:`ansys.dpf.core.custom_operator.record_operator`
# method, which records the operators of the plug-in package.
#
# Download the ``gltf_plugin`` plug-in package that has already been
# created for you.

import os

from ansys.dpf.core import examples
from ansys.dpf import core as dpf


print("\033[1m gltf_plugin")
file_list = [
    "gltf_plugin/__init__.py",
    "gltf_plugin/operators.py",
    "gltf_plugin/operators_loader.py",
    "gltf_plugin/requirements.txt",
    "gltf_plugin/gltf_export.py",
    "gltf_plugin/texture.png",
    "gltf_plugin.xml",
]
import os

folder_root = os.path.join(os.getcwd().rsplit("pydpf-core")[0], "pydpf-core")
source_path_in_repo = r"docs\source\examples\07-python-operators\plugins"
operator_folder = os.path.join(folder_root, source_path_in_repo)
print(operator_folder)
plugin_path = None

for file in file_list:
    operator_file_path = os.path.join(operator_folder, file)

    print(f"\033[1m {file}\n \033[0m")
    if (
        os.path.splitext(file)[1] == ".py" or os.path.splitext(file)[1] == ".xml"
    ) and file != "gltf_plugin/gltf_export.py":
        with open(operator_file_path, "r") as f:
            for line in f.readlines():
                print("\t\t\t" + line)
        print("\n\n")
        if plugin_path is None:
            plugin_path = os.path.dirname(operator_file_path)

# %%
# To add third-party modules as dependencies to a plug-in package, you must
# create and reference a folder or ZIP file with the sites of the dependencies
# in an XML file located next to the folder for the plug-in package. The XML
# file must have the same name as the plug-in package plus an ``.xml`` extension.
#
# When the :py:func:`ansys.dpf.core.core.load_library` method is called,
# DPF-Core uses the ``site`` Python module to add custom to the path
# for the Python interpreter.
#
# To create these custom sites, requirements of the plug-in package should be
# installed in a Python virtual environment, the site-packages
# (with unnecessary folders removed) should be compressed to a ZIP file and
# placed with the plugin. The path to this ZIP file should be referenced in
# the XML as shown in the preceding code.
#
# To simplify this step, you can add a requirements file in the plug-in package:
#
print("\033[1m gltf_plugin/requirements.txt: \n \033[0m")
with open(os.path.join(plugin_path, "requirements.txt"), "r") as f:
    for line in f.readlines():
        print("\t\t\t" + line)


# %%
# Download the script for your operating system.
#
# - For Windows, download this
#   :download:`PowerShell script </user_guide/create_sites_for_python_operators.ps1>`.
# - For Linux, download this
#   :download:`Shell script </user_guide/create_sites_for_python_operators.sh>`.
#
# Run the downloaded script with the mandatory arguments:
#
# - ``-pluginpath``: Path to the folder with the plug-in package.
# - ``-zippath``: Path and name for the ZIP file.
#
# Optional arguments are:
#
# - ``-pythonexe``: Path to a Python executable of your choice.
# - ``-tempfolder``: Path to a temporary folder to work in. The default is the environment variable
#   ``TEMP`` on Windows and ``/tmp/`` on Linux.
#
# Run the command for your operating system.
#
# - From Windows PowerShell, run::
#
#     create_sites_for_python_operators.ps1 -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/winx64.zip # noqa: E501
#
# - From Linux Shell, run::
#
#    create_sites_for_python_operators.sh -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/linx64.zip # noqa: E501


if os.name == "nt" and not os.path.exists(
    os.path.join(plugin_path, "assets", "gltf_sites_winx64.zip")
):
    cmd_file = os.path.join(
        folder_root,
        "docs",
        "source",
        "user_guide",
        "create_sites_for_python_operators.ps1",
    )
    args = [
        "powershell",
        cmd_file,
        "-pluginpath",
        plugin_path,
        "-zippath",
        os.path.join(plugin_path, "assets", "gltf_sites_winx64.zip"),
    ]
    print(args)
    import subprocess

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stderr:
        raise RuntimeError(
            "Installing pygltf in a virtual environment failed with error:\n"
            + process.stderr.decode()
            + "\n\n and log:\n"
            + process.stdout.decode()
        )
    else:
        print("Installing pygltf in a virtual environment succeeded")
elif os.name == "posix" and not os.path.exists(
    os.path.join(plugin_path, "assets", "gltf_sites_linx64.zip")
):
    cmd_file = os.path.join(
        folder_root,
        "docs",
        "source",
        "user_guide",
        "create_sites_for_python_operators.sh",
    )
    run_cmd = f"{cmd_file}"
    args = (
        f' -pluginpath "{plugin_path}" '
        f"-zippath \"{os.path.join(plugin_path, 'assets', 'gltf_sites_linx64.zip')}\""
    )
    print(run_cmd + args)
    os.system(f"chmod u=rwx,o=x {cmd_file}")
    os.system(run_cmd + args)
    print("\nInstalling pygltf in a virtual environment succeeded")

###############################################################################
# Load the plug-in package
# ------------------------
# You use the function :py:func:`ansys.dpf.core.core.load_library` to load the
# plug-in package.
#
# - The first argument is the path to the directory where the plug-in package
#   is located.
# - The second argument is ``py_<package>``, where ``<package>`` is the name
#   identifying the plug-in package.
# - The third argument is the name of the function exposed in the ``__init__`` file
#   for the plug-in package that is used to record operators.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Python plugins are not supported in process.
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(dpf.path_utilities.join(tmp, "plugins", "gltf_plugin"), plugin_path)
dpf.upload_file(plugin_path + ".xml", dpf.path_utilities.join(tmp, "plugins", "gltf_plugin.xml"))

dpf.load_library(
    dpf.path_utilities.join(tmp, "plugins", "gltf_plugin"),
    "py_dpf_gltf",
    "load_operators",
)

###############################################################################
# Instantiate the operator.

new_operator = dpf.Operator("gltf_export")

###############################################################################
# This new ``gltf_export`` operator requires the following as inputs: a triangle
# surface mesh, a displacement field on this surface mesh, and a path to export
# the GLTF file to.
#
# To demonstrate this new operator, a :class:`ansys.dpf.core.model.Model` class
# is created on a simple file and the
# :class:`ansys.dpf.core.operators.mesh.tri_mesh_skin` operator is used
# to extract the surface of the mesh in triangle elements.

# %%
# .. graphviz::
#
#    digraph workflow {
#       graph [pad="0.5", nodesep="0.3", ranksep="0.3"]
#       node [shape=box, style=filled, fillcolor="#ffcc00", margin="0"];
#       rankdir=LR;
#       splines=line;
#       ds [label="data_sources", shape=box, style=filled, fillcolor=cadetblue2];
#       ds -> mesh_provider [style=dashed];
#       mesh_provider -> skin_mesh [splines=ortho];
#       ds -> displacement [style=dashed];
#       skin_mesh -> displacement [splines=ortho];
#       skin_mesh -> gltf_export [splines=ortho];
#       displacement -> gltf_export [splines=ortho];
#    }

###############################################################################
# Use the custom operator
# -----------------------

import os

model = dpf.Model(dpf.upload_file_in_tmp_folder(examples.find_static_rst()))

mesh = model.metadata.meshed_region
skin_mesh = dpf.operators.mesh.tri_mesh_skin(mesh=mesh)

displacement = model.results.displacement()
displacement.inputs.mesh_scoping(skin_mesh)
displacement.inputs.mesh(skin_mesh)
new_operator.inputs.path(os.path.join(tmp, "out"))
new_operator.inputs.mesh(skin_mesh)
new_operator.inputs.field(displacement.outputs.fields_container()[0])
new_operator.run()

print("operator ran successfully")

dpf.download_file(os.path.join(tmp, "out.glb"), os.path.join(os.getcwd(), "out.glb"))

# %%
# You can download :download:`output <images/thumb/out02.glb>` from the ``gltf`` operator.
