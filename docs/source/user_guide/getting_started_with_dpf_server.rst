.. _ref_getting_started_with_dpf_server:

===============================
Getting started with DPF Server
===============================

What is DPF Server
------------------

DPF provides numerical simulation users and engineers with a toolbox for accessing and transforming 
simulation data. With DPF, you can perform complex preprocessing or postprocessing of large amounts of simulation data within a 
simulation workflow.

DPF Server is a package that contains all the necessary files to run the DPF Server, enabling DPF capabilities. It is available 
on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_ of the Ansys Customer Portal.
The first version of DPF Server is 6.0 (2023 R2).

The sections on this page describe how to use DPF Server. 

* For a quick start on DPF Server, see :ref:`ref_getting_started`. 
* For more information on DPF and its use, see :ref:`ref_user_guide`. 


Install DPF Server
------------------

.. _target_installing_server:

#. Download the ``ansys_dpf_server_win_v2023.2.pre1.zip`` or ``ansys_dpf_server_lin_v2023.2.pre1.zip`` file as appropriate.
#. Unzip the package.
#. Optional: download any other plugin ZIP file as appropriate and unzip the package. For example, to access the ``composites`` plugin for Linux, 
   download ``ansys_dpf_composites_lin_v2023.2.pre1.zip`` and unzip the package in the same location as ``ansys_dpf_server_lin_v2023.2.pre1.zip``.
#. Change to the root folder (``ansys_dpf_server_win_v2023.2.pre1``) of the unzipped package. 
#. In a Python environment, run this command:

.. code::

    pip install -e . 

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
for PyDPF-Core are available in the PyDPF-Core `Getting started <https://dpf.docs.pyansys.com/getting_started/install.html>`_.
Installation instructions for PyDPF-Post are available in the PyDPF-Post `Getting started <https://post.docs.pyansys.com/getting_started/install.html>`_.

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

Run DPF Server in a Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DPF server can be run in a Docker container.

#. Along with the ``ansys_dpf_server_lin_v2023.2.pre1.zip`` file mentioned earlier
   in :ref:`Install DPF Server <target_installing_server>`, download the ``Dockerfile`` file.
#. Optional: download any other plugin ZIP file as appropriate. For example, to access ``composites`` plugin for Linux, 
   download ``ansys_dpf_composites_lin_v2023.2.pre1.zip``.
#. Copy all the ZIP files and ``Dockerfile`` file in a folder and navigate into that folder.
#. To build the DPF Docker container, run the following command:

.. code::

    docker build . -t dpf-core:v2023_2_pre1 --build-arg DPF_VERSION=232

4. To run the DPF Docker container, license it. For more information, see'
   :ref:`DPF Preview License Agreement<target_to_license_terms>`.

License terms
-------------

.. _target_to_license_terms:

DPF Preview License Agreement 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DPF Server is protected using license terms specified in the `DPFPreviewLicenseAgreement <https://download.ansys.com/-/media/dpf/dpfpreviewlicenseagreement.ashx?la=en&hash=CCFB07AE38C638F0D43E50D877B5BC87356006C9>`_
file that can be found on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_
of the Ansys Customer Portal. The ``DPFPreviewLicenseAgreement`` file s a text file, which means that you can
open it with a text editor, such as notepad.

To accept the terms of this license agreement, you must set the following environment variable: 

.. code::

    ANSYS_DPF_ACCEPT_LA=Y

The ``ANSYS_DPF_ACCEPT_LA`` environment variable confirms your acceptance of the DPF License Agreement.
By passing the value ``Y`` to this environment variable, you are indicating that you have a valid and
existing license for the edition and version of DPF Server that you intend to use.

For DPF Docker container usage only, you can use the following code to set both the `ANSYS_DPF_ACCEPT_LA``
and ``ANSYSLMD_LICENSE_FILE`` environment variables. For the ``ANSYSLMD_LICENSE_FILE`` environment variable,
ensure that you replace ``<license_server_to_use>`` to point to the Ansys license server.

.. code::

    docker run -e "ANSYS_DPF_ACCEPT_LA=Y" -e ANSYSLMD_LICENSE_FILE=1055@<license_server_to_use> -p 50052:50052 -e DOCKER_SERVER_PORT=50052 --expose=50052 dpf-core:v2023_2_pre1

The next section, :ref:`Ansys licensing<target_to_ansys_license_mechanism>`, provides information on
the Ansys license mechanism that is used with DPF Server.


.. _target_to_ansys_license_mechanism:

Ansys licensing
~~~~~~~~~~~~~~~

DPF Server is protected by an Ansys licensing mechanism.

DPF capabilities are available through the following main contexts:

- **Premium:** This default context allows DPF to perform license checkouts,
  making licensed DPF operators available.
- **Entry:** This context does not allow DPF to perform any license checkout,
  meaning that licensed DPF operators fail.

To update the context, apply a new server context:

.. code::

    dpf.apply_server_context(dpf.AvailableServerContexts.premium)

.. _target_to_ansys_license_increments_list:

The following Ansys licensing increments provide rights to use DPF Server: 

- ``preppost`` available in the ``Ansys Mechanical Enterprise PrepPost`` product
- ``meba`` available in the ``ANSYS Mechanical Enterprise Solver`` product
- ``mech_2`` available in the ``ANSYS Mechanical Premium`` product
- ``mech_1`` available in the ``ANSYS Mechanical Pro`` product
- ``ansys`` available in the ``ANSYS Mechanical Enterprise`` product
- ``dynapp`` available in the ``ANSYS LS-DYNA PrepPost`` product
- ``vmotion`` available in the ``Ansys Motion`` product
- ``acpreppost`` available in the ``Ansys Mechanical Enterprise`` product
- ``acdi_adprepost`` available in the ``Ansys AUTODYN`` and ``Ansys AUTODYN PrepPost`` products
- ``cfd_preppost`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_preppost_pro`` available in the ``Ansys CFD Enterprise`` product
- ``vmotion_post`` available in the ``Ansys Motion Post`` product
- ``vmotion_pre`` available in the ``Ansys Motion Pre`` product
- ``advanced_meshing`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_meshing_pro`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_setup_post`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_setup_post_pro`` available in the ``Ansys CFD Enterprise`` product
- ``acfx_pre`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_base`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level1`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level2`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level3`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_meshing`` available in the ``Ansys CFD Enterprise`` product
- ``avrxp_snd_level1`` available in the ``Ansys Sound Enterprise`` product
- ``sherlock`` available in the ``Ansys Sherlock`` product

Each increment may be available in other products. On the Ansys Customer Portal,
the `Licensing section <https://download.ansys.com/Installation%20and%20Licensing%20Help%20and%20Tutorials>`_
provides product/increment mapping.