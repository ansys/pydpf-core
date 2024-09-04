# noqa: D400
"""
.. _lsdyna_operators:

Results extraction and analysis from LS-DYNA sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example provides an overview of the LS-DYNA results providers.

.. note::
    This example requires DPF 6.1 (ansys-dpf-server-2023-2-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

import matplotlib.pyplot as plt
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

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
model = dpf.Model(ds)
print(model)

###############################################################################
# The model has solid (3D) elements and beam (1D) elements. Some of the results
# only apply to one type of elements (such as the stress tensor for solids, or
# the axial force for beams, for example).
#
# Let's extract beam axial force for the last time step and plot it, deforming
# the mesh according to the displacement field at the same time step.

N = model.results.beam_axial_force(time_scoping=[12]).eval()
u = model.results.displacement(time_scoping=[12]).eval()

sargs = dict(title="N", fmt="%.2e", title_font_size=30, label_font_size=20)
N[0].plot(deform_by=u[0], scalar_bar_args=sargs)

###############################################################################
# The axial force has only been computed for the beam elements (the bottom
# frame), whereas the top sphere, which is comprised by solid elements, has
# only been deformed by the displacement field.
#
# PyDPF also allows you to animate the results in a FieldsContainer. Thus, if
# all time steps are extracted, an animation can be produced.

N_all = model.results.beam_axial_force.on_all_time_freqs.eval()
u_all = model.results.displacement.on_all_time_freqs.eval()
N_all.animate(deform_by=u_all, save_as="falling_ball.gif", scalar_bar_args=sargs)

###############################################################################
# Some of the results are marked as global. They are not scoped over any mesh
# entity, but are global variables of the model.

K = model.results.global_kinetic_energy().eval()
print(K)

###############################################################################
# Energy plots over time (the sphere was released with some initial velocity).

U = model.results.global_internal_energy().eval()
H = model.results.global_total_energy().eval()

plt.plot(K.time_freq_support.time_frequencies.data, K[0].data, label="Kinetic")
plt.plot(U.time_freq_support.time_frequencies.data, U[0].data, label="Internal")
plt.plot(H.time_freq_support.time_frequencies.data, H[0].data, label="Total")
plt.xlabel("Time ({:s})".format(K.time_freq_support.time_frequencies.unit))
plt.ylabel("Energies ({:s})".format(K[0].unit))
plt.legend()
plt.show()

###############################################################################
# binout file results extraction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create the model and dprint its contents. This LS-DYNA binout file contains
# several branches (glstat, matsum and rcforc).

binout = examples.download_binout_matsum()
ds = dpf.DataSources()
ds.set_result_file_path(binout, "binout")
model = dpf.Model(ds)
print(model)

###############################################################################
# In this case, the Unit System is not attached to the data_source, but it can
# be directly assigned to the results. As we are employing the dpf.Model API, we
# only need to assign the Unit System once (the Model will assign it for the
# rest of the results).
#
# Results from the matsum branch of the binout file are a FieldsContainer on a
# LabelSpace comprised by part IDs. Extract part kinetic energy for all parts:

PKE_op = model.results.part_kinetic_energy()
PKE_op.inputs.unit_system.connect(dpf.unit_systems.solver_mks)
PKE = PKE_op.eval()
print(PKE)

###############################################################################
# Extract part internal energy for only a selected number of parts.

part_sco = dpf.Scoping(ids=[50, 1522], location="part")
PIE_op = model.results.part_internal_energy()
PIE_op.inputs.entity_scoping.connect(part_sco)
PIE = PIE_op.eval()

###############################################################################
# Plot part kinetic and internal energy for a selection of parts. In this case,
# the TimeFreqSupport of the matsum branch does not have all the time steps in
# the binout file. Thus, a rescoping operation is needed:

rescope_op = dpf.operators.scoping.rescope()
rescope_op.inputs.fields.connect(PKE.time_freq_support.time_frequencies)
rescope_op.inputs.mesh_scoping.connect(PKE[0].scoping)
t_field = rescope_op.outputs.fields_as_field()
t_vals = t_field.data

plt.plot(t_vals, PKE.get_field({"part": 50}).data, label="Kinetic, Part 50")
plt.plot(t_vals, PKE.get_field({"part": 1522}).data, label="Kinetic, Part 1522")
plt.plot(t_vals, PIE.get_field({"part": 50}).data, label="Internal, Part 50")
plt.plot(t_vals, PIE.get_field({"part": 1522}).data, label="Internal, Part 1522")
plt.xlabel("Time ({:s})".format(t_field.unit))
plt.ylabel("Energy ({:s})".format(PIE.get_field({"part": 50}).unit))
plt.legend()
plt.show()

###############################################################################
# Similarly, results from the rcforc branch of the binout file are a
# FieldsContainer on a LabelSpace comprised by interface IDs. Extract interface
# contact force for only one interface.

interface_sco = dpf.Scoping(ids=[19], location="interface")
FC_op = model.results.interface_contact_force()
FC_op.inputs.entity_scoping.connect(interface_sco)
FC = FC_op.eval()
print(FC)

###############################################################################
# In addition to interface, the FieldsContainer is scoped on idtype (0 for the
# master side of the interface, 1 for the slave). Contact force is a vector, and
# the three components are available.

rescope_op = dpf.operators.scoping.rescope()
rescope_op.inputs.fields.connect(FC.time_freq_support.time_frequencies)
rescope_op.inputs.mesh_scoping.connect(FC[0].scoping)
t_field = rescope_op.outputs.fields_as_field()
t_vals = t_field.data

FX = FC.select_component(0)
FY = FC.select_component(1)
FZ = FC.select_component(2)

plt.plot(t_vals, FX.get_field({"interface": 19, "idtype": 0}).data, label="FX, slave")
plt.plot(t_vals, FX.get_field({"interface": 19, "idtype": 1}).data, label="FX, master")
plt.plot(t_vals, FY.get_field({"interface": 19, "idtype": 0}).data, label="FY, slave")
plt.plot(t_vals, FY.get_field({"interface": 19, "idtype": 1}).data, label="FY, master")
plt.plot(t_vals, FZ.get_field({"interface": 19, "idtype": 0}).data, label="FZ, slave")
plt.plot(t_vals, FZ.get_field({"interface": 19, "idtype": 1}).data, label="FZ, master")
plt.xlabel("Time ({:s})".format(t_field.unit))
plt.xlim([0, 10])
plt.ylabel("Contact Force ({:s})".format(FX.get_field({"interface": 19, "idtype": 0}).unit))
plt.legend()
plt.show()
