"""Verify all examples can be accessed or downloaded"""
import os.path

import pytest

import dpf.core
from ansys.dpf.core import Model
from ansys.dpf.core import examples


def test_download_all_kinds_of_complexity_modal():
    path = examples.download_all_kinds_of_complexity_modal()
    assert isinstance(Model(path), Model)


def test_download_all_kinds_of_complexity():
    path = examples.download_all_kinds_of_complexity()
    assert isinstance(Model(path), Model)


def test_download_example_asme_result():
    path = examples.download_example_asme_result()
    assert isinstance(Model(path), Model)


def test_download_crankshaft():
    path = examples.download_crankshaft()
    assert isinstance(Model(path), Model)


def test_download_piston_rod():
    path = examples.download_piston_rod()
    assert isinstance(Model(path), Model)

list_examples =  [
        "simple_bar",
        "static_rst",
        "complex_rst",
        "multishells_rst",
        "electric_therm",
        "steady_therm",
        "transient_therm",
        "msup_transient",
    ]

@pytest.mark.parametrize(
    "example", list_examples,
)
def test_examples(example):
    # get example by string, so we can parameterize it without breaking
    # collection
    path = getattr(globals()["examples"], example)
    assert isinstance(Model(path), Model)


@pytest.mark.parametrize(
    "example", list_examples,
)
def test_find_examples(example, server_type_remote_process):
    # get example by string, so we can parameterize it without breaking
    # collection
    assert server_type_remote_process.local_server is True
    server_type_remote_process.local_server = False
    func = getattr(globals()["examples"], "find_" + example)
    path = func(server=server_type_remote_process)
    assert isinstance(Model(path).metadata.result_info, dpf.core.ResultInfo)
    assert path != getattr(globals()["examples"], example)
    server_type_remote_process.local_server = True
    path = func(server=server_type_remote_process)
    assert path == getattr(globals()["examples"], example)


def test_delete_downloaded_files():
    path = examples.download_multi_stage_cyclic_result()
    assert os.path.exists(path)
    examples.delete_downloads()
    assert not os.path.exists(path)
    path = examples.download_multi_stage_cyclic_result()
    assert os.path.exists(path)
    assert os.path.exists(examples.simple_bar)
    assert os.path.exists(examples.static_rst)
    assert os.path.exists(examples.complex_rst)
    assert os.path.exists(examples.distributed_msup_folder)
