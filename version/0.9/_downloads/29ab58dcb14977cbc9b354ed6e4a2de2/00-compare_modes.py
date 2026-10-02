# noqa: D400
"""
.. _ref_compare_modes:

Use Result Helpers to compare mode shapes for solids and then shells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`Result <ansys.dpf.core.results.Result>` class which instances
are created by the :class:`Model <ansys.dpf.core.model.Model>` gives access to
helpers to request results on specific mesh and time scopings.
With those helpers, working on a custom spatial and temporal subset of the
model is straightforward.
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# First, create a model object to establish a connection with an
# example result file
model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
print(model)

###############################################################################
# Visualize specific mode shapes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Choose the modes to visualize
modes = [1, 5, 10, 15]

###############################################################################
# Choose to split the displacement on solid/shell/beam to only focus on shell
# elements
disp = model.results.displacement
for mode in modes:
    fc = disp.on_time_scoping(mode).split_by_shape.eval()
    model.metadata.meshed_region.plot(fc.shell_field())

###############################################################################
# Choose to split the displacement on solid/shell/beam to only focus on solid
# elements
disp = model.results.displacement
for mode in modes:
    fc = disp.on_time_scoping(mode).split_by_shape.eval()
    model.metadata.meshed_region.plot(fc.solid_field())
