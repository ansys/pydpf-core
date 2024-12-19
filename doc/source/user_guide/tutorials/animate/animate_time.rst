.. _ref_tutorials_animate_time:

======================
Animate data over time
======================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst
.. |Animator| replace:: :class:`Animator<ansys.dpf.core.animator.Animator>`
.. |animate| replace:: :func:`FieldsContainer.animate() <ansys.dpf.core.fields_container.FieldsContainer.animate>`
.. |Workflow| replace:: :class:`Workflow<ansys.dpf.core.workflow.Workflow>`
.. |Elemental| replace:: :class:`elemental<ansys.dpf.core.common.locations>`
.. |ElementalNodal| replace:: :class:`elemental_nodal<ansys.dpf.core.common.locations>`
.. |Nodal| replace:: :class:`nodal<ansys.dpf.core.common.locations>`
.. |Overall| replace:: :class:`overall<ansys.dpf.core.common.locations>`
.. |open_movie| replace:: :class:`pyvista.Plotter.open_movie`

This tutorial demonstrates how to create 3D animations of data in time.

:jupyter-download-script:`Download tutorial as Python script<animate_time>`  :jupyter-download-notebook:`Download tutorial as Jupyter notebook<animate_time>`

To animate data across time, you must store the data in a |FieldsContainer| with a ``time`` label.


Get the result files
--------------------

First, import a results file. For this tutorial, you can use the one available in the |Examples| module.
For more information about how to import your own result file in DPF, see
the :ref:`ref_tutorials_import_data` tutorial section.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops
    
    # Define the result file path
    result_file_path = examples.find_msup_transient()
    # Create the model
    model = dpf.Model(data_sources=result_file_path)

Define a time scoping
---------------------

To animate across time, you must define the time steps you are interested in.
This tutorial retrieves all the time steps available in |TimeFreqSupport|, but you can also filter them.
For more information on how to define a scoping, see the ``Narrow down data`` tutorial in the
:ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Get a scoping of all time steps available
    time_steps = model.metadata.time_freq_support.time_frequencies

Extract the results
-------------------

Extract the results to animate. In this tutorial, you extract the displacement and stress results.

.. note::

    Only the |Elemental|, |Nodal|, or |Faces| locations are supported for animations.
    |Overall| and |ElementalNodal| locations are not currently supported.


.. jupyter-execute::

    # Get the displacement fields (already on nodes) at all time steps
    disp_fc = model.results.displacement(time_scoping=time_steps).eval()
    print(disp_fc)

.. jupyter-execute::

    # Get the stress fields on nodes at all time steps
    # Request the stress on |Nodal| location as the default |ElementalNodal| location is not supported.
    stress_fc = model.results.stress.on_location(location=dpf.locations.nodal).on_time_scoping(time_scoping=time_steps).eval()
    print(stress_fc)

Animate the results
-------------------

Animate the results with the |animate| method.
You can animate them on a deformed mesh (animate the color map and the mesh)
or on a static mesh (animate the color map only).

The default behavior of the |animate| method is to:

- Display the norm of the data components;
- Display data at the top layer for shells;
- Display the deformed mesh when animating displacements;
- Display the static mesh for other types of results;
- Use a constant and uniform scale factor of 1.0 when deforming the mesh.

You can animate any result on a deformed geometry by providing displacement results in the `deform_by` parameter.

The geometry can be deformed by a |Result| object, an |Operator| (It must evaluate to a |FieldsContainer|
of same length as the one being animated), or a |FieldsContainer| (also of same length as the one being animated).

.. note::

    The behavior of the |animate| method is defined by a |Workflow| it creates and feeds to an |Animator|.
    This |Workflow| loops over a |Field| of frame indices and for each frame generates a field of norm contours
    to render, as well as a displacement field to deform the mesh if `deform_by` is provided.
    For more information on plots on deformed meshes see: :ref:`ref_plotting_data_on_deformed_mesh`.


Animate the displacement results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use |animate| with the displacement results.

.. tab-set::

    .. tab-item:: Deformed mesh

        .. jupyter-execute::
           :hide-output:

           # Animate the displacement results in a deformed geometry
           disp_fc.animate()

        .. jupyter-execute::
           :hide-code:
           :hide-output:

           disp_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_1.gif")

        .. image:: animate_disp_1.gif
           :scale: 50 %
           :align: center

    .. tab-item:: Static mesh

        .. jupyter-execute::
           :hide-output:

           # Animate the displacement results on a static mesh using ``deform_by=False``
           disp_fc.animate(deform_by=False)

        .. jupyter-execute::
           :hide-code:
           :hide-output:

           disp_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_2.gif",
                             deform_by=False)

        .. image:: animate_disp_2.gif
           :scale: 50 %
           :align: center

Animate the stress
^^^^^^^^^^^^^^^^^^

Use |animate| with the stress results.

.. tab-set::

    .. tab-item:: Deformed mesh

        .. jupyter-execute::
           :hide-output:

            # Animate the stress results on a deformed mesh
            # Use the ``deform_by`` argument and give the displacement results.
            stress_fc.animate(deform_by=disp_fc)

        .. jupyter-execute::
           :hide-code:
           :hide-output:

           stress_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_stress_1.gif",
                               deform_by=disp_fc)

        .. image:: animate_stress_1.gif
           :scale: 50 %
           :align: center

    .. tab-item:: Static mesh

        .. jupyter-execute::
           :hide-output:

            # Animate the stress results in a static geometry
            stress_fc.animate()

        .. jupyter-execute::
           :hide-code:
           :hide-output:

           stress_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_stress_2.gif")

        .. image:: animate_stress_2.gif
           :scale: 50 %
           :align: center

Change the scale factor
-----------------------

You can change the scale factor using:

- A single number for a uniform constant scaling;
- A list of numbers for a varying scaling (same length as the number of frames).

Uniform constant scaling
^^^^^^^^^^^^^^^^^^^^^^^^
.. jupyter-execute::
    :hide-output:

    # Define a uniform scale factor
    uniform_scale_factor=10.
    # Animate the displacements
    disp_fc.animate(scale_factor=uniform_scale_factor)

.. jupyter-execute::
    :hide-code:
    :hide-output:

    disp_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_3.gif",
                      scale_factor=uniform_scale_factor, text="Uniform scale factor")

.. image:: animate_disp_3.gif
   :scale: 45 %
   :align: center

Varying scaling
^^^^^^^^^^^^^^^

.. jupyter-execute::
    :hide-output:

    # Define a varying scale factor
    varying_scale_factor = [i for i in range(len(disp_fc))]
    # Animate the displacements
    disp_fc.animate(scale_factor=varying_scale_factor)

.. jupyter-execute::
    :hide-code:
    :hide-output:

    disp_fc.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_4.gif",
                      scale_factor=varying_scale_factor, text="Varying scale factor")

.. image:: animate_disp_4.gif
   :scale: 45 %
   :align: center

Save the animation
------------------

You can save the animation using the ``save_as`` argument with a target file path with the desired format as the extension key.
Accepted extensions are:

-  ``.gif``;
- ``.avi``;
- ``.mp4`` 

For more information see |open_movie|.

.. jupyter-execute::
   :hide-output:

    # Animate the stress results and save it
    stress_fc.animate(deform_by=disp_fc, save_as="animate_stress.gif")


Control the camera
------------------

Control the camera with the ``cpos`` argument.

A camera position is a combination of:

- A position;
- A focal point (the target);
- A upwards vector. 

It results in a list of format:

.. code-block:: python

   camera_position= [[pos_x, pos_y, pos_z],  # position
                     [fp_x, fp_y, fp_z],  # focal point
                     [up_x, up_y, up_z]]  # upwards vector

The |animate| method accepts a single camera position or a list of camera positions for each frame.

.. note::
    A tip for defining a camera position is to do a first interactive plot of the data
    with argument ``return_cpos=True``, position the camera as desired in the view, and retrieve
    the output of the plotting command.

Fixed camera
^^^^^^^^^^^^

.. jupyter-execute::
   :hide-output:

   # Define the camera position
   cam_pos = [[0., 2.0, 0.6], [0.05, 0.005, 0.5], [0.0, 0.0, 1.0]]
   # Animate the stress with a custom fixed camera position
   stress_fc.animate(cpos=cam_pos)

.. jupyter-execute::
   :hide-code:
   :hide-output:

   stress_fc.animate(save_as="source/user_guide/tutorials/animate/animate_disp_5.gif",
                       cpos=cam_pos,
                       off_screen=True)

.. image:: animate_disp_5.gif
   :scale: 50 %
   :align: center

Moving camera
^^^^^^^^^^^^^

.. jupyter-execute::
   :hide-output:

   import copy
   # Define the list of camera positions
   cpos_list = [cam_pos]
   # Incrementally increase the x coordinate of the camera by 0.1 for each frame
   for i in range(1, len(disp_fc)):
       new_pos = copy.deepcopy(cpos_list[i-1])
       new_pos[0][0] += 0.1
       cpos_list.append(new_pos)

   # Animate the stress with a moving camera
   stress_fc.animate(cpos=cpos_list)

.. jupyter-execute::
   :hide-code:
   :hide-output:

   stress_fc.animate(save_as="source/user_guide/tutorials/animate/animate_disp_6.gif",
                       cpos=cpos_list,
                       off_screen=True)

.. image:: animate_disp_6.gif
   :scale: 50 %
   :align: center

Additional options
------------------

You can use additional PyVista arguments of |open_movie|), such as:

- Show or hide the coordinate system axis with ``show_axes=True`` or ``show_axes=False``;
- Render off-screen for batch animation creation with ``off_screen=True``;
- Change the frame-rate with ``framerate``;
- Change the image quality with ``quality``.
