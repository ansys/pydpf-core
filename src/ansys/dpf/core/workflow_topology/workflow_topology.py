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

"""
WorkflowTopology.

This module contains the `WorkflowTopology` class, which represents
the structure and relationships within a workflow, including its operators,
connections, and exposed input/output pins.
"""

from typing import Optional

from ansys.dpf.core import OperatorsCollection
from ansys.dpf.core.custom_container_base import CustomContainerBase
from ansys.dpf.core.generic_data_container import GenericDataContainer
from ansys.dpf.core.workflow_topology.data_connection import DataConnectionsCollection
from ansys.dpf.core.workflow_topology.exposed_pin import ExposedPinsCollection
from ansys.dpf.core.workflow_topology.operator_connection import OperatorConnectionsCollection


class WorkflowTopology(CustomContainerBase):
    """Represent the workflow topology, including operators, connections, and input/output pins."""

    def __init__(self, container: GenericDataContainer) -> None:
        """
        Initialize a WorkflowTopology object.

        Parameters
        ----------
        container : GenericDataContainer
            The underlying data container that holds the workflow topology information.
        """
        super().__init__(container)

        self._operators: Optional[OperatorsCollection] = None
        self._operator_connections: Optional[OperatorConnectionsCollection] = None
        self._data_connections: Optional[DataConnectionsCollection] = None
        self._exposed_inputs: Optional[ExposedPinsCollection] = None
        self._exposed_outputs: Optional[ExposedPinsCollection] = None

    @property
    def operators(self) -> OperatorsCollection:
        """
        Retrieve the operators in the workflow.

        Returns
        -------
        OperatorsCollection
            A collection of all the operators in the workflow.
        """
        if self._operators is None:
            self._operators = self._container.get_property("operators", OperatorsCollection)

        return self._operators

    @property
    def operator_connections(self) -> OperatorConnectionsCollection:
        """
        Retrieve the operator connections in the workflow.

        Returns
        -------
        OperatorConnectionsCollection
            A collection of all the operator connections in the workflow.
        """
        from ansys.dpf.core import GenericDataContainersCollection

        if self._operator_connections is None:
            self._operator_connections = OperatorConnectionsCollection(
                self._container.get_property(
                    "operator_connections", GenericDataContainersCollection
                )
            )

        return self._operator_connections

    @property
    def data_connections(self) -> DataConnectionsCollection:
        """
        Retrieve the data connections in the workflow.

        Returns
        -------
        OperatorConnectionsCollection
            A collection of all the data connections in the workflow.
        """
        from ansys.dpf.core import GenericDataContainersCollection

        if self._data_connections is None:
            self._data_connections = DataConnectionsCollection(
                self._container.get_property("data_connections", GenericDataContainersCollection)
            )

        return self._data_connections

    @property
    def exposed_inputs(self) -> ExposedPinsCollection:
        """
        Retrieve the exposed inputs in the workflow.

        Returns
        -------
        ExposedPinsCollection
            A collection of all the exposed inputs in the workflow.
        """
        from ansys.dpf.core import GenericDataContainersCollection

        if self._exposed_inputs is None:
            self._exposed_inputs = ExposedPinsCollection(
                self._container.get_property("exposed_inputs", GenericDataContainersCollection)
            )

        return self._exposed_inputs

    @property
    def exposed_outputs(self) -> ExposedPinsCollection:
        """
        Retrieve the exposed outputs in the workflow.

        Returns
        -------
        ExposedPinsCollection
            A collection of all the exposed outputs in the workflow.
        """
        from ansys.dpf.core import GenericDataContainersCollection

        if self._exposed_outputs is None:
            self._exposed_outputs = ExposedPinsCollection(
                self._container.get_property("exposed_outputs", GenericDataContainersCollection)
            )

        return self._exposed_outputs

    def __str__(self) -> str:
        """
        Return a string representation of the workflow topology.

        The string provides details about the workflow's operators, connections, and exposed pins.

        Returns
        -------
        str
            String representation of the workflow topology.
        """
        from ansys.dpf.core.helpers.utils import indent

        def indent_operators(operators):
            indents = ("     ", "   - ")
            return "\n".join([indent(operator.name, *indents) for operator in operators])

        indents = "  "
        return (
            "WorkflowTopology with properties:\n"
            f" - operators (len: {len(self.operators)}):\n"
            f"{indent_operators(self.operators)}\n"
            f" - operator_connections (len: {len(self.operator_connections)}):\n"
            f"{indent(self.operator_connections, indents)}\n"
            f" - data_connections (len: {len(self.data_connections)}):\n"
            f"{indent(self.data_connections, indents)}\n"
            f" - exposed_inputs (len: {len(self.exposed_inputs)}):\n"
            f"{indent(self.exposed_inputs, indents)}\n"
            f" - exposed_outputs (len: {len(self.exposed_outputs)}):\n"
            f"{indent(self.exposed_outputs, indents)}"
        )
