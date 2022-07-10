"""Verify all examples can be accessed or downloaded"""
import pytest

from ansys.dpf.core import Model, examples


def test_download_all_kinds_of_complexity_modal():
    path = examples.download_all_kinds_of_complexity_modal()
    assert isinstance(Model(path), Model)


def test_download_all_kinds_of_complexity():
    path = examples.download_all_kinds_of_complexity()
    assert isinstance(Model(path), Model)


def test_download_example_asme_result():
    path = examples.download_example_asme_result()
    assert isinstance(Model(path), Model)


@pytest.mark.parametrize(
    "example",
    [
        "simple_bar",
        "static_rst",
        "complex_rst",
        "multishells_rst",
        "electric_therm",
        "steady_therm",
        "transient_therm",
        "msup_transient",
    ],
)
def test_examples(example):
    # get example by string so we can parameterize it without breaking
    # collection
    path = getattr(globals()["examples"], example)
    assert isinstance(Model(path), Model)
