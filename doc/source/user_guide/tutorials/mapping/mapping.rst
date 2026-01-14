.. _ref_tutorials_mapping:

=================
Mapping tutorials
=================

These tutorials demonstrate the main mapping features in PyDPF-Core for interpolating
and transferring field data between different spatial supports. Each tutorial covers
a specific mapping operator type.

Understanding mapping in DPF
============================

Mapping is the process of transferring or interpolating field data from one spatial
support to another. DPF provides several mapping operators, each designed for
specific use cases and offering different levels of precision and performance.

Direct coordinate mapping
-------------------------

The most common mapping approach uses the :ref:`ref_tutorials_mapping_on_coordinates` operator,
which interpolates field data at arbitrary spatial locations using element shape functions.
This method:

- Accepts a set of target coordinates where you want to evaluate field values
- Automatically finds which elements contain each coordinate
- Uses the element's shape functions to interpolate values at the exact location
- Is ideal for extracting results along paths, at sensor locations, or on custom grids

**When to use**: Use this approach when you need quick interpolation at specific points
and standard shape function accuracy is sufficient for your analysis.

Reduced coordinates mapping
---------------------------

For applications requiring higher precision or more control over the interpolation process,
the :ref:`ref_tutorials_mapping_on_reduced_coordinates` approach offers a two-step workflow:

#. **Find reduced coordinates**: The ``find_reduced_coordinates`` operator locates which
   element contains each target coordinate and computes the element-local (reference)
   coordinates within that element
#. **Map to reduced coordinates**: The ``on_reduced_coordinates`` operator uses these
   element-local coordinates to perform high-precision interpolation

Both this method and direct coordinate mapping use element shape functions for interpolation.
The key difference is that this approach provides explicit control over the element-local
(reduced) coordinates, while direct mapping handles the coordinate transformation internally.

This approach offers several advantages:

- Provides explicit access to element-local positions within reference elements
- Enables efficient reuse of the same element-local positions for multiple field types
- Offers better control over quadratic element interpolation for higher accuracy
- Is essential for advanced applications like Gauss point mapping or precise mesh-to-mesh transfer

**When to use**: Use this approach when you need explicit control over element-local precision,
want to map multiple fields to the same locations efficiently, or require the highest
interpolation accuracy for critical analyses.

Solid-to-skin mapping
---------------------

The :ref:`ref_tutorials_mapping_solid_to_skin` operator specializes in transferring field
data from volume (solid) elements to surface (skin) elements. This operator:

- Handles elemental, nodal, and elementalnodal field locations
- Copies or rescopes data based on the topological relationship between solid and skin meshes
- Is optimized for surface visualization and analysis of 3D results

**When to use**: Use this when you need to extract surface results from volumetric data,
for example to visualize external surfaces or analyze boundary conditions.

RBF-based workflow mapping
---------------------------

The :ref:`ref_tutorials_mapping_prepare_workflow` operator generates reusable workflows
that employ Radial Basis Function (RBF) filters for smooth interpolation between supports.
Unlike the other mapping methods that perform pure interpolation within elements using shape
functions, this approach uses RBF filters that can map data between non-conforming meshes.
This method:

- Creates a workflow that can be applied to multiple field types
- Uses RBF filters for smooth, continuous interpolation
- Allows customization through filter radius and influence box parameters
- Is particularly useful for transferring data between meshes with different topologies or structures

**When to use**: Use this for mapping between non-conforming meshes where the source and
target meshes have different structures, or for repeated mapping operations on various
field types.

Choosing the right mapping method
==================================

To select the appropriate mapping method for your application:

- For **quick point evaluation**: Use :ref:`ref_tutorials_mapping_on_coordinates`
- For **high-precision or repeated mapping**: Use :ref:`ref_tutorials_mapping_on_reduced_coordinates`
- For **volumetric to surface transfer**: Use :ref:`ref_tutorials_mapping_solid_to_skin`
- For **non-conforming mesh transfer**: Use :ref:`ref_tutorials_mapping_prepare_workflow`

Tutorials
=========

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Interpolation at coordinates
       :link: ref_tutorials_mapping_on_coordinates
       :link-type: ref
       :text-align: center

       Uses ``on_coordinates`` to interpolate field values at arbitrary spatial coordinates using mesh shape functions. Ideal for extracting results along paths or at sensor locations.

    .. grid-item-card:: Reduced coordinates mapping
       :link: ref_tutorials_mapping_on_reduced_coordinates
       :link-type: ref
       :text-align: center

       Uses ``find_reduced_coordinates`` and ``on_reduced_coordinates`` for a two-step high-precision mapping process using element-local coordinates. Useful for Gauss point mapping and accurate mesh-to-mesh transfer.

    .. grid-item-card:: Solid-to-skin mapping
       :link: ref_tutorials_mapping_solid_to_skin
       :link-type: ref
       :text-align: center

       Uses ``solid_to_skin`` to transfer field data from volume elements to surface elements. Supports elemental, nodal, and elementalnodal locations.

    .. grid-item-card:: RBF-based workflow mapping
       :link: ref_tutorials_mapping_prepare_workflow
       :link-type: ref
       :text-align: center

       Uses ``prepare_mapping_workflow`` to generate reusable workflows based on Radial Basis Function (RBF) filters to map results between non-conforming meshes with customizable filter parameters.

.. toctree::
   :maxdepth: 2
   :hidden:

   mapping_on_coordinates
   mapping_on_reduced_coordinates
   mapping_solid_to_skin
   mapping_prepare_workflow
