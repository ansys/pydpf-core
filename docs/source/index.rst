================
PyANSYS DPF-Core
================

The Data Processing Framework (DPF) is designed to provide numerical
simulation users/engineers with a toolbox for accessing and
transforming simulation data. DPF can access data from solver result
files as well as several neutral formats (csv, hdf5, vtk,
etc.). Various operators are available allowing the manipulation and
the transformation of this data.

DPF is a workflow-based framework which allows simple and/or complex
evaluations by chaining operators. The data in DPF is defined based on
physics agnostic mathematical quantities described in a
self-sufficient entity called field. This allows DPF to be a modular
and easy to use tool with a large range of capabilities. It's a
product designed to handle large amount of data.

The Python ``ansys.dpf.core`` module provides a Python interface to
the powerful DPF framework enabling rapid post-processing of a variety
of Ansys file formats and physics solutions without ever leaving a
Python environment.  


Brief Demo
~~~~~~~~~~
Opening a result file generated from Ansys workbench or MAPDL is as easy as:

.. code:: python

    >>> from ansys.dpf.core import Model
    >>> model = Model('file.rst')
    >>> print(model)
    DPF Model
    ------------------------------
    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mecanic
    Available results:
         -  displacement
         -  element_nodal_forces
         -  volume
         -  energy_stiffness_matrix
         -  hourglass_energy
         -  thermal_dissipation_energy
         -  kinetic_energy
         -  co_energy
         -  incremental_energy
         -  temperature

See the :ref:`gallery` for detailed examples.


Key Features
~~~~~~~~~~~~

**Computation Efficiency**

DPF is a modern framework and it has been developed by taking advantages of new hardware architectures. Thanks to continued development, new capabilities are frequently added.

**Generic Interface**

DPF is physic agnostic. Thus, its use is not limited to a particular field, physics solution, or file format.

**Extensibility and Customization**

DPF is developed around a two core entities: data represented as a
``field``, and the ``operator`` to act upon that data. Each DPF
capability is developed through operators which allows for a
componentization of the framework. DPF is also plugin based, allowing
new features or new formats to be easily added within the operators
framework.


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting_started/index
   user_guide/index
   api/index
   examples/index
   contributing
   woa
