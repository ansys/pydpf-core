"""
.. _animate_results:

Review of available animation commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example lists the different commands available for creating animations of results,
shown with the arguments available.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Plot the bare mesh of a model
model = dpf.Model(examples.msup_transient)
# print(model)
# model.plot(title='Model', text='Transient thermal model')

# Get the fields_container of interest
# temperature_fields = model.results.temperature.on_all_time_freqs().outputs.fields_container()
# # Animate and save to a file
# temperature_fields.animate(save_as='animate_fields_container.gif', off_screen=False)
#
#
# # One can also animate deformed geometries
# model = dpf.Model(examples.msup_transient)
# displacement_fields = model.results.displacement.on_all_time_freqs().outputs.fields_container()
# displacement_fields.animate(save_as='animate_deformed_fields_container.mp4', framerate=3,
#                             warping_field=model.results.displacement, scale_factor=5.0)

# # Use case 1

# displacements

# scoping sur la zone spatiale d'intérêt
mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(model.metadata.meshed_region.nodes.scoping)

# scoping sur les frames d'intérêt
time_scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(model)

displacement_op = model.results.displacement
displacement_op = displacement_op.on_time_scoping(time_scoping)
displacement_op = displacement_op.on_mesh_scoping(mesh_scoping)
displacement_fields = displacement_op().outputs.fields_container()
print(displacement_fields)
# >>>
# scale_factor = 10.
# scale_factor = [10.]*len(displacement_fields)
# # ! Si un champ est vectoriel, on affiche la norme du champ.
# displacement_fields.animate(deform_by=True, scale_factor=scale_factor,
#                             show_axes=True)
#
# # ! On affiche le temps de chaque frame, avec son unité, et un formatage optionnel
# displacement_fields.select_component(0).animate(deform_by=displacement_fields, scale_factor=1.,
#                                                 show_axes=True,
#                                                 freq_kwargs={"font_size": 12,
#                                                              "fmt": ".3"})
#
# # ! Par défaut on affiche la géométrie déformée par le champ donné, si vectoriel 3D.
# displacement_fields.animate(scale_factor=10.,
#                             freq_kwargs={"font_size": 12,
#                                          "fmt": ".3e"})

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

# # Use case 3

# Champ scalaire créé variant au cours du temps

# Champ vectoriel variant au cours du temps

# # Use case 4

# Champ vectoriel complexe à animer selon la phase
# Champ vectoriel à animer selon le rpm

# # Use case 12

# Animer un mode vibratoire avec scaling de la déformée de 0 à 1, de 1 à 0
# Animer ce mode vibratoire en aller-retour

# field.animate(warp_by=XXX, scale_factor=[0.1, 0.3, 0.2, 0.0])
# field.animate(warp_by=XXX, scale_factor=FieldsContainer) --> on a un champ de scale à chaque frame
#
# disp_op = model.results.displacement
# scale_op = operators.math.scale(disp_op)
# scale_factor = [0.1, 0.2, 0.3]
# pl = DpfPlotter()
# pl.add_workflow(input=disp_op.input.scale_factor, output=scale_op.output.field)
# pl.animate(input=scale_factor)
#
# pl.add_workflow(input={"scale_factor": disp_op.input.scale_factor},
#                 output={"scaled": scale_op.output.field})
# pl.add_workflow(workflow=workflow)
# pl.animate(input={"scale_factor": scale_factor}, output="scaled")

# # Use case 5

# Animer un maillage qui change (NLAD) avec des contours et du warp

# # Use case 6

# Animer une collection de maillages avec des contours et du warp définis par body.

# # Use case 7

# Gestion de la position de la caméra   - position fixe
#                                       - relatif à un noeud
#                                       - relatif à une face
#                                       - qui reste normal à une face
#                                       - relatif à un élément
#                                       - relatif à un body ***** P1
#                                       - qui suit un body  ***** P1
#                                       - selon un path

# # Use case 8

# Sauvegarder l'animation en gif ou mp4, avec gestion du framerate... etc.
# displacement_fields.animate(scale_factor=10.,
#                             freq_kwargs={"font_size": 12,
#                                          "fmt": ".3e"},
#                             save_as="toto.gif")
# Can save a movie, accepts as kwargs any argument or kwargs taken by pyvista.Plotter.open_movie
displacement_fields.animate(scale_factor=10.,
                            freq_kwargs={"font_size": 12,
                                         "fmt": ".3e"},
                            save_as="toto.avi",
                            framerate=4,
                            quality=8)

# # Use case 9

# Appliquer une texture (couleur, PRB...) à un body

# # Use case 10

# Appliquer une texture d'environnement

# # Use case 11

# Ajouter des lumières, gérer les lumières
# Activer les ombres

# # Use case X

# Animer une courbe
