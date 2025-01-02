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

"""Here we write all the doc string examples. This way we can be sure that they
still work.
A method is written for each python file of dpf-core.
If a failure occurs, the change must be done here and in the corresponding
docstring."""

import doctest
import os
from pathlib import Path

import pytest


@pytest.mark.skipif(True, reason="examples are created for windows")
def test_doctest_allfiles():
    directory = r"../ansys/dpf/core"
    actual_path = Path(__file__).parent.absolute()
    print(actual_path)
    for filename in os.listdir(actual_path / directory):
        if filename.endswith(".py"):
            path = Path(directory) / filename
            print(path)
            doctest.testfile(str(path), verbose=True, raise_on_error=True)
        else:
            continue


@pytest.mark.skipif(True, reason="examples are created for windows")
def test_doctest_allexamples():
    directory = r"../examples"
    actual_path = Path(__file__).parent.absolute()
    handled_files = []
    for root, subdirectories, _ in os.walk(actual_path / directory):
        for subdirectory in subdirectories:
            subdir = Path(root) / subdirectory
            print(subdir)
            for filename in os.listdir(subdir):
                if filename.endswith(".py"):
                    path = subdir / filename
                    if ".ipynb_checkpoints" in str(path):
                        continue
                    print(path)
                    handled_files.append(str(path))
                    exec(
                        path.read_text(encoding="utf-8"),
                        globals(),
                        globals(),
                    )
                else:
                    continue
    print(handled_files)


if __name__ == "__main__":
    test_doctest_allfiles()
