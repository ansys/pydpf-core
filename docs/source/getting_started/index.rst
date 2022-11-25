.. _ref_getting_started:

===============
Getting started
===============

The Data Processing Framework (DPF) provides numerical simulation users and engineers with a toolbox
for accessing and transforming simulation data. DPF can access data from solver result files as well
as several neutral formats (csv, hdf5, vtk, etc.).
This **workflow-based** framework allows to perform complex preprocessing and postprocessing
operations of large amounts of simulation data.

PyDPF-Core is a python client API communicating with a **DPF Server** either through the network using gRPC
or directly in the same process.


Installing PyDPF-Core Client
----------------------------

In a Python environment, run the following command:

.. code::

   pip install ansys-dpf-core

For more installation options, refer to :ref:`Installation section <installation>`.


Installing DPF Server
---------------------

#. DPF Server is packaged within **Ansys Unified Installer** starting with Ansys 2021 R1.
   To use it, install Ansys following the installer instructions. For any trouble, refer to the
   :ref:`Environment variable section <ref_compatibility>`.
   For more information on getting a licensed copy of Ansys,
   visit the `Ansys website <https://www.ansys.com/>`_.

#. DPF Server is available as a **standalone** package (independent of the Ansys Installer) available on the Ansys Customer Portal.
   Protected by Ansys license mechanism (see
   :ref:`Ansys licensing section <ref_getting_started_with_dpf_server>`), once having access to an
   Ansys license, install DPF Server with:

.. card::

    * Download the ansys_dpf_server_win_v2023.2.pre0.zip or ansys_dpf_server_lin_v2023.2.pre0.zip
      file as appropriate.
    * Unzip the package and go to the root folder of the unzipped package
      (ansys_dpf_server_win_v2023.2.pre0 or ansys_dpf_server_lin_v2023.2.pre0).
    * In a Python environment, run the following command:

    .. code::

        pip install -e .

    * DPF Server is protected using license terms specified in the DPFUserLicensingAgreement.txt
      file that can be found on the Ansys Customer Portal. To accept the DPF User Licensing
      Agreement terms, the following environment flag must be set:

    .. code::

        ANSYS_DPF_ACCEPT_LA=Y



For other ways of using the Server (without pip install, user **Docker Containers**...), see
:ref:`ref_getting_started_with_dpf_server`.


Use PyDPF-Core
--------------

In the same Python environment, run the following command:

.. code:: python

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_crankshaft())
    >>> print(model)


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Model
    ------------------------------
    Static analysis
    Unit system: MKS: m, kg, N, s, V, A, degC
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  velocity: Nodal Velocity
         -  acceleration: Nodal Acceleration
         -  reaction_force: Nodal Force
         -  stress: ElementalNodal Stress
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  elastic_strain: ElementalNodal Strain
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region:
      69762 nodes
      39315 elements
      Unit: m
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support:
      Number of sets: 3
    Cumulative     Time (s)       LoadStep       Substep
    1              1.000000       1              1
    2              2.000000       1              2
    3              3.000000       1              3



.. code:: python

    >>> over_time_disp = model.results.displacement().eval()
    >>> over_time_disp[0].plot()


.. figure:: ../images/plotting/crankshaft_disp.png


.. toctree::
   :hidden:
   
   compatibility
   install
   dependencies

