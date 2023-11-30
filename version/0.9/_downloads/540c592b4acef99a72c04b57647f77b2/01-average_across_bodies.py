"""
.. _ref_average_across_bodies:

Average across bodies
~~~~~~~~~~~~~~~~~~~~~

In multibody simulations, some nodes may be shared by the bodies at their interfaces,
but the values of the results (for example stresses or strains) calculated at these nodes
may differ between the bodies. This can cause discontinuous plots, given that a single
node will have multiple values for a variable. To avoid this, you can average these results
across the bodies of the model.


This example demonstrates how to average across bodies in DPF when
dealing with ``Nodal`` variables. It also illustrates how the end results
of a postprocessing workflow can be different when averaging and when not.

.. note::
    This example requires DPF 6.1 or above.
    For more information, see :ref:`ref_compatibility`.

"""
###############################################################################
# Import the necessary modules

from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops
from ansys.dpf.core import examples


###############################################################################
# Load the simulation results from an RST file and create a model of it.

analysis = examples.download_piston_rod()
model = dpf.Model(analysis)
print(model)

###############################################################################
# To visualize the model and see how the bodies are connected, extract their
# individual meshes using the ``split_mesh`` operator with the ``mat`` (or "material")
# property.

mesh = model.metadata.meshed_region
split_mesh_op = ops.mesh.split_mesh(mesh=mesh, property="mat")
meshes = split_mesh_op.outputs.meshes()

meshes.plot(text="Body meshes")

###############################################################################
# As can be seen in the preceding image, even though the piston rod is one single part,
# it is composed of two different bodies. Additionally, their interface shares common nodes.

###############################################################################
# Averaging across bodies with DPF
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # To compare the results of averaging across bodies and not averaging,
# define two workflows.
# The variable of interest is the Von Mises stress field, which is
# calculated by applying the ``eqv_fc`` operator on the
# stresses extracted from the model.

# %%
# .. graphviz::
#
#   digraph foo {
#       graph [pad="0", nodesep="0.3", ranksep="0.3"]
#       node [shape=box, style=filled, fillcolor="#ffcc0", margin="0"];
#       rankdir=LR;
#       splines=line;
#       node [fixedsize=true,width=2.5]
#       ds [label="data_src", shape=box, style=filled, fillcolor=cadetblue2];
#       stress [label="stress"];
#       scp [label="split_on_property_type"];
#       eln_to_n ["elemental_nodal_to_nodal_fc"];
#       vm [label="eqv_fc"];
#       avg [label="weighted_merge_fields_by_label"];
#       subgraph cluster_1 {
#           ds -> scp [style=dashed];
#           scp -> stress;
#           stress -> eln_to_n;
#           eln_to_n -> vm;
#           label="Without averaging across bodies";
#           style=filled;
#           fillcolor=lightgrey;
#       }
#       subgraph cluster_2 {
#           ds -> scp [style=dashed];
#           scp -> stress;
#           stress -> eln_to_n;
#           eln_to_n -> vm;
#           vm -> avg;
#           label="With averaging across bodies";
#           style=filled;
#           fillcolor=lightgrey;
#       }
#   }


###############################################################################
# Workflow for not averaging across bodies
# ----------------------------------------
# Computing Von Mises stresses without averaging across the bodies of the
# model requires the stresses to be extracted separately for each body.
# To do this in DPF, pass a scopings container the stress operator that
# contains the elements of each body in scopings, separated by the ``mat`` label

split_scop_op = ops.scoping.split_on_property_type()
split_scop_op.inputs.mesh.connect(mesh)
split_scop_op.inputs.requested_location.connect(dpf.locations.elemental)
split_scop_op.inputs.label1.connect("mat")

print(split_scop_op.outputs.mesh_scoping())

###############################################################################
# Set the time set of interest to the last time set:

time_set = 3
###############################################################################
# Extracting the stresses for each body of the simulation:

stress_op = ops.result.stress()
stress_op.inputs.time_scoping.connect(time_set)
stress_op.inputs.data_sources.connect(model)
stress_op.inputs.mesh_scoping.connect(split_scop_op)
stress_op.inputs.requested_location.connect(dpf.locations.elemental_nodal)

###############################################################################
# Proceeding with the workflow to obtain ``Nodal`` Von Mises stresses:

eln_to_n_op = ops.averaging.elemental_nodal_to_nodal_fc()
eln_to_n_op.inputs.fields_container.connect(stress_op)

von_mises_op = ops.invariant.von_mises_eqv_fc()
von_mises_op.inputs.fields_container.connect(eln_to_n_op)

print(von_mises_op.outputs.fields_container())
###############################################################################
# As you can see, the final Von Mises stresses fields container has the ``mat``
# label with two different entries, meaning that it holds data for two separate bodies.
# Finally, define this workflow as a function for better organization and
# ease of use:


def not_average_across_bodies(analysis):
    # This function extracts the ElementalNodal stress tensors of the simulation
    # for each body involved, averages them to the nodes and computes Von Mises

    model = dpf.Model(analysis)
    mesh = model.metadata.meshed_region

    time_set = 3

    split_scop_op = ops.scoping.split_on_property_type()
    split_scop_op.inputs.mesh.connect(mesh)
    split_scop_op.inputs.requested_location.connect(dpf.locations.elemental)
    split_scop_op.inputs.label1.connect("mat")

    stress_op = ops.result.stress()
    stress_op.inputs.time_scoping.connect(time_set)
    stress_op.inputs.data_sources.connect(model)
    stress_op.inputs.mesh_scoping.connect(split_scop_op)
    stress_op.inputs.requested_location.connect(dpf.locations.elemental_nodal)

    eln_to_n_op = ops.averaging.elemental_nodal_to_nodal_fc()
    eln_to_n_op.inputs.fields_container.connect(stress_op)

    von_mises_op = ops.invariant.von_mises_eqv_fc()
    von_mises_op.inputs.fields_container.connect(eln_to_n_op)

    vm_stresses = von_mises_op.outputs.fields_container()

    return vm_stresses


###############################################################################
# Workflow for averaging across bodies
# ------------------------------------
# The workflow for performing averaging across bodies in DPF is similar to to the
# one shown above, with the extraction of stresses per body. The difference comes
# in the end, where a weighted merge is done between the fields that contain different
# values for the ``mat`` label to actually average the results across the bodies.
# Define a function like the one above:


def average_across_bodies(analysis):
    # This function extracts the ElementalNodal stress tensors of the simulation
    # for each body involved, averages them to the nodes and computes Von Mises

    model = dpf.Model(analysis)
    mesh = model.metadata.meshed_region

    time_set = 3

    split_scop_op = ops.scoping.split_on_property_type()
    split_scop_op.inputs.mesh.connect(mesh)
    split_scop_op.inputs.requested_location.connect(dpf.locations.elemental)
    split_scop_op.inputs.label1.connect("mat")

    stress_op = ops.result.stress()
    stress_op.inputs.time_scoping.connect(time_set)
    stress_op.inputs.data_sources.connect(model)
    stress_op.inputs.mesh_scoping.connect(split_scop_op)
    stress_op.inputs.requested_location.connect(dpf.locations.elemental_nodal)

    eln_to_n_op = ops.averaging.elemental_nodal_to_nodal_fc()
    eln_to_n_op.inputs.fields_container.connect(stress_op)
    # Mid node weights needed for averaging across bodies
    eln_to_n_op.inputs.extend_weights_to_mid_nodes.connect(True)

    von_mises_op = ops.invariant.von_mises_eqv_fc()
    von_mises_op.inputs.fields_container.connect(eln_to_n_op)

    # Merging fields that represent different bodies
    merge_op = ops.utility.weighted_merge_fields_by_label()
    merge_op.inputs.fields_container.connect(von_mises_op)
    merge_op.inputs.label.connect("mat")
    # Connecting weights needed to perform the weighted average
    merge_op.connect(1000, eln_to_n_op, 1)

    vm_stresses = merge_op.outputs.fields_container()

    return vm_stresses


###############################################################################
# In this case, we can see that the output fields container only has one field, indicating
# that the results of the two different bodies were averaged successfully.

print(average_across_bodies(analysis))

###############################################################################
# Plot and compare the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The two different approaches can be compared. The first plot shows the
# results when averaging across bodies is not performed, while the second illustrates
# when it is.

non_avg_stresses = not_average_across_bodies(analysis)
avg_stresses = average_across_bodies(analysis)

meshes.plot(non_avg_stresses)
mesh.plot(avg_stresses)
###############################################################################
# Finally, the maximum stresses for both cases can be compared:

min_max = dpf.operators.min_max.min_max_fc()

# Non averaged across bodies
min_max.inputs.fields_container.connect(non_avg_stresses)
max_non_avg = max(min_max.outputs.field_max().data)

# Averaged across bodies
min_max.inputs.fields_container.connect(avg_stresses)
max_avg = max(min_max.outputs.field_max().data)


diff = abs(max_avg - max_non_avg) / max_non_avg * 100
print("Max stress when averaging across bodies is activated: {:.2f} Pa".format(max_avg))
print("Max stress when averaging across bodies is deactivated: {:.2f} Pa".format(max_non_avg))
print(
    "The maximum stress value when averaging across bodies is PERFORMED \
is {:.2f}% LOWER than when it is NOT PERFORMED".format(
        diff
    )
)

###############################################################################
# Dedicated Operator
# ~~~~~~~~~~~~~~~~~~
#
# .. note::
#     The operator detailed below is available in Ansys 23R2 and later versions.
#
# Alternatively, those workflows can be automatically instantiated by calling the
# ``stress_eqv_as_mechanical`` operator, which does exactly the same thing as described
# in the functions above, depending on what is passed to the "average_across_bodies" input
# pin:

stress_op = ops.result.stress_eqv_as_mechanical()
stress_op.inputs.time_scoping.connect([time_set])
stress_op.inputs.data_sources.connect(model)
stress_op.inputs.requested_location.connect(dpf.locations.nodal)
stress_op.inputs.average_across_bodies.connect(False)

print(stress_op.outputs.fields_container())
