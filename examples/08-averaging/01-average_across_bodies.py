"""
.. _ref_average_across_bodies:

Average across bodies
~~~~~~~~~~~~~~~
This example is aimed towards explaining how to activate or deactivate the averaging
across bodies option in DPF. When we have a multibody simulation that involves the
calculation of ElementalNodal fields, like stresses or strains, we can either
activate or deactivate the option of averaging theses fields across the different
bodies when they share common nodes. This will likely change the end results that are
displayed after the post processing of the simulation, as we will see below.

"""
###############################################################################
# Let's start by importing the necessary modules.

from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core import examples

###############################################################################
# Then we can load the simulation results from a .rst file and create a model of it.

analysis = examples.download_piston_rod()
model = dpf.Model(analysis)
print(model)

###############################################################################
# Now, let's take a look at our system to see how our bodies are connected to
# each other. First, we extract the mesh of our model and then we divide it into
# different meshes using the split_mesh operator.

mesh = model.metadata.meshed_region
split_mesh_op = ops.mesh.split_mesh(mesh=mesh, property="mat")
meshes = split_mesh_op.outputs.meshes()

# Uncomment this block to obtain the plot
# meshes.plot(
#     text='Body meshes')

# %%
# .. image:: images/01-meshes_plot.png
#     :align: center
#     :width: 600

###############################################################################
# As we can see in the image above, even though the piston rod is one single part,
# it's composed of two different bodies. Additionally, we can observe that the region
# where the two bodies are bonded together contains nodes that are common between them.

###############################################################################
# Now, let's take a look into how the averaging across bodies option alters the
# results of a simulation.

###############################################################################
# Averaging across bodies with DPF
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Let's define two workflows. The first one does averaging across bodies, while the
# second one doesn't. The variable of interest here is the stress in the Z direction,
# which will be obtained using the "stress_Z" operator.

# %%
# .. image:: 01-average_across_bodies.svg
#     :align: center
#     :width: 800

###############################################################################
# Averaging across bodies activated
# ---------------------------------
# The extraction of the stresses in the Z direction in DPF applies by default averaging
# across bodies. Therefore, a simple workflow like the one shown below can be used
# in this case.


def average_across_bodies(analysis):
    # This function will extract the stresses in the Z direction (with the average
    # across bodies property activated) and plot them.

    # Create a model from the simulation results.
    model = dpf.Model(analysis)
    mesh = model.metadata.meshed_region

    # We're interested in the last time step, so:
    time_step = 3

    # Extracting the stresses in the Z direction. By default, DPF already applies
    # averaging across bodies when extracting the stresses.
    stress_op = ops.result.stress_Z()
    stress_op.inputs.connect(model)
    stress_op.inputs.time_scoping.connect(time_step)
    stress_op.inputs.requested_location.connect("Nodal")
    stresses = stress_op.outputs.fields_container()

    # Finding the maximum stress value
    min_max = dpf.operators.min_max.min_max_fc()
    min_max.inputs.fields_container.connect(stresses)
    max_val = min_max.outputs.field_max()

    # Uncomment this block to obtain the plot
    # mesh.plot(
    #     stresses,
    #     text='Averaged across bodies')

    return max(max_val.data)


###############################################################################
# Averaging across bodies deactivated
# -----------------------------------
# To extract the stresses without averaging across the bodies of the simulated
# part, the workflow is a bit more complicated. So, instead of being presented
# as a function, it will be broken into various parts with explanations of what
# is being done.

###############################################################################
# First, we create a model from the simulation results and extract its mesh and
# step informations.
model = dpf.Model(analysis)
mesh = model.metadata.meshed_region
time_freq = model.metadata.time_freq_support
steps = time_freq.time_frequencies.data.tolist()

###############################################################################
# We need to split the meshes of the two bodies so we can then create separate
# scopings for each one of them. The 'mat' label is used to split the mesh by bodies.
mesh_scop_op = ops.scoping.split_on_property_type(mesh=mesh, label1="mat")
mesh_scop_cont = mesh_scop_op.outputs.mesh_scoping()

###############################################################################
# Then, as we have 3 different time steps, we need to create a ScopingsContainer
# that contains the meshes of each one of these steps. We do so as follows:

scop_cont = dpf.ScopingsContainer()
scop_cont.add_label("body")
scop_cont.add_label("time")
for step in steps:
    body = 1
    for mesh_scop in mesh_scop_cont:
        scop_cont.add_scoping(
            scoping=mesh_scop, label_space={"body": body, "time": int(step)}
        )
        body += 1
print(scop_cont)

###############################################################################
# As we can see, we've got 6 different Scopings inside our ScopingsContainer, one for
# each body over each one of the three time steps. Let's now focus our analysis on the
# last time step:
time_step = 3

###############################################################################
# Then, to retrieve the Z stresses without averaging across the two bodies, we can pass
# a ScopingsContainer that contains their respective meshes as a parameter to the
# stress_Z operator. To be able to do that, we need a new ScopingsContainer that contains
# the meshes of the two bodies in the desired time step.

scop_list = scop_cont.get_scopings(label_space={"time": time_step})
scopings = dpf.ScopingsContainer()
scopings.add_label("body")
body = 1
for scop in scop_list:
    scopings.add_scoping(label_space={"body": body}, scoping=scop)
    body += 1
print(scopings)
###############################################################################
# We can see that, in this container, we only have two Scopings, one for each body
# in the last time step, as desired.

###############################################################################
# Finally, we can extract the stresses in the Z direction.

stress_op = ops.result.stress_Z()
stress_op.inputs.connect(model)
stress_op.inputs.time_scoping.connect(time_step)
stress_op.inputs.mesh_scoping.connect(
    scopings
)  # This option deactivates averaging across bodies.
stress_op.inputs.requested_location.connect("Nodal")
stresses = stress_op.outputs.fields_container()
print(stresses)
###############################################################################
# Additionally, we can find the maximum value of the stress field for comparison purposes.

min_max = dpf.operators.min_max.min_max_fc()
min_max.inputs.fields_container.connect(stresses)
max_val = min_max.outputs.field_max()

###############################################################################
# Finally, we can plot the results. To do that, we can extract the meshes of each
# body as a meshed_region object and use them to build our plot.

split_mesh_op = ops.mesh.split_mesh(mesh=mesh, property="mat")
meshes = split_mesh_op.outputs.meshes()

# Uncomment this block to obtain the plot.
# meshes.plot(
#         stresses,
#         text='Not averaged across bodies')
###############################################################################
# We can also define the workflow presented above as a function:


def not_average_across_bodies(analysis):
    # This function will extract the stresses in the Z direction (with the average
    # across bodies option deactivated) and plot them.

    model = dpf.Model(analysis)
    mesh = model.metadata.meshed_region

    time_freq = model.metadata.time_freq_support
    steps = time_freq.time_frequencies.data.tolist()

    mesh_scop_op = ops.scoping.split_on_property_type(mesh=mesh, label1="mat")
    mesh_scop_cont = mesh_scop_op.outputs.mesh_scoping()

    scop_cont = dpf.ScopingsContainer()
    scop_cont.add_label("body")
    scop_cont.add_label("time")
    for step in steps:
        body = 1
        for mesh_scop in mesh_scop_cont:
            scop_cont.add_scoping(
                scoping=mesh_scop, label_space={"body": body, "time": int(step)}
            )
            body += 1

    time_step = 3

    scop_list = scop_cont.get_scopings(label_space={"time": time_step})
    scops = dpf.ScopingsContainer()
    scops.add_label("body")
    body = 1
    for scop in scop_list:
        scops.add_scoping(label_space={"body": body}, scoping=scop)
        body += 1

    stress_op = ops.result.stress_Z()
    stress_op.inputs.connect(model)
    stress_op.inputs.time_scoping.connect(time_step)
    stress_op.inputs.mesh_scoping.connect(scops)
    stress_op.inputs.requested_location.connect("Nodal")
    stresses = stress_op.outputs.fields_container()

    min_max = dpf.operators.min_max.min_max_fc()
    min_max.inputs.fields_container.connect(stresses)
    max_val = min_max.outputs.field_max()

    split_mesh_op = ops.mesh.split_mesh(mesh=mesh, property="mat")
    meshes = split_mesh_op.outputs.meshes()

    # Uncomment this block to obtain the plot
    # meshes.plot(
    #     stresses,
    #     text='Not averaged across bodies')

    return max(max_val.data)


###############################################################################
# Plotting the results
# ~~~~~~~~~~~~~~~~~~~~
# Finally, let's plot the results to see how they compare. In the first image, we have
# the stress distribution when the averaging across bodies options is activated, while
# in the second one it's deactivated.

max_avg_on = average_across_bodies(analysis)
max_avg_off = not_average_across_bodies(analysis)

# %%
# |pic1| |pic2|
#
# .. |pic1| image:: images/01-averaged_across_bodies.png    
#     :width: 45%
#
# .. |pic2| image:: images/01-not_averaged_across_bodies.png
#     :width: 45%
###############################################################################
diff = abs(max_avg_on - max_avg_off) / max_avg_off * 100
print(
    "Max stress when averaging across bodies is activated: {:.2f} Pa".format(max_avg_on)
)
print(
    "Max stress when averaging across bodies is deactivated: {:.2f} Pa".format(
        max_avg_off
    )
)
print(
    "The maximum stress value when averaging across bodies is ACTIVATED \
is {:.2f}% LOWER than when it is DEACTIVATED".format(
        diff
    )
)