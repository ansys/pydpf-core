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

from all_types import dpf_types_op, integral_types_op
from ansys.dpf.core.custom_operator import record_operator


def load_operators(*args):
    record_operator(integral_types_op.ForwardBoolOperator, *args)
    record_operator(integral_types_op.ForwardIntOperator, *args)
    record_operator(integral_types_op.ForwardFloatOperator, *args)
    record_operator(integral_types_op.ForwardStringOperator, *args)
    record_operator(integral_types_op.ForwardVecIntOperator, *args)
    record_operator(integral_types_op.SetOutVecDoubleOperator, *args)
    record_operator(integral_types_op.SetOutNpArrayIntOperator, *args)
    record_operator(integral_types_op.SetOutNpArrayDoubleOperator, *args)

    record_operator(dpf_types_op.ForwardFieldOperator, *args)
    record_operator(dpf_types_op.ForwardDataSourcesOperator, *args)
    record_operator(dpf_types_op.ForwardPropertyFieldOperator, *args)
    record_operator(dpf_types_op.ForwardStringFieldOperator, *args)
    record_operator(dpf_types_op.ForwardCustomTypeFieldOperator, *args)
    record_operator(dpf_types_op.ForwardScopingOperator, *args)
    record_operator(dpf_types_op.ForwardScopingsContainerOperator, *args)
    record_operator(dpf_types_op.ForwardFieldsContainerOperator, *args)
    record_operator(dpf_types_op.ForwardMeshesContainerOperator, *args)
    record_operator(dpf_types_op.ForwardWorkflowOperator, *args)
    record_operator(dpf_types_op.ForwardDataTreeOperator, *args)
    record_operator(dpf_types_op.ForwardGenericDataContainerOperator, *args)
