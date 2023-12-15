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
    assert data_sources.get_path(0) == allkindofcomplexity
    assert data_sources[0] == allkindofcomplexity
    assert len(data_sources) == 1
    assert data_sources.get_namespace("rst") == "mapdl"
    assert data_sources.result_key == "rst"
    assert data_sources.num_result_keys == 1
    assert data_sources.get_result_key(0) == "rst"


def test_setresultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)
    assert len(data_sources) == 1
    assert data_sources[0] == allkindofcomplexity
    assert data_sources.num_result_keys == 1
    assert data_sources.result_key == "rst"
    assert data_sources.get_result_key(0) == "rst"
    assert data_sources.get_key_by_path_index(0) == "rst"
    assert data_sources.result_files == [allkindofcomplexity]
    assert data_sources.get_namespace(data_sources.get_key_by_path_index(0)) == "mapdl"


def test_setdomainresultpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(allkindofcomplexity, 0)
    ls = data_sources._get_label_space_by_path_index(0)
    assert ls["domain"] == 0


def test_setdomainresultpath_data_sources_with_key(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(allkindofcomplexity, key='rst', domain_id=0)
    ls = data_sources._get_label_space_by_path_index(0)
    assert ls["domain"] == 0


def test_addpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    assert len(data_sources) == 0
    data_sources.add_file_path(allkindofcomplexity)
    assert len(data_sources) == 1


def test_adddomainpath_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path(allkindofcomplexity, "rst", is_domain=True, domain_id=1)
    ls = data_sources._get_label_space_by_path_index(0)
    assert ls["domain"] == 1


def test_addfilepathspecifiedresult_data_sources(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(filepath=allkindofcomplexity)
    assert data_sources.get_key_by_path_index(0) == "rst"
    assert data_sources.get_result_key(0) == "rst"
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(filepath=allkindofcomplexity, key="d3plot")
    assert data_sources.get_key_by_path_index(0) == "d3plot"
    assert data_sources.get_result_key(0) == "d3plot"
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(
        filepath=allkindofcomplexity, result_key="d3plot"
    )
    assert data_sources.get_key_by_path_index(0) == "rst"
    assert data_sources.get_result_key(0) == "d3plot"
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.add_file_path_for_specified_result(
        filepath=allkindofcomplexity, key="test", result_key="d3plot"
    )
    assert data_sources.get_key_by_path_index(0) == "test"
    assert data_sources.get_result_key(0) == "d3plot"


def test_setresultpath_data_sources_no_extension(d3plot_beam, binout_glstat, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(d3plot_beam)
    assert data_sources.result_key == "d3plot"
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(binout_glstat)
    assert data_sources.result_key == "binout"


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
        _ = dpf.core.DataSources(data_sources="Wrong Input", server=server_type)
        assert "gRPC data sources" in e
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources2 = dpf.core.DataSources(data_sources=data_sources, server=server_type)
    assert data_sources == data_sources2


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
    assert len(data_sources) == 2


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Copying data is supported starting server version 3.0",
)
def test_delete_auto_data_sources(server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    ref = weakref.ref(data_sources)
    data_sources = None
    assert data_sources is None
    import gc

    gc.collect()
    assert ref() is None


@conftest.raises_for_servers_version_under("7.0")
def test_register_namespace(allkindofcomplexity, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(allkindofcomplexity)
    op = dpf.core.operators.result.displacement(data_sources=data_sources, server=server_type)
    assert op.eval() is not None
    assert data_sources.get_namespace("rst") == "mapdl"
    data_sources.register_namespace("rst", "notmapdl")
    assert data_sources.get_namespace("rst") == "notmapdl"
    with pytest.raises(Exception):
        op = dpf.core.operators.result.displacement(data_sources=data_sources, server=server_type)
        assert op.eval() is not None


def test_data_sources_get_path(distributed_files, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(path=distributed_files[0], key="rst", domain_id=0)
    data_sources.set_domain_result_file_path(path=distributed_files[1], key="d3plot", domain_id=1)
    data_sources.add_file_path(filepath=distributed_files[0])
    assert data_sources.get_path(0) == distributed_files[0]
    assert data_sources.get_path(1) == distributed_files[1]
    assert data_sources.get_path(2) == distributed_files[0]


def test_data_sources_get_paths(distributed_files, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_domain_result_file_path(path=distributed_files[0], key="rst", domain_id=0)
    data_sources.set_domain_result_file_path(path=distributed_files[1], key="d3plot", domain_id=1)
    assert len(data_sources) == 2
    assert len(data_sources.get_paths()) == 2
    assert len(data_sources.get_paths(keys="rst")) == 1
    assert len(data_sources.get_paths(keys="d3plot")) == 1
    assert len(data_sources.get_paths(keys=["rst", "d3plot"])) == 2
    assert len(data_sources.get_paths(keys="test")) == 0


def test_data_sources_result_paths(distributed_files, server_type):
    data_sources = dpf.core.DataSources(server=server_type)
    data_sources.set_result_file_path(filepath=distributed_files[0], key="d3plot")
    data_sources.add_file_path_for_specified_result(filepath=distributed_files[1])
    assert data_sources.result_key == "d3plot"
    assert data_sources.result_keys == ["d3plot", "rst"]
    assert data_sources.result_paths == [distributed_files[0], distributed_files[1]]


def test_data_sources_result_keys(distributed_files, server_type):
    ds = dpf.core.DataSources(server=server_type)
    ds.set_domain_result_file_path(path=distributed_files[0], key="rst", domain_id=0)
    ds.set_domain_result_file_path(path=distributed_files[1], key="d3plot", domain_id=1)
    result_keys = ds.result_keys
    assert len(result_keys) == 2
    assert "d3plot" in result_keys and "rst" in result_keys
    assert ds.get_result_key() == "rst"
    assert ds.get_result_key(0) == "rst"
    assert ds.get_result_key(1) == "d3plot"
