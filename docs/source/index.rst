==========
PyDPF-Core
==========

PyDPF-Core is part of the larger `PyAnsys <https://docs.pyansys.com>`_
effort to facilitate the use of Ansys technologies directly from
Python. Its primary package, ``ansys.dpf.core``, provides a Python
interface to the powerful Data Processing Framework (DPF), enabling
rapid postprocessing of a variety of Ansys file formats and physics
solutions without ever leaving the Python environment.

Background
~~~~~~~~~~
DPF provides numerical simulation engineers with a toolbox for
accessing and transforming simulation data. DPF can access data from
solver result files as well as several neutral formats, such as CSV,
HDF5, and VTK. Various operators provide for the manipulation and
transformation of the data.

DPF is a workflow-based framework that allows simple and complex
evaluations by chaining operators. The data in DPF is defined based on
physics-agnostic mathematical quantities described in self-sufficient 
entities called fields. This allows DPF to be a modular and easy-to-use 
tool with a large range of capabilities. It is designed to handle 
large amounts of data.

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

- Data represented as a ``field``
- An ``operator`` to act upon this data 

Each DPF capability is developed through operators that allow for 
componentization of the framework. Because DPF is plugin-based, new 
features or formats can be easily added.


.. autosummary::
   :toctree: _autosummary

   getting_started/index
   user_guide/index
   api/index
   operator_reference
   examples/index
   contributing
   
   *.ipynb
