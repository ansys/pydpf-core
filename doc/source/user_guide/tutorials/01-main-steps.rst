.. _tutorials_main_steps:

Postprocessing main steps
-------------------------

There are five main steps to transform simulation data into output data that can
be used to visualize and analyze simulation results:

.. grid::
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: 1
       :link: tutorials_main_steps_1
       :link-type: ref
       :text-align: center

       Importing and opening results files

    .. grid-item-card:: 2
       :link: tutorials_main_steps_2
       :link-type: ref
       :text-align: center

       Access and extract results

    .. grid-item-card:: 3
       :link: tutorials_main_steps_3
       :link-type: ref
       :text-align: center

       Transform available data

    .. grid-item-card:: 4
       :link: tutorials_main_steps_4
       :link-type: ref
       :text-align: center

       Visualize the data

    .. grid-item-card:: 5
       :link: tutorials_main_steps_5
       :link-type: ref
       :text-align: center

       Extract data

.. _tutorials_main_steps_1:

1- Importing and opening results files
**************************************

First, import the DPF-Core module as ``dpf`` and import the included examples file

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops

`DataSources' is a class that manages paths to their files. Use this object to declare
data inputs for DPF and define their locations.

.. code-block:: python

   # Define the DataSources object
   my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())


The model is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.

Printing the model displays:

  - Analysis type
  - Available results
  - Size of the mesh
  - Number of results

.. code-block:: python

   # Define the Model object
   my_model = dpf.Model(data_sources=my_data_sources)
   print(my_model)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())
    my_model = dpf.Model(data_sources=my_data_sources)
    print(my_model)

.. _tutorials_main_steps_2:

2- Access and extract results
*****************************

We see in the model that a displacement result is available. You can access this result by:

.. code-block:: python

   # Define the displacement results through the models property `results`
   my_displacements = my_model.results.displacement.eval()
   print(my_displacements)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_displacements = my_model.results.displacement.eval()
    print(my_displacements)

The displacement data can be extract by:

.. code-block:: python

   # Extract the data of the displacement field
   my_displacements_0 = my_displacements[0].data
   print(my_displacements_0)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_displacements_0 = my_displacements[0].data
    print(my_displacements_0)

.. _tutorials_main_steps_3:

3- Transform available data
***************************

Several transformations can be made with the data. They can be a single operation,
by using only one operator, or they can represent a succession of operations, by defining a
workflow with chained operators.

Here we star by computing the displacements norm.

.. code-block:: python

   # Define the norm operator (here for a fields container) for the displacement
   my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
   print(my_norm[0].data)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
    print(my_norm[0].data)

Then we compute the maximum values of the normalised displacement

.. code-block:: python

   # Define the maximum operator and chain it to the norm operator
   my_max= ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
   print(my_max)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_max = ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
    print(my_max)

.. _tutorials_main_steps_4:

4- Visualize the data
*********************

Plot the transformed displacement results

.. code-block:: python

   # Define the support of the plot (here we plot the displacement over the mesh)
   my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)

.. _tutorials_main_steps_5:

5- Extract the data
*******************