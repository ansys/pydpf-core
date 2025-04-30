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

import numpy as np
import pytest

from ansys.dpf import core
from ansys.dpf.core import operators as ops
import conftest
from conftest import local_servers


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_connect_remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2)
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_connect_3remote_operators(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op1 = ops.result.displacement(data_sources=data_sources1)
    data_sources2 = core.DataSources(simple_bar, server=local_servers[0])
    op2 = ops.result.displacement(data_sources=data_sources2, server=local_servers[0])
    add = ops.math.add_fc(op1, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op1.outputs.fields_container()[0].data)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Connecting data from different servers is " "supported starting server version 4.0",
)
def test_connect_remote_data_to_operator(simple_bar):
    data_sources1 = core.DataSources(simple_bar)
    op2 = ops.result.displacement(data_sources=data_sources1, server=local_servers[0])
    add = ops.math.add_fc(op2, op2, server=local_servers[1])
    fc = add.outputs.fields_container()
    assert np.allclose(fc[0].data, 2 * op2.outputs.fields_container()[0].data)
