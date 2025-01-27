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

import os
from pathlib import Path

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import animation, examples, misc

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
else:
    HAS_PYVISTA = False

gif_name = "test.gif"


@pytest.fixture(autouse=False)
def remove_gifs(request):
    """Remove GIF once finished."""

    def remove_gif():
        if Path.cwd().joinpath(gif_name).exists():
            Path.cwd().joinpath(gif_name).unlink()

    request.addfinalizer(remove_gif)


@pytest.fixture()
def displacement_fields():
    model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    result = model.results.displacement.on_all_time_freqs.eval()
    return result


def test_animate_mode(displacement_fields):
    animation.animate_mode(displacement_fields, mode_number=10)


def test_animate_mode_positive_disp(displacement_fields):
    animation.animate_mode(displacement_fields, mode_number=3, type_mode=1)


def test_animator_animate_mode_fields_container_one_component(displacement_fields):
    animation.animate_mode(displacement_fields.select_component(0), mode_number=10)
