"""Verify all examples can be accessed or downloaded"""

import os.path

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import Model
from ansys.dpf.core import DataSources
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


def test_download_cycles_to_failure():
    path = examples.download_cycles_to_failure()
    assert isinstance(Model(path), Model)


def test_download_modal_frame():
    path = examples.download_modal_frame()
    assert isinstance(Model(path), Model)


def test_download_harmonic_clamped_pipe():
    path = examples.download_harmonic_clamped_pipe()
    assert isinstance(Model(path), Model)


def test_download_modal_cyclic():
    path = examples.download_modal_cyclic()
    assert isinstance(Model(path), Model)


def test_download_fluent_multi_species():
    path = examples.download_fluent_multi_species()
    assert isinstance(Model(path), Model)


def test_download_fluent_axial_comp():
    path = examples.download_fluent_axial_comp()
    assert isinstance(Model(path), Model)


def test_download_fluent_mixing_elbow_steady_state():
    path = examples.download_fluent_mixing_elbow_steady_state()
    assert isinstance(Model(path), Model)


def test_download_fluent_mixing_elbow_transient():
    path = examples.download_fluent_mixing_elbow_transient()
    assert isinstance(Model(path), Model)


def test_download_cfx_heating_coil():
    path = examples.download_cfx_heating_coil()
    assert isinstance(Model(path), Model)


def test_download_cfx_mixing_elbow():
    path = examples.download_cfx_mixing_elbow()
    assert isinstance(Model(path), Model)


def test_fluid_axial_model():
    ds = examples.fluid_axial_model()
    assert isinstance(ds, DataSources)


list_examples = [
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
    "example",
    list_examples,
)
def test_examples(example):
    # get example by string, so we can parameterize it without breaking
    # collection
    path = getattr(globals()["examples"], example)
    assert isinstance(Model(path), Model)


@pytest.mark.parametrize(
    "example",
    list_examples,
)
def test_find_examples(example, server_type_remote_process):
    # get example by string, so we can parameterize it without breaking
    # collection
    server_type_remote_process.local_server = False
    func = getattr(globals()["examples"], "find_" + example)
    path = func(server=server_type_remote_process)
    assert isinstance(
        Model(path, server=server_type_remote_process).metadata.result_info,
        dpf.ResultInfo,
    )


def test_delete_downloaded_files():
    path = examples.download_multi_stage_cyclic_result(return_local_path=True)
    assert os.path.exists(path)
    examples.delete_downloads(verbose=False)
    assert not os.path.exists(path)
    path = examples.download_multi_stage_cyclic_result(return_local_path=True)
    assert os.path.exists(path)


def test_get_example_required_minimum_dpf_version(tmp_path):
    # Check version is parsed
    example_header = """
\"\"\"
.. _ref_average_across_bodies:

Average across bodies
~~~~~~~~~~~~~~~~~~~~~
.. note::
    This example requires DPF 6.1 or above.
    For more information, see :ref:`ref_compatibility`.
\"\"\"
    """
    p = tmp_path / "test_example_version_0.py"
    p.write_text(example_header)
    assert examples.get_example_required_minimum_dpf_version(p) == "6.1"
    # Check default version is 0.0, and versions declared outside a note in a header do not work
    example_header = """
\"\"\"
.. _ref_average_across_bodies:

Average across bodies
~~~~~~~~~~~~~~~~~~~~~
.. note::
    This example requires Premium

This example requires DPF 1.2 or above.
\"\"\"
This example requires DPF 2.3 or above.
from ansys.dpf import core as dpf
    """
    p = tmp_path / "test_example_version_1.py"
    p.write_text(example_header)
    assert examples.get_example_required_minimum_dpf_version(p) == "0.0"
