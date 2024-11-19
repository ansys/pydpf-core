.. _ref_basic_math:

===========
Basic maths
===========

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |Fields| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`
.. |FieldsContainers| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`
.. |add| replace:: :class:`add<ansys.dpf.core.operators.math.add.add>`
.. |add_fc| replace:: :class:`add_fc<ansys.dpf.core.operators.math.add_fc.add_fc>`
.. |minus| replace:: :class:`minus<ansys.dpf.core.operators.math.minus.minus>`
.. |minus_fc| replace:: :class:`minus_fc<ansys.dpf.core.operators.math.minus_fc.minus_fc>`
.. |accumulate| replace:: :class:`accumulate<ansys.dpf.core.operators.math.accumulate.accumulate>`
.. |accumulate_fc| replace:: :class:`accumulate_fc<ansys.dpf.core.operators.math.accumulate_fc.accumulate_fc>`
.. |cross_product| replace:: :class:`cross_product<ansys.dpf.core.operators.math.cross_product.cross_product>`
.. |cross_product_fc| replace:: :class:`cross_product_fc<ansys.dpf.core.operators.math.cross_product_fc.cross_product_fc>`
.. |component_wise_divide| replace:: :class:`component_wise_divide<ansys.dpf.core.operators.math.component_wise_divide.component_wise_divide>`
.. |component_wise_divide_fc| replace:: :class:`component_wise_divide_fc<ansys.dpf.core.operators.math.component_wise_divide_fc.component_wise_divide_fc>`
.. |generalized_inner_product| replace:: :class:`generalized_inner_product<ansys.dpf.core.operators.math.generalized_inner_product.generalized_inner_product>`
.. |generalized_inner_product_fc| replace:: :class:`generalized_inner_product_fc<ansys.dpf.core.operators.math.generalized_inner_product_fc.generalized_inner_product_fc>`
.. |overall_dot| replace:: :class:`overall_dot<ansys.dpf.core.operators.math.overall_dot.overall_dot>`
.. |outer_product| replace:: :class:`outer_product<ansys.dpf.core.operators.math.outer_product.outer_product>`
.. |pow| replace:: :class:`pow<ansys.dpf.core.operators.math.pow.pow>`
.. |pow_fc| replace:: :class:`pow_fc<ansys.dpf.core.operators.math.pow_fc.pow_fc>`
.. |sqr| replace:: :class:`sqr<ansys.dpf.core.operators.math.sqr.sqr>`
.. |sqr_fc| replace:: :class:`sqr_fc<ansys.dpf.core.operators.math.sqr_fc.sqr_fc>`
.. |norm| replace:: :class:`norm<ansys.dpf.core.operators.math.norm.norm>`
.. |norm_fc| replace:: :class:`norm_fc<ansys.dpf.core.operators.math.norm_fc.norm_fc>`

This tutorial demonstrate how to do some basic mathematical operations with PyDPF-Core.

We use |Field| and |FieldsContainer| created from scratch to facilitate the understanding on how the mathematical operators works.
For more information on creating a field from scratch check :ref:`ref_tutorials_data_structures`.

Define the |Field| and |FieldsContainer|
----------------------------------------

Define the |Fields| and |FieldsContainers| by choosing the number of entities, defining their ids, location and adding data.

If not specified the location is nodal by default.

We need to provide information about the scoping. DPF needs to know the IDs of the data we provide,
so that it can apply an operator on the correspondent entities. For more detailed explanation see `Scoping handling`_

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including the math operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core.operators import math as maths

    # Instantiate the Fields
    num_entities = 2
    field1 = dpf.Field(nentities=num_entities)
    field2 = dpf.Field(nentities=num_entities)
    field3 = dpf.Field(nentities=num_entities)
    field4 = dpf.Field(nentities=num_entities)

    # Define the scoping ids
    field1.scoping.ids = range(num_entities)
    field2.scoping.ids = range(num_entities)
    field3.scoping.ids = range(num_entities)
    field4.scoping.ids = range(num_entities)

    # Check the entities ids
    print("Field 1 ids: ",field1.scoping.ids , "\n")
    print("Field 2 ids: ",field2.scoping.ids , "\n")
    print("Field 3 ids: ",field3.scoping.ids , "\n")
    print("Field 4 ids: ",field4.scoping.ids , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core.operators import math as maths

    # Instantiate the Fields
    num_entities = 2
    field1 = dpf.Field(nentities=num_entities)
    field2 = dpf.Field(nentities=num_entities)
    field3 = dpf.Field(nentities=num_entities)
    field4 = dpf.Field(nentities=num_entities)

    # Define the scoping ids
    field1.scoping.ids = range(num_entities)
    field2.scoping.ids = range(num_entities)
    field3.scoping.ids = range(num_entities)
    field4.scoping.ids = range(num_entities)

    # Check the entities ids
    print("Field 1 ids: ",field1.scoping.ids , "\n")
    print("Field 2 ids: ",field2.scoping.ids , "\n")
    print("Field 3 ids: ",field3.scoping.ids , "\n")
    print("Field 4 ids: ",field4.scoping.ids , "\n")

.. code-block:: python

    # Define the Fields data
    field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    field2.data = [7.0, 3.0, 5.0, 8.0, 1.0, 2.0]
    field3.data = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    field4.data = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

    # Create the FieldsContainers
    fc1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field1, field2])
    fc2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field3, field4])

    # Check the Fields and FieldsContainer
    print("Field 1","\n", field1 , "\n")
    print("Field 2","\n", field2 , "\n")
    print("Field 3","\n", field3 , "\n")
    print("Field 4","\n", field4 , "\n")
    print("FieldsContainer1","\n", fc1 , "\n")
    print("FieldsContainer2","\n", fc2 , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    # Define the Fields data
    field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    field2.data = [7.0, 3.0, 5.0, 8.0, 1.0, 2.0]
    field3.data = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    field4.data = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

    # Create the FieldsContainers
    fc1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field1, field2])
    fc2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field3, field4])

    # Check the Fields and FieldsContainer
    print("Field 1", "\n", field1 , "\n")
    print("Field 2", "\n", field2 , "\n")
    print("Field 3", "\n", field3 , "\n")
    print("Field 4", "\n",field4 , "\n")
    print("FieldsContainer1", "\n",fc1 , "\n")
    print("FieldsContainer2", "\n",fc2 , "\n")

To make the mathematics operations, instantiate the operator and use ``eval()`` to compute and retrieve the result

Addition and Subtraction
------------------------

This section shows how the basic addition and subtraction operators works.

Addition
^^^^^^^^

Here we use:

a) |add| and |add_fc| operators for component wise addition;
b) |accumulate| and |accumulate_fc| operators for the total sum of each component for all the entities.

a) |add| and |add_fc| operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- |add|: Sum between the data vectors for the correspondent entity id

.. code-block:: python

    # Addition Fields
    add_field = maths.add(fieldA=field1, fieldB=field2).eval()
    # id 0: [1.+7. 2.+3. 3.+5.]
    # id 1: [4.+8. 5.+1. 6.+2.]

    print("Addition fields",add_field , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    add_field = maths.add(fieldA=field1, fieldB=field2).eval()
    print("Addition",add_field , "\n")

- |add_fc|: Selects all fields with the same label space in the input |FieldsContainers| and add those together

.. code-block:: python

    # Addition FieldsContainers
    add_fc = maths.add_fc(fields_container1=fc1, fields_container2=fc2).eval()
    # {time: 1}: field1 + field3
    #           -->      id 0: [1.+6. 2.+5. 3.+4.]
    #                    id 1: [4.+3. 5.+2. 6.+1.]
    #
    # {time: 2}: field2 + field4
    #           -->      id 0: [7.+4. 3.+1. 5.+8.]
    #                    id 1: [8.+5. 1.+7. 2.+9.]

    print("Addition FieldsContainers","\n", add_fc , "\n")
    print(add_fc[0], "\n")
    print(add_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    add_fc = maths.add_fc(fields_container1=fc1, fields_container2=fc2).eval()
    print("Addition FieldsContainers",add_fc , "\n")
    print(add_fc[0], "\n")
    print(add_fc[1], "\n")


b) |accumulate| and |accumulate_fc| operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- |accumulate| : Sums all the elementary data of a field to produce one elementary data for each vector component.
  You can give a scale ("ponderation") argument.

  Mind the |Fields| dimension: Our |Fields| represent 3D vectors so one elementary data is a 3D vector.
  The optional "ponderation" field is a field which attributes one value to multiply each data component per entity,
  so we need to change its dimensionality (1D).

.. code-block:: python

    # Total sum Field (accumulate)
    tot_sum_field = maths.accumulate(fieldA=field1).eval()
    # vector component 0 = 1.+ 4.
    # vector component 1 =  2.+ 5.
    # vector component 2 = 3.+ 6.

    # Total sum Field with scale vector (accumulate)
    scale_vect = dpf.Field(num_entities)
    scale_vect.dimensionality = dpf.Dimensionality([1])
    scale_vect.scoping.ids = range(num_entities)
    scale_vect.data = [5., 2.]

    # Total sum Field scale (accumulate)
    tot_sum_field_scale = maths.accumulate(fieldA=field1, ponderation=scale_vect).eval()
    # vector component 0 = (1.0 * 5.0) + (4.0 * 2.0)
    # vector component 1 = (2.0 * 5.0) + (5.0 * 2.0)
    # vector component 2 = (3.0 * 5.0) + (6.0 * 2.0)

    print("Total sum fields","\n", tot_sum_field, "\n")
    print("Total sum fields scale","\n", tot_sum_field_scale, "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    tot_sum_field = maths.accumulate(fieldA=field1).eval()
    scale_vect = dpf.Field(num_entities)
    scale_vect.dimensionality = dpf.Dimensionality([1])
    scale_vect.scoping.ids = range(num_entities)
    scale_vect.data = [5., 2.]
    tot_sum_field_scale = maths.accumulate(fieldA=field1, ponderation=scale_vect).eval()
    print("Total sum fields","\n", tot_sum_field, "\n")
    print("Total sum fields scale","\n", tot_sum_field_scale, "\n")

- |accumulate_fc| :  Sums all the elementary data of a |Field| with the same label space to produce
  one elementary data for each vector component.

.. code-block:: python

    # Total sum FieldsContainers (accumulate)
    tot_sum_fc = maths.accumulate_fc(fields_container=fc1).eval()
    # {time: 1}: field1
    #           -->      vector component 0 = 1.+ 4.
    #                    vector component 1 =  2.+ 5.
    #                    vector component 2 = 3.+ 6.
    #
    # {time: 2}: field2
    #           -->      vector component 0 = 7.+ 8.
    #                    vector component 1 =  3.+ 1.
    #                    vector component 2 = 5.+ 2.

    # Total sum FieldsContainers scale (accumulate)
    tot_sum_fc_scale = maths.accumulate_fc(fields_container=fc1, ponderation=scale_vect).eval()
    # {time: 1}: field1
    #           -->      vector component 0 = (1.0 * 5.0) + (4.0 * 2.0)
    #                    vector component 1 = (2.0 * 5.0) + (5.0 * 2.0)
    #                    vector component 2 = (3.0 * 5.0) + (6.0 * 2.0)
    #
    # {time: 2}: field2
    #           -->      vector component 0 = (7.0 * 5.0) + (8.0 * 2.0)
    #                    vector component 1 = (3.0 * 5.0) + (1.0 * 2.0)
    #                    vector component 2 = (5.0 * 5.0) + (2.0 * 2.0)


    print("Total sum FieldsContainers","\n", tot_sum_fc , "\n")
    print(tot_sum_fc[0], "\n")
    print(tot_sum_fc[1], "\n")

    print("Total sum FieldsContainers scale","\n", tot_sum_fc_scale , "\n")
    print(tot_sum_fc_scale[0], "\n")
    print(tot_sum_fc_scale[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    tot_sum_fc = maths.accumulate_fc(fields_container=fc1).eval()
    tot_sum_fc_scale = maths.accumulate_fc(fields_container=fc1, ponderation=scale_vect).eval()
    print("Total sum FieldsContainers","\n", tot_sum_fc , "\n")
    print(tot_sum_fc[0], "\n")
    print(tot_sum_fc[1], "\n")
    print("Total sum FieldsContainers scale","\n", tot_sum_fc_scale , "\n")
    print(tot_sum_fc_scale[0], "\n")
    print(tot_sum_fc_scale[1], "\n")

Subtraction
^^^^^^^^^^^

Here we use:

a) |minus| operator to compute the difference between the data vectors for the correspondent entity id of |Fields|
b) |minus_fc| operator that selects all fields with the same label space in the input |FieldsContainers|
  and compute their difference.

a) |minus| operator
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Subtraction Fields
    minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
    # id 0: [1.-7. 2.-3. 3.-5.]
    # id 1: [4.-8. 5.-1. 6.-2.]

    print("Subtraction fields","\n", minus_field , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
    print("Subtraction","\n", minus_field , "\n")

b) |minus_fc| operator
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Subtraction FieldsContainers
    minus_fc = maths.minus_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
    # {time: 1}: field1 - field3
    #           -->      id 0: [1.-6. 2.-5. 3.-4.]
    #                    id 1: [4.-3. 5.-2. 6.-1.]
    #
    # {time: 2}: field2 - field4
    #           -->      id 0: [7.-4. 3.-1. 5.-8.]
    #                    id 1: [8.-5. 1.-7. 2.-9.]

    print("Subtraction FieldsContainers","\n", minus_fc , "\n")
    print(minus_fc[0], "\n")
    print(minus_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    minus_fc = maths.minus_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
    print("Subtraction FieldsContainers","\n", minus_fc , "\n")
    print(minus_fc[0], "\n")
    print(minus_fc[1], "\n")

Product and Division
--------------------

This section shows how the basic product and division operators works.

Component-wise division
^^^^^^^^^^^^^^^^^^^^^^^

These operators computes the component-wise division between two |Fields| (with the |component_wise_divide| operator)
or between two |FieldsContainers|(with the |component_wise_divide_fc| operator) with same dimensionality.

.. code-block:: python

    # Component-wise division Fields
    comp_wise_div = maths.component_wise_divide(fieldA=field1, fieldB=field2).eval()
    # id 0: [1./7. 2./3. 3./5.]
    # id 1: [4./8. 5./1. 6./2.]

    print("Component-wise division Fields","\n", comp_wise_div , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    comp_wise_div = maths.component_wise_divide(fieldA=field1, fieldB=field2).eval()
    print("Component-wise division Fields","\n", comp_wise_div , "\n")

.. code-block:: python

    # Component-wise division FieldsContainers
    comp_wise_div_fc = maths.component_wise_divide_fc(fields_containerA=fc1, fields_containerB=fc2).eval()
    # {time: 1}: field1 - field3
    #           -->      id 0: [1./6. 2./5. 3./4.]
    #                    id 1: [4./3. 5./2. 6./1.]
    #
    # {time: 2}: field2 - field4
    #           -->      id 0: [7./4. 3./1. 5./8.]
    #                    id 1: [8./5. 1./7. 2./9.]

    print("Component-wise division Fields","\n", comp_wise_div , "\n")
    print("Component-wise division FieldsContainer","\n", comp_wise_div_fc , "\n")
    print(comp_wise_div_fc[0], "\n")
    print(comp_wise_div_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    comp_wise_div_fc = maths.component_wise_divide_fc(fields_containerA=fc1, fields_containerB=fc2).eval()
    print("Component-wise division FieldsContainer","\n", comp_wise_div_fc , "\n")
    print(comp_wise_div_fc[0], "\n")
    print(comp_wise_div_fc[1], "\n")

Cross product
^^^^^^^^^^^^^

These operators computes the cross product between two vector |Fields| (with the |cross_product| operator)
or between two |FieldsContainers|(with the |cross_product_fc| operator and with |Fields| with same label space).
The |Fields| can have the same location or Elemental Nodal and Nodal locations.

.. code-block:: python

    #  Cross product Fields
    cross_prod_fields = maths.cross_product(fieldA=field1,fieldB=field2).eval()
    # id 0: [(2.*5. - 3.*3.)  (3.*7. - 1.*5.)  (1.*3. - 2.*7.)]
    # id 1: [(5.*2. - 6.*1.)  (6.*8. - 4.*2.)  (4.*1. - 5.*8.)]

    print("Cross product Fields","\n", cross_prod_fields , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    cross_prod_fields = maths.cross_product(fieldA=field1,fieldB=field2).eval()
    print("Cross product Fields","\n", cross_prod_fields , "\n")

.. code-block:: python

    # Cross product FieldsContainer
    cross_prod_fc = maths.cross_product_fc(field_or_fields_container_A=fc1,field_or_fields_container_B=fc2).eval()
    # {time: 1}: field1 X field3
    #           -->      id 0: [(2.*4. - 3.*5.)  (3.*6. - 1.*4.)  (1.*5. - 2.*6.)]
    #                    id 1: [(5.*1. - 6.*2.)  (6.*3. - 4.*1.)  (4.*2. - 5.*3.)]
    #
    # {time: 2}: field2 X field4
    #           -->      id 0: [(3.*8. - 5.*1.)  (5.*4. - 7.*8.)  (7.*1. - 3.*4.)]
    #                    id 1: [(1.*9. - 2.*7.)  (2.*5. - 8.*9.)  (8.*7. - 1.*5.)]

    print("Cross product FieldsContainer","\n", cross_prod_fc , "\n")
    print(cross_prod_fc[0], "\n")
    print(cross_prod_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    cross_prod_fc = maths.cross_product_fc(field_or_fields_container_A=fc1,field_or_fields_container_B=fc2).eval()
    print("Cross product FieldsContainer","\n", cross_prod_fc , "\n")
    print(cross_prod_fc[0], "\n")
    print(cross_prod_fc[1], "\n")

Dot product
^^^^^^^^^^^

These operators computes a general notion of inner product between between two vector |Fields|
(with the |generalized_inner_product| operator) or between two |FieldsContainers|
(with the |generalized_inner_product_fc| operator and with |Fields| with same label space).
The |Fields| may have different dimensionality.

.. code-block:: python

    # Dot product Fields
    dot_prod_fields = maths.generalized_inner_product(fieldA=field1, fieldB=field2).eval()
    # id 0: (1. * 7.) + (2. * 3.) + (3. * 5.)
    # id 1: (4. * 8.) + (5. * 1.) + (6. * 2.)

    print("Dot product Fields","\n", dot_prod_fields , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    dot_prod_fields = maths.generalized_inner_product(fieldA=field1, fieldB=field2).eval()
    print("Dot product Fields","\n", dot_prod_fields , "\n")

.. code-block:: python

    # Dot product FieldsContainer
    dot_prod_fields_fc = maths.generalized_inner_product_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
    # {time: 1}: field1 X field3
    #           -->      id 0: (1. * 6.) + (2. * 5.) + (3. * 4.)
    #                    id 1: (4. * 3.) + (5. * 2.) + (6. * 1.)
    #
    # {time: 2}: field2 X field4
    #           -->      id 0: (7. * 4.) + (3. * 1.) + (5. * 8.)
    #                    id 1: (8. * 5.) + (1. * 7.) + (2. * 9.)

    print("Dot product FieldsContainer","\n", dot_prod_fields_fc , "\n")
    print(dot_prod_fields_fc[0], "\n")
    print(dot_prod_fields_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    dot_prod_fields_fc = maths.generalized_inner_product_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
    print("Dot product FieldsContainer","\n", dot_prod_fields_fc , "\n")
    print(dot_prod_fields_fc[0], "\n")
    print(dot_prod_fields_fc[1], "\n")

Overall dot
^^^^^^^^^^^

The |overall_dot| operator computes a dot product between the entities of same ID of two |Fields| and then adds
all the entities data to return a scalar

.. code-block:: python

    # Overall dot
    overall_dot = maths.overall_dot(fieldA=field1, fieldB=field2).eval()
    # id 1: (1. * 7.) + (2. * 3.) + (3. * 5.) + (4. * 8.) + (5. * 1.) + (6. * 2.)

    print("Overall dot","\n", overall_dot , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    overall_dot = maths.overall_dot(fieldA=field1, fieldB=field2).eval()
    print("Dot product Fields","\n", overall_dot , "\n")

Outer product
^^^^^^^^^^^^^

The |outer_product| operator computes the outer product of two vector fields. It makes the product of all the
components by all the components data.

.. code-block:: python

    # Outer product Fields
    outer_prod = maths.outer_product(fieldA=field1, fieldB=field2).eval()
    # id 0: [1.*7. 2.*7. 3.*7. 1.*3. 2.*3. 3.*3. 1.*5. 2.*5. 3.*5.]
    # id 1: [4.*8. 5.*8. 6.*8. 4.*1. 5.*1. 6.*1. 4.*2. 5.*2. 6.*2.]

    print("Outer product Fields","\n", outer_prod , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    outer_prod = maths.outer_product(fieldA=field1, fieldB=field2).eval()
    print("Outer product Fields","\n", outer_prod , "\n")

Power
-----

This section shows how the basic power operators works.

Squared
^^^^^^^

These operators computes the element-wise data squared of a |Field| (with the |sqr| operator) and of |Fields| from a
|FieldsContainer| (with the |sqr_fc| operator).

.. code-block:: python

    # ^2 Fields
    sqr_field = maths.sqr(field=field1).eval()
    # id 0: [(1.^2.) (2.^2.) (3.^2.)]
    # id 1: [(4.^2.) (5.^2.) (6.^2.)]

    print("^2 Fields","\n", sqr_field , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    sqr_field = maths.sqr(field=field1).eval()
    print("^2 Fields","\n", sqr_field , "\n")

.. code-block:: python

    # ^2 FieldsContainer
    sqr_fc = maths.sqr_fc(fields_container=fc1).eval()
    # {time: 1}: field1
    #           -->      id 0: [(1.^2.) (2.^2.) (3.^2.)]
    #                    id 1: [(4.^2.) (5.^2.) (6.^2.)]
    #
    # {time: 2}: field2
    #           -->      id 0: [(7.^2.) (3.^2.) (5.^2.)]
    #                    id 1: [(8.^2.) (1.^2.) (2.^2.)]

    print("^2 FieldsContainer","\n", sqr_fc , "\n")
    print(sqr_fc[0], "\n")
    print(sqr_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    sqr_fc = maths.sqr_fc(fields_container=fc1).eval()
    print("^2 FieldsContainer","\n", sqr_fc , "\n")
    print(sqr_fc[0], "\n")
    print(sqr_fc[1], "\n")

Power
^^^^^

These operators computes the element-wise data power a factor of a |Field| (with the |pow| operator) and of |Fields| from a
|FieldsContainer| (with the |pow_fc| operator).

.. code-block:: python

    # Power factor
    pow_factor = 3.0
    # Power Fields
    pow_field = maths.pow(field=field1, factor=pow_factor).eval()
    # id 0: [(1.^3.) (2.^3.) (3.^3.)]
    # id 1: [(4.^3.) (5.^3.) (6.^3.)]

    print("Power Fields","\n", pow_field , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    pow_factor = 3.0
    pow_field = maths.pow(field=field1, factor=pow_factor).eval()
    print("Power Fields","\n", pow_field , "\n")

.. code-block:: python

    # Power FieldsContainer
    pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
    # {time: 1}: field1
    #           -->      id 0: [(1.^3.) (2.^3.) (3.^3.)]
    #                    id 1: [(4.^3.) (5.^3.) (6.^3.)]
    #
    # {time: 2}: field2
    #           -->      id 0: [(7.^3.) (3.^3.) (5.^3.)]
    #                    id 1: [(8.^3.) (1.^3.) (2.^3.)]

    print("Power FieldsContainer","\n", pow_fc , "\n")
    print(pow_fc[0], "\n")
    print(pow_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
    print("Power","\n", pow_fc , "\n")
    print(pow_fc[0], "\n")
    print(pow_fc[1], "\n")

Norm
----

These operators computes the element-wise Lp norm (Default Lp=L2 ) of a |Field| elementary data (with the |norm|
operator) and of |Fields| elementary data from a |FieldsContainer| (with the |norm_fc| operator).

.. code-block:: python

    # Norm Fields
    norm_field = maths.norm(field=field1).eval()
    # id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2
    # id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2

    print("Norm Fields","\n", norm_field , "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    pow_factor = 3.0
    pow_field = maths.pow(field=field1, factor=pow_factor).eval()
    print("Dot product Fields","\n", pow_field , "\n")

.. code-block:: python

    # Power FieldsContainer
    norm_fc = maths.norm_fc(fields_container=fc1).eval()
    # {time: 1}: field1
    #           -->      id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2
    #                    id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2
    #
    # {time: 2}: field2
    #           -->      id 0: [(7.^2.) + (3.^2.) + (5.^2.)] ^1/2
    #                    id 1: [(8.^2.) + (1.^2.) + (2.^2.)] ^1/2

    print("Norm FieldsContainer","\n", norm_fc , "\n")
    print(pow_fc[0], "\n")
    print(pow_fc[1], "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
    print("Dot product FieldsContainer","\n", pow_fc , "\n")
    print(pow_fc[0], "\n")
    print(pow_fc[1], "\n")

Scoping handling
----------------

DPF needs to know the IDs of the data on the fields, so that it can apply an operator on on the correspondent entities.

By providing these integers we only select the data with an ID in common.

Here we will use two different fields to understand this functioning:

.. code-block:: python

    # Instantiate the Fields
    field5 = dpf.Field(nentities=3)
    field6 = dpf.Field(nentities=3)

    # Define the Fields data
    field5.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    field6.data = [5.0, 1.0, 6.0, 3.0, 8.0, 9.0, 7.0, 2.0, 4.0]

    # Define the scoping ids
    field5.scoping.ids = [1, 2, 3]
    field6.scoping.ids = [3, 4, 5]

    print(field5,"\n")
    print(field5.data,"\n")
    print(field6,"\n")
    print(field6.data,"\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    field5 = dpf.Field(nentities=3)
    field6 = dpf.Field(nentities=3)

    # Define the Fields data
    field5.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    field6.data = [5.0, 1.0, 6.0, 3.0, 8.0, 9.0, 7.0, 2.0, 4.0]

    # Define the scoping ids
    field5.scoping.ids = [1, 2, 3]
    field6.scoping.ids = [3, 4, 5]

    print(field5,"\n")
    print(field5.data,"\n")
    print(field6,"\n")
    print(field6.data,"\n")


Here the only entities with matching ids the third one of the first field, and the first one of the
second field. Other entities elementary data is not taken into account when using an operator that needs two operands.

For example the |add| operator:

.. code-block:: python

    # Use the add operator
    add_scop = dpf.operators.math.add(fieldA=field5, fieldB=field6).eval()

    # Only the entity id 3 is changed.
    print(add_scop,"\n")
    print(add_scop.data,"\n)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    add_scop = dpf.operators.math.add(fieldA=field5, fieldB=field6).eval()
    print(add_scop,"\n")
    print(add_scop.data,"\n")

Or the |generalized_inner_product| operator:

.. code-block:: python

    # Use the dot product operator
    dot_scop = dpf.operators.math.generalized_inner_product(fieldA=field5, fieldB=field6).eval()
    # id 3: (7. * 5.) + (8. * 1.) + (9. * 6.)

    # We obtain zeros for IDs where have no matches in the two fields.
    print(dot_scop,"\n")
    print(dot_scop.data,"\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    dot_scop = dpf.operators.math.generalized_inner_product(fieldA=field5, fieldB=field6).eval()
    print(dot_scop,"\n")
    print(dot_scop.data,"\n")