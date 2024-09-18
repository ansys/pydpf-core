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

import os
import shutil

from ansys import dpf


def test_create_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    assert hasattr(sc, "release_handles")


def test_release_handles(server_in_process, simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0] + "copy" + split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path, server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    sc.release_handles()
    os.remove(copy_path)


def test_release_streams_model(server_in_process, simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0] + "copy2" + split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path, server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    model.metadata.release_streams()
    os.remove(copy_path)


def test_release_streams_model_empty(server_in_process):
    model = dpf.core.Model(server=server_in_process)
    model.metadata.release_streams()


def test_create_from_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    dpf.core.streams_container.StreamsContainer(streams_container=sc, server=server_in_process)
