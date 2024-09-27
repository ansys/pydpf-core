.. _ref_tutorials_data_arrays:

===========
Data Arrays
===========

.. |Field| replace::  :class:`Field <ansys.dpf.core.field.Field>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
.. |StringField| replace:: :class:`StringField <ansys.dpf.core.string_field.StringField>`
.. |CustomTypeField| replace:: :class:`CustomTypeField <ansys.dpf.core.custom_type_field.CustomTypeField>`

When DPF employ operators to manipulate the data, it uses data containers to
store and return it. Therefore, it is important to be aware of how the data is
structured in those containers.

The data containers can be:

    - **Raw data storage structures**: Data arrays (a ``Field`` for example) or Data Maps (a ``DataTree`` for example)
    - **Collections**: a group of same labeled objects from one DPF raw data storage structure (a ``FieldsContainer`` for example, that is a group of ``Fields`` with the same label)

This tutorial presents how some DPF data arrays are defined and manipulated. The main difference between
them is the data type they contain:

    - |Field| :  float;
    - |StringField|: string.
    - |PropertyField|: int;
    - |CustomTypeField|: custom type (numpy.dtype)

Therefore, the first one is typically found when manipulating the results. The two following are
typically found when analysing the mesh and its properties.

Their data is always associated to:

    - A ``location``: What typology of the finite element method was used to give the results. There are different spatial ``locations`` that can be found at: :class:`locations <ansys.dpf.core.common.locations>` but the most used are : ``Nodal``, ``Elemental`` and ``Elemental Nodal``.

    - The ``support``: The simulation basis functions are integrated over a calculus domain, the support of the analysis. This domain is a physical component, usually represented by: a mesh, geometrical component, time or frequency values.

When defining an operator, you must narrow down which parts of the initial data
are relevant for the goals of the analysis. Thus, you must define the data container
scoping.

A field is also defined by its dimensionality, it can for example, describe
a displacement vector or norm, stresses and strains tensors, stresses and strains
equivalent, min max over time of any result...  The data is stored as a vector of
double values and each elementary entity has a number of components (thanks to the
dimensionality, a displacement will have 3 components, a symmetrical stress matrix 6...).

Define the studied results
--------------------------

In this tutorial we are going to use the result file from a transient analysis for the
|Field| and a fluid analysis for the |PropertyField| and |StringField|.

Create the ``model`` object. The :class:`Model <ansys.dpf.core.model.Model>`
class helps to organize access methods for the result by keeping track of the
operators and data sources used by the result file.

.. tab-set::

    .. tab-item:: Field

        .. code-block:: python

            # Import the DPF-Core module as ``dpf``
            from ansys.dpf import core as dpf
            # Import the included examples file.
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_transient_result())
            my_model = dpf.Model(data_sources=my_data_sources)
            print(my_model)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_transient_result())
            my_model = dpf.Model(data_sources=my_data_sources)
            print(my_model)

    .. tab-item:: StringField

        .. code-block:: python

            # Import the DPF-Core module as ``dpf``
            from ansys.dpf import core as dpf
            # Import the included examples file.
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            print(my_model_2)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            print(my_model_2)

    .. tab-item:: PropertyField

        .. code-block:: python

            # Import the DPF-Core module as ``dpf``
            from ansys.dpf import core as dpf
            # Import the included examples file.
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            print(my_model_2)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
            my_model_2 = dpf.Model(data_sources=my_data_sources)
            print(my_model_2)

Scoping
-------

To begin the workflow set up, you need to establish the ``scoping``, that is
a spatial and/or temporal subset of the simulation data.

The field’s scoping also defines how the data is ordered, for example: the first
ID in the scoping identifies to which entity the first data entity belongs.

The following explanations concern only the |Field| manipulation. Since the |StringField|
and |PropertyField| are mostly an informational tool, you can only extract and visualize
the analysis scoping.

If the scoping is not specified the operators will only use the final result data.
For example, we can see in our model that the displacement results are available
with a time support.

.. code-block:: python

    # create the displacement operator
    my_disp = my_model.results.displacement()
    # Print the evaluated results output
    print(my_disp.eval())

.. rst-class:: sphx-glr-script-out

 .. exec_code::
    :hide_code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    my_model = dpf.Model(examples.download_transient_result())
    my_disp = my_model.results.displacement()
    print(my_disp.eval())


To define the scope we have to make two considerations: the location and the
support of interest:

    1) The location: which component will be enumerated (list of nodes for example)
    2) The support: the list is relative about which domain (list of nodes of a given, meshed region)

Therefore, we have two main supports to scope in: time and mesh domains. You specify
the set of components by defining a range of IDs:

.. image:: ../../images/drawings/scoping-eg.png

Creating a scoping object
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Scoping`` object can be created by the :class:`Scoping <ansys.dpf.core.scoping.Scoping>`
class or with a scoping factory:

**Time scoping**

.. code-block:: python

    # 1) Using the Scoping class
    my_time_scoping = dpf.Scoping(ids=[14, 15, 16, 17], location=dpf.locations.time_freq)

    # 2) Using the time_freq_scoping_factory class
    # a. Define a time list that targets the times ids 14, 15, 16, 17
    my_time_list = [14, 15, 16, 17]
    # b. Create the time scoping object
    my_time_scoping = dpf.time_freq_scoping_factory.scoping_by_sets(cumulative_sets=my_time_list)

**Mesh scoping**

.. code-block:: python

    # 1) Using the Scoping class in a nodal location
    my_mesh_scoping = dpf.Scoping(ids=[103, 204, 334, 1802], location=dpf.locations.nodal)

    # 2) Using the mesh_scoping_factory class
    # a. Define a nodes list that targets the nodes with the ids 103, 204, 334, 1802
    my_nodes_ids = [103, 204, 334, 1802]
    # b. Create the mesh scoping object
    my_mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping(node_ids=my_nodes_ids)

Using the scoping object
~~~~~~~~~~~~~~~~~~~~~~~~

The ``Scoping`` object can be assign to an operator by using ``Model`` helpers or
directly in the operator indentation if it assumes a scoping as an argument:

**Time scoping**

.. code-block:: python

    # 3) Using the on_time_scoping() helper
    my_disp = my_model.results.displacement.on_time_scoping(time_scoping=[14, 15, 16, 17])
    # or
    my_disp = my_model.results.displacement.on_time_scoping(time_scoping=my_time_scoping)

    # 4) Directly with the operator indentation
    my_disp = my_model.results.displacement(time_scoping= my_time_scoping)

**Mesh scoping**

.. code-block:: python

    # 3) Using the on_time_scoping() helper
    my_disp = my_model.results.displacement.on_mesh_scoping(mesh_scoping=[103, 204, 334, 1802])
    # or
    my_disp = my_model.results.displacement.on_mesh_scoping(mesh_scoping=my_mesh_scoping)

    # 4) Directly with the operator indentation
    my_disp = my_model.results.displacement(mesh_scoping=my_mesh_scoping)

The final operator with those scopes would look like:

.. code-block:: python

    # Time scoping targets the times ids 14, 15, 16, 17
    # Mesh scoping targets the nodes with the ids 103, 204, 334, 1802
    my_disp = my_model.results.displacement(time_scoping=my_time_scoping, mesh_scoping=my_mesh_scoping)
    print(my_disp.eval())

.. rst-class:: sphx-glr-script-out

 .. exec_code::
    :hide_code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    my_model = dpf.Model(examples.download_transient_result())
    my_mesh_scoping = dpf.Scoping(ids=[103, 204, 334, 1802], location=dpf.locations.nodal)
    my_disp = my_model.results.displacement(time_scoping=[14, 15, 16, 17], mesh_scoping=my_mesh_scoping)
    print(my_disp.eval())

Other scope helpers are available at: :class:`Result <ansys.dpf.core.results.Result>`.

Specific examples about how to implement some scopings can be found at:

    - :mod:`Scope results over time domain <ref_results_over_time>`
    - :mod:`Scope results over space domain <ref_results_over_space>`

Fields
------

Each part of this subsection explain how to explore the data in the studied data arrays.

Defining a field
~~~~~~~~~~~~~~~~

A |Field|, |StringField| or |PropertyField| can be created directly by instantiating an object
of their classes or they can be evaluated data from an operator. In particular, a
|Field| can also be created with the functions in the :mod:`fields_factory <ansys.dpf.core.fields_factory>`
module:

**Class object instance**

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

Operate on field data
~~~~~~~~~~~~~~~~~~~~~

Oftentimes, you do not need to directly act on the data of an array within
Python. For example, if you want to know the maximum of the data, you can
use the ``array.max()`` method to compute the maximum of the array with the
``numpy`` package.

However, this requires sending the entire array to Python and then computing
the maximum there.

Rather than copying the array over and computing the maximum in Python, you can
instead compute the maximum directly from the field itself.

Here we the ``min_max`` operator (through a fields helper) to compute
the maximum of the displacement field and return a field with only the max values:

.. code-block:: python

    # Returns the maximum value for each component
    # So with displacement results we expect having a field with :
    # - 3 elementary data (one for each dimension)
    # - 1 component (each entity will have a value for one dimension (X, Y or Z))
    my_max = my_disp_field.max()
    print(my_max)

.. rst-class:: sphx-glr-script-out

 .. exec_code::
    :hide_code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    my_model = dpf.Model(examples.download_transient_result())
    my_disp_field = my_model.results.displacement.eval()[0]
    print(my_disp_field.max())

You can for example get the element or node ID of the maximum value.

.. code-block:: python

    my_disp_field.max()
    print(my_disp_field.scoping.ids)

.. rst-class:: sphx-glr-script-out

 .. exec_code::
    :hide_code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    my_model = dpf.Model(examples.download_transient_result())
    my_disp_field = my_model.results.displacement.eval()[0]
    my_disp_field.max()
    print(my_disp_field.scoping.ids)