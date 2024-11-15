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

from ansys.dpf.core.custom_container_base import CustomContainerBase


class DataConnection(CustomContainerBase):
    def __init__(self, container):
        super().__init__(container)
        self._source_data = None
        self._target_operator = None
        self._target_pin_id = None

    @property
    def source_data(self):
        if self._source_data is None:
            self._source_data = self._container.get_property("source_data")

        return self._source_data

    @property
    def target_operator(self):
        from ansys.dpf.core.dpf_operator import Operator

        if self._target_operator is None:
            self._target_operator = self._container.get_property("target_operator", Operator)

        return self._target_operator

    @property
    def target_pin_id(self):
        if self._target_pin_id is None:
            self._target_pin_id = self._container.get_property("target_pin_id", int)

        return self._target_pin_id

    def __str__(self):
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
    def __init__(self, collection):
        self._collection = collection

    def __len__(self):
        return len(self._collection)

    def __getitem__(self, index):
        return DataConnection(self._collection[index])

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        from ansys.dpf.core.helpers.utils import indent

        indents = ("   ", " - ")
        return "\n".join([indent(data_connection, *indents) for data_connection in self])
