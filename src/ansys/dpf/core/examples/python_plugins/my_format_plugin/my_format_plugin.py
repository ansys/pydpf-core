# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Entry point for the MyFormat DPF plugin.

DPF calls ``load_operators`` when the plugin is loaded.  Every custom operator
class must be registered here with
:func:`~ansys.dpf.core.custom_operator.record_operator`.
"""

from mesh_info_provider import mesh_info_provider
from mesh_provider import mesh_provider
from result_info_provider import result_info_provider
from result_provider import displacement_provider, temperature_provider
from streams_provider import streams_provider
from time_freq_support_provider import time_freq_support_provider

from ansys.dpf.core.custom_operator import record_operator


def load_operators(*args):
    """Call with the DPF server to register all operators of the plugin."""
    record_operator(streams_provider, *args)
    record_operator(result_info_provider, *args)
    record_operator(time_freq_support_provider, *args)
    record_operator(mesh_info_provider, *args)
    record_operator(mesh_provider, *args)
    record_operator(displacement_provider, *args)
    record_operator(temperature_provider, *args)
