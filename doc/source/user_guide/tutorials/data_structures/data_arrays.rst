.. _ref_tutorials_data_arrays:

===========
Data Arrays
===========

.. |Field| replace::  :class:`Field <ansys.dpf.core.field.Field>`
.. |MeshInfo| replace::  :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
.. |StringField| replace:: :class:`StringField <ansys.dpf.core.string_field.StringField>`
.. |CustomTypeField| replace:: :class:`CustomTypeField <ansys.dpf.core.custom_type_field.CustomTypeField>`

To process your data with DPF, you must format it according to the DPF data model.
You can achieve this either by using DPF data readers on result files, or by using the data to build DPF data storage containers.

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

Extract a |Field|
~~~~~~~~~~~~~~~~~

You can obtain a |Field| from a model by requesting a result.

.. jupyter-execute::

    # Request the collection of displacement result fields from the model and take the first one.
    my_disp_field = my_model.results.displacement.eval()[0]
    # Print the field
    print(my_disp_field)

The field is located on nodes since it stores the displacement at each node.

Extract a |StringField|
~~~~~~~~~~~~~~~~~~~~~~~

You can obtain a |StringField| from a |MeshInfo| by requesting the names of the zones in the model.

.. jupyter-execute::

    # Request the name of the face zones in the fluid analysis
    my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
    # Print the field of strings
    print(my_string_field)

The field is located on zones since it stores the name of each zone.

Extract a |PropertyField|
~~~~~~~~~~~~~~~~~~~~~~~~~

You can obtain a |PropertyField| from a |MeshInfo| by requesting the element types in the mesh.

.. jupyter-execute::

    # We can get the body_face_topology property for example
    my_property_field = my_mesh_info.get_property(property_name="element_types")
    # Print the field of integers
    print(my_property_field)

The field is located on elements since it stores the element type ID for each element.

Creates fields from scratch
---------------------------

You can also create a |Field|, |StringField| or |PropertyField| from scratch based on your data.

The :mod:`fields_factory <ansys.dpf.core.fields_factory>` module provides helpers to create a |Field|.

Using the class constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            # Create the Field object with 2 entities
            num_entities = 2
            my_field = dpf.Field(nentities=num_entities)
            # By default, the field contains 3d vectors
            # So with 2 entities we need 6 data values
            my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            # Assign a location
            my_field.location = dpf.locations.nodal
            # Define the scoping
            my_field.scoping.ids = range(num_entities)
            # Define the units (only for the Field object)
            my_field.unit = "m"

            print(my_field)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            num_entities = 2
            my_field = dpf.Field(nentities=num_entities)
            my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            my_field.location = dpf.locations.nodal
            my_field.scoping.ids = range(num_entities)
            my_field.unit = "m"
            print(my_field)

    .. tab-item:: StringField

        .. code-block:: python

            # Create the Field object with 2 entities
            num_entities = 2
            my_StringField = dpf.StringField(nentities=num_entities)
            # By default, the field contains 3d vectors
            # So with 2 entities we need 6 data values
            my_StringField.data = ["string_1", "string_2"]
            # Assign a location
            my_StringField.location = dpf.locations.nodal
            # Define the scoping
            my_StringField.scoping.ids = range(num_entities)

            print(my_field)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            num_entities = 2
            my_StringField = dpf.StringField(nentities=num_entities)
            my_StringField.data = ["string_1", "string_2"]
            my_StringField.location = dpf.locations.nodal
            my_StringField.scoping.ids = range(num_entities)
            print(my_StringField)

    .. tab-item:: PropertyField

        .. code-block:: python

            # Create the Field object with 2 entities
            num_entities = 2
            my_PropertyField = dpf.PropertyField(nentities=num_entities)
            # By default, the field contains 3d vectors
            # So with 2 entities we need 6 data values
            my_PropertyField.data = [12, 25]
            # Define the scoping
            my_PropertyField.scoping.ids = range(num_entities)
            # Assign a location
            my_PropertyField.location = dpf.locations.nodal

            print(my_PropertyField)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            num_entities = 2
            my_PropertyField = dpf.PropertyField(nentities=num_entities)
            my_PropertyField.data = [12, 25]
            my_PropertyField.scoping.ids = range(num_entities)
            my_PropertyField.location = dpf.locations.nodal
            print(my_PropertyField)


**2) Evaluated data**

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            # Create the displacement operator
            # Here we use [0] because the displacement operator gives an FieldsContainer as an output
            my_disp_field = my_model.results.displacement.eval()[0]
            # Print the evaluated results output
            print(my_disp_field)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp = my_model.results.displacement()
            print(my_disp.eval())

    .. tab-item:: StringField

        .. code-block:: python

            # Usually the StringField can be found at the mesh_info
            # Get the mesh_info by tht models metadata
            my_mesh_info = my_model_2.metadata.mesh_info
            print(my_mesh_info)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            print(my_mesh_info)

        .. code-block:: python

            # We can get the face_zone_names property for example
            my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
            print(my_string_field)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
            print(my_string_field)

    .. tab-item:: PropertyField

        .. code-block:: python

            # Usually the StringField can be found at the mesh_info
            # Get the mesh_info by tht models metadata
            my_mesh_info = my_model_2.metadata.mesh_info
            print(my_mesh_info)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            print(my_mesh_info)

        .. code-block:: python

            # We can get the body_face_topology property for example
            my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
            print(my_property_field)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
            print(my_property_field)

**3) With the fields_factory module**

.. code-block:: python

    # Define a field with entities that are scalar.
    my_field = dpf.fields_factory.create_scalar_field(num_entities=2)
    # This is a “reserve” mechanism, at the beginning you have 0 entities.
    # This means that you need to append data to grow the size of your field.
    # Gives 2 vectors in the same id
    my_field.append(data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], scopingid=0)

    # Gives 2 vectors in different ids
    my_field.append(data=[1.0, 2.0, 3.0], scopingid=1)
    my_field.append(data=[4.0, 5.0, 6.0], scopingid=2)

    print(my_field)

.. rst-class:: sphx-glr-script-out

 .. exec_code::
    :hide_code:

    from ansys.dpf import core as dpf
    my_field = dpf.fields_factory.create_scalar_field(num_entities=2)
    my_field.append(data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], scopingid=0)
    my_field.append(data=[1.0, 2.0, 3.0], scopingid=1)
    my_field.append(data=[ 4.0, 5.0, 6.0], scopingid=2)
    print(my_field)

Accessing fields metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

A field contains the metadata for the result it is associated with. The metadata
includes the location, the scoping, the shape of the data stored, number of components,
and units of the data.

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            # Location of the fields data
            my_location = my_disp_field.location
            print("location", '\n', my_location,'\n')

            # Fields scoping
            my_scoping = my_disp_field.scoping  # Location entities type and number
            print("scoping", '\n',my_scoping, '\n')

            my_scoping_ids = my_disp_field.scoping.ids  # Available ids of locations components
            print("scoping.ids", '\n', my_scoping_ids, '\n')

            # Elementary data count
            # Number of the location entities (how many data vectors we have)
            my_elementary_data_count = my_disp_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')

            # Components count
            # Vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z)
            my_components_count = my_disp_field.component_count
            print("components_count", '\n', my_components_count, '\n')

            # Size
            # Length of the data entire vector (equal to the number of elementary data times the number of components.)
            my_field_size = my_disp_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_disp_field.shape
            print("shape", '\n', my_shape, '\n')

            # Units
            my_unit = my_disp_field.unit
            print("unit", '\n', my_unit, '\n')

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            my_location = my_disp_field.location
            print("location", '\n', my_location,'\n')
            my_scoping = my_disp_field.scoping
            print("scoping", '\n',my_scoping, '\n')
            print("We have a location entity of type 'Nodal' (consistent with the output of the `location` helper) and 3820 nodes", '\n')
            my_scoping_ids = my_disp_field.scoping.ids
            print("scoping.ids", '\n', my_scoping_ids, '\n')
            my_components_count = my_disp_field.component_count
            print("components_count", '\n', my_components_count, '\n')
            my_elementary_data_count = my_disp_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')
            my_shape = my_disp_field.shape
            print("shape", '\n', my_shape, '\n')
            print("We have a Field with 3820 data vectors (consistent with the number of nodes) and each vector has 3 components (consistent with a displacement vector dimension)", '\n')
            my_unit = my_disp_field.unit
            print("unit", '\n', my_unit, '\n')

    .. tab-item:: StringField

        .. code-block:: python

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
            my_components_count = my_string_field.component_count
            print("components_count", '\n', my_components_count, '\n')

            # Size
            # Length of the data entire array (equal to the number of elementary data times the number of components.)
            my_field_size = my_string_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_string_field.shape
            print("shape", '\n', my_shape, '\n')

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
            my_location = my_string_field.location
            print("location", '\n', my_location,'\n')
            my_scoping = my_string_field.scoping
            print("scoping", '\n',my_scoping, '\n')
            print("We have a location entity of type 'Zone' (consistent with the output of the `location` helper) and 24 zones", '\n')
            my_scoping_ids = my_string_field.scoping.ids
            print("scoping.ids", '\n', my_scoping_ids, '\n')
            my_components_count = my_string_field.component_count
            print("components_count", '\n', my_components_count, '\n')
            my_elementary_data_count = my_string_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')
            my_shape = my_string_field.shape
            print("shape", '\n', my_shape, '\n')
            print("We have a StringField with 24 names (consistent with the number of zones) and each zone has one name", '\n')

    .. tab-item:: PropertyField

        .. code-block:: python

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
            my_components_count = my_property_field.component_count
            print("components_count", '\n', my_component_count, '\n')

            # Size
            # Length of the data entire array (equal to the number of elementary data times the number of components.)
            my_field_size = my_property_field.size
            print("size", '\n', my_field_size, '\n')

            # Fields shape
            # Gives a tuple with the elementary data count and the components count
            my_shape = my_property_field.shape
            print("shape", '\n', my_shape, '\n')

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
            my_location = my_property_field.location
            print("location", '\n', my_location,'\n')
            my_scoping = my_property_field.scoping
            print("scoping", '\n',my_scoping, '\n')
            print("We have a location entity of type 'Body' (consistent with the output of the `location` helper) and  2 bodies", '\n')
            my_scoping_ids = my_property_field.scoping.ids
            print("scoping.ids", '\n', my_scoping_ids, '\n')
            my_components_count = my_property_field.component_count
            print("components_count", '\n', my_components_count, '\n')
            my_elementary_data_count = my_property_field.elementary_data_count
            print("elementary_data_count", '\n', my_elementary_data_count, '\n')
            my_shape = my_property_field.shape
            print("shape", '\n', my_shape, '\n')
            print("We have a Field with 24 face ids (consistent with the number of faces) and each face has one id", '\n')

Accessing fields data
~~~~~~~~~~~~~~~~~~~~~

When DPF-Core returns the |Field| class object,
what Python actually has is a client-side representation of the field,
not the entirety of the field itself. This means that all the data of
the field is stored within the DPF service. This is important because
when building your postprocessing workflows, the most efficient way of
interacting with result data is to minimize the exchange of data between
Python and DPF, either by using operators or by accessing only the data
that is needed.

**1) Helpers**

The field's ``data`` is ordered with respect to its ``scoping ids`` (as shown above).
To access the entire data in the field as an array (``numpy`` array``):

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            my_data_array = my_disp_field.data
            print(my_data_array)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            my_data_array = my_disp_field.data
            print(my_data_array)

        Note that this array is a genuine, local, numpy array (overloaded by the DPFArray).

        .. code-block:: python

            print(type(my_data_array))

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            my_data_array = my_disp_field.data
            print(type(my_data_array))

    .. tab-item:: StringField

        .. code-block:: python

            my_data_array = my_string_field.data
            print(my_data_array)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
            my_data_array = my_string_field.data
            print(my_data_array)

    .. tab-item:: PropertyField

        .. code-block:: python

            my_data_array = my_property_field.data
            print(my_data_array)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            my_mesh_info = my_model_2.metadata.mesh_info
            my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
            my_data_array = my_property_field.data
            print(my_data_array)

**2) Functions**

If you need to access an individual node or element, request it
using either the :func:`get_entity_data()<ansys.dpf.core.field.Field.get_entity_data>` or
:func:`get_entity_data_by_id()<ansys.dpf.core.field.Field.get_entity_data_by_id>` methods:

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            # Get the data from the third element in the field
            my_disp_field.get_entity_data(index=3)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            print(my_disp_field.get_entity_data(index=3))

        .. code-block:: python

            # Get the data from the element with id 533
            my_disp_field.get_entity_data_by_id(id=533)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            print(my_disp_field.get_entity_data_by_id(id=533))

        Note that this would correspond to an index of 2 within the
        field. Be aware that scoping IDs are not sequential. You would
        get the index of element 2 in the field with:

        .. code-block:: python

            # Get index of the element with id 533
            my_disp_field.scoping.index(id=533)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_model = dpf.Model(examples.download_transient_result())
            my_disp_field = my_model.results.displacement.eval()[0]
            print(my_disp_field.scoping.index(id=533))

While these methods are acceptable when requesting data for a few elements
or nodes, they should not be used when looping over the entire array. For efficiency,
a field's data can be recovered locally before sending a large number of requests:

.. code-block:: python

    # Create a deep copy of the field that can be accessed and modified locally.
    with my_disp_field.as_local_field() as f:
        for i in range(1,100):
            f.get_entity_data_by_id(i)

Note on the field data
~~~~~~~~~~~~~~~~~~~~~~

It is important when interacting with remote data to remember that any PyDPF request for the
``Field.data`` downloads the whole array to your local machine.

This is particularly inefficient within scripts handling a large amount of data where the request
is made to perform an action locally which could have been made remotely with a DPF operator.

For example, if you want to know the entity-wise maximum of the field, you should prefer the
``min_max.min_max_by_entity`` operator to the ``array.max()`` method from ``numpy``.
