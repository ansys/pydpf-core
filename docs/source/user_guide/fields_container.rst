.. _ref_user_guide_fields_container:

***************************
Fields Container and Fields
***************************

Results are more than the data comprising the results itself, and to
track the units, associated mesh, and nodes or elements numbers
associated with the data, DPF uses the
:py:class:`ansys.dpf.core.field.Field` class.  For example, the volume
field for the ``examples.simple_bar`` example result is:

.. code:: python

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.simple_bar)
    >>> vol_op = model.results.volume()
    >>> field = vol_op.outputs.fields_container()[0]
    DPF elemental_volume_1.s Field
        Location:   Elemental
        Unit:       m^3
        Num. id(s): 3000
        Shape:      3000

The field contains the metadata associated with the result its
returning, including the location (either elemental, nodal, or
elemental nodal) and ids associated with that location.

.. code:: python

    >>> field.scoping.ids
    [141,
     441,
     741,
     1041,
     ...]

