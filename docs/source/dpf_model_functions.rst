.. _dpf_model_functions_ref:

PyANSYS DPF Documentation
=========================
This is a basic draft of the source documentation.  It is meant to be
paired with live Jupyterlab notebooks and is for reference only.


Model Class
-----------
The model class encapsulates several operators and methods and is used to streamline reading and plotting result files.

.. autoclass:: ansys.dpf.core.Model
    :members:
    :private-members:


Operator Class
--------------
The ``dpf.Operator`` class used to represent an Operator which is an
elementary operation.

.. autoclass:: ansys.dpf.core.Operator
    :members:


FieldsContainer Class
---------------------
.. autoclass:: ansys.dpf.core.FieldsContainer
    :members:


Field Class
-----------
.. autoclass:: ansys.dpf.core.Field
    :members:


Wrapped Operators
-----------------
These operators are available as functions from ``dpf.operators`` and simplify the creation of new chained operators.

.. automodule:: ansys.dpf.core.operators
    :members:
