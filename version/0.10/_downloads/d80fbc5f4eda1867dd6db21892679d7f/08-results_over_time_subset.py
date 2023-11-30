# noqa: D400
"""
.. _ref_results_over_time:

Scope results over custom time domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Result <ansys.dpf.core.results.Result>` class, which are instances
created by the :class:`Model <ansys.dpf.core.model.Model>`, give
access to helpers for requesting results on specific mesh and time scopings.
With these helpers, working on a temporal subset of the
model is straightforward. In this example, different ways to choose the temporal subset to
evaluate a result are exposed. This example can be extended to frequency subsets.

"""

# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Create a model object to establish a connection with an example result file:
model = dpf.Model(examples.download_transient_result())
print(model)

###############################################################################
# Request specific time sets
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# If specific time sets are of interest, looking into the ``TimeFreqSupport``
# and connect a given ``time_scoping`` accordingly to the cumulative indexes can be useful.

print(model.metadata.time_freq_support)

time_sets = [1, 3, 10]
disp = model.results.displacement.on_time_scoping(time_sets).eval()

print(disp)

# Or using a scoping
time_sets_scoping = dpf.time_freq_scoping_factory.scoping_by_sets([1, 3, 10])
disp = model.results.displacement.on_time_scoping(time_sets_scoping).eval()

print(disp)

###############################################################################
# Equivalent to:
disp_op = model.results.displacement()
disp_op.inputs.time_scoping(time_sets)
disp = disp_op.outputs.fields_container()

###############################################################################
# Equivalent to:
disp = model.results.displacement(time_scoping=time_sets_scoping).eval()

###############################################################################
# Request specific time steps
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# If specific time steps or load steps are of interest, looking into the
# ``TimeFreqSupport`` and connect a given ``time_scoping`` located on steps can be done.
time_steps_scoping = dpf.time_freq_scoping_factory.scoping_by_load_step(1)
disp = model.results.displacement.on_time_scoping(time_steps_scoping).eval()

print(disp)

###############################################################################
# Equivalent to:
disp_op = model.results.displacement()
disp_op.inputs.time_scoping(time_steps_scoping)
disp = disp_op.outputs.fields_container()

###############################################################################
# Using helpers
# ~~~~~~~~~~~~~
# Evaluate at all times.

disp = model.results.displacement.on_all_time_freqs().eval()

###############################################################################
# Evaluate at first and last times
disp = model.results.displacement.on_first_time_freq().eval()
print(disp)
disp = model.results.displacement.on_last_time_freq().eval()
print(disp)
