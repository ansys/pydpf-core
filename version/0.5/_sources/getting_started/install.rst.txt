.. _installation:

*********************
Installation with PIP
*********************
Once Ansys 2021 R2 or later is installed, you can install PyDPF-Core with:

.. code::

   pip install ansys-dpf-core


This installs the latest version of PyDPF-Core and all necessary
dependencies.

To use PyDPF-Core with Ansys 2021 R1, you must install PyDPF-Core with:

.. code::

   pip install ansys-dpf-core<0.3.0

If you are unable to install this module on the host machine due to
network isolation, download the latest or a specific release wheel at `PyDPF-Core
GitHub <https://github.com/pyansys/pydpf-core/releases>`_ or from PyPi at
`PyDPF-Core PyPi <https://pypi.org/project/ansys-dpf-core/>`_


****************************************
Editable Installation (Development Mode)
****************************************

If you want to edit and potentially contribute to the DPF-Core 
module, clone the repository and install it using pip with the ``-e``
development flag:

.. include:: ../pydpf-core_clone_install.rst

