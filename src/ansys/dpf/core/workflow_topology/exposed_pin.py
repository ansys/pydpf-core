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


class ExposedPin(CustomContainerBase):
    def __init__(self, container):
        super().__init__(container)
        self._name = None
        self._operator = None
        self._pin_id = None

    @property
    def name(self):
        if self._name is None:
            self._name = self._container.get_property("name", str)

        return self._name

    @property
    def operator(self):
        from ansys.dpf.core.dpf_operator import Operator

        if self._operator is None:
            self._operator = self._container.get_property("operator", Operator)

        return self._operator

    @property
    def pin_id(self):
        if self._pin_id is None:
            self._pin_id = self._container.get_property("pin_id", int)

        return self._pin_id

    def __str__(self):
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
    def __init__(self, collection):
        self._collection = collection

    def __len__(self):
        return len(self._collection)

    def __getitem__(self, index):
        return ExposedPin(self._collection[index])

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        from ansys.dpf.core.helpers.utils import indent

        indents = ("   ", " - ")
        return "\n".join([indent(exposed_pin, *indents) for exposed_pin in self])
