================
PyAnsys DPF-Core
================

DPF (Data Processing Framework) provides numerical
simulation engineers with a toolbox for accessing and
transforming simulation data. DPF can access data from solver result
files as well as several neutral formats, such as CSV, HDF5, and VTK. 
Various operators provide for the manipulation and transformation 
of the data.

DPF is a workflow-based framework that allows simple and complex
evaluations by chaining operators. The data in DPF is defined based on
physics-agnostic mathematical quantities described in self-sufficient 
entities called fields. This allows DPF to be a modular and easy-to-use 
tool with a large range of capabilities. It is designed to handle 
large amounts of data.

The module `ansys.dpf.core` provides a Python interface to
the powerful DPF framework, enabling rapid postprocessing of a variety
of Ansys file formats and physics solutions without ever leaving the
Python environment.  


Brief Demo
~~~~~~~~~~

.. include:: _static/simple_example.rst

See the :ref:`gallery` for detailed examples.


Key Features
~~~~~~~~~~~~

**Computation Efficiency**

DPF is a modern framework based on new hardware architectures. 
Thanks to continued development, new capabilities are frequently added.

**Generic Interface**

DPF is physics-agnostic, which means that its use is not limited to a 
particular field, physics solution, or file format.

**Extensibility and Customization**

DPF is developed around two core entities: 

* Data represented as a ``field``
* An ``operator`` to act upon this data 

Each DPF capability is developed through operators that allow for 
componentization of the framework. Because DPF is plugin-based, new 
features or formats can be easily added.


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting_started/index
   user_guide/index
   api/index
   operator_reference
   examples/index
   contributing
   
   *.ipynb
