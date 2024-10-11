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
# print(model)

###############################################################################
# The model has solid (3D) elements and beam (1D) elements. Some of the results
# only apply to one type of elements (such as the stress tensor for solids, or
# the axial force for beams, for example).

# By splitting the mesh by element shape we see that the ball is made by the solid
# 3D elements and the plate by the beam 1D elements

my_meshed_region = my_model.metadata.meshed_region

my_meshes = ops.mesh.split_mesh(mesh=my_meshed_region, property="elemental").eval()
# print(my_meshes)
###############################################################################
# Ball

# print(my_meshes[0])
# my_meshes[0].plot()

###############################################################################
# Plate

# print(my_meshes[1])
# my_meshes[1].plot()


###############################################################################
# We can split the mesh scoping so it's easier to chose from which body we are
# analysing the results

my_meshes_scopings = ops.scoping.split_on_property_type(mesh=my_meshed_region).eval()
my_time_scoping = my_model.metadata.time_freq_support.time_frequencies
# For example the ball velocity
v = my_model.results.velocity(time_scoping=my_time_scoping).eval()


# Forces

###############################################################################
# compare results in different time steps
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sforces = my_model.results.beam_s_shear_force(mesh_scoping=my_meshes_scopings[1]).eval()
Sforces2 = my_model.results.beam_s_shear_force(mesh_scoping=my_meshes_scopings[0]).eval()

comparison_plot = dpf.plotter.DpfPlotter
comparison_plot.add_field(field=Sforces, meshed_region=my_meshes[1])
comparison_plot.add_field(field=Sforces2, meshed_region=my_meshes[0])

comparison_plot.show_figure()
