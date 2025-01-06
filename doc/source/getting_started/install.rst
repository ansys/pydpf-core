.. _installation:

************
Installation
************

Install using ``pip``
---------------------

The standard package installer for Python is `pip <https://pypi.org/project/pip/>`_.

To use PyDPF-Core with Ansys 2022 R2 or later, install the latest version
with this command:

.. code::

   pip install ansys-dpf-core

PyDPF-Core plotting capabilities require you to have `PyVista <https://pyvista.org/>`_ installed.
To install PyDPF-Core with its optional plotting functionalities, use:

.. code::

   pip install ansys-dpf-core[plotting]

For more information about PyDPF-Core plotting capabilities, see :ref:`user_guide_plotting`.

To use PyDPF-Core with Ansys 2022 R1, install the latest compatible version
with this command:

.. code::

   pip install ansys-dpf-core<0.10.0

To use PyDPF-Core with Ansys 2021 R2, install the latest compatible version
with this command:

.. code::

   pip install ansys-grpc-dpf<0.4.0; pip install ansys-dpf-core<0.10.0

To use PyDPF-Core with Ansys 2021 R1, install the latest compatible version
with this command:

.. code::

   pip install ansys-grpc-dpf<0.3.0; pip install ansys-dpf-core<0.3.0


Install without internet
------------------------

If you are unable to install PyDPF-Core on the host machine using ``pip`` due to
network isolation, download the wheelhouse corresponding to your platform and Python interpreter version
for the latest release of PyDPF-Core from the assets section of the `latest PyDPF-Core release on GitHub <https://github.com/ansys/pydpf-core/releases/latest>`_.

The wheelhouse is a ZIP file containing Python wheels for all the packages PyDPF-Core requires to run.
To install PyDPF-Core using the downloaded wheelhouse, unzip the wheelhouse to a local directory,
then use the following command from within this local directory:

.. code::

   pip install --no-index --find-links=. ansys-dpf-core

Note that PyDPF-Core wheelhouses do not include the optional plotting dependencies.
To use the plotting capabilities, also download the wheels corresponding to your platform and Python interpreter version
for `PyVista <https://pypi.org/project/pyvista/#files>`_ and 
`matplotlib <https://pypi.org/project/matplotlib/#files>`_, then place them in the same previous local directory and run the command above.


Install in development mode
---------------------------

If you want to edit and potentially contribute to PyDPF-Core,
clone the repository and install it using ``pip`` with the ``-e``
development flag:

.. include:: ../pydpf-core_clone_install.rst


.. _target_to_install_with_plotting_capabilities:


Check the installation
----------------------

Run the following Python code to verify your PyDPF-Core installation:

.. code::

   from ansys.dpf.core import Model
   from ansys.dpf.core import examples
   model = Model(examples.find_simple_bar())
   print(model)