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
compatibility from the client to the server. We ensure backward compatibility for
the 4 latest Ansys versions. For example, ansys-dpf-core module with 0.8.0 version has been
developed for Ansys 2023 R2 pre1 release, for 2023 R2 Ansys version. It is compatible with
2023 R2, 2023 R1, 2022 R2 and 2022 R1 Ansys versions.

We strongly encourage to use the latest packages available, as far they are compatible
with the Server version you want to use. Using Ansys 2022 R2, if ansys-dpf-core module with
0.8.0 version is the latest available package, it should be used.

The `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ package
should also be synchronized with the server version.

.. list-table:: Client-server compatibility
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Server version
     - ``ansys.dpf.gatebin`` binaries Python module version
     - ``ansys.dpf.gate`` Python module version
     - ``ansys.grpc.dpf`` Python module version
     - ``ansys.dpf.core`` Python module version
   * - 6.1 (Ansys 2023 R2 pre1)
     - 0.3.1 and later
     - 0.3.1 and later
     - 0.7.1 and later
     - 0.8.0 and later
   * - 6.0 (Ansys 2023 R2 pre0)
     - 0.3.0 and later
     - 0.3.0 and later
     - 0.7.0 and later
     - 0.7.0 and later
   * - 5.0 (Ansys 2023 R1)
     - 0.2.0 and later
     - 0.2.0 and later
     - 0.6.0 and later
     - 0.6.0 and later
   * - 4.0 (Ansys 2022 R2)
     - 0.1.0 and later
     - 0.1.0 and later
     - 0.5.0 and later
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
     - 0.3.0 and later**
   * - 1.0 (Ansys 2021 R1)
     - None
     - None
     - 0.2.2
     - 0.2.*

(** Compatibility of DPF 2.0 with ansys-dpf-core 0.5.0 and later is assumed but no longer certified.)

Update Python environment
-------------------------

When moving from one Ansys release to another, you must update the ``ansys-dpf-core`` package and its dependencies.
To get the latest version of the ``ansys-dpf-core`` package, use this command:

.. code::
    
	pip install --upgrade --force-reinstall ansys-dpf-core

To get a specific version of the ``ansys-dpf-core`` package, such as 0.7.0, use this command:

.. code::

    pip install --force-reinstall ansys-dpf-core==0.7.0

.. _target_environment_variable_with_dpf_section:

Environment variable
--------------------

The ``start_local_server()``  method uses the ``Ans.Dpf.Grpc.bat`` file or
``Ans.Dpf.Grpc.sh`` file to start the server. Ensure that the ``AWP_ROOT{VER}``
environment variable is set to your installed Ansys version. For example, if Ansys
2022 R2 is installed, ensure that the ``AWP_ROOT222`` environment
variable is set to the path for this Ansys installation.
  