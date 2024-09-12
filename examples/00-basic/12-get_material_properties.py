# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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
.. _ref_get_material_properties:

Get material properties from the result file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Material properties are assigned to each element in APDL and by default they
are written out in the APDL result file. This example shows how you can extract
material properties of each element using PyDPF-Core.

"""

# Import necessary modules
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
# To extract the Young's modulus for element ID ``1``, first we need to get the
# mat_id for EID ``1``.
mat_id = mats.get_entity_data_by_id(1)

###############################################################################
# And then use the mat_id get the material property.
mat_prop.inputs.properties_name.connect("EX")
mat_field = mat_prop.outputs.properties_value.get_data()[0]
print(mat_field.get_entity_data_by_id(mat_id[0]))

###############################################################################
# Extract Poisson's ratio for element ID ``1``.
mat_prop.inputs.properties_name.connect("NUXY")
mat_field = mat_prop.outputs.properties_value.get_data()[0]
print(mat_field.get_entity_data_by_id(mat_id[0]))
