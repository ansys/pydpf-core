# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from pathlib import Path

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
        if Path.cwd().joinpath(gif_name).exists():
            Path.cwd().joinpath(gif_name).unlink()

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
    wf.progress_bar = False
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
    wf.progress_bar = False
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
    with pytest.raises(ValueError, match="scale_factor list length"):
        displacement_fields.animate(scale_factor=scale_factor_list)


def test_animator_animate_fields_container_scale_factor_field(displacement_fields):
    # A Field object is not a valid scale_factor type; expect a clear ValueError.
    scale_factor_field = dpf.fields_factory.field_from_array(displacement_fields[0].data)
    with pytest.raises(ValueError, match="Argument scale_factor must be"):
        displacement_fields.animate(scale_factor=scale_factor_field)


def test_animator_animate_fields_container_scale_factor_fc(displacement_fields):
    # A FieldsContainer object is not a valid scale_factor type; expect a clear ValueError.
    fields = []
    for f in displacement_fields:
        fields.append(dpf.fields_factory.field_from_array(f.data))
    scale_factor_fc = dpf.fields_container_factory.over_time_freq_fields_container(fields)
    scale_factor_fc.time_freq_support = displacement_fields.time_freq_support
    with pytest.raises(ValueError, match="Argument scale_factor must be"):
        displacement_fields.animate(scale_factor=scale_factor_fc)


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
    assert Path(gif_name).is_file()
    assert Path(gif_name).stat().st_size > 6000


def test_animator_animate_scale_factor_none(displacement_fields):
    """Passing scale_factor=None is accepted (treated internally as no scaling)."""
    displacement_fields.animate(scale_factor=None, off_screen=True)


def test_animator_animate_fields_container_invalid_label_raises(displacement_fields):
    """FieldsContainer.animate raises ValueError for a label not present."""
    with pytest.raises(ValueError, match="not found"):
        displacement_fields.animate(label="nonexistent_label")


def test_animator_animate_fields_container_none_time_freq_raises(displacement_fields):
    """FieldsContainer.animate raises ValueError when time_frequencies is None."""
    fc = displacement_fields.deep_copy()
    tfs = dpf.TimeFreqSupport()
    # A fresh TimeFreqSupport has no time_frequencies set
    fc.time_freq_support = tfs
    with pytest.raises(ValueError, match="no time_frequencies"):
        fc.animate(off_screen=True)


# ---------------------------------------------------------------------------
# Tests for ansys.dpf.core.animation.animate_mode
# ---------------------------------------------------------------------------


@pytest.fixture()
def modal_fields():
    """Displacement FieldsContainer over the first two time steps, used as mock mode data."""
    model = dpf.Model(examples.find_msup_transient())
    return model.results.displacement.on_time_scoping([1, 2]).eval()


def test_animate_mode_type_mode_1(modal_fields):
    """animate_mode with type_mode=1 (positive half) runs without error."""
    from ansys.dpf.core import animation

    animation.animate_mode(modal_fields, mode_number=1, type_mode=1, off_screen=True)


def test_animate_mode_even_frame_number(modal_fields):
    """animate_mode with type_mode=0 and an even frame_number auto-corrects to odd."""
    from ansys.dpf.core import animation

    # Even frame_number should be silently decremented by one; no exception expected.
    animation.animate_mode(modal_fields, mode_number=1, type_mode=0, frame_number=10, off_screen=True)


def test_animate_mode_invalid_type_mode_raises(modal_fields):
    """animate_mode raises ValueError for an unsupported type_mode."""
    from ansys.dpf.core import animation

    with pytest.raises(ValueError, match="type_mode 2 is not accepted"):
        animation.animate_mode(modal_fields, mode_number=1, type_mode=2, off_screen=True)


def test_animate_mode_invalid_mode_number_raises(modal_fields):
    """animate_mode raises ValueError when mode_number is absent from the container."""
    from ansys.dpf.core import animation

    with pytest.raises(ValueError, match="mode 999"):
        animation.animate_mode(modal_fields, mode_number=999, off_screen=True)
