.. _dpf_model_functions_ref:

=============
API Reference
=============
Details of the DPF API.

.. toctree::
   :maxdepth: 2
   :hidden:
   
   operators


Model Class
-----------
The model class encapsulates several operators and methods and is used to streamline reading and plotting result files.

.. autoclass:: ansys.dpf.core.model.Model
    :members:
    :private-members:


Operator Class
--------------
The ``dpf.Operator`` class used to represent an Operator which is an
elementary operation.

.. autoclass:: ansys.dpf.core.dpf_operator.Operator
    :members:


FieldsContainer Class
---------------------
.. autoclass:: ansys.dpf.core.fields_container.FieldsContainer
    :members:


Field Class
-----------
.. autoclass:: ansys.dpf.core.field.Field
    :members:


Wrapped Operators
-----------------
These operators are available as functions from ``dpf.operators`` and
simplify the creation of new chained operators.

 .. automodule:: ansys.dpf.core.operators_helper
    :members:


..
   Plotting
   --------
   The ``ansys.dpf.plotting`` module contains several plotting functions to simplify the creation of plots within Jupyter notebooks.

   .. automodule:: ansys.dpf.plotting
       :members:


MeshedRegion Class
------------------
.. autoclass:: ansys.dpf.core.meshed_region.MeshedRegion
    :members:
    :noindex: elements


Elements Class
--------------
.. autoclass:: ansys.dpf.core.meshed_region.Elements
    :members:


Element Class
--------------
.. autoclass:: ansys.dpf.core.meshed_region.Element
    :members:
