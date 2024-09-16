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

# Tests the result.coordinate_system operator
import ansys.dpf.core as dpf
from ansys.dpf.core import examples
import conftest
import numpy as np


def test_operator_coordinate_system_rst(server_type):
    model = dpf.Model(examples.download_hemisphere(server=server_type), server=server_type)
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_1:
        # Starting with DPF 2025.1.pre1
        cs = dpf.operators.result.coordinate_system(server=server_type)
        cs.inputs.data_sources.connect(model)
    else:
        # For previous DPF versions
        cs = model.operator(r"mapdl::rst::CS")
    cs.inputs.cs_id.connect(12)
    cs_rot_mat = cs.outputs.field().data
    ref = np.array(
        [
            [
                -0.18966565,
                0.91517569,
                0.35564083,
                -0.91517569,
                -0.03358143,
                -0.40165376,
                -0.35564083,
                -0.40165376,
                0.84391579,
                4.74164122,
                22.87939222,
                8.89102077,
            ]
        ]
    )
    assert np.allclose(cs_rot_mat.data, ref)
