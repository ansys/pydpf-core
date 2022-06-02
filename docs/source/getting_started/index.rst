.. _ref_getting_started:

===============
Getting Started
===============

Compatibility
~~~~~~~~~~~~~
DPF supports Windows 10 and CentOS 7 and later.  For
more information, see `Ansys Platform Support <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_.

Other platforms may be supported by using DPF within a
containerization ecosystem such as Docker or Kubernetes.
For more information, see :ref:`docker`.

***************************
Client Server Compatibility
***************************

The `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ module should be synchronized
with the server version as shown here:

.. list-table:: Client-Server Compatibility
   :widths: 35 35 35
   :header-rows: 1

   * - Ans.Dpf.Grpc.exe server version
     - ansys.grpc.dpf python module version
     - ansys.dpf.core python module version
   * - 3.0 (Ansys 2022R1)
     - 0.4.0
     - >=0.4.0
   * - 2.0 (Ansys 2021R2)
     - 0.3.0
     - >=0.3.0
   * - 1.0 (Ansys 2021R1)
     - 0.2.2
     - 0.2.*


Future development will try to ensure backward compatibility from the client to the server.


To start a server with Ans.Dpf.Grpc.bat or Ans.Dpf.Grpc.sh (used in the `start_local_server`  function),
please make sure that the environment variable `AWP_ROOT{VER}` with (VER=212, 221, ...) is set.

Architecture
~~~~~~~~~~~~~

DPF-Core is a Python gRPC client communicating with the ``Ans.Dpf.Grpc`` 
server. To use the native DPF server, you must have a local installation of
Ansys 2021 R2.  For more information on getting a licensed copy of Ansys,
visit the `Ansys website <https://www.ansys.com/>`_.


.. _basic-gallery:

Installation
~~~~~~~~~~~~

.. include:: install.rst


.. toctree::
   :hidden:
   :maxdepth: 2

   docker
   
   
Tryout Installation
~~~~~~~~~~~~~~~~~~~

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
    Physics Type: Mecanic
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
    


Dependencies
~~~~~~~~~~~~~

DPF-Core dependencies are automatically checked when packages are 
installed. The package dependencies are:

- `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ (gRPC code generated from protobufs)
- `psutil <https://pypi.org/project/psutil/>`_
- `progressbar2 <https://pypi.org/project/progressbar2/>`_

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

Optional package dependencies can be installed for specific usage:

- `Matplotlib <https://pypi.org/project/matplotlib/>`_ for chart plotting
- `PyVista <https://pypi.org/project/pyvista/>`_ for 3D plotting
- `Scooby <https://pypi.org/project/scooby/>`_ for dependency reports
