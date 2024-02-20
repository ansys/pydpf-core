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
Ansys versions. With Ansys 2022 R2 and later, you can use PyDPF-Core ``0.10`` and later.
With Ansys 2021 R2 and 2022 R1, you can use PyDPF-Core
version ``0.3`` up to ``0.9``. With Ansys 2021 R1, you must use a PyDPF-Core ``0.2``
version.

As new features are developed, every attempt is made to ensure backward
compatibility from the client to the server. Backward compatibility is generally ensured for
the 4 latest Ansys versions. For example, ansys-dpf-core module with 0.8.0 version has been
developed for Ansys 2023 R2 pre1 release, for 2023 R2 Ansys version. It is compatible with
2023 R2, 2023 R1, 2022 R2 and 2022 R1 Ansys versions.

Starting with version ``0.10`` of ``ansys-dpf-core``, the packages ``ansys-dpf-gate``,
``ansys-dpf-gatebin`` and ``ansys-grpc-dpf`` are no longer dependencies and are directly integrated
within ``ansys-dpf-core`` as modules. This introduced a breaking change to simplify installation
and prevent synchronization issues between the PyDPF libraries, requiring to drop support for Ansys
previous to 2022 R2.

**Ansys strongly encourages you to use the latest packages available**, as far they are compatible
with the Server version you want to run. Considering Ansys 2023 R1 for example, if ansys-dpf-core
module with 0.10.0 version is the latest available compatible package, it should be used.

For ``ansys-dpf-core<0.10``, the `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_
package should also be synchronized with the server version.

.. list-table:: Client-server compatibility
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Server version
     - ``ansys.dpf.core`` Python module version
     - ``ansys.grpc.dpf`` Python module version
     - ``ansys.dpf.gatebin`` binaries Python module version
     - ``ansys.dpf.gate`` Python module version
   * - 8.0 (Ansys 2024 R2 pre0)
     - 0.11.0 and later
     - None
     - None
     - None
   * - 7.1 (Ansys 2024 R1)
     - 0.10.1 and later
     - None
     - None
     - None
   * - 7.0 (Ansys 2024 R1 pre0)
     - | 0.10.0 and later
       | 0.9.0
     - | None
       | 0.8.1
     - | None
       | 0.4.1
     - | None
       | 0.4.1
   * - 6.2 (Ansys 2023 R2)
     - | 0.10.0 and later
       | 0.8.0 and later
     - | None
       | 0.7.1 and later
     - | None
       | 0.3.1 and later
     - | None
       | 0.3.1 and later
   * - 6.1 (Ansys 2023 R2 pre1)
     - | 0.10.0 and later
       | 0.8.0 and later
     - | None
       | 0.7.1 and later
     - | None
       | 0.3.1 and later
     - | None
       | 0.3.1 and later
   * - 6.0 (Ansys 2023 R2 pre0)
     - | 0.10.0 and later
       | 0.7.0 and later
     - | None
       | 0.7.0 and later
     - | None
       | 0.3.0 and later
     - | None
       | 0.3.0 and later
   * - 5.0 (Ansys 2023 R1)
     - | 0.10.0 and later
       | 0.6.0 and later
     - | None
       | 0.6.0 and later
     - | None
       | 0.2.0 and later
     - | None
       | 0.2.0 and later
   * - 4.0 (Ansys 2022 R2)
     - | 0.10.0 and later
       | 0.5.0 and later
     - | None
       | 0.5.0 and later
     - | None
       | 0.1.0 and later
     - | None
       | 0.1.0 and later
   * - 3.0 (Ansys 2022 R1)
     - 0.4.0 to 0.9.0
     - 0.4.0
     - None
     - None
   * - 2.0 (Ansys 2021 R2)
     - 0.3.0 and later**
     - 0.3.0
     - None
     - None
   * - 1.0 (Ansys 2021 R1)
     - 0.2.*
     - 0.2.2
     - None
     - None

(** Compatibility of DPF 2.0 with ansys-dpf-core 0.5.0 to 0.9.0 is assumed but not certified.)

Update Python environment
-------------------------

When moving from one Ansys release to another, you must update the ``ansys-dpf-core`` package.
To get the latest version of the ``ansys-dpf-core`` package, use this command:

.. code::
    
	pip install --upgrade --force-reinstall ansys-dpf-core

To get a specific version of the ``ansys-dpf-core`` package, such as 0.7.0, use this command:

.. code::

    pip install --force-reinstall ansys-dpf-core==0.7.0
