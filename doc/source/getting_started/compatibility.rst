.. _ref_compatibility:

=============
Compatibility
=============

Operating system
----------------

DPF supports Windows 10 and Rocky Linux 8 and later.
To run DPF on CentOS 7, use DPF for 2024 R2 (8.2) or later.
For more information, see `Ansys Platform Support <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_.

Compatibility with DPF and ANSYS releases
-----------------------------------------

The DPF server version depends on your installed Ansys version or your installed standalone DPF Server pre-release version.


The compatibility table below shows the client-server (``ansys-dpf-core`` to ``DPF``) compatibility for supported DPF versions.

Here is a summary of the compatibility rules:

- With DPF for Ansys 2023 R1 and later, you can use PyDPF-Core ``0.10`` and later.
- With DPF for Ansys 2022 R2, you can use PyDPF-Core version ``0.10`` up to ``0.15``.
- With DPF for Ansys 2021 R2 and 2022 R1, you can use PyDPF-Core version ``0.3`` up to ``0.9``.
- With DPF for Ansys 2021 R1, you must use PyDPF-Core version ``0.2``.

As new features are developed, every attempt is made to ensure backward
compatibility from the client to the server.

Backward compatibility policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PyDPF-Core follows the official Ansys support policy for retro-compatibility:

When ``ansys-dpf-core`` is released, compatibility is officially ensured with all revisions of:

- DPF for Ansys releases that same year
- DPF for Ansys releases at year -1
- DPF for Ansys releases at year -2

For example, ``ansys-dpf-core`` 0.15 supports:

- DPF for Ansys 2025 R2 and R1 (Ansys 2025 R2 being the latest released version at that time)
- DPF for Ansys 2024 R2 and R1
- DPF for Ansys 2023 R2 and R1


Breaking changes
^^^^^^^^^^^^^^^^

Starting with version ``0.10`` of ``ansys-dpf-core``, the packages ``ansys-dpf-gate``,
``ansys-dpf-gatebin`` and ``ansys-grpc-dpf`` are no longer dependencies and are directly integrated
within ``ansys-dpf-core`` as modules. This introduced a breaking change to simplify installation
and prevent synchronization issues between the PyDPF libraries, requiring to drop support for Ansys
previous to 2022 R2.

**Ansys strongly encourages you to use the latest packages available**, as far they are compatible
with the server version you want to run. Considering Ansys 2023 R1 for example, if ``ansys-dpf-core``
module 0.10.0 is the latest available compatible package, it should be used.

For ``ansys-dpf-core<0.10``, the `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_
package should also be synchronized with the server version.

Compatibility tables
^^^^^^^^^^^^^^^^^^^^

The following tables list the client-server compatibility for recent and legacy DPF versions.

Recent DPF versions
+++++++++++++++++++

.. list-table:: Client-server compatibility for supported DPF versions
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Server version
     - ``ansys.dpf.core`` Python module version
     - ``ansys.grpc.dpf`` Python module version
     - ``ansys.dpf.gatebin`` binaries Python module version
     - ``ansys.dpf.gate`` Python module version
   * - 12.0 (2026 R1)
     - 0.15.0 and later
     - None
     - None
     - None
   * - 11.0 (2026 R1 pre0)
     - 0.14.0 and later
     - None
     - None
     - None
   * - 10.0 (2025 R2)
     - 0.13.8 and later
     - None
     - None
     - None
   * - 9.1 (2025 R1)
     - 0.13.4 and later
     - None
     - None
     - None
   * - 9.0 (2025 R1 pre0)
     - 0.13.0 and later
     - None
     - None
     - None
   * - 8.2 (2024 R2)
     - 0.12.1 and later
     - None
     - None
     - None
   * - 8.1 (2024 R2 pre1)
     - 0.12.0 and later
     - None
     - None
     - None
   * - 8.0 (2024 R2 pre0)
     - 0.11.0 and later
     - None
     - None
     - None
   * - 7.1 (2024 R1)
     - 0.10.1 and later
     - None
     - None
     - None
   * - 7.0 (2024 R1 pre0)
     - | 0.10.0 and later
       | 0.9.0
     - | None
       | 0.8.1
     - | None
       | 0.4.1
     - | None
       | 0.4.1
   * - 6.2 (2023 R2)
     - | 0.10.0 and later
       | 0.8.0 to 0.9.0
     - | None
       | 0.7.1 and later
     - | None
       | 0.3.1 and later
     - | None
       | 0.3.1 and later
   * - 6.1 (2023 R2 pre1)
     - | 0.10.0 and later
       | 0.8.0 to 0.9.0
     - | None
       | 0.7.1 and later
     - | None
       | 0.3.1 and later
     - | None
       | 0.3.1 and later
   * - 6.0 (2023 R2 pre0)
     - | 0.10.0 and later
       | 0.7.0 to 0.9.0
     - | None
       | 0.7.0 and later
     - | None
       | 0.3.0 and later
     - | None
       | 0.3.0 and later
   * - 5.0 (2023 R1)
     - | 0.10.0 and later
       | 0.6.0 to 0.9.0
     - | None
       | 0.6.0 and later
     - | None
       | 0.2.0 and later
     - | None
       | 0.2.0 and later

Legacy DPF versions
+++++++++++++++++++

    .. list-table:: Client-server compatibility
       :widths: 20 20 20 20 20
       :header-rows: 1

       * - Server version
         - ``ansys.dpf.core`` Python module version
         - ``ansys.grpc.dpf`` Python module version
         - ``ansys.dpf.gatebin`` binaries Python module version
         - ``ansys.dpf.gate`` Python module version
       * - 4.0 (2022 R2)
         - | 0.10.0 to 0.15
           | 0.5.0 to 0.9.0
         - | None
           | 0.5.0 and later
         - | None
           | 0.1.0 and later
         - | None
           | 0.1.0 and later
       * - 3.0 (2022 R1)
         - 0.4.0 to 0.9.0
         - 0.4.0
         - None
         - None
       * - 2.0 (2021 R2)
         - 0.3.0 to 0.9.0**
         - 0.3.0
         - None
         - None
       * - 1.0 (2021 R1)
         - 0.2.*
         - 0.2.2
         - None
         - None

    (** Compatibility of DPF 2.0 with ``ansys-dpf-core`` 0.5.0 to 0.9.0 is assumed but not certified.)

Python version support
----------------------

PyDPF-Core strives to follow `SPEC-0 <https://scientific-python.org/specs/spec-0000/>`_ for Python version support,
as stated in the PyAnsys ecosystem `Python version support policy <https://docs.pyansys.com/version/stable/getting-started/prerequisites.html#supported-python-versions>`_.

This means that, barring other factors, the state of SPEC-0 as at when a particular version of PyDPF-Core is released determines the supported Python versions.
The following table lists the Python versions supported by every PyDPF-Core release.

.. list-table:: Python version support
   :widths: 20 20 20
   :header-rows: 1

   * - ``ansys-dpf-core`` version
     - Supported Python versions
     - Additional notes
   * - 0.2.1
     - 3.5, 3.6, 3.7, 3.8
     -
   * - 0.3.0 – 0.4.2
     - 3.5, 3.6, 3.7, 3.8, 3.9
     -
   * - 0.5.2
     - 3.7, 3.8, 3.9
     -
   * - 0.6.0 – 0.6.2
     - 3.7, 3.8, 3.9, 3.10
     -
   * - 0.7.0 – 0.8.1
     - 3.7, 3.8, 3.9, 3.10
     -
   * - 0.9.0
     - 3.8, 3.9, 3.10
     -
   * - 0.10.0 – 0.10.1
     - 3.9, 3.10, 3.11
     -
   * - 0.11.0 – 0.12.2
     - 3.9, 3.10, 3.11
     -
   * - 0.13.0 – 0.13.6
     - 3.9, 3.10, 3.11
     -
   * - 0.13.7 – 0.13.8
     - 3.10, 3.11, 3.12
     - Can be installed on Python 3.9 but not tested
   * - 0.14.0 – 0.14.2
     - 3.10, 3.11, 3.12, 3.13
     - Can be installed on Python 3.9 but not tested
   * - 0.15.0
     - 3.10, 3.11, 3.12, 3.13
     - Can be installed on Python 3.9 but not tested
   * - dev
     - 3.10, 3.11, 3.12, 3.13, 3.14
     - Can only be installed in development mode (see `Install in development mode <https://dpf.docs.pyansys.com/version/stable/getting_started/install.html#install-in-development-mode>`_)

Update Python environment
-------------------------

When moving from one Ansys release to another, you must update the ``ansys-dpf-core`` package.
To get the latest version of the ``ansys-dpf-core`` package, use this command:

.. code::
    
	pip install --upgrade --force-reinstall ansys-dpf-core

To get a specific version of the ``ansys-dpf-core`` package, such as 0.7.0, use this command:

.. code::

    pip install --force-reinstall ansys-dpf-core==0.7.0
