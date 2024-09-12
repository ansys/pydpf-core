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
