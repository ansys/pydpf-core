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
    """Remove GIF once finished."""
    def remove_gif():
        if os.path.exists(os.path.join(os.getcwd(), gif_name)):
            os.remove(os.path.join(os.getcwd(), gif_name))
    request.addfinalizer(remove_gif)


@pytest.fixture()
def displacement_fields():
    model = dpf.Model(examples.msup_transient)
    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(
        model.metadata.meshed_region.nodes.scoping)
    time_scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(model)
    displacement_op = model.results.displacement
    displacement_op = displacement_op.on_time_scoping(time_scoping)
    displacement_op = displacement_op.on_mesh_scoping(mesh_scoping)
    return displacement_op.eval()


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
    field = dpf.Field()
    with pytest.raises(ValueError) as e:
        an.animate(frequencies=field)
        assert "self.workflow" in e


def test_animator_animate(remove_gifs, displacement_fields):
    frequencies = displacement_fields.time_freq_support.time_frequencies

    wf = Workflow()
    extract_field_op = dpf.operators.utility.extract_field(displacement_fields)
    wf.set_input_name("index", extract_field_op.inputs.indices)
    wf.set_output_name("to_render", extract_field_op.outputs.field)

    an = Animator(wf)
    an.animate(frequencies=frequencies, save_as=gif_name)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_animator_animate_fields_container(remove_gifs, displacement_fields):
    displacement_fields.animate(save_as=gif_name)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_animator_animate_fields_container_deform_by_convert_unit(displacement_fields):
    new_displacement_fields = displacement_fields.deep_copy()
    dpf.operators.math.unit_convert_fc(
        fields_container=new_displacement_fields, unit_name="mm")
    displacement_fields.animate(save_as=gif_name, deform_by=new_displacement_fields)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_animator_animate_fields_container_scale_factor_float(remove_gifs, displacement_fields):
    displacement_fields.animate(save_as=gif_name, scale_factor=2.0)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_animator_animate_fields_container_scale_factor_zero(remove_gifs, displacement_fields):
    displacement_fields.animate(save_as=gif_name, scale_factor=0.0)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


def test_animator_animate_fields_container_scale_factor_list(remove_gifs, displacement_fields):
    scale_factor_list = [2.0]*len(displacement_fields)
    displacement_fields.animate(save_as=gif_name, scale_factor=scale_factor_list)
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 600000


# def test_animator_animate_fields_container_scale_factor_field(remove_gifs, displacement_fields):
#     scale_factor_field = dpf.fields_factory.field_from_array(displacement_fields[0].data)
#     displacement_fields.animate(save_as=gif_name, scale_factor=scale_factor_field)
#     assert os.path.isfile(gif_name)
#     assert os.path.getsize(gif_name) > 600000
#
#
# def test_animator_animate_fields_container_scale_factor_fc(remove_gifs, displacement_fields):
#     fields = []
#     for f in displacement_fields:
#         fields.append(dpf.fields_factory.field_from_array(f.data))
#     scale_factor_fc = dpf.fields_container_factory.over_time_freq_fields_container(fields)
#     scale_factor_fc.time_freq_support = displacement_fields.time_freq_support
#     displacement_fields.animate(save_as=gif_name, scale_factor=scale_factor_fc)
#     assert os.path.isfile(gif_name)
#     assert os.path.getsize(gif_name) > 600000
