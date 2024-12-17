.. _ref_tutorials_load_custom_data:

=======================
Load custom data in DPF
=======================

.. include:: ../../../links_and_refs.rst
.. |Field.append| replace:: :func:`append()<ansys.dpf.core.field.Field.append>`
.. |Field.data| replace:: :attr:`Field.data<ansys.dpf.core.field_base._FieldBase.data>`
.. |fields_factory| replace:: :mod:`fields_factory<ansys.dpf.core.fields_factory>`
.. |fields_container_factory| replace:: :mod:`fields_container_factory<ansys.dpf.core.fields_container_factory>`
.. |location| replace:: :class:`location<ansys.dpf.core.common.locations>`
.. |nature| replace:: :class:`nature<ansys.dpf.core.common.natures>`
.. |dimensionality| replace:: :class:`dimensionality<ansys.dpf.core.dimensionality.Dimensionality>`
.. |Field.dimensionality| replace:: :func:`Field.dimensionality<ansys.dpf.core.field.Field.dimensionality>`
.. |Field.location| replace:: :func:`Field.location<ansys.dpf.core.field.Field.location>`
.. |Field.scoping| replace:: :func:`Field.scoping<ansys.dpf.core.field.Field.scoping>`
.. |field_from_array| replace:: :func:`field_from_array()<ansys.dpf.core.fields_factory.field_from_array>`
.. |create_scalar_field| replace:: :func:`create_scalar_field()<ansys.dpf.core.fields_factory.create_scalar_field>`
.. |create_vector_field| replace:: :func:`create_vector_field()<ansys.dpf.core.fields_factory.create_vector_field>`
.. |create_3d_vector_field| replace:: :func:`create_3d_vector_field()<ansys.dpf.core.fields_factory.create_3d_vector_field>`
.. |create_matrix_field| replace:: :func:`create_matrix_field()<ansys.dpf.core.fields_factory.create_matrix_field>`
.. |create_tensor_field| replace:: :func:`create_tensor_field()<ansys.dpf.core.fields_factory.create_tensor_field>`
.. |over_time_freq_fields_container| replace:: :func:`over_time_freq_fields_container()<ansys.dpf.core.fields_container_factory.over_time_freq_fields_container>`

This tutorial shows how to represent your custom data in DPF data storage structures.

To import you custom data in DPF, you must create a DPF data structure to store it.
DPF uses |Field| and |FieldsContainer| objects to handle data. The |Field| is a homogeneous array
and a |FieldsContainer| is a labeled collection of |Field|. For more information on DPF data structures
such as the |Field| and their use check the :ref:`ref_tutorials_data_structures` tutorials section.

:jupyter-download-script:`Download tutorial as Python script<field_with_custom_data>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<field_with_custom_data>`

Define the data
---------------

In this tutorial, we create different Fields from data stored in Python lists.

Create the python lists with the data to be *set* to the Fields.

.. jupyter-execute::

    # Data for the scalar Fields (lists with 1 and 2 dimensions)
    data_1 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    data_2 = [[12.0, 7.0, 8.0], [ 9.0, 31.0, 1.0]]

    # Data for the vector Fields (lists with 1 and 2 dimensions)
    data_3 = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]
    data_4 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 9.0, 7.0, 8.0, 10.0]
    data_5 = [[8.0, 4.0, 3.0], [31.0, 5.0, 7.0]]

    # Data for the matrix Fields
    data_6 = [3.0, 2.0, 1.0, 7.0]
    data_7 = [15.0, 3.0, 9.0, 31.0, 1.0, 42.0, 5.0, 68.0, 13.0]
    data_8 = [[12.0, 7.0, 8.0], [ 1.0, 4.0, 27.0], [98.0, 4.0, 6.0]]

Create the python lists with the data to be *appended* to the Fields.

.. jupyter-execute::

    # Data for the scalar Fields
    data_9 = [24.0]

    # Data for the vector Fields
    data_10 = [47.0, 33.0, 5.0]

    # Data for the matrix Fields
    data_11 = [8.0, 2.0, 4.0, 64.0, 32.0, 47.0, 11.0, 23.0, 1.0]


Create the Fields
-----------------

In this tutorial, we explain how to create the following Fields:

- Scalar Field;
- Vector Field;
- Matrix Field.

.. note::

    A |Field| must always be given:

    - A |location| and a |Scoping|.

      Here, we create Fields in the default *'Nodal'* |location|. Thus, each entity (here, the nodes) must
      have a |Scoping| id, that can be defined in a random or in a numerical order:

      - If you want to *set* a data array to the |Field|, you must previously set the |Scoping| ids using the |Field.scoping| method.
      - If you want to *append* an entity with a data array to the |Field|, you don't need to previously set the |Scoping| ids.

    - A |nature| and a |dimensionality| (number of data components for each entity). They must respect the type and size of the
      data to be stored in the |Field|.

Import the PyDPF-Core library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, import the PyDPF-Core library.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf

Define the Fields sizing
^^^^^^^^^^^^^^^^^^^^^^^^

The second step consists in defining the Fields dimensions.

.. tab-set::

    .. tab-item:: Scalar fields

        Here, we create one |Field| with 6 scalar. Thus, 6 entities with one |Scoping| id each.

        .. jupyter-execute::

            # Define the number of entities
            num_entities_1 = 6

        You must ensure that this |Field| has a *'scalar'* |nature| and an *'1D'* |dimensionality|.

    .. tab-item:: Vector fields

        Here, we create:

        - One |Field| with 2 vectors (thus, 2 entities) of 3 components each (3D vector |Field|);
        - One |Field| with 2 vectors (thus, 2 entities) of 5 components each (5D vector |Field|);

        .. jupyter-execute::

            # Define the number of entities
            num_entities_2 = 2

        You must ensure that these Fields have a *'vector'* |nature| and the corresponding |dimensionality|
        (*'3D'* and *'5D'*).

    .. tab-item:: Matrix fields

        Here, we create:

        - One Field with 1 matrix (thus, 1 entity) of 2 lines and 2 columns;
        - Two Fields with 1 matrix (thus, 1 entity) of 3 lines and 3 columns (tensor).

        .. jupyter-execute::

            # Define the number of entities
            num_entities_3 = 1

        You must ensure that these Fields have a *'matrix'* |nature| and the corresponding |dimensionality|.

Create the Fields objects
^^^^^^^^^^^^^^^^^^^^^^^^^

You can create the Fields using two approaches:

- :ref:`Instantianting the Field object<ref_create_field_instance>`;
- :ref:`Using the fields_factory module<ref_create_field_fields_factory>`.

.. _ref_create_field_instance:

Create a |Field| by an instance of this object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

    .. tab-item:: Scalar fields

        .. jupyter-execute::

            # Define the number of entities
            num_entities_1 = 6

        You must ensure that this |Field| has a *'scalar'* |nature| and an *'1D'* |dimensionality|.

        For this approach, the default |nature| of the |Field| object is *'vector'*. You can modify it directly with the
        *'nature'* argument or with the |Field.dimensionality| method.

        Create the scalar |Field| and use the *'nature'* argument.

        .. jupyter-execute::

            # Instanciate the Field
            field_11 = dpf.Field(nentities=num_entities_1, nature=dpf.common.natures.scalar)

            # Set the scoping ids
            field_11.scoping.ids = range(num_entities_1)

            # Print the Field
            print("Scalar Field: ", '\n',field_11, '\n')

        Create the scalar |Field| and use the |Field.dimensionality| method.

        .. jupyter-execute::

            # Instanciate the Field
            field_12 = dpf.Field(nentities=num_entities_1)

            # Use the Field.dimensionality method
            field_12.dimensionality = dpf.Dimensionality([1])

            # Set the scoping ids
            field_12.scoping.ids = range(num_entities_1)

            # Print the Field
            print("Scalar Field : ", '\n',field_12, '\n')

    .. tab-item:: Vector fields

        Here, we create:

        - One |Field| with 2 vectors (thus, 2 entities) of 3 components each (3D vector |Field|);
        - One |Field| with 2 vectors (thus, 2 entities) of 5 components each (5D vector |Field|);

        .. jupyter-execute::

            # Define the number of entities
            num_entities_2 = 2

        You must ensure that these Fields have a *'vector'* |nature| and the corresponding |dimensionality| (*'3D'* and *'5D'*).

        For this approach, the default |nature| is *'vector'* and the default |dimensionality| is *'3D'*. So for the second vector
        |Field| you must set a *'5D'* |dimensionality| using the |Field.dimensionality| method.

        Create the *'3D'* vector Field.

        .. jupyter-execute::

            # Instantiate the Field
            field_21 = dpf.Field(nentities=num_entities_2)

            # Set the scoping ids
            field_21.scoping.ids = range(num_entities_2)

            # Print the Field
            print("3D vector Field : ", '\n',field_21, '\n')

        Create the *'5D'* vector Field.

        .. jupyter-execute::

            # Instantiate the Field
            field_31 = dpf.Field(nentities=num_entities_2)

            # Use the Field.dimensionality method
            field_31.dimensionality = dpf.Dimensionality([5])

            # Set the scoping ids
            field_31.scoping.ids = range(num_entities_2)

            # Print the Field
            print("5D vector Field (5D): ", '\n',field_31, '\n')

.. _ref_create_field_fields_factory:

Create a |Field| using the |fields_factory| module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

    .. tab-item:: Scalar fields

        You can use two functions from the |fields_factory| module to create a scalar |Field|:

        - The |create_scalar_field| function;
        - The |field_from_array| function.

        **Create the Field using the create_scalar_field function**

        For this approach, the default |nature| of the |Field| object is *'scalar'* and the default |dimensionality| is *'1D'*.
        Thus, you just have to use the |create_scalar_field| function to create a scalar |Field|.

        .. jupyter-execute::

            # Create the scalar Field
            field_13 = dpf.fields_factory.create_scalar_field(num_entities=num_entities_1)

            # Set the scoping ids
            field_13.scoping.ids = range(num_entities_1)

            # Print the Field
            print("Scalar Field: ", '\n',field_13, '\n')

        **Create the Field using the field_from_array function**

        Different from the other approaches, where you set or append the data after creating the |Field|, here, the data is
        used as an input of the |field_from_array| function.

        This function gets an Numpy array or Python list of either:

        - 1 dimension (one array). In this case, you get directly a scalar |Field|;
        - 2 dimensions (one array containing multiple arrays with 3 components each). In the is case, you get a 3D vector |Field|.
          Thus, you have to change the |Field| |dimensionality| using the |Field.dimensionality| method.

        Create the scalar Field with an 1 dimensional list.

        .. jupyter-execute::

            # Use the field_from_array function
            field_14 = dpf.fields_factory.field_from_array(arr=data_1)

            # Set the scoping ids
            field_14.scoping.ids = range(num_entities_1)

            # Print the Field
            print("Scalar Field: ", '\n',field_14, '\n')

        Create the scalar Field with a 2 dimensional list.

        .. jupyter-execute::

            # Use the field_from_array function
            field_15 = dpf.fields_factory.field_from_array(arr=data_2)

            # Use the |Field.dimensionality| method
            field_15.dimensionality = dpf.Dimensionality([1])

            # Set the scoping ids
            field_15.scoping.ids = range(num_entities_1)

            # Print the Field
            print("Scalar Field (b): ", '\n',field_15, '\n')


    .. tab-item:: Vector fields

        You can use three functions from the |fields_factory| module to create a vector |Field|:

        - The |create_vector_field| function;
        - The |create_3d_vector_field| function (Specifically to create a 3D vector |Field|
          (a vector |Field| with 3 components for each entity));
        - The |field_from_array| function.

        **Create the Field using the create_vector_field() function**

        For this approach, the default |nature| is *'vector'*. To define the |dimensionality| you must use the *'num_comp'* argument.

        Create the *'3D'* vector Field.

        .. jupyter-execute::

            # Use the create_vector_field function
            field_22 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=3)

            # Set the scoping ids
            field_22.scoping.ids = range(num_entities_2)

            # Print the Field
            print("3D vector Field : ", '\n',field_22, '\n')

        Create the *'5D'* vector Field.

        .. jupyter-execute::

            # Use the create_vector_field function
            field_32 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=5)

            # Set the scoping ids
            field_32.scoping.ids = range(num_entities_2)

            # Print the Field
            print("5D vector Field : ", '\n',field_32, '\n')

        **Create a 3d vector Field using the create_3d_vector_field() function**

        For this approach, the default |nature| is *'vector'* and the |dimensionality| is *'3D'*. Thus, you just
        have to use the |create_3d_vector_field| function to create a 3D vector |Field|.

        .. jupyter-execute::

            # Create the 3d vector Field
            field_25 = dpf.fields_factory.create_3d_vector_field(num_entities=num_entities_2)
            # Set the scoping ids
            field_25.scoping.ids = range(num_entities_2)

            # Print the Field
            print("Vector Field (3D): ", '\n',field_25, '\n')

        **Create the Field using the field_from_array() function**

        Different from the other approaches, where you set or append the data after creating the |Field|, here, the data is
        used as an input of the |field_from_array| function.

        This function gets an Numpy array or Python list of either:

        - 1 dimension (one array). In this case, you have to change the |Field| |dimensionality| using the
          |Field.dimensionality| method.
        - 2 dimensions (one array containing multiple arrays with 3 components). In the is case, you get a 3D vector |Field|.

        .. note::

            The |Field| must always assure a homogeneous shape. The shape is a tuple with the number of elementary data and the
            number of components.

            So, for the *'5D* vector |field| we would want a shape of (10,5). Nevertheless, the 2 dimensions data vector we
            defined ("data_5") has a elementary data count of 6 (2*3). Thus, we cannot define the *'5D'* vector |Field| because it would
            have a (6,5) shape.

        Create the *'3D'* vector Field with an 1 dimensional list.

        .. jupyter-execute::

            # Use the field_from_array function
            field_23 = dpf.fields_factory.field_from_array(arr=data_3)

            # Use the Field.dimensionality method
            field_23.dimensionality = dpf.Dimensionality([3])

            # Set the scoping ids
            field_23.scoping.ids = range(num_entities_2)

            # Print the Field
            print("3D vector Field: ", '\n',field_23, '\n')

        Create the *'3D'* vector Field and give a 2 dimensional list.

        .. jupyter-execute::

            # Use the field_from_array function
            field_24 = dpf.fields_factory.field_from_array(arr=data_5)

            # Set the scoping ids
            field_24.scoping.ids = range(num_entities_2)

            # Print the Field
            print("3D vector Field: ", '\n',field_24, '\n')

    .. tab-item:: Matrix fields

        You can create a matrix |Field| using the |create_matrix_field| function from the |fields_factory| module.

        The default |nature| here is *'matrix'*. Thus, you only have to define the matrix |dimensionality| using the
        *'num_lines'* and *'num_col'* arguments.

        Create the (2,2) matrix Field.

        .. jupyter-execute::

            # Use the create_matrix_field function
            field_41 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=2, num_col=2)

            # Set the scoping ids
            field_41.scoping.ids = range(num_entities_3)

            # Print the Field
            print("Matrix Field (2,2) : ", '\n',field_41, '\n')

        Create the (3,3) matrix Fields.

        .. jupyter-execute::

            # Use the create_matrix_field function
            field_51 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=3, num_col=3)
            field_52 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=3, num_col=3)

            # Set the scoping ids
            field_51.scoping.ids = range(num_entities_3)
            field_52.scoping.ids = range(num_entities_3)

            # Print the Field
            print("Matrix Field 1 (3,3) : ", '\n',field_51, '\n')
            print("Matrix Field 2 (3,3) : ", '\n',field_52, '\n')

Set data to the Fields
----------------------

To set a data array to a |Field| use the |Field.data| method. The |Field| |Scoping| defines how the data is ordered.
For example: the first id in the scoping identifies to which entity the first data entity belongs to.

The data can be in a 1 dimension (one array) or 2 dimensions (one array containing multiple arrays)
Numpy array or Python list. When attributed to a |Field|, these data arrays are reshaped to respect
the |Field| definition.

.. tab-set::

    .. tab-item:: Scalar fields

        Set the data from a 1 dimensional array to the scalar Field.

        .. jupyter-execute::

            # Set the data
            field_11.data = data_1

            # Print the Field
            print("Scalar Field : ", '\n',field_11, '\n')

            # Print the Fields data
            print("Data scalar Field : ", '\n',field_11.data, '\n')

        Set the data from a 2 dimensional array to the scalar Field.

        .. jupyter-execute::

            # Set the data
            field_12.data = data_2

            # Print the Field
            print("Scalar Field : ", '\n',field_12, '\n')

            # Print the Fields data
            print("Data scalar Field : ", '\n',field_12.data, '\n')

    .. tab-item:: Vector fields

        Set the data from a 1 dimensional array to the *'3D'* vector Field.

        .. jupyter-execute::

            # Set the data
            field_21.data = data_3

            # Print the Field
            print("Vector Field : ", '\n',field_21, '\n')

            # Print the Fields data
            print("Data vector Field: ", '\n',field_21.data, '\n')

        Set the data from a 1 dimensional array to the *'5D'* vector Field.

        .. jupyter-execute::

            # Set the data
            field_31.data = data_4

            # Print the Field
            print("Vector Field: ", '\n',field_31, '\n')

            # Print the Fields data
            print("Data vector Field : ", '\n',field_31.data, '\n')

        Set the data from a 2 dimensional array to the *'3D'* vector Field.

        .. jupyter-execute::

            # Set the data
            field_22.data = data_5

            # Print the Field
            print("Vector Field: ", '\n',field_22, '\n')

            # Print the Fields data
            print("Data vector Field: ", '\n',field_22.data, '\n')

    .. tab-item:: Matrix fields

        Set the data from a 1 dimensional array to the (2,2) matrix Field.

        .. jupyter-execute::

            # Set the data
            field_41.data = data_6

            # Print the Field
            print("Matrix Field: ", '\n',field_41, '\n')

            # Print the Fields data
            print("Data matrix Field: ", '\n',field_41.data, '\n')

        Set the data from a 1 dimensional array to the (3,3) matrix Field.

        .. jupyter-execute::

            # Set the data
            field_51.data = data_7

            # Print the Field
            print("Matrix Field: ", '\n',field_51, '\n')

            # Print the Fields data
            print("Data matrix Field: ", '\n',field_51.data, '\n')

        Set the data from a 2 dimensional array to the (3,3) matrix Field.

        .. jupyter-execute::

            # Set the data
            field_52.data = data_8

            # Print the Field
            print("Matrix Field: ", '\n',field_51, '\n')

            # Print the Fields data
            print("Data matrix Field: ", '\n',field_51.data, '\n')

Append data to the Fields
-------------------------

You can append a data array to a |Field|, this means adding a new entity with the new data in the |Field|. You have to
give the |Scoping| id that this entities will have.

.. tab-set::

    .. tab-item:: Scalar fields

        Append data to a scalar |Field|.

        .. jupyter-execute::

            # Append the data
            field_11.append(scopingid=6, data=data_9)

            # Print the Field
            print("Scalar Field : ", '\n',field_11, '\n')

            # Print the Fields data
            print("Data scalar Field: ", '\n',field_11.data, '\n')

    .. tab-item:: Vector fields

        Append data to a vector |Field|.

        .. jupyter-execute::

            # Append the data
            field_21.append(scopingid=2, data=data_10)

            # Print the Field
            print("Vector Field : ", '\n',field_21, '\n')

            # Print the Fields data
            print("Data vector Field: ", '\n',field_21.data, '\n')


    .. tab-item:: Matrix fields

        Append data to a matrix |Field|.

        .. jupyter-execute::

            # Append the data
            field_51.append(scopingid=1, data=data_11)

            # Print the Field
            print("VMatrix Field : ", '\n',field_51, '\n')

            # Print the Fields data
            print("Data Matrix Field: ", '\n',field_51.data, '\n')

Create a |FieldsContainer|
--------------------------

A |FieldsContainer| is a collection of |Field| ordered by labels. Each |Field| of the |FieldsContainer| has
an ID for each label. These ids allow splitting the fields on any criteria.

The most common |FieldsContainer| have the label *'time'* with ids corresponding to time sets. The label *'complex'*,
which is used in a harmonic analysis for example, allows real parts (id=0) to be separated from imaginary parts (id=1).

For more information on DPF data structures, see the :ref:`ref_tutorials_data_structures` tutorials section.

You can create a |FieldsContainer| by:

- :ref:`Instantiating the FieldsContainer object<ref_fields_container_instance>`;
- :ref:`Using the fields_container_factory module<ref_fields_container_factory_module>`.

.. _ref_fields_container_instance:

Create a |FieldsContainer| by an instance of this object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After defining a |FieldsContainer| by an instance of this object you need to set the labels. Here, we define
Fields over time steps labels. So, when you add a |Field| to the |FieldsContainer| you must specify the time step id
it belongs to.

.. jupyter-execute::

    # Create the FieldsContainer object
    fc_1 = dpf.FieldsContainer()

    # Define the labels
    fc_1.add_label(label="time")

    # Add the Fields
    fc_1.add_field(label_space={"time": 0}, field=field_21)
    fc_1.add_field(label_space={"time": 1}, field=field_31)

    # Print the FieldsContainer
    print(fc_1)

.. _ref_fields_container_factory_module:

Create a |FieldsContainer| with the |fields_container_factory| module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |fields_container_factory| module contains functions that create a |FieldsContainer| with predefined
labels. Here, we use the |over_time_freq_fields_container| function that create a |FieldsContainer| with a *'time'*
label.

.. jupyter-execute::

    # Create the FieldsContainer
    fc_2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field_21, field_31])

    # Print the FieldsContainer
    print(fc_2)