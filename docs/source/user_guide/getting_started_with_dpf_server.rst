.. _ref_getting_started_with_dpf_server:

===============================
Getting started with DPF Server
===============================

What is DPF Server
------------------

The Data Processing Framework (DPF) provides numerical simulation users and engineers with a toolbox for accessing and transforming 
simulation data. With DPF, you can perform complex preprocessing or postprocessing of large amounts of simulation data within a 
simulation workflow.

DPF Server is a package that contains all the necessary files to run the DPF Server, enabling DPF capabilities. It is available 
on the `DPF Pre-Release page of the Ansys Customer Portal <https://download.ansys.com/Others/DPF%20Pre-Release>`_. DPF Server first available version is 6.0 (2023 R2).

For more information about DPF and its use, see :ref:`ref_user_guide`. 

The following section details how to use DPF Server package. For a quick start with DPF Server, see :ref:`ref_getting_started`. 

Installing DPF Server
---------------------

.. _target_installing_server:

#. Download the ansys_dpf_server_win_v2023.2.pre0.zip or ansys_dpf_server_lin_v2023.2.pre0.zip file as appropriate.
#. Unzip the package.
#. Change to the root folder (ansys_dpf_server_win_v2023.2.pre0) of the unzipped package. 
#. In a Python environment, run the following command:

.. code::

    pip install -e . 

Using DPF Server
----------------

DPF Server use is protected using license terms. For more information, see the :ref:`DPF Preview License Agreement<target_to_license_terms>` section.

Running the DPF Server with PyDPF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyDPF-Core is a Python client API communicating with a **DPF Server**, either
through the network using gRPC or directly in the same process. PyDPF-Post is a Python
module for postprocessing based on PyDPF-Core. 

Both PyDPF-Core and PyDPF-Post python modules can be used with the DPF Server. The instructions to install and get started with PyDPF-Core 
can be found at `PyDPF-Core, Getting Started section <https://dpf.docs.pyansys.com/getting_started/install.html>`_. The instructions to install and get
started with PyDPF-Post can be found at `PyDPF-Post, Getting Started section <https://post.docs.pyansys.com/getting_started/install.html>`_.

With PyDPF-Core and PyDPF-Post, the first creation of most DPF entities starts a DPF Server with the current default configuration and context.
For example, the following code automatically starts a DPF Server behind the scenes:

.. code::

    from ansys.dpf import core as dpf
    data_sources = dpf.DataSources()

With PyDPF-Core, you can also explicitly start a DPF Server using:

.. code::

    from ansys.dpf import core as dpf
    server = dpf.start_local_server()

To start a DPF Server from outside a Python environment, you can also use the execution script provided with your DPF Server package.
On Windows, start the DPF Server by running the ``Ans.Dpf.Grpc.bat`` file in the unzipped package.
On Linux, start the DPF Server by running the ``Ans.Dpf.Grpc.sh`` file in the unzipped package.

Running DPF Server in a Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Along with the ansys_dpf_server_lin_v2023.2.pre0.zip archive mentioned in :ref:`Installing DPF Server <target_installing_server>`, download the ``Dockerfile``.
2. Copy both the archive and ``Dockerfile`` in a folder and navigate into that folder.
3. To build the DPF Docker container, run the following commands:

.. code::

    docker build . -t dpf-core:v2023_2_pre0 --build-arg DPF_VERSION=232 --build-arg DPF_SERVER_FILE=ansys_dpf_server_lin_v2023.2.pre0.zip

4. To run the DPF Docker container, see the :ref:`DPF Preview License Agreement<target_to_license_terms>` section.

License terms
-------------

.. _target_to_license_terms:

DPF Preview License Agreement 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DPF Server use is protected using license terms specified in the `DPFPreviewLicenseAgreement <https://download.ansys.com/-/media/dpf/dpfpreviewlicenseagreement.ashx?la=en&hash=CCFB07AE38C638F0D43E50D877B5BC87356006C9>`_ file that 
can be found on the `DPF Pre-Release page of the Ansys Customer Portal <https://download.ansys.com/Others/DPF%20Pre-Release>`_. 
``DPFPreviewLicenseAgreement`` is a text file and can be opened with a text editor, such as notepad.

To accept the DPF User Licensing Agreement terms, the following environment variable must be set: 

.. code::

    ANSYS_DPF_ACCEPT_LA=Y

``ANSYS_DPF_ACCEPT_LA`` confirms your acceptance of the DPF User Licensing Agreement. By passing the value ``Y`` to the environment variable
``ANSYS_DPF_ACCEPT_LA``, you are indicating that you have a valid and existing license for the edition and version of DPF Server you intend to use.

For a DPF Docker container usage, it can be set using:

.. code::

    docker run -e "ANSYS_DPF_ACCEPT_LA=Y" -e ANSYSLMD_LICENSE_FILE=1055@<license_server_to_use> -p 50052:50052 -e DOCKER_SERVER_PORT=50052 --expose=50052 dpf-core:v2023_2_pre0

For any other case, set "ANSYS_DPF_ACCEPT_LA" as an environment variable with "Y" value.

Replace "<license_server_to_use>" mention that ANSYSLMD_LICENSE_FILE environment variable points to the Ansys license server.
For more information about Ansys license mechanism use with DPF Server, see :ref:`Ansys licensing<target_to_ansys_license_mechanism>` section.


.. _target_to_ansys_license_mechanism:

Ansys licensing
~~~~~~~~~~~~~~~

DPF Server is protected by Ansys licensing mechanism.

DPF capabilities are available through the following main contexts: 

- Entry: Loads the minimum number of plugins for basic use. It is the default. Checks if at least one increment exists 
  from the following :ref:`Ansys licensing increments list<target_to_ansys_license_increments_list>`. This increment won't be blocked.
- Premium: Loads the Entry and the Premium capabilities that require a license checkout. Blocks an increment from the
  following :ref:`Ansys licensing increments list<target_to_ansys_license_increments_list>`.

To update the context, apply a new server context:

.. code::

    dpf.apply_server_context(dpf.AvailableServerContexts.premium)

.. _target_to_ansys_license_increments_list:

The following Ansys licensing increments currently provide rights to use DPF Server: 

- ``preppost`` available in ``Ansys Mechanical Enterprise PrepPost`` product
- ``meba`` available in ``ANSYS Mechanical Enterprise Solver`` product
- ``mech_2`` available in ``ANSYS Mechanical Premium`` product
- ``mech_1`` available in ``ANSYS Mechanical Pro`` product
- ``ansys`` available in ``ANSYS Mechanical Enterprise`` product
- ``dynapp`` available in ``ANSYS LS-DYNA PrepPost`` product
- ``vmotion`` available in ``Ansys Motion`` product
- ``acpreppost`` available in ``Ansys Mechanical Enterprise`` product
- ``acdi_adprepost`` available in ``Ansys AUTODYN`` and ``Ansys AUTODYN PrepPost`` products
- ``cfd_preppost`` available in ``Ansys CFD Enterprise`` product
- ``cfd_preppost_pro`` available in ``Ansys CFD Enterprise`` product
- ``vmotion_post`` available in ``Ansys Motion Post`` product
- ``vmotion_pre`` available in ``Ansys Motion Pre`` product
- ``advanced_meshing`` available in ``Ansys CFD Enterprise`` product
- ``fluent_meshing_pro`` available in ``Ansys CFD Enterprise`` product
- ``fluent_setup_post`` available in ``Ansys CFD Enterprise`` product
- ``fluent_setup_post_pro`` available in ``Ansys CFD Enterprise`` product
- ``acfx_pre`` available in ``Ansys CFD Enterprise`` product
- ``cfd_base`` available in ``Ansys CFD Enterprise`` product
- ``cfd_solve_level1`` available in ``Ansys CFD Enterprise`` product
- ``cfd_solve_level2`` available in ``Ansys CFD Enterprise`` product
- ``cfd_solve_level3`` available in ``Ansys CFD Enterprise`` product
- ``fluent_meshing`` available in ``Ansys CFD Enterprise`` product

Each increment may be available in other products. The product/increment mapping can be found in the 
`Licensing section of the Ansys Customer Portal <https://download.ansys.com/Installation%20and%20Licensing%20Help%20and%20Tutorials>`_.