import pytest

from ansys import dpf

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
    print(data_sources)


def test_setdomainresultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(allkindofcomplexity, 0)
    print(data_sources)


def test_addpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity)
    print(data_sources)


def test_adddomainpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity, "rst", is_domain=True, domain_id=1)
    print(data_sources)


def test_addfilepathspecifiedresult_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(allkindofcomplexity, "d3plot")
    print(data_sources)


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
    print(data_sources)
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == [allkindofcomplexity]


def test_data_sources_from_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources2 = dpf.core.DataSources(data_sources=data_sources, server=server_type)


def test_several_result_path_data_sources(server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path("file_hello.rst")
    data_sources.set_result_file_path("file_bye.rst")
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == ["file_hello.rst", "file_bye.rst"]


# TODO: Parameter to MergeFrom() must be instance of same class
@pytest.mark.xfail()
def test_delete_auto_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources2 = dpf.core.DataSources(data_sources=data_sources, server=server_type)
    del data_sources
    data_sources2.set_result_file_path(allkindofcomplexity)
