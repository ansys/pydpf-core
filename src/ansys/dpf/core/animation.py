import ansys.dpf.core as dpf
import numpy as np


def animate_mode(
    fields_container,
    mode_number=1,
    type_mode="positive_disp",
    frame_number=None,
    save_as="",
    deform_scale_factor=1.0,
    **kwargs,
):
    # other option: instead of `type` use `min_factor` and `max_factor`.

    """Creates an animation based on the ``Fields`` contained in the ``FieldsContainer``.

    This method creates a movie or a gif based on the time ids of a ``FieldsContainer``.
    For kwargs see pyvista.Plotter.open_movie/add_text/show.

    Parameters
    ----------
    field_container :
        Field container containing the modal results.
    mode_number : int, optional
        Mode number of the results to animation. The default is ``1``.
    type : str, optional
        Whether it is "full_disp" or "positive_disp".
        If "full_disp", the norm of the displacements will be scaled between -1 and 1.
        If "positive_disp", the norm of the displacements will be scaled between 0 and 1.
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

    if type_mode == "positive_disp":
        if frame_number is None:
            frame_number = 21
        scale_factor_per_frame = list(abs(np.linspace(-1, 1, frame_number, dtype=np.double)))
    elif type_mode == "full_disp":
        if frame_number is None:
            frame_number = 42
        scale_factor_per_frame = 2 * list(
            abs(np.linspace(-1, 1, int(frame_number / 2), dtype=np.double))
        )
        print(len(scale_factor_per_frame))
    else:
        raise ValueError(f"The type_mode {type_mode} is not accepted.")

    # time_freq_support = list(np.arange(1, len(scale_factor_per_frame)+1))
    # print("time_freq_support : ", time_freq_support)
    fake_frq = dpf.TimeFreqSupport()
    fake_frq.append_step(1, scale_factor_per_frame)

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

    max = float(np.max(field_mode.data))
    if type_mode == "positive_disp":
        min = 0
    elif type_mode == "full_disp":
        min = -max

    list_field = [field_mode for i in range(frame_number)]
    new_field_mode = dpf.fields_container_factory.over_time_freq_fields_container(
        list_field, time_freq_unit="Hz"
    )
    new_field_mode._set_time_freq_support(time_freq_support=fake_frq)

    # Create workflow
    wf = dpf.Workflow()

    # Add scaling operator
    scaling_op = dpf.operators.math.scale()
    wf.add_operators(scaling_op)

    wf.set_input_name("field_in", scaling_op.inputs.field)
    wf.set_input_name("ponderation", scaling_op.inputs.ponderation)
    wf.set_output_name("field_out", scaling_op.outputs.field)

    anim = Animator(workflow=wf, **kwargs)

    return anim.animate(
        loop_over=new_field_mode,
        input_name=["field_in", "ponderation"],
        output_name="field_out",
        save_as=save_as,
        mode_number=mode_number,
        clim=[min, max],
        **kwargs,
    )
