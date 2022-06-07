# Tests specific to pathlib.Path support as path argument instead of str
import pytest
import functools

from ansys import dpf
from pathlib import Path

skip_always = pytest.mark.skipif(True, reason="Investigate why this is failing")


def test_create_with_resultpath_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources(path)
    assert data_sources._internal_obj.id != 0


def test_addpath_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path(path)
    print(data_sources)


def test_print_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(path)
    print(data_sources)
    assert data_sources.result_key == "rst"
    assert data_sources.result_files == [allkindofcomplexity]


def test_all_result_operators_exist_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    model = dpf.core.Model(path)
    res = model.results
    for key in res.__dict__:
        if isinstance(res.__dict__[key], functools.partial):
            res.__dict__[key]()


def test_operator_connect_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    op = dpf.core.operators.serialization.field_to_csv()
    op.connect(0, path)
    op.inputs.connect(path)
    op.inputs.file_path.connect(path)
