"""
.. _animate_results:

Review of available animation commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example lists the different commands available for creating animations of results,
shown with the arguments available.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples


# Load the model
# model = dpf.Model(examples.msup_transient)
model = dpf.Model(examples.download_piston_rod())
print(model)

# Use scopings to adjust the region and the time steps involved.
# Create a scoping on all nodes
mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(model.metadata.meshed_region.nodes.scoping)
# Create a scoping on all time steps
time_scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(model)

# Instantiate the operator of interest and scope it
displacement_op = model.results.displacement
displacement_op = displacement_op.on_time_scoping(time_scoping)
displacement_op = displacement_op.on_mesh_scoping(mesh_scoping)
# Get the resulting fields container
displacement_fields = displacement_op().outputs.fields_container()

# Animate the fields container by going through the fields and plotting contours
# of the norm. Default behavior consists in:
# - Showing the deformed geometry based on the field itself if 3D.
# - Using a constant and global scale factor of 1.0
displacement_fields.animate(save_as="piston_rod.mp4", framerate=1)

exit()
# scale_factor = 10.
scale_factor = [10.]*len(displacement_fields)
# If the fields contained have several components, then the norm is shown by default.
displacement_fields.animate(deform_by=True, scale_factor=scale_factor,
                            show_axes=True)

# One can format the frequency legend.
displacement_fields.select_component(0).animate(deform_by=displacement_fields, scale_factor=1.,
                                                show_axes=True,
                                                freq_kwargs={"font_size": 12,
                                                             "fmt": ".3"})

# ! Par défaut on affiche la géométrie déformée par le champ donné, si vectoriel 3D.
displacement_fields.animate(scale_factor=10.,
                            freq_kwargs={"font_size": 12,
                                         "fmt": ".3e"})

# # Use case 2

# stress

# géométrie déformée au cours du temps (warp)

# stress_op = model.results.stress
# stress_op = stress_op.on_time_scoping(time_scoping)
# stress_op = stress_op.on_mesh_scoping(mesh_scoping)
# stress_fields = stress_op.eqv().outputs.fields_container()
# stress_fields.animate(deformation_by=model.results.displacement)
# stress_fields.animate(warp_by=model.results.displacement())
# stress_fields.animate(warp_by=model.results.velocity())
# stress_fields.animate(warp_by=model.results.displacement.outputs.fields_container())


# Save the animation using "save_as" with a target path with the desired format as extension.
# (accepts .gif, .avi or .mp4, see pyvista.Plotter.open_movie)
# Can be made off_screen for batch animation creation.
displacement_fields.animate(scale_factor=10.,
                            freq_kwargs={"font_size": 12,
                                         "fmt": ".3e"},
                            save_as="toto.gif")
# This accepts as kwargs arguments taken by pyvista.Plotter.open_movie such as "framerate" and
# "quality".
displacement_fields.animate(scale_factor=10.,
                            freq_kwargs={"font_size": 12,
                                         "fmt": ".3e"},
                            save_as="toto.avi",
                            framerate=4,
                            quality=8,
                            off_screen=True)
