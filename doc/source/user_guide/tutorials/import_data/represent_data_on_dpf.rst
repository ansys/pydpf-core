.. _ref_tutorials_represent_data_on_dpf:

========================
Manual input data on DPF
========================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |append| replace:: :func:`append()<ansys.dpf.core.field.Field.append>`
.. |data| replace:: :attr:`Field.data<ansys.dpf.core.field_base._FieldBase.data>`
.. |scoping| replace:: :attr:`Field.scoping<ansys.dpf.core.field_base._FieldBase.scoping>`

This tutorial shows how to represent your manual input data in a DPF data storage structures.

When handling data DPF uses |FieldsContainer| and |Field| to store and return it. The |Field| is a DPF array
and a collection of |Field| is called |FieldsContainer|. For more information on how the data is structure
in a |Field| and how the DPF data storage structures works check the :ref:`ref_tutorials_data_structures`
tutorial section.

Here we will create some 3d vector |Field|, where the data comes from lists.

Defining the fields
-------------------

To manually import data on DPF you have to create the structure to store it.

Here we create a |Field| from scratch by instantiating this object. When using this approach the |Field| has
vector nature by default. Check the :ref:`ref_tutorials_data_structures` tutorial section for more information
on others approaches.

We will need two 3d vector |Field|:

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf

    # Create the fields
    # a. Define the number of entities
    num_entities_1 = 2

    # b. Instanciate the field
    field_1 = dpf.Field(nentities=num_entities_1)
    field_2 = dpf.Field(nentities=num_entities_1)
    field_3 = dpf.Field(nentities=num_entities_1)
    field_4 = dpf.Field(nentities=num_entities_1)

    # c. Define the scoping ids

    field_3.scoping.ids = range(num_entities_1)
    field_4.scoping.ids = range(num_entities_1)

    # d. Create a FieldsContainer
    fc_1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field_1, field_2])

    # Check the Fields and the FieldsContainer
    print("Field 1: ", "\n" ,field_1, "\n")
    print("Field 2: ", "\n" ,field_2, "\n")
    print("Field 3: ", "\n" ,field_3, "\n")
    print("Field 4: ", "\n" ,field_4, "\n")
    print("FieldsContainer: ", "\n" ,fc_1, "\n")

Add data to the fields
----------------------

Here we define the data and then add it to the fields.

You can add data to a |Field| by using the |append| method, if you have not set the |scoping| property
with the scoping ids, or the |data| property, if you have set the |scoping| property
with the scoping ids.

.. jupyter-execute::

    # Define and add the data to the fields
    # a. Using the append method

    # Define the Fields data
    data_11 = [1.0, 2.0, 3.0]
    data_12 = [4.0, 5.0, 6.0]
    data_21 = [7.0, 3.0, 5.0]
    data_22 = [8.0, 1.0, 2.0]

    # Add the data to the field
    field_1.append(data=data_11, scopingid=0)
    field_1.append(data=data_12, scopingid=1)
    field_2.append(data=data_21, scopingid=0)
    field_2.append(data=data_22, scopingid=1)

    # b. Using the data property

    # Define the Fields data
    data_3b = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    data_4b = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

    # Add the data to the field
    field_3.data = data_3b
    field_4.data = data_4b

    # Check the Fields
    print("Field 1: ", "\n", field_1, "\n")
    print("Field 2: ", "\n", field_2, "\n")
    print("Field 3: ", "\n" ,field_3, "\n")
    print("Field 4: ", "\n" ,field_4, "\n")
