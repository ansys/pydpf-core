.. _installation:

************
Installation
************

Install using ``pip``
---------------------

`pip <https://pypi.org/project/pip/>`_ is the package installer for Python.

To use PyDPF-Core with Ansys 2021 R2 or later, install a 0.2.* PyDPF-Core
version with:

.. code::

   pip install ansys-dpf-core<0.3.0


To use PyDPF-Core with Ansys 2021 R1, install the latest version
with:

.. code::

   pip install ansys-dpf-core<0.3.0


Install using a wheel file
--------------------------

If you are unable to install PyDPF-Post on the host machine due to
network isolation, download the latest wheel file from `PyDPF-Post
GitHub <https://github.com/pyansys/pydpf-post>`_ or
`PyDPF-Post PyPi <https://pypi.org/project/ansys-dpf-post/>`_.


Install in development mode
---------------------------

If you want to edit and potentially contribute to PyDPF-Core,
clone the repository and install it using ``pip`` with the ``-e``
development flag:

.. include:: ../pydpf-post_clone_install.rst
