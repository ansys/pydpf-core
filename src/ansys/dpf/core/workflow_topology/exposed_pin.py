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
ExposedPin.

This module contains the `ExposedPin` and `ExposedPinsCollection` classes,
which represent individual exposed pins and a collection of exposed pins in a workflow,
respectively. These classes enable easy access to the pins that serve as input/output points
for the workflow.
"""

from typing import Iterator, Optional

from ansys.dpf.core import GenericDataContainersCollection
from ansys.dpf.core.custom_container_base import CustomContainerBase
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.generic_data_container import GenericDataContainer


class ExposedPin(CustomContainerBase):
    """
    Represents an exposed input or output pin in a workflow.

    This class provides access to the name and the associated operator, as well as its pin ID.
    """

    def __init__(self, container: GenericDataContainer) -> None:
        """
        Initialize an ExposedPin object.

        Parameters
        ----------
        container : GenericDataContainer
            The underlying data container that holds the exposed pin's information.
        """
        super().__init__(container)

        self._name: Optional[str] = None
        self._operator: Optional[Operator] = None
        self._pin_id: Optional[int] = None

    @property
    def name(self) -> str:
        """
        Retrieve the name of the exposed pin.

        Returns
        -------
        str
            The name of the exposed pin.
        """
        if self._name is None:
            self._name = self._container.get_property("name", str)

        return self._name

    @property
    def operator(self) -> Operator:
        """
        Retrieve the operator associated with the exposed pin.

        Returns
        -------
        Operator
            The operator associated with this exposed pin.
        """
        if self._operator is None:
            self._operator = self._container.get_property("operator", Operator)

        return self._operator

    @property
    def pin_id(self) -> int:
        """
        Retrieve the pin ID of the operator.

        Returns
        -------
        int
            The pin ID of the operator.
        """
        if self._pin_id is None:
            self._pin_id = self._container.get_property("pin_id", int)

        return self._pin_id

    def __str__(self) -> str:
        """
        Return a string representation of the exposed pin.

        This includes the name and associated operator, with its pin ID.

        Returns
        -------
        str
            String representation of the exposed pin.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = "     "
        return (
            "ExposedPin with properties:\n"
            " - name:\n"
            f"{indent(self.name, indents)}\n"
            " - operator:\n"
            f"{indent(self.operator.name, indents)}\n"
            " - pin_id:\n"
            f"{indent(self.pin_id, indents)}"
        )


class ExposedPinsCollection:
    """
    Represents a collection of exposed pins in a workflow.

    This class provides iterable access to all exposed pins, allowing retrieval
    of individual exposed pins or iteration through the entire collection.
    """

    def __init__(self, collection: GenericDataContainersCollection) -> None:
        """
        Initialize an ExposedPinsCollection object.

        Parameters
        ----------
        collection : GenericDataContainersCollection
            The underlying collection of exposed pins.
        """
        self._collection = collection

    def __len__(self) -> int:
        """
        Return the number of exposed pins in the collection.

        Returns
        -------
        int
            The number of exposed pins.
        """
        return len(self._collection)

    def __getitem__(self, index: int) -> ExposedPin:
        """
        Retrieve an exposed pin by its index.

        Parameters
        ----------
        index : int
            The index of the exposed pin to retrieve.

        Returns
        -------
        ExposedPin
            The exposed pin at the specified index.
        """
        return ExposedPin(self._collection[index])

    def __iter__(self) -> Iterator[ExposedPin]:
        """
        Iterate over the exposed pins in the collection.

        Yields
        ------
        ExposedPin
            The next exposed pin in the collection.
        """
        for i in range(len(self)):
            yield self[i]

    def __str__(self) -> str:
        """
        Return a string representation of the exposed pins collection.

        Returns
        -------
        str
            String representation of the collection.
        """
        from ansys.dpf.core.helpers.utils import indent

        indents = ("   ", " - ")
        return "\n".join([indent(exposed_pin, *indents) for exposed_pin in self])
