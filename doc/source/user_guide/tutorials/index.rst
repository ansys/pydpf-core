.. _ref_tutorials_index:

Tutorials
---------

What you need to know
+++++++++++++++++++++

These tutorials go through the steps required to access, analyze,
and transform simulation data using  PyDPF-Core.

Tutorials are more substantive and complex than examples. They are designed to teach how to perform a task and understand
the underlying concepts, providing detailed explanations at each stage, whereas examples showcase end-to-end specific processes.

DPF interacts with data stored in DPF data structures.
These DPF data structures are generated automatically when reading data from results file (`ref_to_section`) but they can also be generated from scratch (`ref_to_section`) when no supported result file is available.

Overview
++++++++

There are four main steps to transform simulation data into output data that can
be used to visualize and analyze simulation results:

.. grid::
   :gutter: 0

   .. grid-item::
      :child-direction: row

      .. button-ref:: initial_topic
         :ref-type: ref
         :color: primary
         :shadow:
         :expand:

         Importing and opening results files

      :octicon:`arrow-right;1em`

      .. button-ref:: disp_results
         :ref-type: ref
         :color: primary
         :shadow:
         :expand:

         Access and extract results

      :octicon:`arrow-right;1em`

      .. button-ref:: disp_results
         :ref-type: ref
         :color: primary
         :shadow:

         Transform available data

      :octicon:`arrow-right;1em`

      .. button-ref:: disp_results
         :ref-type: ref
         :color: primary
         :shadow:

         Visualize the data

      :octicon:`arrow-right;1em`

      .. button-ref:: disp_results
         :ref-type: ref
         :color: primary
         :shadow:

         Extract data

The following tutorial go through each of these steps in a basic manipulation. More advanced
approaches can be accessed with the listed buttons. Each tutorial presents code snippets specific
to each supported file format.

.. centered:: Importing and opening results files

.. grid::
   :gutter: 5
   :padding: 2

   .. grid-item::
      :columns: 7
      :class: sd-shadow-sm

      .. code-block:: python

         # First, import the DPF-Core module as ``dpf`` and import the included
         # examples file
         from ansys.dpf import core as dpf
         from ansys.dpf.core import examples
         from ansys.dpf.core import operators as ops

         # `DataSources' is a class that manages paths to their files.
         # Use this object to declare data inputs for DPF and define their locations.
         my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())

         # The model is a helper designed to give shortcuts to access the analysis
         # results metadata, by opening a DataSources or a Streams, and to
         # instanciate results provider for it.

         my_model = dpf.Model(data_sources=my_data_sources)
         print(my_model)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          print(my_model)

   .. grid-item::
      :columns: 1

   .. grid-item::
      :columns: 4
      :class: sd-shadow-sm

      .. centered:: :octicon:`pin;1em`

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         I have one file.

      .. button-ref:: disp_results
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         I have more than one file

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         I don’t know my file(s) type(s)


.. centered:: **Access and extract results**

.. grid:: 2
   :gutter: 5
   :padding: 2

   .. grid-item::
      :columns: 7
      :class: sd-shadow-sm

      .. code-block:: python

         # We see that we have a displacement result
         # Define the displacement results through the models property `results`
         my_displacements = my_model.results.displacement.eval()
         print(my_displacements)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          my_displacements = my_model.results.displacement.eval()
          print(my_displacements)

      .. code-block:: python

         # Extract the data of the displacement field
         my_displacements_0 = my_displacements[0].data
         print(my_displacements_0)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          my_displacements = my_model.results.displacement.eval()
          my_displacements_0 = my_displacements[0].data
          print(my_displacements_0)

   .. grid-item::
      :columns: 1

   .. grid-item::
      :columns: 4
      :class: sd-shadow-sm

      .. centered:: More specific tutorials

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         Narrow down data

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         Extract and explore results data

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         Extract and explore results metadata

.. centered:: **Transform data**

.. grid:: 2
   :gutter: 5
   :padding: 2

   .. grid-item::
      :columns: 7
      :class: sd-shadow-sm

      .. code-block:: python

         # Compute the norm of the displacement
         # Define the norm operator (here for a fields container) for the displacement
         my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
         print(my_norm[0].data)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          my_displacements = my_model.results.displacement.eval()
          my_displacements_0 = my_displacements[0].data
          my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
          print(my_norm[0].data)

      .. code-block:: python

         # Compute the maximum of the normalised displacement
         # Define the maximum operator and chain it to the norm operator
         my_max= ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
         print(my_max)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          my_displacements = my_model.results.displacement.eval()
          my_displacements_0 = my_displacements[0].data
          my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
          my_max = ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
          print(my_max)

   .. grid-item::
      :columns: 1

   .. grid-item::
      :columns: 4
      :class: sd-shadow-sm

      .. centered:: More specific tutorials

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :shadow:
         :expand:
         :class: sd-bg-secondary
         :color: secondary

         Using operators

      .. button-ref:: disp_results
         :ref-type: ref
         :class: sd-bg-secondary
         :shadow:
         :expand:

         Create a workflow

.. centered:: **Visualize data**

.. grid:: 2
   :gutter: 5
   :padding: 2

   .. grid-item::
      :columns: 7
      :class: sd-shadow-sm

      .. code-block:: python

         # Plot the displacement
         # Define the support of the plot (here we plot the displacement over the mesh)
         my_plot = my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)
         print(my_plot)

      .. rst-class:: sphx-glr-script-out

       .. exec_code::
          :hide_code:

          from ansys.dpf import core as dpf
          from ansys.dpf.core import examples
          from ansys.dpf.core import operators as ops
          my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
          my_model = dpf.Model(data_sources=my_data_sources)
          my_displacements = my_model.results.displacement.eval()
          my_displacements_0 = my_displacements[0].data
          my_norm_operator = dpf.operators.math.norm_fc(fields_container=my_displacements).eval()
          my_max_operator = dpf.operators.min_max.min_max_fc(fields_container=my_norm_operator).eval()
          # my_plot = my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)
          # print(my_plot)

   .. grid-item::
      :columns: 1

   .. grid-item::
      :columns: 4
      :class: sd-shadow-sm

      .. centered:: More specific tutorials

      .. button-ref:: ref_tutorials_model
         :ref-type: ref
         :class: sd-btn-secondary
         :shadow:
         :expand:

         Plotting

      .. button-ref:: disp_results
         :ref-type: ref
         :color: secondary
         :shadow:
         :expand:

         Animation