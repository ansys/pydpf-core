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
.. _lsdyna_operators:

Results extraction and analysis from LS-DYNA sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example provides an overview of the LS-DYNA beam results manipulations.

.. note::
    This example requires DPF 6.1 (ansys-dpf-server-2023-2-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

import matplotlib.pyplot as plt
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# d3plot file results extraction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create the model and print its contents. This LS-DYNA d3plot file contains
# several individual results, each at different times. The d3plot file does not
# contain information related to Units. In this case, as the simulation was run
# through Mechanical, a file.actunits file is produced. If this file is
# supplemented in the data_sources, the units will be correctly fetched for all
# results in the file as well as for the mesh.

d3plot = examples.download_d3plot_beam()
ds = dpf.DataSources()
ds.set_result_file_path(d3plot[0], "d3plot")
ds.add_file_path(d3plot[3], "actunits")
my_model = dpf.Model(ds)
# print(my_model)

###############################################################################
# The model has solid (3D) elements and beam (1D) elements. Some of the results
# only apply to one type of elements (such as the stress tensor for solids, or
# the axial force for beams, for example).

# By splitting the mesh by element shape we see that the ball is made by the solid
# 3D elements and the plate by the beam 1D elements

# Define the analysis mesh
my_meshed_region = my_model.metadata.meshed_region

# Get separate meshes for each body
my_meshes = ops.mesh.split_mesh(
    mesh=my_meshed_region, property=dpf.common.elemental_properties.element_shape
).eval()

# Define the meshes in separate variables
ball_mesh = my_meshes.get_mesh(label_space_or_index={"body": 1, "elshape": 1})
plate_mesh = my_meshes.get_mesh(label_space_or_index={"body": 2, "elshape": 2})

# print(my_meshes)
###############################################################################
# Ball

# print(ball_mesh)
# my_ball_mesh.plot()

###############################################################################
# Plate

# print(my_plate_mesh)
# my_plate_mesh.plot()

###############################################################################

my_meshes_scopings = ops.scoping.split_on_property_type(mesh=my_meshed_region).eval()

# Define the mesh scoping in separate variables
# Here we have a elemental location
ball_scoping = my_meshes_scopings.get_scoping(label_space_or_index={"elshape": 1})
plate_scoping = my_meshes_scopings.get_scoping(label_space_or_index={"elshape": 2})

# We will need a nodal location, so we have to transpose the mesh scoping from elemental to nodal
ball_scoping_nodal = dpf.operators.scoping.transpose(
    mesh_scoping=ball_scoping, meshed_region=my_meshed_region
).eval()
plate_scoping_nodal = dpf.operators.scoping.transpose(
    mesh_scoping=plate_scoping, meshed_region=my_meshed_region
).eval()
###############################################################################
# Comparing results in different time steps
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) Define the time steps
time_steps_set = [2, 6, 12]
j = -400
# 2) Copy the mesh of interest. Here it is the plate mesh that we copy along the X axis
for i in time_steps_set:
    # Copy the mesh
    globals()[f"plate_mesh_{i}"] = plate_mesh.deep_copy()

    # 3) Get the plot coordinates that will be changed
    coords_to_update = globals()[f"plate_mesh_{i}"].nodes.coordinates_field
    # 4) Define the coordinates where the new mesh will be placed
    overall_field = dpf.fields_factory.create_3d_vector_field(
        num_entities=1, location=dpf.locations.overall
    )
    overall_field.append(data=[j, 0.0, 0.0], scopingid=1)

    # 5) Define the updated coordinates
    new_coordinates = ops.math.add(fieldA=coords_to_update, fieldB=overall_field).eval()
    coords_to_update.data = new_coordinates.data

    # 6) Extract the result, here we start by getting the displacement
    globals()[f"my_displacement_{i}"] = my_model.results.displacement(
        time_scoping=i, mesh_scoping=plate_scoping_nodal
    ).eval()[0]

    # Increment the coordinate value for the loop
    j = j - 400
###############################################################################
# Use the :class: `Plotter <ansys.dpf.core.plotter.DpfPlotter>` class to add the plots
# in the same image

comparison_plot = dpf.plotter.DpfPlotter()

comparison_plot.add_field(
    field=my_displacement_2, meshed_region=plate_mesh_2, deform_by=my_displacement_2
)
comparison_plot.add_field(
    field=my_displacement_6, meshed_region=plate_mesh_6, deform_by=my_displacement_6
)
comparison_plot.add_field(
    field=my_displacement_12, meshed_region=plate_mesh_12, deform_by=my_displacement_12
)

comparison_plot.show_figure()

###############################################################################
# For example the ball velocity
# v = my_model.results.velocity(time_scoping=my_time_scoping, mesh_scoping=ball_scoping).eval()

###############################################################################
