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

from ansys import dpf
import conftest
import weakref

skip_always = pytest.mark.skipif(True, reason="Investigate why this is failing")


def test_create_data_sources(server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    assert data_sources._internal_obj


def test_create_with_resultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(allkindofcomplexity, server=server_type)
    assert data_sources._internal_obj


def test_setresultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)


def test_setdomainresultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(allkindofcomplexity, 0)
    data_sources.set_domain_result_file_path(allkindofcomplexity, 0, key="rst")


def test_addpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity)


def test_add_domain_file_path_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_domain_file_path(allkindofcomplexity, "rst", 1)


def test_adddomainpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity, "rst", is_domain=True, domain_id=1)


def test_addfilepathspecifiedresult_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(allkindofcomplexity, "d3plot")


def test_setresultpath_data_sources_no_extension(d3plot_beam, binout_glstat, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(d3plot_beam)
    assert data_sources.result_key == "d3plot"
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(binout_glstat)
    assert data_sources.result_key == "binout"


def test_set_resultpath_data_sources_h5(server_type):
    from ansys.dpf.core import examples

    cas_h5_file = examples.download_fluent_axial_comp(server=server_type)["cas"][0]
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(cas_h5_file)
    assert data_sources.result_key == "cas"
    data_sources = dpf.core.DataSources(result_path=cas_h5_file, server=server_type)
    assert data_sources.result_key == "cas"


def test_set_resultpath_data_sources_cff(server_type):
    from ansys.dpf.core import examples

    cas_h5_file = examples.download_cfx_heating_coil(server=server_type)["cas"]
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(cas_h5_file)
    assert data_sources.result_key == "cas"
    data_sources = dpf.core.DataSources(result_path=cas_h5_file, server=server_type)
    assert data_sources.result_key == "cas"


def test_set_resultpath_data_sources_cfx_res(server_type):
    from ansys.dpf.core import examples

    res_file = examples.download_cfx_mixing_elbow(server=server_type)
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(res_file)
    assert data_sources.result_key == "cas"


def test_addupstream_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources2 = dpf.core.DataSources(server=server_type)
    data_sources.add_upstream(data_sources2)


def test_delete_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)


def test_print_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == [allkindofcomplexity]


def test_data_sources_from_data_sources(allkindofcomplexity, server_type):
    with pytest.raises(ValueError) as e:
        dpf.core.DataSources(data_sources="Wrong Input", server=server_type)
        assert "gRPC data sources" in e
    data_sources = dpf.core.DataSources(server=server_type)
    dpf.core.DataSources(data_sources=data_sources, server=server_type)


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Bug in server version lower than 4.0",
)
def test_several_result_path_data_sources(server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path("file_hello.rst")
    data_sources.set_result_file_path("file_bye.rst")
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == ["file_hello.rst", "file_bye.rst"]


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Copying data is supported starting server version 3.0",
)
def test_delete_auto_data_sources(server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    ref = weakref.ref(data_sources)
    data_sources = None
    import gc

    gc.collect()
    assert ref() is None


@conftest.raises_for_servers_version_under("7.0")
def test_register_namespace(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)
    op = dpf.core.operators.result.displacement(data_sources=data_sources, server=server_type)
    assert op.eval() is not None
    data_sources.register_namespace("rst", "notmapdl")
    with pytest.raises(Exception):
        op = dpf.core.operators.result.displacement(data_sources=data_sources, server=server_type)
        assert op.eval() is not None
