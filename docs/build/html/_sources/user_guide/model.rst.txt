.. _user_guide_model:

==============
The DPF Model
==============

The DPF model is the basic starting point for opening a file through
DPF.  From here you can connect various operators and display results
and data from the result file.

To create a ``Model`` instance, import ``dpf`` and load a file.  The
path provided must be an absolute path or a path relative to the DPF
server.

.. code-block:: default

    from ansys.dpf import core as dpf    
    from ansys.dpf.core import examples
    
    path = examples.simple_bar
    model = dpf.Model(path)

Printing the model (or any other instance) ca be useful to understand what 
is available in the result file 

.. code-block:: default

    print(model)



.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    DPF Model
    ------------------------------
    DPF Result Info 
      Analysis: static 
      Physics Type: mecanic 
      Unit system: MKS: m, kg, N, s, V, A, degC 
      Available results: 
        U Displacement :nodal displacements 
        ENF Element nodal Forces :element nodal forces 
        ENG_VOL Volume :element volume 
        ENG_SE Energy-stiffness matrix :element energy associated with the stiffness matrix 
        ENG_AHO Hourglass Energy :artificial hourglass energy 
        ENG_TH thermal dissipation energy :thermal dissipation energy 
        ENG_KE Kinetic Energy :kinetic energy 
        ENG_CO co-energy :co-energy (magnetics) 
        ENG_INC incremental energy :incremental energy (magnetics) 
        BFE Temperature :element structural nodal temperatures 
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
    


For a full example using the model, see :ref:`ref_basic_example`.

For a full description of the Model object, see the APIs section :ref:`ref_model`.


Model Metadata
--------------
The metadata of the model can be used to access all the information about an analysis:

- the type of analysis
- the time or frequencies description
- the mesh
- the available results

For example, you can get the analysis type with:


.. code-block:: default
    
    model.metadata.result_info.analysis_type
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    'static'

You can get information about the mesh:


.. code:: default
    
    >>> model.metadata.meshed_region.nodes.n_nodes
    >>> model.metadata.meshed_region.elements.n_elements
    >>> print(model.metadata.meshed_region.elements.element_by_id(1))
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    3751
    3000
    DPF Element 1
    	Index:         1400
    	Nodes:            8
    	Type:       element_types.Hex8
    	Shape:        Solid


You can the time sets with:


.. code-block:: default
    
    time_freq_support =  model.metadata.time_freq_support
    print(time_freq_support.time_frequencies.data)
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    [1.]


For a full description of the Metadata object, see the APIs section :ref:`ref_model`.


Model Results
-------------
The model contains the ``results`` attribute, which you can use to
create operators to access certain results.  To view the available
results, print them with:


.. code-block:: default

    print(model.results)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
 DPF Result Info 
  Analysis: static 
  Physics Type: mecanic 
  Unit system: MKS: m, kg, N, s, V, A, degC 
  Available results: 
    U Displacement :nodal displacements 
    ENF Element nodal Forces :element nodal forces 
    ENG_VOL Volume :element volume 
    ENG_SE Energy-stiffness matrix :element energy associated with the stiffness matrix 
    ENG_AHO Hourglass Energy :artificial hourglass energy 
    ENG_TH thermal dissipation energy :thermal dissipation energy 
    ENG_KE Kinetic Energy :kinetic energy 
    ENG_CO co-energy :co-energy (magnetics) 
    ENG_INC incremental energy :incremental energy (magnetics) 
    BFE Temperature :element structural nodal temperatures 
    

.. autoattribute:: ansys.dpf.core.model.Model.results
  :noindex:
    
Choosing the time or frequencies or the spatial subset on which to get a given result
is straightforward with this ``results`` attribute:


.. code-block:: default

    disp_result = model.results.displacement
    disp_at_all_times_on_node_1 =  disp_result.on_all_time_freqs.on_mesh_scoping([1])
    

For a full example using the Result API, see :ref:`ref_transient_easy_time_scoping`.

For a full description of the Model object, see the APIs section :ref:`ref_results`.



API Reference
~~~~~~~~~~~~~

See :ref:`ref_model` or :ref:`ref_results` for more information.
