"""
.. _ref_python_operators_with_deps:

Write user defined Operators having third party dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how advanced DPF python plugins of Operators
can be created as standard python packages
and how third party python modules dependencies can be added to the package.
For a first introduction on user defined python Operators see example
:ref:`ref_wrapping_numpy_capabilities`
and for a simpler example on user defined python Operators as a package
see :ref:`ref_python_plugin_package`.

This plugin will hold an Operator which implementation depends on a
third party python module named
`gltf <https://pypi.org/project/gltf/>`_. This Operator takes a path,
a mesh and 3D vector field in input and exports the mesh and the norm of the input
field in a gltf file located at the given path.

"""

###############################################################################
# Write Operator
# --------------
# For this more advanced use case, a python package is created.
# Each Operator implementation derives from
# :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
# and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator`
# records the Operators of the plugin.
# The python package `gltf_plugin` is downloaded and displayed here:

import os
from ansys.dpf.core import examples

print('\033[1m gltf_plugin')
file_list = ["gltf_plugin/__init__.py", "gltf_plugin/operators.py",
             "gltf_plugin/operators_loader.py", "gltf_plugin/requirements.txt",
             "gltf_plugin/gltf_export.py", "gltf_plugin/texture.png", "gltf_plugin.xml"
             ]
plugin_path = None
GITHUB_SOURCE_URL = "https://github.com/pyansys/pydpf-core/raw/" \
                    "" \
                    "examples/first_python_plugins/python_plugins"

for file in file_list:
    EXAMPLE_FILE = GITHUB_SOURCE_URL + "/gltf_plugin/" + file
    operator_file_path = examples.downloads._retrieve_file(
        EXAMPLE_FILE, file, os.path.join("python_plugins", os.path.dirname(file)))

    print(f'\033[1m {file}\n \033[0m')
    if (os.path.splitext(file)[1] == ".py" or os.path.splitext(file)[1] == ".xml") \
            and file != "gltf_plugin/gltf_export.py":
        with open(operator_file_path, "r") as f:
            for line in f.readlines():
                print('\t\t\t' + line)
        print("\n\n")
        if plugin_path is None:
            plugin_path = os.path.dirname(operator_file_path)

# %%
# To add third party modules as dependencies to a custom DPF python plugin,
# a folder or zip file with the sites of the dependencies needs to be created
# and referenced in an xml located next to the plugin's folder
# and having the same name as the plugin plus the ``.xml`` extension. The ``site``
# python module is used by DPF when
# calling :py:func:`ansys.dpf.core.core.load_library` function to add these custom
# sites to the python interpreter path.
# To create these custom sites, the requirements of the custom plugin should be
# installed in a python virtual environment, the site-packages
# (with unnecessary folders removed) should be zipped and put with the plugin. The
# path to this zip should be referenced in the xml as done above.
#
# To simplify this step, a requirements file can be added in the plugin, like:
#
print(f'\033[1m gltf_plugin/requirements.txt: \n \033[0m')
with open(os.path.join(plugin_path, "requirements.txt"), "r") as f:
    for line in f.readlines():
        print('\t\t\t' + line)


# %%
# And this :download:`powershell script </user_guide/create_sites_for_python_operators.ps1>`
# for windows or this :download:`shell script </user_guide/create_sites_for_python_operators.sh>`
# can be ran with the mandatory arguments:
#
# - -pluginpath : path to the folder of the plugin.
# - -zippath : output zip file name.
#
# optional arguments are:
#
# - -pythonexe : path to a python executable of your choice.
# - -tempfolder : path to a temporary folder to work on, default is the environment variable
#   ``TEMP`` on Windows and /tmp/ on Linux.
#
# For windows powershell, call::
#
#     create_sites_for_python_operators.ps1 -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/winx64.zip # noqa: E501
#
# For linux shell, call::
#
#    create_sites_for_python_operators.sh -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/linx64.zip # noqa: E501


if os.name == "nt" and \
        not os.path.exists(os.path.join(plugin_path, 'assets', 'gltf_sites_winx64.zip')):
    CMD_FILE_URL = GITHUB_SOURCE_URL + "/create_sites_for_python_operators.ps1"
    cmd_file = examples.downloads._retrieve_file(
        CMD_FILE_URL, "create_sites_for_python_operators.ps1", "python_plugins")
    run_cmd = f"powershell {cmd_file}"
    args = f" -pluginpath \"{plugin_path}\" " \
           f"-zippath {os.path.join(plugin_path, 'assets', 'gltf_sites_winx64.zip')}"
    print(run_cmd + args)
    import subprocess
    process = subprocess.run(run_cmd + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stderr:
        raise RuntimeError(
            "Installing pygltf in a virtual environment failed with error:\n"
            + process.stderr.decode())
    else:
        print("Installing pygltf in a virtual environment succeeded")
elif os.name == "posix" and \
        not os.path.exists(os.path.join(plugin_path, 'assets', 'gltf_sites_linx64.zip')):
    CMD_FILE_URL = GITHUB_SOURCE_URL + "/create_sites_for_python_operators.sh"
    cmd_file = examples.downloads._retrieve_file(
        CMD_FILE_URL, "create_sites_for_python_operators.ps1", "python_plugins"
    )
    run_cmd = f"{cmd_file}"
    args = f" -pluginpath \"{plugin_path}\" " \
           f"-zippath \"{os.path.join(plugin_path, 'assets', 'gltf_sites_linx64.zip')}\""
    print(run_cmd + args)
    os.system(f"chmod u=rwx,o=x {cmd_file}")
    os.system(run_cmd + args)
    print("\nInstalling pygltf in a virtual environment succeeded")

###############################################################################
# Load Plugin
# -----------
# Once a python plugin is written as a package, it can be loaded with the function
# :py:func:`ansys.dpf.core.core.load_library` taking as first argument
# the path to the directory of the plugin,
# as second argument ``py_`` + any name identifying the plugin,
# and as last argument the function's name exposed in the ``__init__.py``
# file and used to record operators.

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# python plugins are not supported in process
dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer)

tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(
    dpf.path_utilities.join(tmp, "plugins", "gltf_plugin"),
    plugin_path
)
dpf.upload_file(
    plugin_path + ".xml",
    dpf.path_utilities.join(tmp, "plugins", "gltf_plugin.xml")
)

dpf.load_library(
    dpf.path_utilities.join(tmp, "plugins", "gltf_plugin"),
    "py_dpf_gltf",
    "load_operators")

###############################################################################
# Once the Plugin loaded, Operators recorded in the plugin can be used with:

new_operator = dpf.Operator("gltf_export")

###############################################################################ser
# This new Operator ``gltf_export`` requires a triangle surface mesh,
# a displacement Field on this surface mesh
# as well as an export path as inputs.
# To demo this new Operator, a :class:`ansys.dpf.core.model.Model` on a simple file is created,
# :class:`ansys.dpf.core.operators.mesh.tri_mesh_skin` Operator is used
# to extract the surface of the mesh in triangles elements.

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
# Use the Custom Operator
# -----------------------

import os

model = dpf.Model(dpf.upload_file_in_tmp_folder(examples.static_rst))

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
# The gltf Operator output can be downloaded :download:`here <images/thumb/out02.glb>`.
