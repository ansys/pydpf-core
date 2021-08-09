===============
Getting Started
===============

Architecture
~~~~~~~~~~~~~

DPF-Core is a Python gRPC client communicating with the ``Ans.Dpf.Grpc`` 
server. To use the native DPF server, you must have a local installation of
Ansys 2021 R2.  For more information on getting a licensed copy of Ansys,
visit https://www.ansys.com.


.. _basic-gallery:

Installation
~~~~~~~~~~~~

.. include:: install.rst


.. toctree::
   :hidden:
   :maxdepth: 2

   docker
   
   
Tryout Installation
~~~~~~~~~~~~~~~~

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
    


Dependencies
~~~~~~~~~~~~~

DPF-Core dependencies are automatically checked when packages are 
installed. The dependencies are:

- `ansys.grpc.dpf` with thegRPC code generated from protobufs
- ``psutil``
- ``progressbar2``

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

Optional dependencies can be installed for specific usage:

- ``matplotlib`` for chart plotting
- ``pyvista`` for 3D plotting
- ``scooby`` for dependency reports


Compatibility
~~~~~~~~~~~~~
DPF supports Windows 10 and CentOS 7 and later.  For
more information, see `Ansys Platform Support <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_.

Other platforms may be supported by using DPF within a
containerization ecosystem such as Docker or Kubernetes. 
For more information, see :ref:`docker`.


