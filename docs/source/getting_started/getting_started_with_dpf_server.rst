.. _ref_getting_started_with_dpf_server:

.. VERSION - 2023.2.pre0 

===============================
Getting Started with DPF Server
===============================

What is DPF Server
------------------

The Data Processing Framework (DPF) provides numerical simulation users and engineers with a toolbox for accessing and transforming 
simulation data. With DPF, you can perform complex preprocessing or postprocessing of large amounts of simulation data within a 
simulation workflow.

DPF Server is a package that contains all the necessary files to run the DPF Server, enabling DPF capabilities. It is available 
on the Ansys Customer Portal.

For more information about DPF and its use, see `PyDPF-Core documentation <https://dpf.docs.pyansys.com/>`_. 

Installing DPF Server
---------------------

.. _target_to_installing_server:

.. card:: Installing DPF Server step by step
    :text-align: left
	   
    #. Download the ansys_dpf_server_win_v2023.2.pre0.zip or ansys_dpf_server_lin_v<version_to_set>.zip file as appropriate.
    #. Unzip the package.
    #. Change to the root folder (ansys_dpf_server_win_v2023.2.pre0) of the unzipped package. 
    #. In a Python environment, run the following command:
    
    .. code::
    
        pip install -e . 
	
PyDPF-Core and PyDPF-Post python modules can now be used. The instructions to install and get started with PyDPF-Core 
(ansys-dpf-core module) can be found at `Getting Started section <https://dpf.docs.pyansys.com/getting_started/install.html>`_. 

Using DPF Server
----------------

Running the DPF Server
~~~~~~~~~~~~~~~~~~~~~~

On Windows, start the DPF Server by running the Ans.Dpf.Grpc.bat file in the unzipped package.
On Linux, start the DPF Server by running the Ans.Dpf.Grpc.sh file in the unzipped package.

Running the DPF Server in a Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Along with the ansys_dpf_server_lin_v2023.2.pre0.zip archive mentioned in :ref:`Installing DPF Server <target_to_installing_server>`, download the Dockerfile.
2. Copy both the archive and Dockerfile in a folder and navigate into that folder.
3. To build the DPF Docker container, run the following commands:

.. code::

    docker build . -t dpf-core:v2023.2.pre0 --build-arg DPF_VERSION=232 --build-arg DPF_SERVER_FILE=ansys_dpf_server_lin_v2023.2.pre0.zip

4. To run the DPF Docker container, see the :ref:`License terms <target_to_license_terms>` section.

License terms
-------------

DPF User License Agreement 
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _target_to_license_terms:

DPF Server is protected using license terms specified in the DPFUserLicensingAgreement.txt file that 
can be found on the Ansys Customer Portal, along with this file.

To accept the DPF User Licensing Agreement terms, the following environment flag must be set: 

.. code::

    "ANSYS_DPF_ACCEPT_LA=Y"

ANSYS_DPF_ACCEPT_LA confirms your acceptance of the DPF User Licensing Agreement. By passing the value "Y" to the environment variable 
"ANSYS_DPF_ACCEPT_LA", you are expressing that you have a valid and existing license for the edition and version of DPF server you intend to use.

For a DPF Docker container usage, it can be set using:

.. code::

    docker run -e "ANSYS_DPF_ACCEPT_LA=Y" -p 50052:50052 -e DOCKER_SERVER_PORT=50052 --expose=50052 dpf-core:v2023.2.pre0

For any other case, set "ANSYS_DPF_ACCEPT_LA" as an environment variable with "Y" value.

Ansys licensing
~~~~~~~~~~~~~~~

DPF Server is protected by Ansys licensing mechanism.

DPF capabilities are available through the following main services: 
- Entry: load the minimum number of plugins for a basic usage. It is the default. It will only check if an Ansys License is available. 
- Premium: get the specific premium DataProcessingCore.xml to load most plugins with their environments. It will checkout a license. 

The context can be updated by applying a new server context:

.. code::

    dpf.apply_server_context(dpf.AvailableServerContexts.premium)

Setting ANSYSLMD_LICENSE_FILE environment variable to point to the server  might also be needed 
(Example ANSYSLMD_LICENSE_FILE = 1055@my_license_server.ansys.com).

The following Ansys licensing increments currently provide rights to use DPF Server: 

- "preppost" available in Ansys Mechanical Enterprise PrepPost product
- "meba" available in ANSYS Mechanical Enterprise Solver product
- "mech_2" availale in ANSYS Mechanical Premium product
- "mech_1" availale in ANSYS Mechanical Pro product
- "ansys" available in ANSYS Mechanical Enterprise product
- "dynapp" available in ANSYS LS-DYNA PrepPost product
- "vmotion" available in Ansys Motion product
- "acpreppost" available in Ansys Mechanical Enterprise product
- "acdi_adprepost" available in Ansys AUTODYN and Ansys AUTODYN PrepPost products
- "cfd_preppost" available in Ansys CFD Enterprise product
- "cfd_preppost_pro" available in Ansys CFD Enterprise product
- "vmotion_post" available in Ansys Motion Post product
- "vmotion_pre" available in Ansys Motion Pre product
- "advanced_meshing" available in Ansys CFD Enterprise product
- "fluent_meshing_pro" available in Ansys CFD Enterprise product
- "fluent_setup_post" available in Ansys CFD Enterprise product
- "fluent_setup_post_pro" available in Ansys CFD Enterprise product
- "acfx_pre" available in Ansys CFD Enterprise product
- "cfd_base" available in Ansys CFD Enterprise product
- "cfd_solve_level1" available in Ansys CFD Enterprise product
- "cfd_solve_level2" available in Ansys CFD Enterprise product
- "cfd_solve_level3" available in Ansys CFD Enterprise product
- "fluent_meshing" available in Ansys CFD Enterprise product

Each increment might be available in other products. The Product/Increment mapping can be found at
`Licensing section of Ansys Customer Portal <https://download.ansys.com/Installation%20and%20Licensing%20Help%20and%20Tutorials>`_. 