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

from ansys.dpf.core.custom_operator import CustomOperatorBase, record_operator
from ansys.dpf.core import Field
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    SpecificationProperties,
    PinSpecification,
)


class AddFloatToFieldData(CustomOperatorBase):
    def run(self):
        field = self.get_input(0, Field)
        to_add = self.get_input(1, float)
        data = field.data
        data += to_add
        self.set_output(0, field)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification()
        spec.description = "Add a custom value to all the data of an input Field"
        spec.inputs = {
            0: PinSpecification("field", [Field], "Field on which float value is added."),
            1: PinSpecification("to_add", [float], "Data to add."),
        }
        spec.outputs = {
            0: PinSpecification("field", [Field], "Field on which the float value is added.")
        }
        spec.properties = SpecificationProperties("custom add to field", "math")
        return spec

    @property
    def name(self):
        return "custom_add_to_field"


def load_operators(*args):
    record_operator(AddFloatToFieldData, *args)
