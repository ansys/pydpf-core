from ansys import dpf


def test_create_data_sources():
    data_sources = dpf.core.DataSources()
    assert data_sources._message.id != 0


def test_create_with_resultpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources(allkindofcomplexity)
    assert data_sources._message.id != 0


def test_setresultpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(allkindofcomplexity)


def test_addpath_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    try:
        data_sources.add_file_path(allkindofcomplexity)
        assert True
    except:
        assert False
        
def test_addupstream_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources2 = dpf.core.DataSources()
    try:
        data_sources.add_upstream(data_sources2)
        assert True
    except:
        assert False

def test_delete_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    try:
        data_sources.set_result_file_path(allkindofcomplexity)
        assert False
    except :
        assert True

def test_print_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(allkindofcomplexity)
    print(data_sources)
    assert data_sources.result_key=="rst"
    assert data_sources.result_files ==[allkindofcomplexity]

def test_delete_auto_data_sources(allkindofcomplexity):
    data_sources = dpf.core.DataSources()
    data_sources2 = dpf.core.DataSources(data_sources=data_sources)
    del data_sources
    try:
        data_sources2.set_result_file_path(allkindofcomplexity)
        assert False
    except:
        assert True
