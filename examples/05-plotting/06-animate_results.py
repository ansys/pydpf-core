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
model = dpf.Model(examples.transient_therm)
print(model)
# model.plot(title='Model', text='Transient thermal model')

# Get the fields_container of interest
temperature_fields = model.results.temperature.on_all_time_freqs().outputs.fields_container()
# Animate and save to a file
temperature_fields.animate(save_as='animate_fields_container.gif', off_screen=False)


# One can also animate deformed geometries
model = dpf.Model(examples.msup_transient)
displacement_fields = model.results.displacement.on_all_time_freqs().outputs.fields_container()
displacement_fields.animate(save_as='animate_deformed_fields_container.mp4', framerate=3,
                            warping_field=model.results.displacement, scale_factor=5.0)
