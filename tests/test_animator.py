import os

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import Workflow, examples, misc

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
    model = dpf.Model(examples.find_msup_transient())
    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(
        model.metadata.meshed_region.nodes.scoping
    )
    # time_scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(model)
    time_scoping = [1, 2]
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
        an.animate(loop_over=field)
        assert "self.workflow" in e


def test_animator_animate(displacement_fields):
    frequencies = displacement_fields.time_freq_support.time_frequencies
    loop_over = displacement_fields.get_time_scoping()
    loop_over_field = dpf.fields_factory.field_from_array(frequencies.data[loop_over.ids - 1])
    loop_over_field.scoping.ids = loop_over.ids
    loop_over_field.unit = frequencies.unit

    wf = Workflow()
    extract_field_op = dpf.operators.utility.extract_field(displacement_fields)
    wf.set_input_name("loop_over", extract_field_op.inputs.indices)
    wf.set_output_name("to_render", extract_field_op.outputs.field)

    an = Animator(wf)
    an.animate(loop_over=loop_over_field)


def test_animator_animate_raise_wrong_scale_factor(remove_gifs, displacement_fields):
    frequencies = displacement_fields.time_freq_support.time_frequencies
    loop_over = displacement_fields.get_time_scoping()
    loop_over_field = dpf.fields_factory.field_from_array(frequencies.data[loop_over.ids - 1])
    loop_over_field.scoping.ids = loop_over.ids
    loop_over_field.unit = frequencies.unit

    wf = Workflow()
    extract_field_op = dpf.operators.utility.extract_field(displacement_fields)
    wf.set_input_name("loop_over", extract_field_op.inputs.indices)
    wf.set_output_name("to_render", extract_field_op.outputs.field)

    an = Animator(wf)
    with pytest.raises(ValueError) as e:
        an.animate(loop_over=loop_over_field, scale_factor=False)
        assert "Argument scale_factor must be" in e


def test_animator_animate_fields_container(displacement_fields):
    displacement_fields.animate()


def test_animator_animate_fields_container_deform_by_false(displacement_fields):
    displacement_fields.animate(deform_by=False)


def test_animator_animate_fields_container_eqv():
    model = dpf.Model(examples.find_msup_transient())
    time_scoping = dpf.time_freq_scoping_factory.scoping_by_sets(list(range(5, 20)))
    stress_result = model.results.stress.on_time_scoping(time_scoping)

    stress_fields = stress_result.on_location(dpf.common.locations.nodal).eval()
    stress_fields.animate()


def test_animator_animate_fields_container_eqv_partial_scoping():
    model = dpf.Model(examples.find_msup_transient())
    time_scoping = dpf.time_freq_scoping_factory.scoping_by_sets(list(range(5, 20)))
    stress_result = model.results.stress.on_time_scoping(time_scoping)

    element_ids = model.metadata.meshed_region.elements.scoping.ids[:-10].tolist()
    mesh_scoping = dpf.mesh_scoping_factory.elemental_scoping(element_ids)
    stress_result = stress_result.on_mesh_scoping(mesh_scoping)

    displacement_result = model.results.displacement.on_time_scoping(time_scoping)

    stress_fields = stress_result.on_location(dpf.common.locations.nodal).eval()
    stress_fields.animate(deform_by=displacement_result, scale_factor=20.0, framerate=1.0)


def test_animator_animate_fields_container_one_component(displacement_fields):
    displacement_fields.select_component(0).animate()


def test_animator_animate_fields_container_deform_by_convert_unit(displacement_fields):
    new_displacement_fields = displacement_fields.deep_copy()
    dpf.operators.math.unit_convert_fc(fields_container=new_displacement_fields, unit_name="mm")
    displacement_fields.animate(deform_by=new_displacement_fields)


def test_animator_animate_fields_container_scale_factor_raise(displacement_fields):
    with pytest.raises(ValueError) as e:
        displacement_fields.animate(scale_factor=False)
        assert "Argument scale_factor must be" in e


def test_animator_animate_fields_container_deform_by_result():
    model = dpf.Model(examples.find_msup_transient())
    displacement_result = model.results.displacement.on_all_time_freqs
    displacement_fields = displacement_result.eval()
    displacement_fields.animate(deform_by=displacement_result)


def test_animator_animate_fields_container_deform_by_result_raise():
    model = dpf.Model(examples.find_msup_transient())
    displacement_result = model.results.displacement
    displacement_fields = displacement_result.on_all_time_freqs.eval()
    with pytest.raises(ValueError) as e:
        displacement_fields.animate(deform_by=displacement_result.on_first_time_freq)
        assert "'deform_by' argument must result in a FieldsContainer" in e


def test_animator_animate_fields_container_deform_by_operator():
    model = dpf.Model(examples.find_msup_transient())
    displacement_op = model.results.displacement.on_all_time_freqs()
    displacement_fields = displacement_op.eval()
    displacement_fields.animate(deform_by=displacement_op)


def test_animator_animate_fields_container_scale_factor_int(displacement_fields):
    displacement_fields.animate(scale_factor=2)


def test_animator_animate_fields_container_scale_factor_float(displacement_fields):
    displacement_fields.animate(scale_factor=2.0)


def test_animator_animate_fields_container_scale_factor_zero(displacement_fields):
    displacement_fields.animate(scale_factor=0.0)


def test_animator_animate_fields_container_scale_factor_list(displacement_fields):
    scale_factor_list = [2.0] * len(displacement_fields)
    displacement_fields.animate(scale_factor=scale_factor_list)


def test_animator_animate_fields_container_scale_factor_raise_list_len(
    displacement_fields,
):
    scale_factor_list = [2.0] * (len(displacement_fields) - 2)
    with pytest.raises(ValueError) as e:
        displacement_fields.animate(scale_factor=scale_factor_list)
        assert "The scale_factor list is not the same length" in e


def test_animator_animate_fields_container_scale_factor_field(displacement_fields):
    scale_factor_field = dpf.fields_factory.field_from_array(displacement_fields[0].data)
    with pytest.raises(NotImplementedError) as e:
        displacement_fields.animate(scale_factor=scale_factor_field)
        assert "Scaling by a Field is not yet implemented." in e


def test_animator_animate_fields_container_scale_factor_fc(displacement_fields):
    fields = []
    for f in displacement_fields:
        fields.append(dpf.fields_factory.field_from_array(f.data))
    scale_factor_fc = dpf.fields_container_factory.over_time_freq_fields_container(fields)
    scale_factor_fc.time_freq_support = displacement_fields.time_freq_support
    with pytest.raises(NotImplementedError) as e:
        displacement_fields.animate(scale_factor=scale_factor_fc)
        assert "Scaling by a FieldsContainer is not yet implemented." in e


def test_animator_animate_fields_container_cpos(remove_gifs, displacement_fields):
    camera_pos = [
        (2.341999327925363, 2.2535751881950388, 3.241992870018055),
        (0.10000000000000725, 0.01157586026968312, 0.9999935420927001),
        (0.0, 0.0, 1.0),
    ]

    displacement_fields.animate(
        scale_factor=10.0,
        save_as=gif_name,
        framerate=4,
        quality=8,
        cpos=camera_pos,
        off_screen=True,
        show_axes=True,
    )
    assert os.path.isfile(gif_name)
    assert os.path.getsize(gif_name) > 6000
