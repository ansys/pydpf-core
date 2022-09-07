import os

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import misc, Workflow
from ansys.dpf.core import examples

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    from ansys.dpf.core.animator import Animator
else:
    HAS_PYVISTA = False

gif_name = "test.gif"


@pytest.fixture(autouse=False)
def remove_gifs(request):
    """Count servers once we are finished."""
    def remove_gif():
        if os.path.exists(os.path.join(os.getcwd(), gif_name)):
            os.remove(os.path.join(os.getcwd(), gif_name))
    request.addfinalizer(remove_gif)


def test_animator_set_get_workflow():
    an = Animator()
    wf = Workflow()
    an.workflow = wf
    assert an.workflow == wf


def test_animator_create_with_workflow():
    wf = Workflow()
    an = Animator(wf)
    assert an.workflow == wf


def test_animator_animate_raise_no_workflow():
    an = Animator()
    with pytest.raises(ValueError) as e:
        an.animate({})
        assert "self.workflow" in e


def test_animator_animate(remove_gifs):
    model = dpf.Model(examples.msup_transient)
    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(
        model.metadata.meshed_region.nodes.scoping)
    time_scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(model)
    displacement_op = model.results.displacement
    displacement_op = displacement_op.on_time_scoping(time_scoping)
    displacement_op = displacement_op.on_mesh_scoping(mesh_scoping)
    displacement_fields = displacement_op.eval()
    frequencies = displacement_fields.time_freq_support.time_frequencies

    wf = Workflow()
    extract_field_op = dpf.operators.utility.extract_field(displacement_fields)
    wf.set_input_name("index", extract_field_op.inputs.indices)
    wf.set_output_name("to_render", extract_field_op.outputs.field)

    an = Animator(wf)
    an.animate(frequencies=frequencies, save_as=gif_name)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_scale_factor_to_fc():
    pass
