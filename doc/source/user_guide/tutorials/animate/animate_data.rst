.. _ref_tutorials_animate_data:

============
Animate data
============

:bdg-warning:`MAPDL` :bdg-success:`LSDYNA`

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |Fields| replace:: :class:`Fields<ansys.dpf.core.field.Field>`
.. |FieldsContainers| replace:: :class:`FieldsContainers<ansys.dpf.core.fields_container.FieldsContainer>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |TimeFreqSupport| replace:: :class:`TimeFreqSupport <ansys.dpf.core.time_freq_support.TimeFreqSupport>`
.. |animate| replace:: :func:`animate() <ansys.dpf.core.fields_container.FieldsContainer.animate>`
.. |Result| replace:: :class:`Result <ansys.dpf.core.results.Result>`
.. |Operator| replace:: :class:`Operator<ansys.dpf.core.dpf_operator.Operator>`

This tutorial shows how to create 3D animations of the data.

To animate data across time you need to get the data stored in a |FieldsContainer| labeled in time.

Get the result files
--------------------

First download a result file such as one available with the `ansys.dpf.core.examples` module.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. tab-set::

    .. tab-item:: MAPDL


        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_1 = examples.find_msup_transient()
            # Create the model
            my_model_1 = dpf.Model(data_sources=result_file_path_1)
            # Get the mesh
            my_meshed_region_1 = my_model_1.metadata.meshed_region

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_2 = examples.download_d3plot_beam()
            # Create the DataSources object
            my_data_sources_2 = dpf.DataSources()
            my_data_sources_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            my_data_sources_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            # Create the model
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)

Define time and mesh scopings
-----------------------------

Here we get all the the time steps of the |TimeFreqSupport| and all the |MeshedRegion| with results in a ``Nodal``
location (only elemental, nodal or faces location are supported for the animation).
For more information on how to define a scoping check the ``Narrow down data`` tutorial in the :ref:`ref_tutorials_import_data`
tutorials section.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Get all the time steps
            time_scoping_1 = my_model_1.metadata.time_freq_support.time_frequencies
            # Get all the mesh in a nodal location
            mesh_scoping_1 = dpf.Scoping(ids=my_meshed_region_1.nodes.scoping.ids, location=dpf.locations.nodal)

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get all the time steps
            time_scoping_2 = my_model_2.metadata.time_freq_support.time_frequencies

Extract the results
-------------------

Extract the results of interest 

When you animate the data you go through the |Fields| of a |FieldsContainer| and plot contours of
the data norm or of the selected data component. This means that the geometry needs to be deformed
based on the |Fields| themselves.

The geometry can be deformed by a |Result| object, an |Operator| (It must evaluate to a FieldsContainer
of same length as the one being animated), a |Field| or a |FieldsContainer|.

To deform the geometry we need a result with a homogeneous unit dimension, thus, a distance unit.
Thus, to deform the mesh we need the displacement result.
For more information see: :ref:`ref_plotting_data_on_deformed_mesh`

Here we get:

- The displacement results and the stress result for the MAPDL result file
- The displacement results and the beam axial force result for the LSDYNA result file

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Get the displacement results
            my_disp_1 = my_model_1.results.displacement(time_scoping=time_scoping_1,
                                                        mesh_scoping=mesh_scoping_1).eval()
            # Get the stress results
            my_stress_1 = my_model_1.results.stress(time_scoping=time_scoping_1,
                                                        mesh_scoping=mesh_scoping_1).eval()

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the displacement results
            my_disp_2 = my_model_2.results.displacement(time_scoping=time_scoping_2.eval()
            # Get the stress results
            my_beam_axial_force_2 = my_model_2.results.beam_axial_force(time_scoping=time_scoping_2).eval()

Animate the results
-------------------

You animate a |FieldsContainer| by using the |animate| method.

The default behavior consists in:

- Using a constant and uniform scale factor of 1.0
- Showing the deformed geometry if the method was used directly with the displacement fields.
- Showing the static geometry if the method was used with other results fields.

Animate the displacement results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the |animate| method with no arguments to get the default animation to the displacement results.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Animate the displacement results
            my_disp_1.animate()

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            result_file_path_1 = examples.find_msup_transient()
            my_model_1 = dpf.Model(data_sources=result_file_path_1)
            my_meshed_region_1 = my_model_1.metadata.meshed_region
            time_scoping_1 = my_model_1.metadata.time_freq_support.time_frequencies
            mesh_scoping_1 = dpf.Scoping(ids=my_meshed_region_1.nodes.scoping.ids, location=dpf.locations.nodal)
            my_disp_1 = my_model_1.results.displacement(time_scoping=time_scoping_1,
                                                        mesh_scoping=mesh_scoping_1).eval()
            my_stress_1 = my_model_1.results.stress(time_scoping=time_scoping_1,
                                                        mesh_scoping=mesh_scoping_1).eval()
            my_disp_1.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_11.gif")

        .. image:: animate_disp_11.gif
           :scale: 50 %
           :align: center

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Animate the displacement results
            my_disp_2.animate()

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            result_file_path_2 = examples.download_d3plot_beam()
            my_data_sources_2 = dpf.DataSources()
            my_data_sources_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            my_data_sources_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)
            time_scoping_2 = my_model_2.metadata.time_freq_support.time_frequencies
            my_disp_2 = my_model_2.results.displacement(time_scoping=time_scoping_2).eval()
            my_beam_axial_force_2 = my_model_2.results.beam_axial_force(time_scoping=time_scoping_2).eval()
            my_disp_2.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_21.gif")

        .. image:: animate_disp_21.gif
           :scale: 50 %
           :align: center

Animate the others results
^^^^^^^^^^^^^^^^^^^^^^^^^^

To animate the others results with a deformed geometry you need to use the ``deform_by`` argument.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Animate the stress results
            my_stress_1.animate(deform_by=my_disp_1)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_stress_1.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_16.gif",
                              deform_by=my_disp_1)

        .. image:: animate_disp_16.gif
           :scale: 50 %
           :align: center

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Animate the beam_axial_force results
            my_beam_axial_force_2.animate(deform_by=my_disp_2)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_beam_axial_force_2.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_26.gif",
                              deform_by=my_disp_2)

        .. image:: animate_disp_26.gif
           :scale: 50 %
           :align: center

Exploring the |animate| method arguments
-----------------------------------------

- You can deactivate the geometry deformation by using the argument ``deform_by=False``.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Animate the displacement results
            my_disp_1.animate(deform_by=False)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_disp_1.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_12.gif",
                              deform_by=False)

        .. image:: animate_disp_12.gif
           :scale: 50 %
           :align: center

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Animate the displacement results
            my_disp_2.animate(deform_by=False)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_disp_2.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_22.gif",
                              deform_by=False)

        .. image:: animate_disp_22.gif
           :scale: 50 %
           :align: center

- You can change the scale factor using:

    a) A number for a uniform constant scaling
    b) A list of numbers for a varying scaling.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Define the scale factors
            uniform_scale_factor=10.
            varying_scale_factor = [i for i in range(len(my_disp_1))]
            # Animate the displacement results
            my_disp_1.animate(scale_factor=uniform_scale_factor,
                              show_axes=True)
            my_disp_1.animate(scale_factor=varying_scale_factor,
                              show_axes=True)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            uniform_scale_factor=10.
            varying_scale_factor = [i for i in range(len(my_disp_1))]
            # Animate the displacement results
            my_disp_1.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_13.gif",
                              scale_factor=uniform_scale_factor, text="Uniform scale factor")
            my_disp_1.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_14.gif",
                              scale_factor=varying_scale_factor, text="Varying scale factor")

        .. image:: animate_disp_13.gif
           :scale: 45 %

        .. image:: animate_disp_14.gif
           :scale: 45 %

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Define the scale factors
            uniform_scale_factor=10.
            varying_scale_factor = [i for i in range(len(my_disp_2))]
            # Animate the displacement results
            my_disp_2.animate(scale_factor=uniform_scale_factor)
            my_disp_2.animate(scale_factor=varying_scale_factor)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            uniform_scale_factor=10.
            varying_scale_factor = [i for i in range(len(my_disp_2))]
            # Animate the displacement results
            my_disp_2.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_23.gif",
                              scale_factor=uniform_scale_factor, text="Uniform scale factor")
            my_disp_2.animate(off_screen=True,save_as="source/user_guide/tutorials/animate/animate_disp_24.gif",
                              scale_factor=varying_scale_factor, legend="Varying scale factor")

        .. image:: animate_disp_23.gif
           :scale: 45 %

        .. image:: animate_disp_24.gif
           :scale: 45 %

- You can save the animation using the "save_as" argument with a target path with the desired format as extension.
  (accepted extension: .gif, .avi or .mp4, see pyvista.Plotter.open_movie)

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Animate the stress results and save it
            my_stress_1.animate(deform_by=my_disp_1, save_as="animate_stress.gif")

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Animate the beam_axial_force results and save it
            my_beam_axial_force_2.animate(deform_by=my_disp_2, save_as="animate_beam_axial_force.gif")

- You can use additional PyVista arguments (available at: :class:`pyvista.Plotter.open_movie`), such as:

    a) Show the coordinate system axis with the "show_axes" argument;
    b) Make the animation with the "off_screen" argument for batch animation creation;
    c) Define a camera position to use with the "cpos" argument (it have to be in one of the three
       formats explained in the following code);
    d) Frames per second with the "framerate" argument;
    e) Image quality with the "quality" argument.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Camera position
            # a) Iterable containing position, focal_point, and view up
            my_cpo_a1 = [(2.0, 5.0, 13.0), (0.0, 0.0, 0.0), (-0.7, -0.5, 0.3)]
            # b) Iterable containing a view vector
            my_cpo_b1 = [-1.0, 2.0, -5.0]
            # c) A string containing the plane orthogonal to the view direction (here the 'xy' direction)
             import copy
             my_camera_pos_list_1 = []
             init_pos = [(1.1710286191854873, 1.1276044794551632, 1.62102216127818),
                         (0.05000000000000724, 0.006575860269683119, 0.4999935420927001),
                         (0.0, 0.0, 1.0)]
             camera_pos_list.append(init_pos)
             for i in range(1, len(displacement_fields)):
                 new_pos = copy.copy(camera_pos_list[i-1])
                 new_pos[0] = (camera_pos_list[i-1][0][0],
                               camera_pos_list[i-1][0][1]-0.2,
                               camera_pos_list[i-1][0][2])
                 camera_pos_list.append(new_pos)

            # Animate the displacement results
            my_stress_1.animate(deform_by=my_disp_1,
                                show_axes=True,
                                framerate=4,
                                cpos=my_cpo_a1,
                                quality=8,
                                off_screen=True)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_cpo_a1 = [(2.0, 5.0, 13.0), (0.0, 0.0, 0.0), (-0.7, -0.5, 0.3)]
            my_stress_1.animate(save_as="source/user_guide/tutorials/animate/animate_disp_17.gif",
                                deform_by=my_disp_1,
                                show_axes=True,
                                framerate=4,
                                cpos=my_cpo_a1,
                                quality=8,
                                off_screen=True)

        .. image:: animate_disp_17.gif
           :scale: 50 %
           :align: center

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Camera position
            # a) Iterable containing position, focal_point, and view up
            my_cpo_a2 = [(2.0, 5.0, 13.0), (0.0, 0.0, 0.0), (-0.7, -0.5, 0.3)]
            # b) Iterable containing a view vector
            my_cpo_b2 = [-1.0, 2.0, -5.0]
            # c) A string containing the plane orthogonal to the view direction (here the 'xy' direction)
             import copy
             my_camera_pos_list_2 = []
             init_pos = [(1.1710286191854873, 1.1276044794551632, 1.62102216127818),
                         (0.05000000000000724, 0.006575860269683119, 0.4999935420927001),
                         (0.0, 0.0, 1.0)]
             camera_pos_list.append(init_pos)
             for i in range(1, len(displacement_fields)):
                 new_pos = copy.copy(camera_pos_list[i-1])
                 new_pos[0] = (camera_pos_list[i-1][0][0],
                               camera_pos_list[i-1][0][1]-0.2,
                               camera_pos_list[i-1][0][2])
                 camera_pos_list.append(new_pos)

            # Animate the displacement results
            my_beam_axial_force_2.animate(deform_by=my_disp_2,
                                          show_axes=True,
                                          framerate=4,
                                          cpos=my_cpo_a2,
                                          quality=8,
                                          off_screen=True)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:
            :hide-output:

            my_cpo_a2 = [(2.0, 5.0, 13.0), (0.0, 0.0, 0.0), (-0.7, -0.5, 0.3)]
            my_beam_axial_force_2.animate(save_as="source/user_guide/tutorials/animate/animate_disp_27.gif",
                                          deform_by=my_disp_2,
                                          show_axes=True,
                                          framerate=4,
                                          cpos=my_cpo_a2,
                                          quality=8,
                                          off_screen=True)

        .. image:: animate_disp_27.gif
           :scale: 50 %
           :align: center