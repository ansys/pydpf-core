.. _ref_user_guide_fields_container:

***************************
Fields Container and Fields
***************************
Where DPF uses :ref:`ref_user_guide_operators` to load operate and operate
on the data, DPF uses ``Field`` and ``FieldsContainer`` to store
the data and return it to the user.  In other words, if ``Operators``
was a verb, the DPF ``Field`` would be the noun.  ``Operators`` acts
on the data, and ``Field`` and ``FieldsContainer`` hold the data.


Obtaining Fields and FieldsContainer
------------------------------------
The ``outputs`` from ``Operators`` can be either a
:py:class:`ansys.dpf.core.field.Field` or
:py:class:`ansys.dpf.core.fields_container.FieldsContainer`.  A Fields
Container is the DPF equivalent of a ``list`` of ``Field``, and is
used to hold a vector of fields within DPF.  In the following the
example, the ``FieldsContainer`` is returned from the volume operator:

.. code:: python

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.simple_bar)
    >>> vol_op = model.results.volume()
    >>> fields = vol_op.outputs.fields_container()
    >>> print(fields)
    DPF Field Container with
    	1 field(s)
	defined on labels ['time'] 


Accessing Fields within a Fields Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Since this result contains a single static result, the
``FieldsContainer`` only contains a single Field.  Access the fields
from the ``FieldsContainer`` using the following methods:

.. code:: python

    >>> len(fields)
    1

    Return a field based on its index

    >>> field = fields[0]

    Return a field based on its time

    >>> field = fields.get_fields_by_time_complex_ids(1)

    Alternatively, use ``get_fields`` with the scoping of the
    requested fields or the index of the field.

    >>> field = fields.get_fields({'time': 1}, {'complex':0})

    Reference the available time frequency support to determine which
    ``time_complex_ids`` are available to in the ``FieldsContainer``

    >>> print(fields.time_freq_support)
    Time/Frequency Info:
	Number of sets: 1

    With complex values

     Cumulative      Time (s)       Loadstep     Substep   
         1             1.0             1            1

    Use ``get_ids`` to get the available IDs of a ``FieldsContainer``.

    >>> fields.get_ids()
    [1]

Note that these results come from MAPDL and are FORTRAN indexed
(i.e. 1 based).  When indexing from pythonic indexing via
``fields[0]``, you can use zero based indexing.  When requesting the
results via ``get_fields``, the request is based on the time scoping
IDs from MAPDL.

Field
-----
The :py:class:`ansys.dpf.core.field.Field` is the fundamental unit of data within DPF and contains the scoping, units associated with the result, and other metadata associated with the data.  Continuing the previous example, the Field returned from the ``FieldsContainer`` is:

.. code:: python

    >>> field = fields[0]
    >>> print(field)
    DPF elemental_volume_1.s Field
        Location:   Elemental
        Unit:       m^3
        Num. id(s): 3000
        Shape:      3000

Note that by printing the field you can get an overview of the field's
metadata.  The next section provides an overview of the metadata associated with the field itself.


Field Metadata
~~~~~~~~~~~~~~
The field contains the metadata associated with the result it is
associated with, including the location (either ``Elemental``, ``Nodal``, or
``ElementalNodal``) and IDs associated with that location.  To access the
scoping of the field, use the ``scoping`` attribute:

.. code:: python

    >>> print(field.scoping)
    DPF Scoping Object
    Size: 3000
    Location: Elemental

    Element numbers associated with the field.

    >>> field.scoping.ids
    [141,
     441,
     741,
     1041,
     ...]

Note that ``Elemental`` denotes one value (multiplied by the number of
components) of data per element, ``Nodal`` is per node, and
``ElementalNodal`` is one value per node per element.  For example,
strain is a ``ElementalNodal`` value as the strain is evaluated at
each node for each element.

The field also contains additional metadata such as the ``shape`` of
the data stored, the location of the field, number of components, and
the units of the data,

.. code:: python

    Units of the field describing volume

    >>> field.unit
    'm^3'

    Elemental, nodal, or nodal element "location" of the field

    >>> field.location
    'Elemental'

    Number of components associated with the field.  It's expected to
    be have a single dimension since there can only be one volume per
    element.

    >>> field.component_count
    1


Field Data
----------

Accessing Field Data
~~~~~~~~~~~~~~~~~~~~
When DPF-Core returns a :py:class:`ansys.dpf.core.field.Field`, what
Python actually has is a client side representation of the Field, but
not the entirety of the field itself.  This means that all the data of
the field is stored within the DPF service.  This is important because
when building your post-processing workflows, keep in mind that the
most efficient way of interacting with the result data is to minimize
the exchange of data between Python and DPF, either by using operators
or by accessing only the data that is needed.

Should you need to access the entire array of data, you can request
the data be returned as a ``numpy`` array with:

.. code:: python

    >>> array = field.data
    >>> array
    array([0.001, 0.001, 0.001, ..., 0.001, 0.001, 0.001])

    Note that this array is a genuine, local, numpy array

    >>> type(array)
    numpy.ndarray

Should you need to request data individual node or element, you can
request it using either ``get_entity_data`` or
``get_entity_data_by_id``.

.. code:: python

    Get the data from the first element in the field.

    >>> field.get_entity_data(0)

    Get the data for the element with the ID 10

    >>> field.get_entity_data_by_id(10)
    array([0.001])

    Note that this would correspond to an index of 1490 within the
    field.  Be aware that scoping IDs are not sequential.  The index
    of Element 1490 in the field can be obtained by:

    >>> field.scoping.ids.index(10)
    1490


These methods are acceptable when requesting data for a few elements
or nodes, but should not be used when looping over the entire array.
It is more efficient to use numpy vectorized operations.  For example,
the sorted element IDs and field data can be obtained with:

.. code:: python

    Sort the scoping indices and get the sorting indices

    >>> import numpy as np
    >>> element_ids = np.array(field.scoping.ids)
    >>> sidx = np.argsort(element_ids)
    >>> element_ids = element_ids[sidx]
    array([   1,    2,    3, ..., 2998, 2999, 3000])

    Now sort the element data

    >>> sorted_data = field.data[sidx]
    >>> sorted_data
    array([0.001, 0.001, 0.001, ..., 0.001, 0.001, 0.001])


Operating on Field Data
~~~~~~~~~~~~~~~~~~~~~~~
Often times, it's not necessary to directly act upon the data of an
array within Python.  For example, if you want to know the maximum of
the data, you could potentially compute the maximum of the array from
``numpy`` with ``array.max()``, but that requires sending the entire
array to Python and then computing the maximum there.  Rather than
copying the array over and then computing the maximum in Python, you
can instead compute the maximum directly from the field itself.  The
``min`` and ``max`` methods of ``Field`` use the ``'min_max'``
Operator was used to compute the maximum of the field while returning
the field.

.. code:: python

    Compute the maximum of the field within DPF and return the result
    a numpy array

    >>> max_field = field.max()
    >>> max_field.data
    array([0.001])

    Get the element or node ID of the maximum value.

    >>> max_field.scoping.ids
    [2168]


Note that is a convenience method.  For more advanced operator
chaining, please see the :ref:`ref_user_guide_operators` section in
the user guide.  Here is a quick example of connecting the
``'entity_average'`` operator to the field data:

.. code:: python

   Compute the average of a field using the 'entity_average' operator.

    >>> avg_op = dpf.Operator('entity_average')
    >>> avg_op.inputs.connect(max_field)
    >>> avg_field = avg_op.outputs.field()
    >>> avg_field.data[0]
    0.001


Further Reference
-----------------
See the API reference at :ref:`ref_api_fields_container` and
:ref:`ref_api_field`.
