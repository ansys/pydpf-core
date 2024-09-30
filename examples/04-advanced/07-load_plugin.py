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

"""
.. _ref_load_plugin:

Load plugin
~~~~~~~~~~~

This example shows how to load a plugin that is not loaded automatically.

"""

###############################################################################
# Import DPF-Core:
from ansys.dpf import core as dpf

server = dpf.global_server()

###############################################################################
# Create a base service for loading a plugin:
if server.os == "posix":
    dpf.core.load_library("libAns.Dpf.Math.so", "math_operators")
else:
    dpf.core.load_library("Ans.Dpf.Math.dll", "math_operators")

###############################################################################
# Math operators are now loaded and accessible in ``ansys.dpf.core.operators``:

from ansys.dpf.core import operators as ops

math_op = ops.math.fft_eval()
