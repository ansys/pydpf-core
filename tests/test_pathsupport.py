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

# Tests specific to pathlib.Path support as path argument instead of str
import functools
import os
from pathlib import Path

import pytest

from ansys import dpf
from conftest import running_docker

skip_always = pytest.mark.skipif(True, reason="Investigate why this is failing")


def test_create_with_resultpath_data_sources_path(allkindofcomplexity, server_type):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources(path, server=server_type)
    assert hasattr(data_sources._internal_obj, "id") or isinstance(data_sources._internal_obj, int)


def test_addpath_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path(path)
    # print(data_sources)


def test_print_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(path)
    assert str(data_sources)
    assert data_sources.result_key == "rst"
    assert len(data_sources.result_files) == 1
    assert os.path.normpath(data_sources.result_files[0]) == os.path.normpath(allkindofcomplexity)


@pytest.mark.skipif(os.name == "nt" and running_docker, reason="Path is setting backslashes")
def test_all_result_operators_exist_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    model = dpf.core.Model(path)
    res = model.results
    for key in res.__dict__:
        if isinstance(res.__dict__[key], functools.partial):
            res.__dict__[key]()


def test_operator_connect_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    op = dpf.core.operators.serialization.field_to_csv()
    op.connect(0, path)
    op.inputs.connect(path)
    op.inputs.file_path.connect(path)
