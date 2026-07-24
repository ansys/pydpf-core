.. _ref_compatibility:

=============
Compatibility
=============

Operating system
----------------

DPF supports Windows 10 and CentOS 7 and later. For
more information, see `Ansys Platform Support <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_.

Client-server
-------------

The DPF server version depends on your installed Ansys version.
The following table shows client-server compatibility for supported
Ansys versions. With Ansys 2021 R2 and later, you can use PyDPF-Core
version 0.3.0 or later. With Ansys 2021 R1, you must use a PyDPF-Core 0.2
version.

As new features are developed, every attempt is made to ensure backward
compatibility from the client to the server.

The `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ package
should also be synchronized with the server version.

.. list-table:: Client-server compatibility
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - ``Ans.Dpf.Grpc.exe`` server version
     - ``ansys.dpf.gatebin`` binaries Python module version
     - ``ansys.dpf.gate`` Python module version
     - ``ansys.grpc.dpf`` Python module version
     - ``ansys.dpf.core`` Python module version
   * - 5.0 (Ansys 2023 R1)
     - 0.2.0 and later
     - 0.2.0 and later
     - 0.6.0 and later
     - 0.6.0 and later
   * - 4.0 (Ansys 2022 R2)
     - 0.1.*
     - 0.1.*
     - 0.5.*
     - 0.5.0 and later
   * - 3.0 (Ansys 2022 R1)
     - None
     - None
     - 0.4.0
     - 0.4.0 and later
   * - 2.0 (Ansys 2021 R2)
     - None
     - None
     - 0.3.0
     - 0.3.0 and later
   * - 1.0 (Ansys 2021 R1)
     - None
     - None
     - 0.2.2
     - 0.2.*


Environment variable
--------------------

The ``start_local_server``  method uses the ``Ans.Dpf.Grpc.bat`` file or
``Ans.Dpf.Grpc.sh`` file to start the server. Ensure that the ``AWP_ROOT{VER}``
environment variable is set to your installed Ansys version. For example, if Ansys
2022 R2 is installed, ensure that the ``AWP_ROOT222`` environment
variable is set to the path for this Ansys installation.
   
