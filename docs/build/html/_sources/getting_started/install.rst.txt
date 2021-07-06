.. _installation:

*********************
Installation with PIP
*********************
Once you've installed Ansys 2021R1 or newer, you can install DPF with:

.. code::

   pip install ansys-dpf-core


This will install the latest version of ``ansys-dpf-core`` and all the
necessary dependencies.

If you are unable to install the module on the host machine due to
network isolation, download the latest release wheel at `DPF-Core
GitHub <https://https://github.com/pyansys/DPF-Core>`_ or from PyPi at
`DPF-Core PyPi <https://pypi.org/project/ansys-dpf-core/>`_


******************************************
Editable Install (Development Mode)
******************************************

If you wish to edit and potentially contribute to the DPF-Core python
module, clone the repository and install it using pip with the ``-e``
development flag.

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


