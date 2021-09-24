import os
import pytest
from ansys.dpf import core

from ansys import dpf

skip_always = pytest.mark.skipif(True, reason="Investigate why this is failing")


def test_create_data_sources():
    data_sources = dpf.core.DataSources()
    assert data_sources._message.id != 0


def test_create_with_resultpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    assert data_sources._message.id != 0


def test_setresultpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(allkindofcomplexity)
    print(data_sources)


def test_setdomainresultpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_domain_result_file_path(allkindofcomplexity, 0)
    print(data_sources)


def test_addpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path(allkindofcomplexity)
    print(data_sources)


def test_adddomainpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path(allkindofcomplexity, "rst", is_domain=True, domain_id=1)
    print(data_sources)


def test_addfilepathspecifiedresult_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path_for_specified_result(allkindofcomplexity, "d3plot")
    print(data_sources)


def test_addupstream_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources2 = dpf.core.DataSources()
    data_sources.add_upstream(data_sources2)


def test_delete_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(allkindofcomplexity)


def test_print_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(allkindofcomplexity)
    print(data_sources)
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == [allkindofcomplexity]


def test_data_sources_from_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources2 = dpf.core.DataSources(data_sources=data_sources)


# TODO: Parameter to MergeFrom() must be instance of same class
@pytest.mark.xfail()
def test_delete_auto_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources2 = dpf.core.DataSources(data_sources=data_sources)
    del data_sources
    data_sources2.set_result_file_path(allkindofcomplexity)
