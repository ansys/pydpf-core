# noqa: D400
"""
.. _ref_use_result_helpers:

Use result helpers to load custom data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Result <ansys.dpf.core.results.Result>` class, which is an instance
created by the :class:`Model <ansys.dpf.core.model.Model>`, gives
access to helpers for requesting results on specific mesh and time scopings.
With these helpers, working on a custom spatial and temporal subset of the
model is straightforward.

"""

# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an example result file:
model = dpf.Model(examples.download_multi_stage_cyclic_result())
print(model)

###############################################################################
# Visualize specific mode shapes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Choose the modes to visualize:
modes = [1, 5, 6]

disp = model.results.displacement.on_time_scoping(modes)

###############################################################################
# Choose a spatial subset
# ~~~~~~~~~~~~~~~~~~~~~~~
# Work on only a named selection (or component).

###############################################################################
# Print the available named selection:
print(model.metadata.available_named_selections)

###############################################################################
# Specify to the result that you want to work on a specific named selection:
disp.on_named_selection("_STAG1_BASE_NOD")
op = disp()
op.inputs.read_cyclic(2)  # expand cyclic
results = op.outputs.fields_container()

# plot
for mode in modes:
    results[0].meshed_region.plot(results.get_fields_by_time_complex_ids(mode, 0)[0])

###############################################################################
# Specify to the result that you want to work on specific nodes:
disp = model.results.displacement.on_time_scoping(modes)
disp.on_mesh_scoping(list(range(1, 200)))
op = disp()
op.inputs.read_cyclic(2)  # expand cyclic
results = op.outputs.fields_container()

# plot
for mode in modes:
    results[0].meshed_region.plot(results.get_fields_by_time_complex_ids(mode, 0)[0])
