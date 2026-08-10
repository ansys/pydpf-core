# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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
import json

import ansys.dpf.core as dpf
from ansys.dpf.core import errors, operators as ops


def test_server_exception_from_operator():
    ds = dpf.DataSources(r"dummy/file.rst")
    op = ops.result.displacement(data_sources=ds)
    with pytest.raises(errors.DPFServerException) as exception_note:
        op.eval()

    exception = exception_note.value
    assert hasattr(exception, "__notes__"), "The exception does not contain any note"
    assert exception.__notes__


def test_server_exception_from_workflow():
    op = dpf.operators.result.displacement(data_sources=dpf.DataSources("toto.rst"))

    wf = dpf.Workflow()
    wf.add_operator(op)
    wf.set_output_name("out", op.outputs.fields_container)

    with pytest.raises(errors.DPFServerException) as exception_note:
        wf.get_output("out", output_type=dpf.FieldsContainer)

    exception = exception_note.value
    assert hasattr(exception, "__notes__"), "The exception does not contain any note"
    assert exception.__notes__


def test_server_exception_legacy_flat_string():
    exception = errors.DPFServerException("V:751<-native::recursor:1930<-actual root cause")
    assert str(exception) == "actual root cause"
    assert exception.__notes__ == ["V:751<-native::recursor:1930"]
    # Structured attributes stay empty for legacy errors.
    assert exception.type is None
    assert exception.what is None
    assert exception.suggestion is None
    assert exception.fields == {}
    assert exception.chain == []


def test_server_exception_legacy_no_chain():
    exception = errors.DPFServerException("a plain error message")
    assert str(exception) == "a plain error message"
    assert exception.type is None


def test_server_exception_structured():
    payload = {
        "depth": 3,
        "frames": {
            "2": {
                "type": "kernel_clayer",
                "what": 'Exception raised through CLayer function "Operator_run".',
                "function_name": "Operator_run",
            },
            "1": {
                "type": "opframe",
                "what": 'Operator "U" (42) threw.',
                "operator_name": "U",
                "operator_id": 42,
            },
            "0": {
                "type": "ansys.dpf.lsdyna.file_not_found",
                "what": "d3plot file not found: /wrong/path/to/d3plot",
                "filepath": "/wrong/path/to/d3plot",
                "suggestion": "Check that the file path is correct and that the file is accessible.",
            },
        },
    }
    exception = errors.DPFServerException(json.dumps(payload))

    assert exception.type == "ansys.dpf.lsdyna.file_not_found"
    assert exception.what == "d3plot file not found: /wrong/path/to/d3plot"
    assert exception.suggestion == "Check that the file path is correct and that the file is accessible."
    assert exception.fields == {"filepath": "/wrong/path/to/d3plot"}
    assert exception.chain == [errors.OperatorFrame("U", 42)]
    # Root cause and suggestion form the user-facing message.
    assert exception.what in str(exception)
    assert exception.suggestion in str(exception)
    # The operator chain is kept as a developer note.
    assert exception.__notes__ == ["Operator chain: U (42)"]


def test_server_exception_structured_multiple_operator_frames():
    payload = {
        "depth": 4,
        "frames": {
            "3": {"type": "kernel_clayer", "what": "clayer", "function_name": "Operator_run"},
            "2": {"type": "opframe", "what": "outer", "operator_name": "V", "operator_id": 751},
            "1": {
                "type": "opframe",
                "what": "inner",
                "operator_name": "native::recursor",
                "operator_id": 1930,
            },
            "0": {"type": "resource_exhaustion", "what": "Out-of-memory.", "resource": "heap_memory"},
        },
    }
    exception = errors.DPFServerException(json.dumps(payload))

    assert exception.type == "resource_exhaustion"
    assert exception.suggestion is None
    assert exception.fields == {"resource": "heap_memory"}
    # Outermost operator first, down to the root cause.
    assert exception.chain == [
        errors.OperatorFrame("V", 751),
        errors.OperatorFrame("native::recursor", 1930),
    ]
    assert str(exception) == "Out-of-memory."


def test_server_exception_not_structured_json():
    # Valid JSON but not a DPF structured error: treated as a plain message.
    exception = errors.DPFServerException('{"unexpected": "payload"}')
    assert exception.type is None
    assert str(exception) == '{"unexpected": "payload"}'
