.. _ref_getting_started_with_dpf_server:

.. VERSION - <2023.2.pre0> 

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

#. Download the ansys_dpf_server_win_v2023.2.pre0.zip or ansys_dpf_server_lin_v2023.2.pre0.zip file as appropriate.
#. Unzip the package.

Using DPF Server
----------------

Using PyDPF-Core and PyDPF-Post clients with DPF Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyDPF-Core and PyDPF-Post are python clients relying on a DPF Server. 
The instructions to install and get started with PyDPF-Core (ansys-dpf-core module) can be found 
at `Getting Started section <https://dpf.docs.pyansys.com/getting_started/install.html>`_. 

Starting Python environment, set ANSYS_DPF_PATH environment variable to use DPF Server:

.. code::

    import os
    os.environ["ANSYS_DPF_PATH"] = r"D:\ansys_dpf_server\v232" # path to DPF Server root

PyDPF-Core and PyDPF-Post python modules can now be used.

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
Setting ANSYSLMD_LICENSE_FILE environment variable might also be needed.