The following example shows how to open a result file generated by Ansys MAPDL (or another Ansys solver) and 
extract results:

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    model = Model(examples.find_simple_bar())
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
    

.. code-block:: default

    disp = model.results.displacement().X()
    model.metadata.meshed_region.plot(disp.outputs.fields_container())



.. rst-class:: sphx-glr-script-out

 .. figure:: images/plotting/simple_example.png
