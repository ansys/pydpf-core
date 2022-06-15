"""
.. _ref_python_operators_with_deps:

Write user defined Operators having third party dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how advanced DPF python plugins of Operators can be created as standard python packages
and how third party python modules dependencies can be added to the package.
For a first introduction on user defined python Operators see example :ref:`ref_wrapping_numpy_capabilities`
and for a simpler example on user defined python Operators as a package see :ref:`ref_python_plugin_package`.

This plugin will hold an Operator which implementation depends on a third party python module named
`gltf <https://pypi.org/project/gltf/>`_. This Operator takes a path, a mesh and 3D vector field in input
and exports the mesh and the norm of the input field in a gltf file located at the given path.
"""

###############################################################################
# Write Operator
# --------------
# For this more advanced use case, a python package is created.
# Each Operator implementation derives from :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
# and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator` records the Operators of the plugin.
# The complete package looks like:

# %%
# .. card:: plugin
#
#    .. card:: gltf_plugin
#
#       .. dropdown:: __init__.py
#
#          .. literalinclude:: plugins/gltf_plugin/__init__.py
#
#       .. dropdown:: operators.py
#
#          .. literalinclude:: plugins/gltf_plugin/operators.py
#
#       .. dropdown:: operators_loader.py
#
#          .. literalinclude:: plugins/gltf_plugin/operators_loader.py
#
#       .. dropdown:: gltf_export.py
#
#          .. literalinclude:: plugins/gltf_plugin/gltf_export.py
#
#       .. dropdown:: texture.png
#
#          .. image:: plugins/gltf_plugin/texture.png
#
#       .. dropdown:: assets
#
#          :download:`plugins/gltf_plugin/assets/gltf_sites_winx64.zip`
#
#          :download:`plugins/gltf_plugin/assets/gltf_sites_linx64.zip`
#
#    .. dropdown:: gltf_plugin.xml
#
#       .. literalinclude:: plugins/gltf_plugin.xml
#          :language: xml
#

# %%
# .. include:: ../../user_guide/custom_operators_deps.rst


###############################################################################
# Load Plugin
# -----------
# Once a python plugin is written as a package, it can be loaded with the function
# :py:func:`ansys.dpf.core.core.load_library` taking as first argument the path to the directory of the plugin,
# as second argument ``py_`` + any name identifying the plugin,
# and as last argument the function's name exposed in the ``__init__.py`` file and used to record operators.

import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

#dpf.connect_to_server(port=50052)
tmp = dpf.make_tmp_dir_server()
dpf.upload_files_in_folder(
    dpf.path_utilities.join(tmp, "plugins","gltf_plugin"),
    os.path.join(os.getcwd(), "..", "..", "docs", "source", "examples", "07-python-operators",
                 "plugins", "gltf_plugin")
)
dpf.upload_file(
    os.path.join(os.getcwd(), "..", "..", "docs", "source", "examples", "07-python-operators",
                 "plugins", "gltf_plugin.xml"),
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
# This new Operator ``gltf_export`` requires a triangle surface mesh, a displacement Field on this surface mesh
# as well as an export path as inputs.
# To demo this new Operator, a :class:`ansys.dpf.core.model.Model` on a simple file is created,
# :class:`ansys.dpf.core.operators.mesh.tri_mesh_skin` Operator is used to extract the surface of the mesh in triangles
# elements.

###############################################################################
# Use the Custom Operator
# -----------------------

import tempfile
import os

model = dpf.Model(dpf.upload_file_in_tmp_folder(examples.static_rst))

mesh = model.metadata.meshed_region
skin_mesh = dpf.operators.mesh.tri_mesh_skin(mesh=mesh)

displacement = model.results.displacement()
displacement.inputs.mesh_scoping(skin_mesh)
displacement.inputs.mesh(skin_mesh)
new_operator.inputs.path(os.path.join(tempfile.mkdtemp(), "out"))
new_operator.inputs.mesh(skin_mesh)
new_operator.inputs.field(displacement.outputs.fields_container()[0])
new_operator.run()

print("operator ran successfully")

# %%
# The gltf Operator output can be downloaded :download:`here <images/thumb/out02.glb>`.

