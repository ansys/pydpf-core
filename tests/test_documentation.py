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

from pathlib import Path

import ansys.dpf.core as dpf
from ansys.dpf.core.documentation.generate_operators_doc import generate_operators_doc


def test_generate_operators_doc(tmp_path: Path):
    generate_operators_doc(ansys_path=dpf.SERVER.ansys_path, output_path=tmp_path, verbose=False)
    file_to_test = tmp_path / "toc.yml"
    assert file_to_test.exists()
    file_to_test = tmp_path / "operator-specifications" / "utility" / "forward.md"
    assert file_to_test.exists()


def test_generate_operators_doc_plugin_and_update(tmp_path: Path):
    specs_path = tmp_path / "operator-specifications"
    specs_path.mkdir()
    utility_path = specs_path / "utility"
    utility_path.mkdir()
    forward_update_path = utility_path / "forward_upd.md"
    test_string = r"""## Description
        
Test update"""
    with forward_update_path.open(mode="w", encoding="utf-8") as ff:
        ff.write(test_string)
    generate_operators_doc(
        ansys_path=dpf.SERVER.ansys_path,
        output_path=tmp_path,
        verbose=False,
        desired_plugin="core",
    )
    file_to_test = tmp_path / "toc.yml"
    assert file_to_test.exists()
    file_to_test = utility_path / "forward.md"
    assert file_to_test.exists()
    with file_to_test.open(mode="r", encoding="utf-8") as ff:
        text = ff.read()
    assert test_string in text
