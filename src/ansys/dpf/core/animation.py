# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

"""Module contains the function for modal animation creation."""

import numpy as np

import ansys.dpf.core as dpf


def animate_mode(
    fields_container,
    mode_number=1,
    type_mode=0,
    frame_number=None,
    save_as="",
    deform_scale_factor=1.0,
    **kwargs,
):
    # other option: instead of `type` use `min_factor` and `max_factor`.
    """Create a modal animation based on Fields contained in the FieldsContainer.

    This method creates a movie or a gif based on the time ids of a ``FieldsContainer``.
    For kwargs see pyvista.Plotter.open_movie/add_text/show.

    Parameters
    ----------
    field_container :
        Field container containing the modal results.
    mode_number : int, optional
        Mode number of the results to animation. The default is ``1``.
    type_mode : int, optional
        Whether it is 0 or 1. Default to 0.
        If 0, the norm of the displacements will be scaled from 1 to -1 to 1.
        If 1, the norm of the displacements will be scaled between -1 and 1.
    save_as : Path of file to save the animation to. Defaults to None. Can be of any format
        supported by pyvista.Plotter.write_frame (.gif, .mp4, ...).
    deform_scale_factor : float, optional
        Scale factor to apply when warping the mesh. Defaults to 1.0.

    Examples
    --------
    Import a modal result from a model.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_modal_frame())
    >>> disp = model.results.displacement.on_all_time_freqs.eval()

    Creates an animation from a modal result.

    >>> from ansys.dpf.core import animation
    >>> animation.animate_mode(disp, mode_number=1, save_as="tmp.gif")


    """
    from ansys.dpf.core.animator import Animator

    # Animation type

    if type_mode == 1:
        if frame_number is None:
            frame_number = 21
        scale_factor_per_frame = list(abs(np.linspace(-1, 1, frame_number, dtype=np.double)))
    elif type_mode == 0:
        if frame_number is None:
            frame_number = 41
        elif frame_number % 2 == 0:
            frame_number -= 1
        half_scale = np.linspace(-1, 1, int((frame_number + 1) / 2), dtype=np.double)
        scale_factor_per_frame = np.concatenate([np.flip(half_scale), half_scale[1:]])
    else:
        raise ValueError(
            f"The type_mode {type_mode} is not accepted. "
            + "Please select one in 'positive_disp' and 'full_disp'."
        )

    # Get fields
    fields_mode = fields_container.get_fields({"time": mode_number})

    # Merge fields if needed
    if len(fields_mode) > 1:
        merge_op = dpf.operators.utility.merge_fields()
        for i, field in enumerate(fields_mode):
            merge_op.connect(i, field)
        field_mode = merge_op.eval()
    else:
        field_mode = fields_mode[0]

    max_data = float(np.max(field_mode.data))
    loop_over = dpf.fields_factory.field_from_array(scale_factor_per_frame)

    # Create workflow
    wf = dpf.Workflow()
    wf.progress_bar = False

    # Add scaling operator
    scaling_op = dpf.operators.math.scale()
    scaling_op.inputs.field.connect(field_mode)
    wf.add_operators([scaling_op])

    wf.set_input_name("weights", scaling_op.inputs.weights)
    wf.set_output_name("field", scaling_op.outputs.field)

    anim = Animator(workflow=wf, **kwargs)

    return anim.animate(
        loop_over=loop_over,
        input_name="weights",
        output_name="field",
        save_as=save_as,
        mode_number=mode_number,
        clim=[0, max_data],
        **kwargs,
    )
