.. _ref_tutorials_mapping_solid_to_skin:

=======================
Solid-to-skin mapping
=======================

.. |solid_to_skin| replace:: :class:`solid_to_skin<ansys.dpf.core.operators.mapping.solid_to_skin>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |MeshedRegion| replace:: :class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model<ansys.dpf.core.model.Model>`

Transfer field data from a volume mesh to a surface mesh.

This tutorial demonstrates how to use the |solid_to_skin| operator to map field
data defined on solid (volume) elements to field data on skin (surface) elements.
This is useful when you need to visualize or analyze results on the external
surface of a model, or when transferring data between different mesh representations.

The operator handles three different field data locations:

- **Elemental**: Values from solid elements are copied to the skin elements they underlie
- **Nodal**: The field is rescoped to the nodes of the skin mesh
- **ElementalNodal**: Values are copied for each element face and its associated nodes

:jupyter-download-script:`Download tutorial as Python script<mapping_solid_to_skin>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<mapping_solid_to_skin>`

Import modules and load the model
----------------------------------

First, import the required modules and load a result file.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf

    # Import the examples module
    from ansys.dpf.core import examples

    # Import the operators module
    from ansys.dpf.core import operators as ops

.. jupyter-execute::

    # Download and load a result file
    result_file = examples.find_static_rst()

    # Create a Model object
    model = dpf.Model(data_sources=result_file)

    # Print model information
    print(model)

Extract the solid mesh
----------------------

Extract the full mesh from the model, which contains both solid and surface elements.

.. jupyter-execute::

    # Get the solid (full) mesh from the model
    solid_mesh = model.metadata.meshed_region

    # Print mesh information
    print(solid_mesh)

    # Print element information
    print(f"\nTotal number of elements: {solid_mesh.elements.n_elements}")
    print(f"Total number of nodes: {solid_mesh.nodes.n_nodes}")

Create or extract the skin mesh
--------------------------------

Create a skin mesh representing the external surface of the model.

.. jupyter-execute::

    # Create a skin mesh from the solid mesh
    # The skin mesh contains only the external surface elements
    skin_mesh_op = ops.mesh.external_layer(mesh=solid_mesh)
    skin_mesh = skin_mesh_op.eval()

    # Print skin mesh information
    print(skin_mesh)

    # Compare with solid mesh
    print(f"\nSkin mesh elements: {skin_mesh.elements.n_elements}")
    print(f"Solid mesh elements: {solid_mesh.elements.n_elements}")
    print(f"Skin mesh nodes: {skin_mesh.nodes.n_nodes}")
    print(f"Solid mesh nodes: {solid_mesh.nodes.n_nodes}")

Extract results on the solid mesh
----------------------------------

Get field data defined on the solid mesh.

.. jupyter-execute::

    # Get stress results on the solid mesh
    stress_fc = model.results.stress.eval()

    # Get the first stress field
    stress_field_solid = stress_fc[0]

    # Print field information
    print("Stress field on solid mesh:")
    print(stress_field_solid)

    # Print location information
    print(f"\nField location: {stress_field_solid.location}")

Map elemental stress to skin mesh
----------------------------------

Map stress data from solid elements to skin elements.

.. jupyter-execute::

    # Get elemental stress on solid elements
    stress_elemental_fc = model.results.stress(location=dpf.locations.elemental).eval()
    stress_elemental_field = stress_elemental_fc[0]

    # Print elemental stress field
    print("Elemental stress field on solid mesh:")
    print(stress_elemental_field)

.. jupyter-execute::

    # Map the elemental stress to the skin mesh
    mapped_stress_op = ops.mapping.solid_to_skin(
        field=stress_elemental_field,
        mesh=skin_mesh,
        solid_mesh=solid_mesh
    )

    # Evaluate to get the mapped field
    mapped_stress_field = mapped_stress_op.eval()

    # Print the mapped field
    print("\nStress field mapped to skin mesh:")
    print(mapped_stress_field)

    # Compare sizes
    print(f"\nOriginal field size: {len(stress_elemental_field.data)}")
    print(f"Mapped field size: {len(mapped_stress_field.data)}")

Map nodal displacement to skin mesh
------------------------------------

Map nodal field data from the solid mesh to the skin mesh.

.. jupyter-execute::

    # Get nodal displacement on solid mesh
    displacement_fc = model.results.displacement(location=dpf.locations.nodal).eval()
    displacement_field = displacement_fc[0]

    # Print nodal displacement field
    print("Nodal displacement field on solid mesh:")
    print(displacement_field)

.. jupyter-execute::

    # Map the nodal displacement to the skin mesh
    mapped_displacement_op = ops.mapping.solid_to_skin(
        field=displacement_field,
        mesh=skin_mesh,
        solid_mesh=solid_mesh
    )

    # Evaluate to get the mapped field
    mapped_displacement_field = mapped_displacement_op.eval()

    # Print the mapped field
    print("\nDisplacement field mapped to skin mesh:")
    print(mapped_displacement_field)

    # The field is rescoped to only the nodes of the skin mesh
    print(f"\nOriginal field scoping size: {len(displacement_field.scoping)}")
    print(f"Mapped field scoping size: {len(mapped_displacement_field.scoping)}")

Map elementalnodal results to skin mesh
----------------------------------------

Map elementalnodal field data from solid to skin mesh.

.. jupyter-execute::

    # Get elementalnodal stress
    stress_en_fc = model.results.stress(location=dpf.locations.elemental_nodal).eval()
    stress_en_field = stress_en_fc[0]

    # Print elementalnodal stress field
    print("ElementalNodal stress field on solid mesh:")
    print(stress_en_field)

.. jupyter-execute::

    # Map the elementalnodal stress to the skin mesh
    mapped_stress_en_op = ops.mapping.solid_to_skin(
        field=stress_en_field,
        mesh=skin_mesh,
        solid_mesh=solid_mesh
    )

    # Evaluate to get the mapped field
    mapped_stress_en_field = mapped_stress_en_op.eval()

    # Print the mapped field
    print("\nElementalNodal stress field mapped to skin mesh:")
    print(mapped_stress_en_field)

Visualize results on skin mesh
-------------------------------

Plot the mapped results on the skin mesh.

.. jupyter-execute::

    # Plot the mapped displacement on the skin mesh
    skin_mesh.plot(field_or_fields_container=mapped_displacement_field)

.. jupyter-execute::

    # Plot the mapped stress on the skin mesh
    skin_mesh.plot(field_or_fields_container=mapped_stress_field)

Map without providing solid mesh
---------------------------------

If the field already has the solid mesh in its support, you can omit the ``solid_mesh`` parameter.

.. jupyter-execute::

    # Map stress to skin mesh without explicitly providing solid mesh
    # The solid mesh is taken from the field's support
    mapped_stress_simple = ops.mapping.solid_to_skin(
        field=stress_field_solid,
        mesh=skin_mesh
    ).eval()

    # Print the result
    print("Stress mapped to skin mesh (solid mesh from field support):")
    print(mapped_stress_simple)

Use with FieldsContainer
-------------------------

The operator also accepts a |FieldsContainer| with a single field.

.. jupyter-execute::

    # Map a FieldsContainer to skin mesh
    # The FieldsContainer should contain only one field
    single_field_fc = dpf.FieldsContainer()
    single_field_fc.add_field(label_space={'time': 1}, field=stress_field_solid)

    # Map the FieldsContainer
    mapped_fc = ops.mapping.solid_to_skin(
        field=single_field_fc,
        mesh=skin_mesh,
        solid_mesh=solid_mesh
    ).eval()

    # Print the result
    print("Mapped field from FieldsContainer:")
    print(mapped_fc)

Compare original and mapped data
---------------------------------

Compare data values between the original solid mesh field and mapped skin mesh field.

.. jupyter-execute::

    # Get some sample data from both fields
    print("Sample stress values on solid mesh (first 5 entities):")
    print(stress_field_solid.data[:5])

    print("\nSample stress values on skin mesh (first 5 entities):")
    print(mapped_stress_simple.data[:5])

    # Print statistics
    print(f"\nSolid mesh stress - min: {stress_field_solid.min().data}, max: {stress_field_solid.max().data}")
    print(f"Skin mesh stress - min: {mapped_stress_simple.min().data}, max: {mapped_stress_simple.max().data}")
