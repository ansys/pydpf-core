.. _ref_dpf_server:

==========
DPF Server
==========

DPF provides numerical simulation users and engineers with a toolbox for accessing and transforming 
simulation data. With DPF, you can perform complex preprocessing or postprocessing of large amounts of simulation data within a 
simulation workflow.

The DPF Server is packaged within the **Ansys installer** in Ansys 2021 R1 and later.

It is also available as a standalone package that contains all the necessary files to run, enabling DPF capabilities.
The standalone DPF Server is available on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_ of the Ansys Customer Portal.
The first standalone version of DPF Server available is 6.0 (2023 R2).

The sections on this page describe how to install and use a standalone DPF Server.

* For a quick start on using PyDPF, see :ref:`ref_getting_started`.
* For more information on DPF and its use, see :ref:`ref_user_guide`.


Install DPF Server
------------------

.. _target_installing_server:

#. Download the ``ansys_dpf_server_win_v2024.2.pre0.zip`` or ``ansys_dpf_server_lin_v2024.2.pre0.zip`` file as appropriate.
#. Unzip the package.
#. Optional: download any other plugin ZIP file as appropriate and unzip the package. For example, to access the ``composites`` plugin for Linux, 
   download ``ansys_dpf_composites_lin_v2024.2.pre0.zip`` and unzip the package in the same location as ``ansys_dpf_server_lin_v2024.2.pre0.zip``.
#. Change to the root folder (``ansys_dpf_server_win_v2024.2.pre0``) of the unzipped package.
#. In a Python environment, run this command:

.. code::

    pip install -e .


As detailed in :ref:`licensing`, a standalone DPF Server is protected using the license terms specified in the
`DPFPreviewLicenseAgreement <https://download.ansys.com/-/media/dpf/dpfpreviewlicenseagreement.ashx?la=en&hash=CCFB07AE38C638F0D43E50D877B5BC87356006C9>`_
file, which is available on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_
of the Ansys Customer Portal.
To accept these terms, you must set this environment variable:

.. code::

    ANSYS_DPF_ACCEPT_LA=Y

To use :ref:`licensed DPF capabilities <target_to_ansys_license_mechanism>` you must set the
``ANSYSLMD_LICENSE_FILE`` environment variable to point to a valid local or remote license
following indications in :ref:`configure_licensing`.


Use DPF Server
--------------

DPF Server is protected using the license terms specified in the
`DPFPreviewLicenseAgreement <https://download.ansys.com/-/media/dpf/dpfpreviewlicenseagreement.ashx?la=en&hash=CCFB07AE38C638F0D43E50D877B5BC87356006C9>`_
file, which is available on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_
of the Ansys Customer Portal.

Run DPF Server with PyDPF
~~~~~~~~~~~~~~~~~~~~~~~~~

PyDPF-Core is a Python client API communicating with a **DPF Server**, either
through the network using gRPC or directly in the same process. PyDPF-Post is a Python
module for postprocessing based on PyDPF-Core. 

Both PyDPF-Core and PyDPF-Post can be used with DPF Server. Installation instructions
for PyDPF-Core are available in the PyDPF-Core `Getting started <https://dpf.docs.pyansys.com/version/stable/getting_started/install.html>`_.
Installation instructions for PyDPF-Post are available in the PyDPF-Post `Getting started <https://post.docs.pyansys.com/version/stable/getting_started/install.html>`_.

With PyDPF-Core and PyDPF-Post, the first creation of most DPF entities starts a DPF Server with the current default configuration and context.
For example, the following code automatically starts a DPF Server behind the scenes:

.. code::

    from ansys.dpf import core as dpf
    data_sources = dpf.DataSources()

With PyDPF-Core, you can also explicitly start a DPF Server using this code:

.. code::

    from ansys.dpf import core as dpf
    server = dpf.start_local_server()

To start a DPF Server from outside a Python environment, you can also use the execution script provided with your DPF Server package.
On Windows, start the DPF Server by running the ``Ans.Dpf.Grpc.bat`` file in the unzipped package.
On Linux, start the DPF Server by running the ``Ans.Dpf.Grpc.sh`` file in the unzipped package.

Manage multiple DPF Server installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyDPF automatically starts a local instance of a DPF Server when you run a method requiring a
connection to a server, or when you use the ``start_local_server()`` method.
The ``start_local_server()`` method allows to choose, if necessary, which DPF Server installation
to use thanks to its ``ansys_path`` argument.
PyDPF otherwise follows the logic below to automatically detect and choose which locally installed
version of DPF Server to run:

- it uses the ``ANSYS_DPF_PATH`` environment variable in priority if set and targeting a valid path to a DPF Server installation.
- it then checks the currently active Python environment for any installed standalone DPF Server, and uses the latest version available.
- it then checks for ``AWP_ROOTXXX`` environment variables, which are set by the **Ansys installer**, and uses the latest version available.
- if then raises an error if all of the steps above failed to return a valid path to a DPF Server installation.

Run DPF Server in a Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DPF Server can be run in a Docker container.

#. Along with the ``ansys_dpf_server_lin_v2024.2.pre0.zip`` file mentioned earlier
   in :ref:`Install DPF Server <target_installing_server>`, download the ``Dockerfile`` file.
#. Optional: download any other plugin ZIP file as appropriate. For example, to access the ``composites`` plugin for Linux, 
   download ``ansys_dpf_composites_lin_v2024.2.pre0.zip``.
#. Copy all the ZIP files and ``Dockerfile`` file in a folder and navigate into that folder.
#. To build the DPF Docker container, run the following command:

.. code::

    docker build . -t dpf-core:v2024.2.pre0 --build-arg DPF_VERSION=242

5. To run the DPF Docker container, license it. For more information, see :ref:`DPF Preview License Agreement<target_to_license_terms>`.
