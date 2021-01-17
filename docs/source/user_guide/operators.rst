.. _ref_user_guide_operators:

*********
Operators
*********

..    include:: <isonum.txt>

The Operator is the only object used to create and transform the data
and is the fundamental method by which DPF loads, operates on, and
outputs data.  Each operator contain the ``input`` and ``output``
attribute, which allows you to connect various inputs and outputs to
each operator.  Operators can be chained together conduct simple or
complex data processing by attaching one operator's outputs to
another's inputs.  Through lazy evaluation, DPF approaches data
processing in an efficient manner by only evaluating each operator
when the final operator is evaluated and the data is requested.

For example, if you desire the maximum normalized displacement of a
result, you will construct operators in the following order:

``Model`` |rarr| ``Disp Op.`` |rarr| ``Norm Op.`` |rarr| ``Max Op.`` |rarr| Maximum Displacement

With this approach, you can efficiently compute the maximum
displacement of a result entirely within the DPF service without
transferring any data from DPF to Python until DPF arrives at the
solution data you desire.


Creating Operators
~~~~~~~~~~~~~~~~~~
Each operator is created within Python from ``dpf.Operator`` with a
string indicating the operator type.  For a full listing of all
available operators, see the :ref:`ref_dpf_operators_reference`.

For example, to create the displacement operator, use the ``'U'``
string to instantiate one with:

.. code:: python

   >>> import ansys.dpf.core as dpf
   >>> oper = dpf.Operator('U')

The description, available inputs, and available outputs of this
particular operator can be viewed by printing the operator:

.. code:: python

    >>> print(oper)
    DPF "U" Operator

    Description:
    Load the appropriate operator based on the data sources and
    read/compute nodal displacements. Regarding the requested location
    and the input mesh scoping, the result location can be
    Nodal/ElementalNodal/Elemental.

    Available inputs:
     -   mesh_scoping : ScopingsContainer, Scoping, optional
         Mesh entities scoping, unordered_map<int, int> id to index (optional)
         (index is optional, to be set if a user wants the results at a given
         order)

     -   data_sources : DataSources
         If the stream is null then we need to get the file path from the data
         sources

     -   streams_container : StreamsContainer, optional
         Streams (result file container) (optional)

     -   domain_id : int, optional

     -   time_scoping : Scoping, list, optional

     -   bool_rotate_to_global : B, optional
         If true the field is rotated to global coordinate system (default true)

     -   requested_location : str, optional

     -   fields_container : FieldsContainer, optional
         Fields container already allocated modified inplace

     -   mesh : MeshedRegion, optional

    Available outputs:
     -   fields_container


Alternatively, you can output just the available inputs or outputs
with ``print(oper.inputs)`` or ``print(oper.outputs)`` respectively.


Connecting Operators
~~~~~~~~~~~~~~~~~~~~
The displacement operator requires the ``data_sources`` input to
output the ``fields_container`` containing the displacement results.
There are two ways of creating the data source, use the ``dpf.Model``
class, or use the ``dpf.DataSources`` class.  This example will
explain the data sources approach as the model approach is used in several other examples.

.. code:: python

   >>> from ansys.dpf.core import examples
   >>> data_src = dpf.DataSources(examples.multishells_rst)
   >>> print(data_src)
   DPF data_sources with result key: rst
   paths: {'rst': ['/dpf/ansys/dpf/core/examples/model_with_ns.rst']}

Connect this data source to the displacement operator with:

.. code:: python

    >>> oper.inputs.data_sources(data_src)

Evaluating Operators
~~~~~~~~~~~~~~~~~~~~
With all the required inputs assigned, the fields_container can now be
output from the operator with:

.. code:: python

    >>> fc = oper.outputs.fields_container()
    >>> print(fc)
    DPF Field Container with
	1 field(s)
	defined on labels ['time'] 

Please note that the operator checks at run-time if all the required
inputs have been assigned.  Evaluating an operator with missing inputs
will raise a ``DPFServerException``:

.. code:: python

    Purposely not assigning inputs in this example

    >>> new_oper = dpf.Operator('U')
    >>> fc = new_oper.outputs.fields_container()
    Exception: U<-Data sources not defined

See the :ref:`ref_user_guide_fields_container` for the user guide
details regarding the use of the ``FieldsContainer``.


Chaining Operators
~~~~~~~~~~~~~~~~~~
Quite often it is necessary to reduce the results of a given solution
down to a single parameter like maximum stress or displacement.  For
small models, it is acceptable to return the entire data array from
the field and compute its maximum.  Repeating the previous example:

.. code:: python

   Extract the displacement fields container from the multishell
   example.

   >>> from ansys.dpf.core import examples
   >>> data_src = dpf.DataSources(examples.multishells_rst)
   >>> print(data_src)
   >>> oper = dpf.Operator('U')
   >>> oper.inputs.data_sources(data_src)
   >>> fc = oper.outputs.fields_container()

   Compute the maximum displacement of the first field using numpy.
   Note that the data returned is a numpy array.

   >>> disp = fc[0].data
   >>> disp.max(axis=0)
   [0.59428386 0.00201751 0.0006032 ]


For small data sets, it is perfectly acceptable to compute the maximum
of the array in numpy.  Indeed, there are times where it may be
necessary to have the entire data array for a given result type, but
many times it is not strictly necessary.  In those cases, it is faster
to not transfer the array to Python, but rather compute the maximum of
the fields container within DPF and then return the result to Python:

.. code:: python

    Compute the component-wise minimum and maximum over a fields container.

    >>> max_fc_op = dpf.Operator('min_max_fc')
    >>> max_fc_op.inputs.fields_container(fc)
    >>> max_field = max_fc_op.outputs.field_max()
    >>> max_field.data
    array([[0.59428386, 0.00201751, 0.0006032 ]])

Here, the only the maximum displacements in the X, Y, and Z components
were transferred and returned as a numpy array.


API Reference
~~~~~~~~~~~~~
See :ref:`ref_user_guide_fields_container` for a full list of all
available operators within DPF.  For additional details regarding the
operator class itself, see :ref:`ref_api_operators`.
