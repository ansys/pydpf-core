.. _user_guide_model:

=========
DPF model
=========

The model is a helper designed to give shortcuts to the user to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.
The metadata is made of all the entities describing the analysis: its MeshedRegion, its
TimeFreqSupport and its ResultInfo. Therefore, from the ``Model`` object, the user can easily
access and display information about the mesh, the time or frequency steps and substeps used
in the analysis and the list of available results.

Creating the model
------------------
To create an instance of the ``Model`` object, import the ``pydpf-core`` package and
load a result file. The path that you provide must be an absolute path
or a path relative to the DPF server.

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples

    # File from PyDPF-Core package
    path = examples.find_simple_bar()
    path
    'C:/Users/user/AppData/local/temp/ASimpleBar.rst'
    model = dpf.Model(path)

To understand what is available in the result file, you can print the model
(or any other instance):

.. code-block:: python

    print(model)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Model
    ------------------------------
    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  element_nodal_forces: ElementalNodal Element nodal Forces
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region:
      3751 nodes
      3000 elements
      Unit: m
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support:
      Number of sets: 1
    Cumulative     Time (s)       LoadStep       Substep
    1              1.000000       1              1



For a model example, see :ref:`ref_basic_example`.

For a complete description of the ``Model`` object and its methods, see :ref:`ref_model`.

Accessing model metadata
------------------------

The model metadata give you access to the following informations:

- Data Sources (result files paths)
- Time or frequency descriptions
- Meshed region
- Available results information (which results are available, type of analysis, unit system
and analysis physical type )

In the sequence are examples on how accessing some of these information:

1) How you get the analysis type:


.. code-block:: python

    model.metadata.result_info.analysis_type

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    'static'

2) How you get mesh information:


.. code:: python
    # a) Number of nodes in the meshed region
    model.metadata.meshed_region.nodes.n_nodes
    # b) Number of elements in the meshed region
    model.metadata.meshed_region.elements.n_elements
    # c) Get an element by its id and give its description
    print(model.metadata.meshed_region.elements.element_by_id(1))

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    3751
    3000
    DPF Element 1
    	Index:         1400
    	Nodes:            8
    	Type:       element_types.Hex8
    	Shape:        Solid


3) How you get time sets:


.. code-block:: python

    time_freq_support =  model.metadata.time_freq_support
    print(time_freq_support, '\n')  # print all the time_freq support
    print(time_freq_support.time_frequencies.data)  # print the time sets values

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF  Time/Freq Support:
    Number of sets: 1
    Cumulative     Time (s)       LoadStep       Substep
    1              1.000000       1              1

    [1.]


For a more detailed description of the ``Metadata`` object, see :class:`Metadata<ansys.dpf.core.model.Metadata>`.

Accessing model results
-----------------------
The model contains the ``results`` attribute, which you can use to
easily access certain results.

This example shows how you view available results:


.. code-block:: python

    print(model.results)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  element_nodal_forces: ElementalNodal Element nodal Forces
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  structural_temperature: ElementalNodal Temperature


Also, with the ``results`` attribute, choosing the time, frequencies, or spatial subset
on which to get a given result is straightforward.

This example shows how you get displacement results on all time frequencies on
the mesh scoping:

.. code-block:: python

    # Define which result will be used
    disp_result = model.results.displacement
    # Define the time and mesh scoping
    disp_at_all_times_on_node_1 =  disp_result.on_all_time_freqs.on_mesh_scoping([1])
    print(disp_at_all_times_on_node_1.eval())

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
    DPF displacement(s)Fields Container
      with 1 field(s)
      defined on labels: time

      with:
      - field 0 {time:  1} with Nodal location, 3 components and 1 entities.


For an example using the ``Result`` object, see :ref:`ref_transient_easy_time_scoping`.

For a description of the ``Results`` object, see :ref:`ref_results`.

