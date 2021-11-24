.. _installation:

*********************
Installation with PIP
*********************
Once Ansys 2021 R1 or later is installed, you can install the 
DPF-Core module with:

.. code::

   pip install ansys-dpf-core


This installs the latest version of DPF-Core and all necessary 
dependencies.

If you are unable to install this module on the host machine due to
network isolation, download the latest release wheel at `DPF-Core
GitHub <https://https://github.com/pyansys/DPF-Core>`_ or from PyPi at
`DPF-Core PyPi <https://pypi.org/project/ansys-dpf-core/>`_


****************************************
Editable Installation (Development Mode)
****************************************

If you want to edit and potentially contribute to the DPF-Core 
module, clone the repository and install it using pip with the ``-e``
development flag:

.. code::

    git clone https://tfs.ansys.com:8443/tfs/ANSYS_Development/DPF/_git/dpf-python-core
    cd dpf-python-core
    pip install -e . --extra-index-url http://canartifactory.ansys.com:8080/artifactory/api/pypi/pypi/simple --trusted-host canartifactory.ansys.com


************************************************************************************
Get started as Ansys internal consumer (Internal Development Mode)
************************************************************************************

To install all dpf python modules and requirements from the Ansys internal pypi, run: 

.. code::

	pip install ansys-dpf-core --extra-index-url http://canartifactory.ansys.com:8080/artifactory/api/pypi/pypi/simple --trusted-host canartifactory.ansys.com


