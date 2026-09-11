"""
.. _ref_get_material_properties:

Get material properties from the result file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Material properties are assigned to each element in APDL and by default they
are written out in the APDL result file. This example shows how you can extract
material properties of each element using PyDPF-Core.

Import necessary modules:
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an example result file.
model = dpf.Model(examples.find_simple_bar())

###############################################################################
# Get the :class:`meshed_region <ansys.dpf.core.meshed_region.MeshedRegion>`
# from model's metadata.
mesh = model.metadata.meshed_region
print(mesh)

###############################################################################
# See available properties in the :class:`meshed_region
# <ansys.dpf.core.meshed_region.MeshedRegion>`.
print(mesh.available_property_fields)

###############################################################################
# Get all material properties.
mats = mesh.property_field("mat")

###############################################################################
# Use the DPF operator :class:`mapdl_material_properties
# <ansys.dpf.core.operators.result.mapdl_material_properties.mapdl_material_properties>`
# to extract data for the # materials - `mats`. For the input
# ``properties_name``, you need the correct material property string. To see
# which strings are supported, you can print the operator help.
mat_prop = model.operator("mapdl_material_properties")
mat_prop.inputs.materials.connect(mats)

###############################################################################
# For the input pin ``properties_name``, you need the correct
# material property string. To see which strings are supported, you can
# print the operator help.
print(mat_prop)

###############################################################################
# Extract the Young's modulus for element ID ``1``.
mat_prop.inputs.properties_name.connect("EX")
mat_field = mat_prop.outputs.properties_value.get_data()[0]
print(mat_field.get_entity_data_by_id(1))

###############################################################################
# Extract Poisson's ratio for element ID ``1``.
mat_prop.inputs.properties_name.connect("NUXY")
mat_field = mat_prop.outputs.properties_value.get_data()[0]
print(mat_field.get_entity_data_by_id(1))
