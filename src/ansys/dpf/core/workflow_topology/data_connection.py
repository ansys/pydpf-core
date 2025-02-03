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
DataConnection.

This module contains the `DataConnection` and `DataConnectionsCollection`
classes, which represent individual connections between data and operator,
and a collection of such connections within a workflow, respectively.
"""

from typing import Any, Iterator, Optional

from ansys.dpf.core import GenericDataContainersCollection
from ansys.dpf.core.custom_container_base import CustomContainerBase
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.generic_data_container import GenericDataContainer


class DataConnection(CustomContainerBase):
    """
    Represents a connection between a data and an operator in a workflow.

    This class provides access to the source data and target operator, as well as its pin ID.
    """

    def __init__(self, container: GenericDataContainer) -> None:
        """
        Initialize an DataConnection object.

        Parameters
        ----------
        container : GenericDataContainer
            The underlying data container that holds the connection's information.
        """
        super().__init__(container)

        self._source_data: Optional[Any] = None
        self._target_operator: Optional[Operator] = None
        self._target_pin_id: Optional[int] = None

    @property
    def source_data(self) -> Any:
        """
        Retrieve the source data of the connection.

        Returns
        -------
        Any
            The data serving as the source of this connection.
        """
        if self._source_data is None:
            self._source_data = self._container.get_property("source_data")

        return self._source_data

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
        Return a string representation of the data connection.

        This includes the source data and target operator, with its pin ID.

        Returns
        -------
        str
            String representation of the data connection.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = "     "
        return (
            "DataConnection with properties:\n"
            " - source_data:\n"
            f"{indent(self.source_data, indents)}\n"
            " - target_operator:\n"
            f"{indent(self.target_operator.name, indents)}\n"
            " - target_pin_id:\n"
            f"{indent(self.target_pin_id, indents)}"
        )


class DataConnectionsCollection:
    """
    Represents a collection of data connections in a workflow.

    This class provides iterable access to all data connections, allowing retrieval
    of individual connections or iteration through the entire collection.
    """

    def __init__(self, collection: GenericDataContainersCollection) -> None:
        """
        Initialize an DataConnectionsCollection object.

        Parameters
        ----------
        collection : GenericDataContainersCollection
            The underlying collection of data connections.
        """
        self._collection = collection

    def __len__(self) -> int:
        """
        Return the number of data connections in the collection.

        Returns
        -------
        int
            The number of data connections.
        """
        return len(self._collection)

    def __getitem__(self, index: int) -> DataConnection:
        """
        Retrieve a data connection by its index.

        Parameters
        ----------
        index : int
            The index of the data connection to retrieve.

        Returns
        -------
        DataConnection
            The data connection at the specified index.
        """
        return DataConnection(self._collection[index])

    def __iter__(self) -> Iterator[DataConnection]:
        """
        Iterate over the data connections in the collection.

        Yields
        ------
        DataConnection
            The next data connection in the collection.
        """
        for i in range(len(self)):
            yield self[i]

    def __str__(self) -> str:
        """
        Return a string representation of the data connections collection.

        Returns
        -------
        str
            String representation of the collection.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = ("   ", " - ")
        return "\n".join([indent(data_connection, *indents) for data_connection in self])
