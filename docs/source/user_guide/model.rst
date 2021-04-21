.. _user_guide_model:

*************
The DPF Model
*************

The DPF model is the basic starting point for opening a file through
DPF.  From here you can connect various operators and display results
and data from the result file.

To create a ``Model`` instance, import ``dpf`` and load a file.  The
path provided must be an absolute path or a path relative to the DPF
server.

.. code:: python

    >>> from ansys.dpf import core as dpf
    >>> model = dpf.Model('C:/Users/user/file.rst')

    Linux path

    >>> model = dpf.Model('/home/user/file.rst')


For a full example using the model, see :ref:`ref_basic_example`.


Model Results
-------------
The model contains the ``results`` attribute, which you can use to
create operators to access certain results.  To view the available
results, print them with ``print(model.results)``.

.. autoattribute:: ansys.dpf.core.model.Model.results
  :noindex:


Model Metadata
--------------
The metadata of the model can be used to get a variety of values not
directly related to the results of the model.  For example, you can
get the analysis type with:

.. code:: python

    >>> model.metadata.result_info.analysis_type
    'static'

Or, you can get the field containing the nodal coordinates with:

.. code:: python

    >>> nodes = model.metadata.meshed_region.nodes
    >>> print(nodes.coordinates_field)
    DPF  Field
        Location:   Nodal
        Unit:       m
        Num. id(s): 3820
        Shape:      (3820, 3)

.. autoattribute:: ansys.dpf.core.model.Model.metadata
  :noindex:
