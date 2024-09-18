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

from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)
from ansys.dpf.core import types


class ForwardIntOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, int)
        f = self.get_input(0, types.int)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_int"


class ForwardFloatOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, float)
        f = self.get_input(0, types.double)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_float"


class ForwardBoolOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, bool)
        f = self.get_input(0, types.bool)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_bool"


class ForwardStringOperator(CustomOperatorBase):
    def run(self):
        f = self.get_input(0, str)
        f = self.get_input(0, types.string)
        self.set_output(0, f)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_str"


class ForwardVecIntOperator(CustomOperatorBase):
    def run(self):
        input = self.get_input(0, types.vec_int)
        self.set_output(0, input)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_forward_vec_int"


class SetOutVecDoubleOperator(CustomOperatorBase):
    def run(self):
        out = [1.0, 2.0, 3.0]
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        return None

    @property
    def name(self):
        return "custom_set_out_vec_double"


class SetOutNpArrayIntOperator(CustomOperatorBase):
    def run(self):
        import numpy

        out = numpy.ones((100, 2), dtype=numpy.int32)
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification()
        spec.outputs = {0: PinSpecification("flat_int_vec", type_names=types.vec_int)}
        spec.description = (
            "Sets a numpy array of shape (100,2) as output. " "The array is flatten by DPF."
        )
        spec.properties = SpecificationProperties(
            user_name="set out numpy array of int", category="logic"
        )
        return spec

    @property
    def name(self):
        return "custom_set_out_np_int"


class SetOutNpArrayDoubleOperator(CustomOperatorBase):
    def run(self):
        import numpy

        out = numpy.ones((100, 2))
        self.set_output(0, out)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification(
            "Sets a numpy array of shape (100,2) as output." " The array is flatten by DPF."
        )
        spec.outputs = {0: PinSpecification("flat_double_vec", type_names=types.vec_double)}
        spec.properties = SpecificationProperties(
            user_name="set out numpy array of double", category="logic"
        )
        return spec

    @property
    def name(self):
        return "custom_set_out_np_double"
