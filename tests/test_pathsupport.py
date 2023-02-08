# Tests specific to pathlib.Path support as path argument instead of str
import functools
import os
from pathlib import Path

import pytest

from ansys import dpf
from conftest import running_docker

skip_always = pytest.mark.skipif(True, reason="Investigate why this is failing")


def test_create_with_resultpath_data_sources_path(allkindofcomplexity, server_type):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources(path, server=server_type)
    assert hasattr(data_sources._internal_obj, "id") or isinstance(data_sources._internal_obj, int)


def test_addpath_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.add_file_path(path)
    # print(data_sources)


def test_print_data_sources_path(allkindofcomplexity):
    path = Path(allkindofcomplexity)
    data_sources = dpf.core.DataSources()
    data_sources.set_result_file_path(path)
    print(data_sources)
    assert data_sources.result_key == "rst"
    assert len(data_sources.result_files) == 1
    assert os.path.normpath(data_sources.result_files[0]) == os.path.normpath(allkindofcomplexity)


@pytest.mark.skipif(os.name == "nt" and running_docker, reason="Path is setting backslashes")
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
