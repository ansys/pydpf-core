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
OperatorConnection.

This module contains the `OperatorConnection` and `OperatorConnectionsCollection`
classes, which represent individual connections between operators and a
collection of such connections within a workflow, respectively.
"""

from typing import Iterator, Optional

from ansys.dpf.core import GenericDataContainersCollection
from ansys.dpf.core.custom_container_base import CustomContainerBase
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.generic_data_container import GenericDataContainer


class OperatorConnection(CustomContainerBase):
    """
    Represents a connection between two operators in a workflow.

    This class provides access to the source and target operators, as well as their respective pin IDs.
    """

    def __init__(self, container: GenericDataContainer) -> None:
        """
        Initialize an OperatorConnection object.

        Parameters
        ----------
        container : GenericDataContainer
            The underlying data container that holds the connection's information.
        """
        super().__init__(container)

        self._source_operator: Optional[Operator] = None
        self._source_pin_id: Optional[int] = None
        self._target_operator: Optional[Operator] = None
        self._target_pin_id: Optional[int] = None

    @property
    def source_operator(self) -> Operator:
        """
        Retrieve the source operator of the connection.

        Returns
        -------
        Operator
            The operator serving as the source of this connection.
        """
        if self._source_operator is None:
            self._source_operator = self._container.get_property("source_operator", Operator)

        return self._source_operator

    @property
    def source_pin_id(self) -> int:
        """
        Retrieve the pin ID of the source operator.

        Returns
        -------
        int
            The pin ID of the source operator.
        """
        if self._source_pin_id is None:
            self._source_pin_id = self._container.get_property("source_pin_id", int)

        return self._source_pin_id

    @property
    def target_operator(self) -> Operator:
        """
        Retrieve the target operator of the connection.

        Returns
        -------
        Operator
            The operator serving as the target of this connection.
        """
        if self._target_operator is None:
            self._target_operator = self._container.get_property("target_operator", Operator)

        return self._target_operator

    @property
    def target_pin_id(self) -> int:
        """
        Retrieve the pin ID of the target operator.

        Returns
        -------
        int
            The pin ID of the target operator.
        """
        if self._target_pin_id is None:
            self._target_pin_id = self._container.get_property("target_pin_id", int)

        return self._target_pin_id

    def __str__(self) -> str:
        """
        Return a string representation of the operator connection.

        This includes the source and target operators and their respective pin IDs.

        Returns
        -------
        str
            String representation of the operator connection.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = "     "
        return (
            "OperatorConnection with properties:\n"
            " - source_operator:\n"
            f"{indent(self.source_operator.name, indents)}\n"
            " - source_pin_id:\n"
            f"{indent(self.source_pin_id, indents)}\n"
            " - target_operator:\n"
            f"{indent(self.target_operator.name, indents)}\n"
            " - target_pin_id:\n"
            f"{indent(self.target_pin_id, indents)}"
        )


class OperatorConnectionsCollection:
    """
    Represents a collection of operator connections in a workflow.

    This class provides iterable access to all operator connections, allowing retrieval
    of individual connections or iteration through the entire collection.
    """

    def __init__(self, collection: GenericDataContainersCollection) -> None:
        """
        Initialize an OperatorConnectionsCollection object.

        Parameters
        ----------
        collection : GenericDataContainersCollection
            The underlying collection of operator connections.
        """
        self._collection = collection

    def __len__(self) -> int:
        """
        Return the number of operator connections in the collection.

        Returns
        -------
        int
            The number of operator connections.
        """
        return len(self._collection)

    def __getitem__(self, index: int) -> OperatorConnection:
        """
        Retrieve an operator connection by its index.

        Parameters
        ----------
        index : int
            The index of the operator connection to retrieve.

        Returns
        -------
        OperatorConnection
            The operator connection at the specified index.
        """
        return OperatorConnection(self._collection[index])

    def __iter__(self) -> Iterator[OperatorConnection]:
        """
        Iterate over the operator connections in the collection.

        Yields
        ------
        OperatorConnection
            The next operator connection in the collection.
        """
        for i in range(len(self)):
            yield self[i]

    def __str__(self) -> str:
        """
        Return a string representation of the operator connections collection.

        Returns
        -------
        str
            String representation of the collection.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = ("   ", " - ")
        return "\n".join([indent(operator_connection, *indents) for operator_connection in self])
