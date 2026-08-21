.. _ref_getting_started:

===============
Getting Started
===============

Compatibility
~~~~~~~~~~~~~
DPF supports Windows 10 and CentOS 7 and later. For
more information, see `Ansys Platform Support <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_.

***************************
Client Server Compatibility
***************************

The DPF server version depends on the Ansys installation version.
The PyDPF-Core client used must be compatible with it according to the table below.
Notice that starting with Ansys 2021 R2 one can use any PyDPF-Core >= 3.0.
Only Ansys 2021 R1 requires a specific version of PyDPF-Core (0.2.*).

Future development will always try to ensure backward compatibility from the client to the server.

The `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ module should also be synchronized
with the server version.

.. list-table:: Client-Server Compatibility
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Ans.Dpf.Grpc.exe server version
     - ansys.dpf.gatebin binaries python module version
     - ansys.dpf.gate python module version
     - ansys.grpc.dpf python module version
     - ansys.dpf.core python module version
   * - 4.0 (Ansys 2022R2)
     - 0.1.1
     - 0.1.1
     - 0.5.1
     - >=0.5.0
   * - 3.0 (Ansys 2022R1)
     - None
     - None
     - 0.4.0
     - >=0.4.0
   * - 2.0 (Ansys 2021R2)
     - None
     - None
     - 0.3.0
     - >=0.3.0
   * - 1.0 (Ansys 2021R1)
     - None
     - None
     - 0.2.2
     - 0.2.*

To start a server with Ans.Dpf.Grpc.bat or Ans.Dpf.Grpc.sh (used in the `start_local_server`  function),
please make sure that the environment variable `AWP_ROOT{VER}` with (VER=212, 221, ...) is set.

Architecture
~~~~~~~~~~~~~

DPF-Core is a Python gRPC client communicating with the ``Ans.Dpf.Grpc`` 
server. To use the native DPF server, you must have a local installation of
Ansys 2021 R1 or higher.  For more information on getting a licensed copy of Ansys,
visit the `Ansys website <https://www.ansys.com/>`_.


.. _getting_started:

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

- `ansys.dpf.gate <https://pypi.org/project/ansys-dpf-gate/>`_ (Gate to DPF C API or python
  grpc API). Dependencies of gate are (and/or depending on the server configuration):
    - `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ (gRPC code generated from
      protobufs)
    - `ansys.dpf.gatebin <https://pypi.org/project/ansys-dpf-gatebin/>`_ (os specific binaries
      with DPF C APIs)
- `psutil <https://pypi.org/project/psutil/>`_
- `tqdm <https://pypi.org/project/tqdm/>`_
- `packaging <https://pypi.org/project/packaging/>`_
- `numpy <https://pypi.org/project/numpy/>`_

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

Optional package dependencies can be installed for specific usage:

- `Matplotlib <https://pypi.org/project/matplotlib/>`_ for chart plotting
- `PyVista <https://pypi.org/project/pyvista/>`_ for 3D plotting
