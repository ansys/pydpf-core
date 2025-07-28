.. _ref_tutorials_data_arrays:

===========
Data Arrays
===========

.. |Field| replace::  :class:`Field <ansys.dpf.core.field.Field>`
.. |MeshInfo| replace::  :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>`
.. |MeshedRegion| replace::  :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
.. |StringField| replace:: :class:`StringField <ansys.dpf.core.string_field.StringField>`
.. |CustomTypeField| replace:: :class:`CustomTypeField <ansys.dpf.core.custom_type_field.CustomTypeField>`

To process your data with DPF, you must format it according to the DPF data model.
You can achieve this either by using DPF data readers on result files, or by using 
data to build DPF data storage containers.

It is important to be aware of how the data is structured in those containers to understand how to create them and how operators process them.

The data containers can be:

    - **Raw data storage structures**: data arrays (such as a ``Field``) or data maps (such as a ``DataTree``)
    - **Collections**: homogeneous groups of labeled raw data storage structures (such as a ``FieldsContainer`` for a group of labeled fields)

This tutorial presents how to define and manipulate DPF data arrays specifically.

Introduction
------------

A data array in DPF usually represents a mathematical field, hence the base name ``Field``.

Different types of ``Field`` store different data types:

    - a |Field| stores float values
    - a |StringField| stores string values
    - a |PropertyField| stores integer values
    - a |CustomTypeField| stores values of a custom type (among valid numpy.dtype)

A ``Field`` is always associated to:

    - a ``location``, which defines the type entity the data applies to.
      You can check the :class:`locations <ansys.dpf.core.common.locations>` list to know what is available.
      Locations related to mesh entities include: ``nodal``, ``elemental``, or ``elemental_nodal``, ``zone``, ``faces``.
      Locations related to time, frequency, or mode are ``modal``, ``time_freq``, and ``time_freq_step``.

    - a ``scoping``, which is the list of entity IDs each data point in the ``Field`` relates to.
      For example, the ``scoping`` of a ``nodal`` ``Field`` represents a list of node IDs.
      It can represent a subset of the ``support`` of the field.
      The data in a ``Field`` is ordered the same way as the IDs in its ``scoping``.

    - a ``support``, which is a data container holding information about the model for the type of entity the ``location`` targets.
      If the ``location`` relates to mesh entities such as nodes or elements, the ``support`` of the ``Field`` is an object holding data
      related to the mesh, called a ``MeshedRegion``.

    - a ``dimensionality``, which gives the structure of the data based on the number of components and dimensions.
      Indeed, a DPF ``Field`` can store data for a 3D vector field, a scalar field, a matrix field,
      but also store data for a multi-component field (for example, a symmetrical matrix field for each component of the stress field).

    - a ``data`` array, which holds the actual data in a vector, accessed according to the ``dimensionality``.


Create fields based on result files
-----------------------------------

In this tutorial we are going to use the result file from a fluid analysis to showcase the
|Field|, |PropertyField|, and |StringField|.

The :class:`Model <ansys.dpf.core.model.Model>` class creates and evaluates common readers for the files it is given,
such as a mesh provider, a result info provider, and a streams provider.
It provides dynamically built methods to extract the results available in the files, as well as many shortcuts
to facilitate exploration of the available data.

.. jupyter-execute::

    # Import the ansys.dpf.core module as ``dpf``
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Create a data source targeting the example file
    my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
    # Create a model from the data source
    my_model = dpf.Model(data_sources=my_data_sources)
    # Print information available for the analysis
    print(my_model)

The |MeshInfo| class stores information relative to the |MeshedRegion| of the analysis.
It stores some of its data as fields of strings or fields of integers, which we extract next.

.. jupyter-execute::

    # Get the mesh metadata
    my_mesh_info = my_model.metadata.mesh_info
    print(my_mesh_info)

.. tab-set::

    .. tab-item:: Field

        You can obtain a |Field| from a model by requesting a result.

        .. jupyter-execute::

            # Request the collection of temperature result fields from the model and take the first one.
            my_temp_field = my_model.results.temperature.eval()[0]
            # Print the field
            print(my_temp_field)

        The field is located on nodes since it stores the displacement at each node.

    .. tab-item:: StringField

        You can obtain a |StringField| from a |MeshInfo| by requesting the names of the zones in the model.

        .. jupyter-execute::

            # Request the name of the face zones in the fluid analysis
            my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
            # Print the field of strings
            print(my_string_field)

        The field is located on zones since it stores the name of each zone.

    .. tab-item:: PropertyField

        You can obtain a |PropertyField| from a |MeshInfo| by requesting the element types in the mesh.

        .. jupyter-execute::

            # Get the body_face_topology property field
            my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
            # Print the field of integers
            print(my_property_field)

        The field is located on elements since it stores the element type ID for each element.

Create fields from scratch
--------------------------

You can also create a |Field|, |StringField| or |PropertyField| from scratch based on your data.

.. tab-set::

    .. tab-item:: Field

        First create a 3D vector field defined for two nodes.

        .. jupyter-execute::

            # Create a 3D vector field ready to hold data for two entities
            # The constructor creates 3D vector fields by default
            my_field = dpf.Field(nentities=2)
            # Set the data values as a flat vector
            my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            # Associate the data to nodes
            my_field.location = dpf.locations.nodal
            # Set the IDs of the nodes the data applies to
            my_field.scoping.ids = [1, 2]
            # Define the unit (only available for the Field type)
            my_field.unit = "m"
            # Print the field
            print(my_field)

        Now create a 3x3 symmetric matrix field defined for a single element.

        .. jupyter-execute::

            # Set the nature to symmatrix
            my_field = dpf.Field(nentities=1, nature=dpf.natures.symmatrix)
            # The symmatrix dimensions defaults to 3x3
            # Set the data values as a flat vector
            my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            # Associate the data to elements
            my_field.location = dpf.locations.elemental
            # Set the IDs of the nodes the data applies to
            my_field.scoping.ids = [1]
            # Define the unit (only available for the Field type)
            my_field.unit = "Pa"
            # Print the field
            print(my_field)

        Now create a 2x3 matrix field defined for a single fluid element face.

        .. jupyter-execute::

            # Set the nature to matrix and the location to elemental
            my_field = dpf.Field(nentities=1, nature=dpf.natures.matrix)
            # Set the matrix dimensions to 2x3
            my_field.dimensionality = dpf.Dimensionality(dim_vec=[2, 3], nature=dpf.natures.matrix)
            # Set the data values as a flat vector
            my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            # Associate the data to faces
            my_field.location = dpf.locations.faces
            # Set the IDs of the face the data applies to
            my_field.scoping.ids = [1]
            # Define the unit (only available for the Field type)
            my_field.unit = "mm"
            # Print the field
            print(my_field)

    .. tab-item:: StringField

        .. jupyter-execute::

            # Create a string field with data for two elements
            my_string_field = dpf.StringField(nentities=2)
            # Set the string values
            my_string_field.data = ["string_1", "string_2"]
            # Set the location
            my_string_field.location = dpf.locations.elemental
            # Set the element IDs
            my_string_field.scoping.ids = [1, 2]
            # Print the string field
            print(my_string_field)

    .. tab-item:: PropertyField

        .. jupyter-execute::

            # Create a property field with data for two modes
            my_property_field = dpf.PropertyField(nentities=2)
            # Set the data values
            my_property_field.data = [12, 25]
            # Set the location
            my_property_field.location = dpf.locations.modal
            # Set the element IDs
            my_property_field.scoping.ids = [1, 2]
            # Print the property field
            print(my_property_field)

Create a |Field| with the fields_factory
----------------------------------------

The :mod:`fields_factory <ansys.dpf.core.fields_factory>` module provides helpers to create a |Field|:

- Use :func:`create_scalar_field <ansys.dpf.core.fields_factory.create_scalar_field>` to create a scalar field:

.. jupyter-execute::

    # Create a scalar field ready to hold data for two entities
    # The field is nodal by default
    my_field = dpf.fields_factory.create_scalar_field(num_entities=2)
    my_field.data = [1.0, 2.0]
    my_field.scoping.ids = [1, 2]
    # Print the field
    print(my_field)

- Use :func:`create_vector_field <ansys.dpf.core.fields_factory.create_vector_field>` to create a generic vector field:

.. jupyter-execute::

    # Create a 2D vector field ready to hold data for two entities
    # The field is nodal by default
    my_field = dpf.fields_factory.create_vector_field(num_entities=2, num_comp=2)
    my_field.data = [1.0, 2.0, 3.0, 4.0]
    my_field.scoping.ids = [1, 2]
    # Print the field
    print(my_field)

- Use :func:`create_3d_vector_field <ansys.dpf.core.fields_factory.create_3d_vector_field>` to create a 3D vector field:

.. jupyter-execute::

    # Create a 3D vector field ready to hold data for two entities
    # The field is nodal by default
    my_field = dpf.fields_factory.create_3d_vector_field(num_entities=2)
    my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    my_field.scoping.ids = [1, 2]
    # Print the field
    print(my_field)

- Use :func:`create_matrix_field <ansys.dpf.core.fields_factory.create_matrix_field>` to create a generic matrix field:

.. jupyter-execute::

    # Create a 2x3 matrix field ready to hold data for two entities
    # The field is nodal by default
    my_field = dpf.fields_factory.create_matrix_field(num_entities=2, num_lines=2, num_col=3)
    my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    my_field.scoping.ids = [1, 2]
    # Print the field
    print(my_field)

- Use :func:`create_tensor_field <ansys.dpf.core.fields_factory.create_tensor_field>` to create a 3x3 matrix field:

.. jupyter-execute::

    # Create a 3x3 matrix field ready to hold data for two entities
    # The field is nodal by default
    my_field = dpf.fields_factory.create_tensor_field(num_entities=2)
    my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    my_field.scoping.ids = [1, 2]
    # Print the field
    print(my_field)

- Use :func:`create_overall_field <ansys.dpf.core.fields_factory.create_overall_field>` to create a field with a single value for the whole support:

.. jupyter-execute::

    # Create a field storing a value applied to every node in the support
    my_field = dpf.fields_factory.create_overall_field(value=1.0)
    # Print the field
    print(my_field)

- Use :func:`field_from_array <ansys.dpf.core.fields_factory.field_from_array>` to create a scalar, 3D vector, or symmetric matrix field directly from a numpy array or a Python list

.. jupyter-execute::

    # Create a scalar field from a 1D array or a list
    arr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    my_field = dpf.fields_factory.field_from_array(arr=arr)
    # Print the field
    print(my_field)

.. jupyter-execute::

    # Create a 3D vector field from an array or a list
    arr = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    my_field = dpf.fields_factory.field_from_array(arr=arr)
    # Print the field
    print(my_field)

.. jupyter-execute::

    # Create a symmetric matrix field from an array or a list
    arr = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]]
    my_field = dpf.fields_factory.field_from_array(arr=arr)
    # Print the field
    print(my_field)


Access the field metadata
-------------------------

The metadata associated to a field includes its name, its location, its scoping,
the shape of the data stored, its number of components, and its unit.

.. tab-set::

    .. tab-item:: Field

        .. jupyter-execute::

            # Location of the fields data
            my_location = my_temp_field.location
            print("location", '\n', my_location,'\n')

            # Fields scoping
            my_scoping = my_temp_field.scoping  # Location entities type and number
            print("scoping", '\n',my_scoping, '\n')

            my_scoping_ids = my_temp_field.scoping.ids  # Available ids of locations components
            print("scoping.ids", '\n', my_scoping_ids, '\n')

            # Elementary data count
            # Number of the location entities (how many data vectors we have)
            my_elementary_data_count = my_temp_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')

            # Components count
            # Vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z)
            my_component_count = my_temp_field.component_count
            print("components_count", '\n', my_component_count, '\n')

            # Size
            # Length of the data entire vector (equal to the number of elementary data times the number of components.)
            my_field_size = my_temp_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_temp_field.shape
            print("shape", '\n', my_shape, '\n')

            # Units
            my_unit = my_temp_field.unit
            print("unit", '\n', my_unit, '\n')

    .. tab-item:: StringField

        .. jupyter-execute::

            # Location of the fields data
            my_location = my_string_field.location
            print("location", '\n', my_location,'\n')

            # StringFields scoping
            my_scoping = my_string_field.scoping  # Location entities type and number
            print("scoping", '\n',my_scoping, '\n')

            my_scoping_ids = my_string_field.scoping.ids  # Available ids of locations components
            print("scoping.ids", '\n', my_scoping_ids, '\n')

            # Elementary data count
            # Number of the location entities (how many data vectors we have)
            my_elementary_data_count = my_string_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')

            # Components count
            # Data dimension, here we expect one name by zone
            my_component_count = my_string_field.component_count
            print("components_count", '\n', my_component_count, '\n')

            # Size
            # Length of the data entire array (equal to the number of elementary data times the number of components.)
            my_field_size = my_string_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_string_field.shape
            print("shape", '\n', my_shape, '\n')

    .. tab-item:: PropertyField

        .. jupyter-execute::

            # Location of the fields data
            my_location = my_property_field.location
            print("location", '\n', my_location,'\n')

            # Fields scoping
            my_scoping = my_property_field.scoping  # Location entities type and number
            print("scoping", '\n',my_scoping, '\n')

            my_scoping_ids = my_property_field.scoping.ids  # Available ids of locations components
            print("scoping.ids", '\n', my_scoping_ids, '\n')

            # Elementary data count
            # Number of the location entities (how many data vectors we have)
            my_elementary_data_count = my_property_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')

            # Components count
            # Data dimension, we expect to have one id by face that makes part of a body
            my_component_count = my_property_field.component_count
            print("components_count", '\n', my_component_count, '\n')

            # Size
            # Length of the data entire array (equal to the number of elementary data times the number of components.)
            my_field_size = my_property_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_property_field.shape
            print("shape", '\n', my_shape, '\n')

Access the field data
---------------------

A |Field| object is a client-side representation of the field server-side.
When a remote DPF server is used, the data of the field is also stored remotely.

To build efficient remote postprocessing workflows, the amount of data exchanged between the client and the remote server has to be minimal.

This is managed with operators and a completely remote workflow, requesting only the initial data needed to build the workflow, and the output of the workflow.

It is for example important when interacting with remote data to remember that any PyDPF request for the
``Field.data`` downloads the whole array to your local machine.

This is particularly inefficient within scripts handling a large amount of data where the request
is made to perform an action locally which could have been made remotely with a DPF operator.

For example, if you want to know the entity-wise maximum of the field, you should prefer the
``min_max.min_max_by_entity`` operator to the ``array.max()`` method from ``numpy``.


Get the complete array
^^^^^^^^^^^^^^^^^^^^^^

The field's ``data`` is ordered with respect to its ``scoping ids`` (as shown above).
To access the entire data in the field as an array (``numpy`` array``):

.. tab-set::

    .. tab-item:: Field

        .. jupyter-execute::

            my_data_array = my_temp_field.data
            print(my_data_array)

        Note that this array is a genuine, local, numpy array (overloaded by the DPFArray).

        .. jupyter-execute::

            print(type(my_data_array))

    .. tab-item:: StringField

        .. jupyter-execute::

            my_data_array = my_string_field.data
            print(my_data_array)

    .. tab-item:: PropertyField

        .. jupyter-execute::

            my_data_array = my_property_field.data
            print(my_data_array)

Get data for a single entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to access an individual node or element, request it
using either the :func:`get_entity_data()<ansys.dpf.core.field.Field.get_entity_data>` or
:func:`get_entity_data_by_id()<ansys.dpf.core.field.Field.get_entity_data_by_id>` methods:

.. tab-set::

    .. tab-item:: Field

        .. jupyter-execute::

            # Get the data from the third element in the field
            my_temp_field.get_entity_data(index=3)

        .. jupyter-execute::

            # Get the data from the element with id 533
            my_temp_field.get_entity_data_by_id(id=533)

        Note that this would correspond to an index of 2 within the
        field. Be aware that scoping IDs are not sequential. You would
        get the index of element 2 in the field with:

        .. jupyter-execute::

            # Get index of the element with id 533
            my_temp_field.scoping.index(id=533)

While these methods are acceptable when requesting data for a few elements
or nodes, they should not be used when looping over the entire array. For efficiency,
a field's data can be recovered locally before sending a large number of requests:

.. jupyter-execute::

    # Create a deep copy of the field that can be accessed and modified locally.
    with my_temp_field.as_local_field() as f:
        for i in range(1,100):
            f.get_entity_data_by_id(i)
