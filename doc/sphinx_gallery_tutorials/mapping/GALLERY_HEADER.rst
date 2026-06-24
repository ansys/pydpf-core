.. _ref_tutorials_mapping:

=======
Mapping
=======

Mapping is the process of transferring or interpolating field data from one spatial
support to another. PyDPF-Core provides several mapping operators, each designed for
specific use cases, from quick shape-function interpolation to RBF-based mesh-to-mesh
transfer.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Interpolation at coordinates
       :link: ref_tutorials_mapping_on_coordinates
       :link-type: ref
       :text-align: center

       Uses ``on_coordinates`` to interpolate field values at arbitrary spatial coordinates
       using mesh shape functions. Ideal for extracting results along paths or at sensor locations.

    .. grid-item-card:: Reduced coordinates mapping
       :link: ref_tutorials_mapping_on_reduced_coordinates
       :link-type: ref
       :text-align: center

       Uses ``find_reduced_coordinates`` and ``on_reduced_coordinates`` for a two-step
       high-precision mapping process. Useful for Gauss point mapping and mesh-to-mesh transfer.

    .. grid-item-card:: Solid-to-skin mapping
       :link: ref_tutorials_mapping_solid_to_skin
       :link-type: ref
       :text-align: center

       Uses ``solid_to_skin`` to transfer field data from volume elements to surface elements.
       Supports elemental, nodal, and elemental-nodal locations.

    .. grid-item-card:: RBF-based workflow mapping
       :link: ref_tutorials_mapping_prepare_workflow
       :link-type: ref
       :text-align: center

       Uses ``prepare_mapping_workflow`` to generate reusable workflows based on Radial Basis
       Function (RBF) filters for mapping results between non-conforming meshes.

.. raw:: html

   <style>.sphx-glr-thumbnails { display: none; }</style>
