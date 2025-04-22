.. _ref_basic_math:

===========
Basic maths
===========

.. include:: ../../../links_and_refs.rst
.. |math operators| replace:: :mod:`math operators <ansys.dpf.core.operators.math>`
.. |fields_container_factory| replace:: :mod:`fields_container_factory<ansys.dpf.core.fields_container_factory>`
.. |over_time_freq_fields_container| replace:: :func:`over_time_freq_fields_container()<ansys.dpf.core.fields_container_factory.over_time_freq_fields_container>`
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

This tutorial explains how to do some basic mathematical operations with PyDPF-Core.

DPF uses |Field| and |FieldsContainer| objects to handle data. The |Field| is a homogeneous array and
a |FieldsContainer| is a labeled collection of |Field|. Thus, when making mathematical operations with the data, you
manipulate |Field| and |FieldsContainer|.

:jupyter-download-script:`Download tutorial as Python script<basic_maths>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<basic_maths>`

Create the Fields and FieldsContainers
--------------------------------------

DPF uses |Field| and |FieldsContainer| objects to handle data. The |Field| is a homogeneous array and
a |FieldsContainer| is a labeled collection of |Field|.

Here, we use |Field| and |FieldsContainer| created from scratch to facilitate the understanding on how the
mathematical operators works. For more information on creating a |Field| from scratch check
:ref:`ref_tutorials_data_structures`.

.. tab-set::

    .. tab-item:: Fields

        Create the Fields by defining:

        - The number of entities
        - The entities ids and location. Thus, the |Field| scoping

            - If not specified, the location is *'nodal'* by default.
            - Each entity (here, the nodes) must have a |Scoping| id. The ids allows DPF to apply an operator on the
              corresponding entities. For more detailed explanation about the influence of the |Scoping| on the operations,
              see the :ref:`ref_basic_maths_scoping_handling` section on this tutorial.

        Import the necessary DPF modules.

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the math operators module
            from ansys.dpf.core.operators import math as maths

        Create the Fields by intanciating the |Field| object.

        .. jupyter-execute::

            # Instantiate the Fields
            num_entities = 2
            field1 = field2 = field3 = field4 = dpf.Field(nentities=num_entities)

            # Define the scoping ids
            field1.scoping.ids = field2.scoping.ids = field3.scoping.ids = field4.scoping.ids = range(num_entities)

            # Set the data to each Field
            field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            field2.data = [7.0, 3.0, 5.0, 8.0, 1.0, 2.0]
            field3.data = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
            field4.data = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

            # Print the Fields
            print("Field 1","\n", field1, "\n"); print("Field 2","\n", field2, "\n");
            print("Field 3","\n", field3, "\n"); print("Field 4","\n", field4, "\n")

    .. tab-item:: FieldsContainers

        Create the FieldsContainers using the |fields_container_factory|.  Here, we use the |over_time_freq_fields_container|
        function that creates a |FieldsContainer| with a *'time'* label.

        .. jupyter-execute::

            # Create the FieldsContainers
            fc1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field1, field2])
            fc2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field3, field4])

            # Print the FieldsContainers
            print("FieldsContainer1","\n", fc1, "\n")
            print("FieldsContainer2","\n", fc2, "\n")


To make the mathematics operations, we use the operators available in the |math operators| module.
Their usage is similar, for each operation you must instantiate the operator and use ``.eval()`` method to compute
and retrieve the results.

Mathematical operations with Fields
-----------------------------------

.. tab-set::

    .. tab-item:: Addition

        Here, we use:

        - The |add| operator for component wise addition
        - The |accumulate| operator to find the total sum of each component for all the entities

        **'add' operator**

        This operator computes the sum between the data vectors for the corresponding entity id.

        .. jupyter-execute::

            # Add the Fields
            add_field = maths.add(fieldA=field1, fieldB=field2).eval()
            # id 0: [1.+7. 2.+3. 3.+5.]
            # id 1: [4.+8. 5.+1. 6.+2.]

            # Print the results
            print("Addition fields",add_field , "\n")

        **'accumulate' operator**

        This operator sums all the elementary data of a field to produce one elementary data for each vector component.
        You can give a scale ("ponderation") argument.

         Mind the |Field| dimension: Our |Field| represents 3D vectors, so one elementary data is a 3D vector.
         The optional "ponderation" |Field| is a |Field| that attributes the values to be multiplied by each data
         component of the entities. Thus, we need to change its dimensionality (1D).

        Define the total sum (accumulate) of the components of the given |Field|.

        .. jupyter-execute::

            # Find the total sum of the Fields
            tot_sum_field = maths.accumulate(fieldA=field1).eval()
            # vector component 0 = 1.+ 4.
            # vector component 1 =  2.+ 5.
            # vector component 2 = 3.+ 6.

            # Print the results
            print("Total sum fields","\n", tot_sum_field, "\n")

        Define the total sum (accumulate) of the components of the given |Field| and give a scale factor.

        .. jupyter-execute::

            # Defines the scale factor Field
            scale_vect = dpf.Field(num_entities)
            # Changes the scale factor Field dimensionality
            scale_vect.dimensionality = dpf.Dimensionality([1])
            # Defines the scale factor Field scoping ids
            scale_vect.scoping.ids = range(num_entities)
            # Defines the scale factor Field data
            scale_vect.data = [5., 2.]

            # Find the total sum of the Field and use a scale vector
            tot_sum_field_scale = maths.accumulate(fieldA=field1, ponderation=scale_vect).eval()
            # vector component 0 = (1.0 * 5.0) + (4.0 * 2.0)
            # vector component 1 = (2.0 * 5.0) + (5.0 * 2.0)
            # vector component 2 = (3.0 * 5.0) + (6.0 * 2.0)

            # Print the results
            print("Total sum fields scale","\n", tot_sum_field_scale, "\n")

    .. tab-item:: Subtraction

        Here, we use the |minus| operator. It computes the difference between the components of
        the data vectors of the corresponding entities of the given Fields.

        .. jupyter-execute::

            # Subtraction with the Fields
            minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
            # id 0: [1.-7. 2.-3. 3.-5.]
            # id 1: [4.-8. 5.-1. 6.-2.]

            # Print the results
            print("Subtraction fields","\n", minus_field , "\n")

    .. tab-item:: Cross product

        Here, we use the |cross_product| operator. It computes the cross product between two vector Fields.

        .. jupyter-execute::

            # Define the cross product
            cross_prod_fields = maths.cross_product(fieldA=field1,fieldB=field2).eval()
            # id 0: [(2.*5. - 3.*3.)  (3.*7. - 1.*5.)  (1.*3. - 2.*7.)]
            # id 1: [(5.*2. - 6.*1.)  (6.*8. - 4.*2.)  (4.*1. - 5.*8.)]

            # Print the results
            print("Cross product Fields","\n", cross_prod_fields , "\n")

    .. tab-item:: Dot product

        Here, we use:

        - The |generalized_inner_product| operator to compute the inner product between two vector Fields;
        - The |overall_dot| operator to compute the total sum of the result of the dot product between two vector Fields.

        **'generalized_inner_product' operator**

        This operator computes a general notion of inner product between between two vector Fields. These Fields
        may be of different dimensionality.

        .. jupyter-execute::

            # Define the dot product
            dot_prod_fields = maths.generalized_inner_product(fieldA=field1, fieldB=field2).eval()
            # id 0: (1. * 7.) + (2. * 3.) + (3. * 5.)
            # id 1: (4. * 8.) + (5. * 1.) + (6. * 2.)

            # Print the results
            print("Dot product Fields","\n", dot_prod_fields , "\n")

        **'overall_dot' operator**

        This operator makes two manipulations to give the result:

        - First, it computes a dot product between the entities of same id of two Fields;
        - Finally, it adds all the entities data to return a scalar.

        .. jupyter-execute::

            # Define the overall dot
            overall_dot = maths.overall_dot(fieldA=field1, fieldB=field2).eval()
            # id 1: (1. * 7.) + (2. * 3.) + (3. * 5.) + (4. * 8.) + (5. * 1.) + (6. * 2.)

            # Print the results
            print("Overall dot","\n", overall_dot , "\n")

    .. tab-item:: Division

        Here, we use the |component_wise_divide| operator. It computes the component-wise division between
        the corresponding entities of two Fields.

        .. jupyter-execute::

            # Divide the components of the Fields
            comp_wise_div = maths.component_wise_divide(fieldA=field1, fieldB=field2).eval()
            # id 0: [1./7. 2./3. 3./5.]
            # id 1: [4./8. 5./1. 6./2.]

            # Print the results
            print("Component-wise division Fields","\n", comp_wise_div , "\n")

    .. tab-item:: Power

        Here we use:

        - The |sqr| operator to compute the component-wise |Field| data to the power of two;
        - The |pow| operator to compute the component-wise |Field| data to the power of a given factor;

        **'sqr' operator**

        This operator computes the data of each component of a |Field| to the power of two.

        .. jupyter-execute::

            # Define the power of two
            sqr_field = maths.sqr(field=field1).eval()
            # id 0: [(1.^2.) (2.^2.) (3.^2.)]
            # id 1: [(4.^2.) (5.^2.) (6.^2.)]

            print("^2 Fields","\n", sqr_field , "\n")

        **'pow' operator**

        This operator computes the data of each component of a |Field| to the power of a given factor.

        Here, we use the power of three.

        .. jupyter-execute::

            # Define the power factor
            pow_factor = 3.0
            # Define the power of three
            pow_field = maths.pow(field=field1, factor=pow_factor).eval()
            # id 0: [(1.^3.) (2.^3.) (3.^3.)]
            # id 1: [(4.^3.) (5.^3.) (6.^3.)]

            # Print the results
            print("Power Fields","\n", pow_field , "\n")

    .. tab-item:: Norm

        Here, we use the |norm| operator. It computes the component-wise Lp norm of a |Field| elementary data.
        The default Lp norm is Lp=L2.

        .. jupyter-execute::

            # Define the norm
            norm_field = maths.norm(field=field1).eval()
            # id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2
            # id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2

            # Print the results
            print("Norm Fields","\n", norm_field , "\n")

Mathematical operations with FieldsContainer
--------------------------------------------

.. tab-set::

    .. tab-item:: Addition

        Here, we use:

        - The 'add_fc' operator for component wise addition of each |Field| from a |FieldsContainer|;
        - The 'accumulate_fc' operator to find the total sum of each component for all the entities of each |Field|
          from a |FieldsContainer|

        **'add_fc' operator**

        This operator selects all fields with the same label space in the input |FieldsContainer| and add those together.

        .. jupyter-execute::

            # Add the FieldsContainers
            add_fc = maths.add_fc(fields_container1=fc1, fields_container2=fc2).eval()
            # {time: 1}: field1 + field3
            #           -->      id 0: [1.+6. 2.+5. 3.+4.]
            #                    id 1: [4.+3. 5.+2. 6.+1.]
            #
            # {time: 2}: field2 + field4
            #           -->      id 0: [7.+4. 3.+1. 5.+8.]
            #                    id 1: [8.+5. 1.+7. 2.+9.]

            # Print the results
            print("Addition FieldsContainers","\n", add_fc , "\n")
            print(add_fc[0], "\n")
            print(add_fc[1], "\n")

        **'accumulate_fc' operator**

        This operator sums all the elementary data of a |Field| with the same label space to produce
        one elementary data for each vector component.

        Define the total sum (accumulate) of the components of the each |Field| in the given |FieldsContainer|.

        .. jupyter-execute::

            # Find the total sum of the Fields in the FieldsContainer
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

            # Print the results
            print("Total sum FieldsContainers","\n", tot_sum_fc , "\n")
            print(tot_sum_fc[0], "\n")
            print(tot_sum_fc[1], "\n")

        Define the total sum (accumulate) of the components of the each |Field| in the given |FieldsContainer|
        and give a scale factor.

        .. jupyter-execute::

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

            # Print the results
            print("Total sum FieldsContainers scale","\n", tot_sum_fc_scale , "\n")
            print(tot_sum_fc_scale[0], "\n")
            print(tot_sum_fc_scale[1], "\n")

    .. tab-item:: Subtraction

        Here, we use the |minus_fc| operator. It computes the difference between the components of the
        data of all Fields with the same label space in the given FieldsContainer.

        .. jupyter-execute::

            # Subtraction with the Fields
            minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
            # id 0: [1.-7. 2.-3. 3.-5.]
            # id 1: [4.-8. 5.-1. 6.-2.]

            # Print the results
            print("Subtraction fields","\n", minus_field , "\n")

    .. tab-item:: Cross product

        Here, we use the |cross_product_fc| operator. It computes the cross product between two vector Fields
        with same label space in the given FieldsContainers.
        These Field can have the same location or Elemental Nodal and Nodal locations.

        .. jupyter-execute::

            # Define the cross product
            cross_prod_fc = maths.cross_product_fc(field_or_fields_container_A=fc1,field_or_fields_container_B=fc2).eval()
            # {time: 1}: field1 X field3
            #           -->      id 0: [(2.*4. - 3.*5.)  (3.*6. - 1.*4.)  (1.*5. - 2.*6.)]
            #                    id 1: [(5.*1. - 6.*2.)  (6.*3. - 4.*1.)  (4.*2. - 5.*3.)]
            #
            # {time: 2}: field2 X field4
            #           -->      id 0: [(3.*8. - 5.*1.)  (5.*4. - 7.*8.)  (7.*1. - 3.*4.)]
            #                    id 1: [(1.*9. - 2.*7.)  (2.*5. - 8.*9.)  (8.*7. - 1.*5.)]

            # Print the results
            print("Cross product FieldsContainer","\n", cross_prod_fc , "\n")
            print(cross_prod_fc[0], "\n")
            print(cross_prod_fc[1], "\n")

    .. tab-item:: Dot product

        Here, we use the |generalized_inner_product_fc| operator. It computes a general notion of inner product
        between between two vector Fields with same label space in the given FieldsContainers. These Fields may
        be of different dimensionality.

        .. jupyter-execute::

            # Define the dot product
            dot_prod_fields_fc = maths.generalized_inner_product_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
            # {time: 1}: field1 X field3
            #           -->      id 0: (1. * 6.) + (2. * 5.) + (3. * 4.)
            #                    id 1: (4. * 3.) + (5. * 2.) + (6. * 1.)
            #
            # {time: 2}: field2 X field4
            #           -->      id 0: (7. * 4.) + (3. * 1.) + (5. * 8.)
            #                    id 1: (8. * 5.) + (1. * 7.) + (2. * 9.)

            # Print the results
            print("Dot product FieldsContainer","\n", dot_prod_fields_fc , "\n")
            print(dot_prod_fields_fc[0], "\n")
            print(dot_prod_fields_fc[1], "\n")

    .. tab-item:: Division

        Here, we use the |component_wise_divide_fc| operator. It computes the component-wise division between
        the corresponding entities of two Fields with same dimensionality of the given FieldsContainers. The
        FieldsContainers must contain only one |Field| each.

        .. jupyter-execute::

            # Define the component-wise division between the Fields in the FieldsContainers
            comp_wise_div_fc = maths.component_wise_divide_fc(fields_containerA=fc1, fields_containerB=fc2).eval()
            # {time: 1}: field1 - field3
            #           -->      id 0: [1./6. 2./5. 3./4.]
            #                    id 1: [4./3. 5./2. 6./1.]
            #
            # {time: 2}: field2 - field4
            #           -->      id 0: [7./4. 3./1. 5./8.]
            #                    id 1: [8./5. 1./7. 2./9.]

            # Print the results
            print("Component-wise division FieldsContainer","\n", comp_wise_div_fc , "\n")
            print(comp_wise_div_fc[0], "\n")
            print(comp_wise_div_fc[1], "\n")

    .. tab-item:: Power

        Here we use:

        - The |sqr_fc| operator to compute the component-wise |Field| data (from a |FieldsContainer|) to the power of two;
        - The |pow_fc| operator to compute the component-wise |Field| data (from a |FieldsContainer|) to the power of a given factor;

        **'sqr_fc' operator**

        This operator computes the data of each component of each |Field| of a |FieldsContainer| to the power of two.

        .. jupyter-execute::

            # Define the power of two
            sqr_fc = maths.sqr_fc(fields_container=fc1).eval()
            # {time: 1}: field1
            #           -->      id 0: [(1.^2.) (2.^2.) (3.^2.)]
            #                    id 1: [(4.^2.) (5.^2.) (6.^2.)]
            #
            # {time: 2}: field2
            #           -->      id 0: [(7.^2.) (3.^2.) (5.^2.)]
            #                    id 1: [(8.^2.) (1.^2.) (2.^2.)]

            # Print the results
            print("^2 FieldsContainer","\n", sqr_fc , "\n")
            print(sqr_fc[0], "\n")
            print(sqr_fc[1], "\n")

        **'pow_fc' operator**

        This operator computes the data of each component of each |Field| of a |FieldsContainer| to the power of a given factor.

        Here, we use the power of three.

        .. jupyter-execute::

            # Define the power of three
            pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
            # {time: 1}: field1
            #           -->      id 0: [(1.^3.) (2.^3.) (3.^3.)]
            #                    id 1: [(4.^3.) (5.^3.) (6.^3.)]
            #
            # {time: 2}: field2
            #           -->      id 0: [(7.^3.) (3.^3.) (5.^3.)]
            #                    id 1: [(8.^3.) (1.^3.) (2.^3.)]

            # Print the results
            print("Power FieldsContainer","\n", pow_fc , "\n")
            print(pow_fc[0], "\n")
            print(pow_fc[1], "\n")

    .. tab-item:: Norm

        Here, we use the |norm_fc| operator. It computes the component-wise Lp norm of |Field|
        (from a |FieldsContainer|) elementary data. The default Lp norm is Lp=L2.

        .. jupyter-execute::

            # Define the norm
            norm_fc = maths.norm_fc(fields_container=fc1).eval()
            # {time: 1}: field1
            #           -->      id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2
            #                    id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2
            #
            # {time: 2}: field2
            #           -->      id 0: [(7.^2.) + (3.^2.) + (5.^2.)] ^1/2
            #                    id 1: [(8.^2.) + (1.^2.) + (2.^2.)] ^1/2

            # Print the results
            print("Norm FieldsContainer","\n", norm_fc , "\n")
            print(pow_fc[0], "\n")
            print(pow_fc[1], "\n")

.. _ref_basic_maths_scoping_handling :

Scoping handling
----------------

DPF needs to know the ids of the data on the fields. By providing these integers, we only select
the data with the same id when using an operator.

Here, we use two different Fields to understand this functioning.

.. jupyter-execute::

    # Instantiate the Fields
    field5 = dpf.Field(nentities=3)
    field6 = dpf.Field(nentities=3)

    # Define the Fields data
    field5.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    field6.data = [5.0, 1.0, 6.0, 3.0, 8.0, 9.0, 7.0, 2.0, 4.0]

    # Define the scoping ids
    field5.scoping.ids = [1, 2, 3]
    field6.scoping.ids = [3, 4, 5]

    # Print the Fields
    print("Field 5", "\n", field5, "\n")
    print("Field 6", "\n",field6,"\n")

    # Print the Fields data
    print("Field 5 data", "\n", field5.data,"\n")
    print("Field 6 data", "\n", field6.data,"\n")

Here the only entities with matching ids are:

- The third one of the first field
- The first one of the second field.

Other entities elementary data is not taken into account when using an operator that needs two operands.

For example the |add| operator:

.. jupyter-execute::

    # Use the add operator
    add_scop = dpf.operators.math.add(fieldA=field5, fieldB=field6).eval()

    # Print the results
    # Only the entity id 3 is changed.
    print(add_scop,"\n")
    print(add_scop.data,"\n")

Or the |generalized_inner_product| operator:

.. jupyter-execute::

    # Use the dot product operator
    dot_scop = dpf.operators.math.generalized_inner_product(fieldA=field5, fieldB=field6).eval()
    # id 3: (7. * 5.) + (8. * 1.) + (9. * 6.)

    # Print the results
    # We obtain zeros for IDs where have no matches in the two fields.
    print(dot_scop,"\n")
    print(dot_scop.data,"\n")