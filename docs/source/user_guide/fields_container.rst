.. _ref_user_guide_fields_container:

==============================
Fields Container and Fields
==============================
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
example, the ``FieldsContainer`` is returned from the elastic_strain operator:

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    model = dpf.Model(examples.msup_transient)
    epel = model.results.elastic_strain.on_all_time_freqs
    fields = epel.eval()
    print(fields)
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPF elastic_strain(s)Fields Container
      with 20 field(s)
      defined on labels: time 
    
      with:
      - field 0 {time:  1} with ElementalNodal location, 6 components and 40 entities.
      - field 1 {time:  2} with ElementalNodal location, 6 components and 40 entities.
      - field 2 {time:  3} with ElementalNodal location, 6 components and 40 entities.
      - field 3 {time:  4} with ElementalNodal location, 6 components and 40 entities.
      - field 4 {time:  5} with ElementalNodal location, 6 components and 40 entities.
      - field 5 {time:  6} with ElementalNodal location, 6 components and 40 entities.
      - field 6 {time:  7} with ElementalNodal location, 6 components and 40 entities.
      - field 7 {time:  8} with ElementalNodal location, 6 components and 40 entities.
      - field 8 {time:  9} with ElementalNodal location, 6 components and 40 entities.
      - field 9 {time:  10} with ElementalNodal location, 6 components and 40 entities.
      - field 10 {time:  11} with ElementalNodal location, 6 components and 40 entities.
      - field 11 {time:  12} with ElementalNodal location, 6 components and 40 entities.
      - field 12 {time:  13} with ElementalNodal location, 6 components and 40 entities.
      - field 13 {time:  14} with ElementalNodal location, 6 components and 40 entities.
      - field 14 {time:  15} with ElementalNodal location, 6 components and 40 entities.
      - field 15 {time:  16} with ElementalNodal location, 6 components and 40 entities.
      - field 16 {time:  17} with ElementalNodal location, 6 components and 40 entities.
      - field 17 {time:  18} with ElementalNodal location, 6 components and 40 entities.
      - field 18 {time:  19} with ElementalNodal location, 6 components and 40 entities.
      - field 19 {time:  20} with ElementalNodal location, 6 components and 40 entities.


Accessing Fields within a Fields Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Since this result contains a transient result, the
``FieldsContainer`` has one Field by time set.  Access the fields
from the ``FieldsContainer`` using the following methods:

.. code-block:: python

    len(fields)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    20
    
Return a field based on its index

.. code-block:: python

    field_first_time = fields[0]
    field_last_time = fields[19]

Return a field based on its time set id:

.. code-block:: python

    field = fields.get_field_by_time_id(1)

Alternatively, use ``get_field`` with the identifier of 
the requested field. This API allows to access fields for more complex
requests. To use ``get_field`` in the same context:

.. code-block:: python
    
    field = fields.get_field({'time': 1})
    print(field)
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
     DPF elastic_strain_0.01s Field
      Location: ElementalNodal
      Unit: 
      40 entities 
      Data:6 components and 320 elementary data 
      
Or in a more complex context, where the ``get_field`` method has a real use compared
to the ``get_field_by_time_id`` method:


.. code-block:: python

    model = dpf.Model(examples.download_all_kinds_of_complexity())
    epel = model.results.elastic_strain.on_all_time_freqs.split_by_shape
    fields = epel.eval()
    field = fields.get_field({'time': 1, 'elshape':0})
    print(field)
    
    field = fields.get_field({'time': 1, 'elshape':1})
    print(field)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
     DPF elastic_strain_1.s_elshape:0 Field
      Location: ElementalNodal
      Unit: 
      203 entities 
      Data:6 components and 2436 elementary data 
      
     DPF elastic_strain_1.s_elshape:1 Field
      Location: ElementalNodal
      Unit: 
      9052 entities 
      Data:6 components and 37580 elementary data 
 

Reference the available time frequency support to determine which
``time_complex_ids`` are available to in the ``FieldsContainer``

.. code-block:: python

    model = dpf.Model(examples.msup_transient)
    epel = model.results.elastic_strain.on_all_time_freqs
    fields = epel.eval()
    print(fields.time_freq_support)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPF  Time/Freq Support: 
      Number of sets: 20 
    Cumulative     Time (s)       LoadStep       Substep         
    1              0.010000       1              1               
    2              0.020000       1              2               
    3              0.030000       1              3               
    4              0.040000       1              4               
    5              0.050000       1              5               
    6              0.060000       1              6               
    7              0.070000       1              7               
    8              0.080000       1              8               
    9              0.090000       1              9               
    10             0.100000       1              10              
    11             0.110000       1              11              
    12             0.120000       1              12              
    13             0.130000       1              13              
    14             0.140000       1              14              
    15             0.150000       1              15              
    16             0.160000       1              16              
    17             0.170000       1              17              
    18             0.180000       1              18              
    19             0.190000       1              19              
    20             0.200000       1              20              

Note that the time set ids used are 1 based.  When indexing from pythonic indexing via
``fields[0]``, you can use zero based indexing.  When requesting the
results via ``get_fields``, the request is based on the time scoping set ids.

Field
-----
The :py:class:`ansys.dpf.core.field.Field` is the fundamental unit of data within DPF.
It contains the actual data and its metadata:
results data are defined by values associated to entities (scoping), and these entities are a subset of a model (support). 
In DPF, field data is always associated to its scoping and support, making the field a self-describing piece of data. 
A field is also defined by its dimensionnality, unit, location...

.. code-block:: python

    field = fields[0]
    print(field)


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
   DPF elastic_strain_0.01s Field
      Location: ElementalNodal
      Unit: 
      40 entities 
      Data:6 components and 320 elementary data 

Note that by printing the field you can get an overview of the field's
metadata.  The next section provides an overview of the metadata associated with the field itself.


Field Metadata
~~~~~~~~~~~~~~
The field contains the metadata associated with the result it is
associated with, including the location (either ``Elemental``, ``Nodal``,
``ElementalNodal``, ...) and IDs associated with that location.  To access the
scoping of the field, use the ``scoping`` attribute:

.. code:: python

    >>> print(field.scoping)
    >>> print('field.scoping.ids:', field.scoping.ids)
    >>> print('field.location:', field.location)


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPF  Scoping: 
      with Elemental location and 40 entities

   field.scoping.ids: [21,
     22,
     23,
     24,
     25,
     26,
     ...
     ]
     
     field.location:'ElementalNodal'


Note that ``Elemental`` denotes one value (multiplied by the number of
components) of data per element, ``Nodal`` is per node, and
``ElementalNodal`` is one value per node per element.  For example,
strain is a ``ElementalNodal`` value as the strain is evaluated at
each node for each element.

The field also contains additional metadata such as the ``shape`` of
the data stored, the location of the field, number of components, and
the units of the data,

    
.. code:: python

    >>> stress = model.results.stress
    >>> field = stress.eval()[0]

    Units of the field describing volume
    
    >>> field.unit
    
    
    Elemental, elemental nodal, or nodal element "location" of the field

    >>> field.location

    Number of components associated with the field.  It's expected to
    be have a single dimension since there can only be one volume per
    element.

    >>> field.component_count



.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
     'Pa'
     'ElementalNodal'
     6


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
    array([[ 4.01372930e+04,  3.85071930e+02, -1.40019130e+07,
         7.48472351e+02, -2.60259531e+04, -2.62856938e+05],
       [-1.19228638e+03, -6.18210815e+02, -1.39912700e+07,
         2.61468994e+03, -1.31871719e+05, -2.59527125e+05],
       [ 9.02558960e+02,  5.63793152e+02, -1.17102740e+07,
        -8.99381836e+02, -1.21302727e+05, -2.45666328e+05],
       ...,
       [-3.99694531e+04,  1.44622528e+02,  9.62343100e+06,
        -7.09812073e+02, -2.26106621e+04, -2.23155891e+05],
       [-4.31104401e+02, -2.67612732e+02,  9.60954800e+06,
         1.93208755e+02, -1.11580734e+05, -2.24406062e+05],
       [ 5.56899536e+02,  3.88515320e+02,  1.17119880e+07,
        -1.68983887e+03, -1.21768023e+05, -2.41346125e+05]])

    This array has 6 components by elementary data (symmetrical tensor XX,YY,ZZ,XY,YZ,XZ)
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
    array([[ 4.99232031e+04,  1.93570602e+02, -3.08514075e+06,
        -5.48255615e+02, -1.37476562e+04,  1.34827719e+05],
       [ 5.23090469e+04, -1.87847885e+02, -1.98004588e+06,
        -1.12942969e+03, -1.11147285e+04,  1.09223398e+05],
       [-4.90510511e+00, -1.16425255e+02, -1.96296662e+06,
        -5.48878540e+02, -5.48524844e+04,  1.09255164e+05],
       [ 2.63994884e+01,  1.50431015e+02, -3.06906050e+06,
        -1.17046680e+03, -6.76924219e+04,  1.34773391e+05],
       [-4.99232031e+04, -1.93571167e+02,  3.08514075e+06,
        -5.48256836e+02, -1.37476562e+04, -1.34827719e+05],
       [-5.23090469e+04,  1.87848083e+02,  1.98004588e+06,
        -1.12943201e+03, -1.11147295e+04, -1.09223398e+05],
       [ 4.90471840e+00,  1.16423714e+02,  1.96296662e+06,
        -5.48877380e+02, -5.48524844e+04, -1.09255164e+05],
       [-2.63994102e+01, -1.50429443e+02,  3.06906050e+06,
        -1.17046619e+03, -6.76924219e+04, -1.34773391e+05]])

    Note that this would correspond to an index of 29 within the
    field.  Be aware that scoping IDs are not sequential.  The index
    of Element 29 in the field can be obtained by:

    >>> field.scoping.ids.index(10)
    29
    
    Here the data of element of id 10 is made of 8 symmetrical tensor, indeed
    the elastic strain has one tensor value by node by element (``ElementalNodal`` location)
    
    For a displacement on node 3, we have :
    >>> disp = model.results.displacement.eval()[0]
    >>> disp.get_entity_data_by_id(3)
    array([[8.06571808e-14, 4.03580652e-04, 2.61804706e-05]])
    
    One 3D vector (X,Y,Z) displacement

These methods are acceptable when requesting data for a few elements
or nodes, but should not be used when looping over the entire array.
Field's data can be recovered locally before sending a large number of requests
for efficiency purpose:

.. code-block:: python

    with field.as_local_field() as f:
        for i in range(1,100):
            f.get_entity_data_by_id(i)


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
    array([0.12492393, 0.06738043, 0.05854268, 0.05807593, 0.08250141,
       0.2068032 ])

    Get the element or node ID of the maximum value.

    >>> max_field.scoping.ids
    [369, 1073, 1031, 1040, 2909, 2909]


Note that is a convenience method.  For more advanced operator
chaining, please see the :ref:`ref_user_guide_operators` section in
the user guide.  Here is a quick example of connecting the
``'elemental_mean'`` operator to the field data:


Compute the average of a field using the 'elemental_mean' operator:

.. code-block:: python

    from ansys.dpf.core import operators as ops
    avg_op = ops.averaging.elemental_mean(field)
    avg_field = avg_op.outputs.field()
    print(avg_field.get_entity_data(0))
    print(avg_field.location)


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    [[ 4.65393066e-04 -2.47955322e-05  0.00000000e+00  7.68026390e+02
      -7.59655688e+04  0.00000000e+00]]  
    Elemental
    
 

API Reference
~~~~~~~~~~~~~
See the API reference at :ref:`ref_fields_container` and
:ref:`ref_field`.
