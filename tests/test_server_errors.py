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

import pytest
import sys
import ansys.dpf.core as dpf
from ansys.dpf.core import errors, operators as ops

def test_server_exception_from_operator():
    ds = dpf.DataSources(r"dummy/file.rst")
    op = ops.result.displacement(data_sources=ds)
    with pytest.raises(errors.DPFServerException) as exception_note:
        op.eval()
    
    exception = exception_note.value
    assert hasattr(exception, '__notes__'), "The exception does not contain any note"
    assert exception.__notes__

def test_server_exception_from_workflow():
    op = dpf.operators.result.displacement(data_sources=dpf.DataSources("toto.rst"))
 
    wf = dpf.Workflow()
    wf.add_operator(op)
    wf.set_output_name("out", op.outputs.fields_container)
    
    with pytest.raises(errors.DPFServerException) as exception_note:
        wf.get_output("out", output_type=dpf.FieldsContainer)
    
    print(type(exception_note))
    exception = exception_note.value
    assert hasattr(exception, '__notes__'), "The exception does not contain any note"
    assert exception.__notes__
  