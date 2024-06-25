import ansys.dpf.core as dpf
import numpy as np


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

    """Creates a modal animation based on Fields contained in the FieldsContainer.

    This method creates a movie or a gif based on the time ids of a ``FieldsContainer``.
    For kwargs see pyvista.Plotter.open_movie/add_text/show.

    Parameters
    ----------
    fields_container :
        Field container containing the modal results.
    mode_number : int, optional
        Mode number of the results to animation. The default is ``1``.
    type_mode : int, optional
        Whether it is 0 or 1. Default to 0.
        If 0, the norm of the displacements will be scaled from 1 to -1 to 1.
        If 1, the norm of the displacements will be scaled between -1 and 1.
    frame_number: int, optional
        Number of frames to create for the animation.
        Defaults to 41 when type_mode=0, or 21 when type_mode=1
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

    wf.set_input_name("ponderation", scaling_op.inputs.ponderation)
    wf.set_output_name("field", scaling_op.outputs.field)

    anim = Animator(workflow=wf, **kwargs)

    return anim.animate(
        loop_over=loop_over,
        input_name="ponderation",
        output_name="field",
        save_as=save_as,
        mode_number=mode_number,
        clim=[0, max_data],
        **kwargs,
    )


def animate_transient(
    fields_container, save_as=None, deform_by=None, deform_scale_factor=1.0, **kwargs
):
    """Creates an animation based on the Fields contained in the FieldsContainer.

    This method creates a movie or a gif based on the time ids of a FieldsContainer.
    For kwargs see pyvista.Plotter.open_movie/add_text/show.

    Parameters
    ----------
    fields_container: FieldsContainer
        Field container containing the results to animate.
    save_as :
        Path of file to save the animation to. Defaults to None. Can be of any format
        supported by pyvista.Plotter.write_frame (.gif, .mp4, ...).
    deform_by : FieldsContainer, Result, Operator, optional
        Used to deform the plotted mesh. Must return a FieldsContainer of the same length as
        fields_container, containing 3D vector Fields of distances.
        Defaults to None, which takes fields_container if possible.
        Set as False to force static animation.
    deform_scale_factor : float, list, optional
        Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
        scaling frequency-dependent.
    """
    from ansys.dpf.core.animator import Animator

    # Create a workflow defining the result to render at each step of the animation
    wf = dpf.Workflow()
    # First define the workflow index input
    forward_index = dpf.operators.utility.forward()
    wf.set_input_name("loop_over", forward_index.inputs.any)
    # Define the field extraction using the fields_container and indices
    extract_field_op = dpf.operators.utility.extract_field(fields_container)
    to_render = extract_field_op.outputs.field
    n_components = fields_container[0].component_count
    if n_components > 1:
        norm_op = dpf.operators.math.norm(extract_field_op.outputs.field)
        to_render = norm_op.outputs.field

    loop_over = fields_container.get_time_scoping()
    frequencies = fields_container.time_freq_support.time_frequencies
    if frequencies is None:
        raise ValueError("The fields_container has no time_frequencies.")

    # TODO /!\ We should be using a mechanical::time_selector, however it is not wrapped.

    wf.set_input_name("indices", extract_field_op.inputs.indices)  # Have to do it this way
    wf.connect("indices", forward_index)  # Otherwise not accepted
    # Add the operators to the workflow
    wf.add_operators([extract_field_op, forward_index])

    deform = True
    # Define whether to deform and what with
    if deform_by is not False:
        if deform_by is None or isinstance(deform_by, bool):
            # By default, set deform_by as fields_container if nodal 3D vector field
            if fields_container[0].location == dpf.common.locations.nodal and n_components == 3:
                deform_by = fields_container
            else:
                deform = False
        if deform_by and not isinstance(deform_by, dpf.FieldsContainer):
            deform_by = deform_by.eval()
            if len(deform_by) != len(fields_container):
                raise ValueError(
                    "'deform_by' argument must result in a FieldsContainer "
                    "of same length as the animated one "
                    f"(len(deform_by.eval())={len(deform_by)} "
                    f"!= len(fields_container)={len(fields_container)})."
                )
    else:
        deform = False

    if deform:
        scale_factor_fc = dpf.animator.scale_factor_to_fc(deform_scale_factor, deform_by)
        scale_factor_invert = dpf.operators.math.invert_fc(scale_factor_fc)
        # Extraction of the field of interest based on index
        # time_selector = dpf.Operator("mechanical::time_selector")
        extract_field_op_2 = dpf.operators.utility.extract_field(deform_by)
        wf.set_input_name("indices", extract_field_op_2.inputs.indices)
        wf.connect("indices", forward_index)  # Otherwise not accepted
        # Scaling of the field based on scale_factor and index
        extract_scale_factor_op = dpf.operators.utility.extract_field(scale_factor_invert)
        wf.set_input_name("indices", extract_scale_factor_op.inputs.indices)
        wf.connect("indices", forward_index)  # Otherwise not accepted

        divide_op = dpf.operators.math.component_wise_divide(
            extract_field_op_2.outputs.field, extract_scale_factor_op.outputs.field
        )
        wf.set_output_name("deform_by", divide_op.outputs.field)
    else:
        deform_scale_factor = None
    wf.set_output_name("to_render", to_render)
    wf.progress_bar = False

    loop_over_field = dpf.fields_factory.field_from_array(frequencies.data[loop_over.ids - 1])
    loop_over_field.scoping.ids = loop_over.ids
    loop_over_field.unit = frequencies.unit

    # Initiate the Animator
    anim = Animator(workflow=wf, **kwargs)

    kwargs.setdefault("freq_kwargs", {"font_size": 12, "fmt": ".3e"})

    return anim.animate(
        loop_over=loop_over_field,
        save_as=save_as,
        scale_factor=deform_scale_factor,
        **kwargs,
    )
