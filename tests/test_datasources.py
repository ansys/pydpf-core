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


def test_addpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity)


def test_adddomainpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity, "rst", is_domain=True, domain_id=1)


def test_addfilepathspecifiedresult_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(allkindofcomplexity, "d3plot")


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
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources2 = dpf.core.DataSources(data_sources=data_sources, server=server_type)


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
