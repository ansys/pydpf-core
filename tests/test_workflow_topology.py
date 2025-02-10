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

import pytest

from ansys import dpf
import ansys.dpf.core.operators as op
import conftest
from conftest import raises_for_servers_version_under


def workflow_forward(server_type) -> dpf.core.Workflow:
    """
    ┌─────────┐      ┌────────────┐      ┌────────────┐      ┌──────────┐
    │"Input 0"├─────►│forward_op_1├─────►│forward_op_1├─────►│"Output 0"│
    └─────────┘      └────────────┘      └────────────┘      └──────────┘
                     ┌───────┐           ┌────────────┐      ┌──────────┐
                     │"hello"├──────────►│forward_op_3├─────►│"Output 1"│
                     └───────┘           └────────────┘      └──────────┘
    """

    forward_op_1 = op.utility.forward(server=server_type)
    forward_op_2 = op.utility.forward(server=server_type)
    forward_op_3 = op.utility.forward(server=server_type)

    forward_op_2.inputs.connect(forward_op_1.outputs)
    forward_op_3.inputs.connect("hello")

    workflow = dpf.core.Workflow(server=server_type)

    workflow.add_operators([forward_op_1, forward_op_2, forward_op_3])

    workflow.set_input_name("Input 0", forward_op_1.inputs.any)
    workflow.set_output_name("Output 0", forward_op_2.outputs.any)
    workflow.set_output_name("Output 1", forward_op_3.outputs.any)

    return workflow


def workflow_forward_5(server_type) -> dpf.core.Workflow:
    """
    ┌─────────┐                        ┌──────────┐
    │"Input 0"├──┐                 ┌──►│"Output 0"│
    └─────────┘  │                 │   └──────────┘
    ┌─────────┐  │                 │   ┌──────────┐
    │"Input 1"├──┤                 ├──►│"Output 1"│
    └─────────┘  │                 │   └──────────┘
    ┌─────────┐  │   ┌──────────┐  │   ┌──────────┐
    │"Input 2"├──┼──►│forward_op├──┼──►│"Output 2"│
    └─────────┘  │   └──────────┘  │   └──────────┘
    ┌─────────┐  │                 │   ┌──────────┐
    │"Input 3"├──┤                 ├──►│"Output 3"│
    └─────────┘  │                 │   └──────────┘
    ┌─────────┐  │                 │   ┌──────────┐
    │"Input 4"├──┘                 └──►│"Output 4"│
    └─────────┘                        └──────────┘
    """

    forward_op = op.utility.forward(server=server_type)

    workflow = dpf.core.Workflow(server=server_type)

    workflow.add_operators([forward_op])

    for i in range(5):
        workflow.set_input_name(f"Input {i}", forward_op, i)
        workflow.set_output_name(f"Output {i}", forward_op, i)

    return workflow


def workflow_disp_min_max(server_type) -> dpf.core.Workflow:
    """
    ┌──────────────┐      ┌───────┐      ┌─────────────┐      ┌─────┐
    │"data_sources"├─────►│disp_op├─────►│min_max_fc_op├──┬──►│"min"│
    └──────────────┘      └───────┘      └─────────────┘  │   └─────┘
                                                          │   ┌─────┐
                                                          └──►│"max"│
                                                              └─────┘
    """

    disp_op = op.result.displacement(server=server_type)
    min_max_fc_op = op.min_max.min_max_fc(disp_op, server=server_type)

    workflow = dpf.core.Workflow(server=server_type)

    workflow.add_operators([disp_op, min_max_fc_op])

    workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    workflow.set_output_name("min", min_max_fc_op.outputs.field_min)
    workflow.set_output_name("max", min_max_fc_op.outputs.field_max)

    return workflow


workflows = {
    "workflow_forward": workflow_forward,
    "workflow_forward_5": workflow_forward_5,
    "workflow_disp_min_max": workflow_disp_min_max,
}
workflow_topologies = {
    "workflow_forward": {
        "operators": 3,
        "operator_connections": 1,
        "data_connections": 1,
        "exposed_inputs": 1,
        "exposed_outputs": 2,
    },
    "workflow_forward_5": {
        "operators": 1,
        "operator_connections": 0,
        "data_connections": 0,
        "exposed_inputs": 5,
        "exposed_outputs": 5,
    },
    "workflow_disp_min_max": {
        "operators": 2,
        "operator_connections": 1,
        "data_connections": 0,
        "exposed_inputs": 1,
        "exposed_outputs": 2,
    },
}


@pytest.fixture(
    params=list(workflows.values()),
    ids=list(workflows.keys()),
)
def workflow(server_type, request) -> dpf.core.Workflow:
    wf = request.param(server_type)
    wf.name = list(workflows.keys())[request.param_index]
    return wf


@pytest.fixture()
def expected_workflow_topology(workflow):
    return workflow_topologies[workflow.name]


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    reason="Operator `workflow_to_workflow_topology` does not exist below 10.0",
)
def test_instantiate_workflow_to_workflow_topology_op(server_type):
    workflow_to_workflow_topology_op = dpf.core.Operator(
        "workflow_to_workflow_topology", server=server_type
    )

    assert workflow_to_workflow_topology_op


@raises_for_servers_version_under("10.0")
def test_workflow_get_topology(workflow):
    workflow_topology = workflow.get_topology()

    assert workflow_topology


@raises_for_servers_version_under("10.0")
def test_workflow_topology_sizes(workflow, expected_workflow_topology):
    workflow_topology = workflow.get_topology()

    assert len(workflow_topology.operators) == expected_workflow_topology["operators"]
    assert (
        len(workflow_topology.operator_connections)
        == expected_workflow_topology["operator_connections"]
    )
    assert len(workflow_topology.data_connections) == expected_workflow_topology["data_connections"]
    assert len(workflow_topology.exposed_inputs) == expected_workflow_topology["exposed_inputs"]
    assert len(workflow_topology.exposed_outputs) == expected_workflow_topology["exposed_outputs"]


@raises_for_servers_version_under("10.0")
def test_workflow_topology_str(workflow):
    workflow_topology = workflow.get_topology()

    # We only check that it does not raise
    assert str(workflow_topology)
