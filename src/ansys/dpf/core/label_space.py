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

# -*- coding: utf-8 -*-

"""
LabelSpace.

LabelSpace is a key component for managing entries in DPF collections such as FieldsContainer and ScopingsContainer.

It provides a mapping between label names and values,
allowing users to organize, filter, and retrieve data based on metadata
such as time steps, zones, element types, and more.

Typical usage:
- FieldsContainer: Each field is indexed by a LabelSpace, enabling access by time, zone, etc.
- ScopingsContainer: Each scoping is indexed by a LabelSpace, allowing management of multiple selections.

LabelSpace enables advanced data organization and querying in DPF workflows.

"""

from __future__ import annotations

import traceback
from typing import TYPE_CHECKING
import warnings

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Generator

    from ansys.dpf.core.server import AnyServerType

from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
    label_space_capi,
    label_space_grpcapi,
)


class LabelSpace:
    """A class representing a label space, which allows storage and management of key-value pairs (labels)."""

    def __init__(
        self,
        label_space: dict[str, int] | LabelSpace | None = None,
        obj: object = None,
        server: AnyServerType = None,
    ) -> None:
        """
        Initialize a LabelSpace instance.

        Parameters
        ----------
        label_space:
            Dictionary of label names and values, another LabelSpace instance, or an internal label space object.
            If a dictionary is provided, it will be used to fill the label space.
        obj:
            Internal object used for advanced initialization (rarely needed by users).
        server:
            DPF server instance to associate with this label space.

        Examples
        --------
        >>> # Create a LabelSpace from a dictionary
        >>> ls = LabelSpace(label_space={"time": 1, "zone": 2})
        >>> print(dict(ls))
        {'time': 1, 'zone': 2}

        >>> # Create a LabelSpace from another LabelSpace
        >>> ls2 = LabelSpace(label_space=ls)
        >>> print(dict(ls2))
        {'time': 1, 'zone': 2}
        """
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(
            label_space._server if isinstance(label_space, LabelSpace) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=label_space_capi.LabelSpaceCAPI,
            grpcapi=label_space_grpcapi.LabelSpaceGRPCAPI,
        )
        # step3: init environment
        self._api.init_label_space_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if label_space is not None and not isinstance(label_space, dict):
            self._internal_obj = label_space._internal_obj
        else:
            self._internal_obj = self._api.label_space_new_for_object(obj)
            if isinstance(label_space, dict):
                self.fill(label_space)

    @property
    def _data_processing_core_api(self):
        core_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        core_api.init_data_processing_environment(self)
        return core_api

    def fill(self, label_space: dict[str, int]) -> None:
        """
        Fill the label space with the provided dictionary of labels.

        Parameters
        ----------
        label_space : dict
            A dictionary where keys are labels (str) and values are indices (int) to be added to the label space.

        Examples
        --------
        >>> label_space = LabelSpace()
        >>> label_space.fill({"time": 1, "node": 42})
        >>> print(dict(label_space))
        {'time': 1, 'node': 42}
        """
        for key, index in label_space.items():
            self._api.label_space_add_data(self, key, index)

    def __str__(self) -> str:
        """
        Return a string representation of the LabelSpace instance.

        Returns
        -------
        str
            A string representation of the label space, formatted as a dictionary.

        Examples
        --------
        >>> label_space = LabelSpace(label_space={"time": 1, "node": 42})
        >>> print(str(label_space))
        "{'time': 1, 'node': 42}"
        """
        return str(dict(self))

    def __iter__(self) -> Generator[tuple[str, int], None, None]:
        """
        Iterate over the labels in the label space, yielding (key, value) pairs.

        Yields
        ------
        tuple
            A tuple of (key, value) for each label in the label space.

        Examples
        --------
        >>> label_space = LabelSpace(label_space={"time": 1, "node": 42})
        >>> for key, value in label_space:
        ...     print(key, value)
        time 1
        node 42
        """
        yield from [
            (
                self._api.label_space_get_labels_name(self, i),
                self._api.label_space_get_labels_value(self, i),
            )
            for i in range(self._api.label_space_get_size(self))
        ]

    def __dict__(self) -> dict[str, int]:
        """
        Return a dictionary representation of the LabelSpace instance.

        Returns
        -------
        dict
            A dictionary where keys are label names (str) and values are label indices (int).

        Examples
        --------
        >>> label_space = LabelSpace(label_space={"time": 1, "node": 42})
        >>> d = label_space.__dict__()
        >>> print(d)
        {'time': 1, 'node': 42}
        """
        if isinstance(self._internal_obj, dict):
            return self._internal_obj
        out = {}

        for i in range(0, self._api.label_space_get_size(self)):
            out[self._api.label_space_get_labels_name(self, i)] = (
                self._api.label_space_get_labels_value(self, i)
            )
        return out

    def __del__(self) -> None:
        """
        Destructor for cleaning up the label space resources.

        Returns
        -------
        None
        """
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
