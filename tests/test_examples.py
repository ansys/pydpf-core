"""Verify all examples can be accessed or downloaded"""
import pytest

from ansys.dpf.core import Model
from ansys.dpf.core import examples


def test_download_all_kinds_of_complexity_modal():
    path = examples.download_all_kinds_of_complexity_modal()
    assert isinstance(Model(path), Model)


def test_download_all_kinds_of_complexity():
    path = examples.download_all_kinds_of_complexity()
    assert isinstance(Model(path), Model)


@pytest.mark.parametrize("example", ['simple_bar',
                                     'static_rst',
                                     'complex_rst',
                                     'multishells_rst',
                                     'static_rst',
                                     'electric_therm',
                                     'steady_therm',
                                     'transient_therm'])
def test_examples(example):
    # get example by string so we can parameterize it without breaking
    # collection
    path = getattr(globals()['examples'], example)
    assert isinstance(Model(path), Model)
