.. _installation:

************
Installation
************

PIP installation
----------------

To use PyDPF-Core with Ansys 2021 R2 or later, install the latest version
of PyDPF-Core with:

.. code::

   pip install ansys-dpf-core


To use PyDPF-Core with Ansys 2021 R1, install a 0.2.* PyDPF-Core version with:

.. code::

   pip install ansys-dpf-core<0.3.0


Wheel file installation
-----------------------
If you are unable to install PyDPF-Core on the host machine due to
network isolation, download the latest wheel file or the wheel file
for a specific release from `PyDPF-Core
GitHub <https://github.com/pyansys/pydpf-core/releases>`_ or
`PyDPF-Core PyPi <https://pypi.org/project/ansys-dpf-core/>`_.

Tryout installation
-------------------

For a quick tryout installation, use:

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    model = Model(examples.simple_bar)
    print(model)



.. rst-class:: sphx-glr-script-out

 Out:

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
    


Development mode installation
-----------------------------

If you want to edit and potentially contribute to PyDPF-Core,
clone the repository and install it using pip with the ``-e``
development flag:

.. code::

    git clone https://github.com/pyansys/pydpf-core
    cd pydpf-core
    pip install -e .

