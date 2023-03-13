from ansys import dpf


def animate_mode(
    field_container, mode_number=1, save_as=None, frame_number=21, scale_factor=1.0, **kwargs
):
    """Creates an animation based on the ``Fields`` contained in the ``FieldsContainer``.

    This method creates a movie or a gif based on the time ids of a ``FieldsContainer``.
    For kwargs see pyvista.Plotter.open_movie/add_text/show.

    Parameters
    ----------
    field_container :
        Field container containing the modal results.
    mode_number : int, optional
        Mode number of the results to animation. The default is ``1``.
    save_as : Path of file to save the animation to. Defaults to None. Can be of any format
        supported by pyvista.Plotter.write_frame (.gif, .mp4, ...).
    scale_factor : float, list, optional
        Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
        scaling frequency-dependent.

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

    # Create a workflow defining the result to render at each step of the animation
    wf = dpf.core.Workflow()
    # First define the workflow index input
    forward_index = dpf.core.operators.utility.forward()
    wf.set_input_name("loop_over", forward_index.inputs.any)
    # Define the field extraction using the fields_container and indices
    extract_field_op = dpf.core.operators.utility.extract_field(
        field_container, indices=[mode_number - 1]
    )
    to_render = extract_field_op.outputs.field
    n_components = field_container[0].component_count
    if n_components > 1:
        norm_op = dpf.core.operators.math.norm(extract_field_op.outputs.field)
        to_render = norm_op.outputs.field

    loop_over = field_container.get_time_scoping()
    frequencies = field_container.time_freq_support.time_frequencies
    if frequencies is None:
        raise ValueError("The fields_container has no time_frequencies.")

    # TODO /!\ We should be using a mechanical::time_selector, however it is not wrapped.

    # Add the operators to the workflow
    wf.add_operators(extract_field_op)

    # TODO: deform is not accepted yet
    # deform = True
    # # Define whether to deform and what with
    # if deform_by is not False:
    #     if deform_by is None or isinstance(deform_by, bool):
    #         # By default, set deform_by as field_container if nodal 3D vector field
    #         if (field_container[0].location == dpf.core.common.locations.nodal
    #               and n_components == 3):
    #             deform_by = field_container
    #         else:
    #             deform = False
    #     if deform_by and not isinstance(deform_by, dpf.core.FieldsContainer):
    #         deform_by = deform_by.eval()
    #         if len(deform_by) != len(field_container):
    #             raise ValueError(
    #                 "'deform_by' argument must result in a FieldsContainer "
    #                 "of same length as the animated one "
    #                 f"(len(deform_by.eval())={len(deform_by)} "
    #                 f"!= len(field_container)={len(field_container)})."
    #             )
    # else:
    #     deform = False

    # if deform:
    #     scale_factor_fc = dpf.core.animator.scale_factor_to_fc(scale_factor, deform_by)
    #     scale_factor_invert = dpf.core.operators.math.invert_fc(scale_factor_fc)
    #     # Extraction of the field of interest based on index
    #     # time_selector = dpf.core.Operator("mechanical::time_selector")
    #     extract_field_op_2 = dpf.core.operators.utility.extract_field(deform_by)
    #     wf.set_input_name("indices", extract_field_op_2.inputs.indices)
    #     wf.connect("indices", forward_index)  # Otherwise not accepted
    #     # Scaling of the field based on scale_factor and index
    #     extract_scale_factor_op = dpf.core.operators.utility.extract_field(
    # scale_factor_invert
    # )
    #     wf.set_input_name("indices", extract_scale_factor_op.inputs.indices)
    #     wf.connect("indices", forward_index)  # Otherwise not accepted

    #     divide_op = dpf.core.operators.math.component_wise_divide(
    #         extract_field_op_2.outputs.field, extract_scale_factor_op.outputs.field
    #     )
    #     wf.set_output_name("deform_by", divide_op.outputs.field)
    # else:
    # scale_factor = None

    wf.set_output_name("to_render", to_render)
    wf.progress_bar = False

    loop_over_field = dpf.core.fields_factory.field_from_array(frequencies.data[loop_over.ids - 1])
    loop_over_field.scoping.ids = loop_over.ids
    loop_over_field.unit = frequencies.unit

    # Initiate the Animator
    anim = Animator(workflow=wf, **kwargs)

    kwargs.setdefault("freq_kwargs", {"font_size": 12, "fmt": ".3e"})

    return anim.animate_modal(
        mode_number=mode_number,
        loop_over=loop_over_field,
        save_as=save_as,
        frame_number=frame_number,
        scale_factor=scale_factor,
        **kwargs,
    )
