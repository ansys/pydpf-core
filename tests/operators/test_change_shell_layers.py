# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

# Tests the utility.change_shell_layers operator

import os

import pytest

import ansys.dpf.core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.check_version import get_server_version, meets_version


@pytest.mark.skipif(
    (not meets_version(get_server_version(dpf.SERVER), meets="9.0")) and os.name == "posix"
)  # Failure under investigation on Ubuntu for DPF 24R2 and older (Issue #2424)
def test_operator_change_shell_layers_connect_enum(server_type):
    model = dpf.Model(
        examples.download_all_kinds_of_complexity_modal(server=server_type), server=server_type
    )

    stress = model.results.stress()
    stress.inputs.requested_location.connect("Nodal")

    # Test connection through signature
    change_shell_layers = dpf.operators.utility.change_shell_layers(
        fields_container=stress, e_shell_layer=dpf.common.shell_layers.bottom, server=server_type
    )
    _ = change_shell_layers.eval()

    # Test connection through Input.connect
    change_shell_layers = dpf.operators.utility.change_shell_layers(server=server_type)
    change_shell_layers.inputs.fields_container.connect(stress)
    change_shell_layers.inputs.e_shell_layer.connect(dpf.common.shell_layers.bottom)
    _ = change_shell_layers.eval()

    # Test connection through Inputs.connect
    change_shell_layers = dpf.operators.utility.change_shell_layers(server=server_type)
    change_shell_layers.inputs.connect(stress)
    change_shell_layers.inputs.connect(dpf.common.shell_layers.bottom)
    _ = change_shell_layers.eval()
