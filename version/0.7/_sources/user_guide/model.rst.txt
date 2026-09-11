.. _user_guide_model:

=========
DPF model
=========

The DPF model provides the starting point for opening a result file.
From the ``Model`` object, you can connect various operators and display results
and data.

To create an instance of the ``Model`` object, import the ``pydpf-core`` package and
load a result file. The path that you provide must be an absolute path
or a path relative to the DPF server.

.. code-block:: default

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples

    path = examples.find_simple_bar()
    model = dpf.Model(path)

To understand what is available in the result file, you can print the model
(or any other instance):

.. code-block:: default

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



For a comprehensive model example, see :ref:`ref_basic_example`.

For a description of the ``Model`` object, see :ref:`ref_model`.


Model metadata
--------------
To access all information about an analysis, you can use model metadata:

- Type of analysis
- Time or frequency descriptions
- Mesh
- Available results

This example shows how you get the analysis type:


.. code-block:: default

    model.metadata.result_info.analysis_type

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    'static'

This example shows how you get mesh information:


.. code:: default

    >>> model.metadata.meshed_region.nodes.n_nodes
    >>> model.metadata.meshed_region.elements.n_elements
    >>> print(model.metadata.meshed_region.elements.element_by_id(1))

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    3751
    3000
    DPF Element 1
    	Index:         1400
    	Nodes:            8
    	Type:       element_types.Hex8
    	Shape:        Solid


This example shows how you get time sets:


.. code-block:: default

    time_freq_support =  model.metadata.time_freq_support
    print(time_freq_support.time_frequencies.data)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    [1.]


For a description of the ``Metadata`` object, see :ref:`ref_model`.

Model results
-------------
The model contains the ``results`` attribute, which you can use to
create operators to access certain results.

This example shows how you view available results:


.. code-block:: default

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


.. autoattribute:: ansys.dpf.core.model.Model.results
  :noindex:

With the ``results`` attribute, choosing the time, frequencies, or spatial subset
on which to get a given result is straightforward.

This example shows how you get displacement results on all time frequencies on
the mesh scoping:

.. code-block:: default

    disp_result = model.results.displacement
    disp_at_all_times_on_node_1 =  disp_result.on_all_time_freqs.on_mesh_scoping([1])


For an example using the ``Result`` object, see :ref:`ref_transient_easy_time_scoping`.

For a description of the ``Model`` object, see :ref:`ref_results`.



API reference
~~~~~~~~~~~~~

For more information, see :ref:`ref_model` or :ref:`ref_results`.
