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

from pathlib import Path
import shutil

from ansys import dpf


def test_create_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    assert hasattr(sc, "release_handles")


def test_release_handles(server_in_process, simple_bar):
    simple_bar = Path(simple_bar)
    copy_path = simple_bar.parent / (simple_bar.stem + "copy" + simple_bar.suffix)
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(str(copy_path), server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    sc.release_handles()
    copy_path.unlink()


def test_release_streams_model(server_in_process, simple_bar):
    simple_bar = Path(simple_bar)
    copy_path = simple_bar.parent / (simple_bar.stem + "copy2" + simple_bar.suffix)
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(str(copy_path), server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    model.metadata.release_streams()
    copy_path.unlink()


def test_release_streams_model_empty(server_in_process):
    model = dpf.core.Model(server=server_in_process)
    model.metadata.release_streams()


def test_create_from_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    dpf.core.streams_container.StreamsContainer(streams_container=sc, server=server_in_process)


def test_streams_container_datasources(server_in_process, simple_bar):
    ds = dpf.core.DataSources(simple_bar, server=server_in_process)
    streams = dpf.core.operators.metadata.streams_provider(
        data_sources=ds, server=server_in_process
    ).eval()
    ds2 = streams.datasources
    assert ds.result_files[0] == ds2.result_files[0]


def test_retrieve_ip(server_in_process):
    start_server = dpf.core.Operator("grpc::stream_provider", server=server_in_process)
    in_thread = 1
    should_start_server = 3

    start_server.connect(2, in_thread)
    start_server.connect(3, should_start_server)

    streams = start_server.get_output(0, dpf.core.types.streams_container)
    ds = streams.datasources

    # look for ip
    assert len(ds.result_files) == 1
    assert ds.result_key == "grpc"

    addr = ds.result_files[0]
    import re

    # can match 999.999.999.999:99999, 0.0.0.0:0
    # but not 0.0.0:0, 9999.999.999.999:999, 0.0.0.0
    ip_addr_regex = r"([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}"
    assert re.match(ip_addr_regex, addr) != None
