.. _installation:

*********************
Installation with PIP
*********************
Once Ansys 2021 R1 or later is installed, you can install 
PyDPF-Core with:

.. code::

   pip install ansys-dpf-core


This installs the latest version of PyDPF-Core and all necessary 
dependencies.

If you are unable to install this module on the host machine due to
network isolation, download the latest release wheel at `pydpf-core
on GitHub <https://github.com/pyansys/DPF-Core>`_ or from
`ansys-dpf-core on PyPi <https://pypi.org/project/ansys-dpf-core/>`_.


****************************************
Editable Installation (Development Mode)
****************************************

If you want to edit and potentially contribute to PyDPF-Core, clone
the repository and install it using pip with the ``-e``
development flag:

.. code::

    git clone https://github.com/pyansys/DPF-Core
    cd DPF-Core
    pip install -e .

