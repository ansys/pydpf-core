.. _ref_tutorials_mesh:

====
Mesh
====

The mesh in DPF is represented by the :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` entity.

These tutorials explains how to explore different attributes of a given mesh with PyDPF-Core.


.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Create a mesh from scratch
       :link: ref_tutorials_create_a_mesh_from_scratch
       :link-type: ref
       :text-align: center

       This tutorial demonstrates how to build a mesh from the scratch.

    .. grid-item-card:: Get a mesh from a result file
       :link: ref_tutorials_get_mesh_from_result_file
       :link-type: ref
       :text-align: center

       This tutorial explains how to extract a mesh from a result file.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Read a mesh metadata
       :link: ref_tutorials_read_mesh_metadata
       :link-type: ref
       :text-align: center

       This tutorial explains how to read a mesh metadata
       (data about the elements, nodes, faces, region, zone ...) before
       extracting the mesh from a result file.

       +++
       :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`


    .. grid-item-card:: Explore a mesh
       :link: ref_tutorials_explore_mesh
       :link-type: ref
       :text-align: center

       This tutorial explains how to access a mesh data and metadata
       so it can be manipulated.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Extract a mesh in split parts
       :link: ref_tutorials_extract_mesh_in_split_parts
       :link-type: ref
       :text-align: center

       This tutorial shows how to extract meshes split on a given space or time from a result file.

       +++
       :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Split a mesh
       :link: ref_tutorials_split_mesh
       :link-type: ref
       :text-align: center

       This tutorial shows how to split a mesh on a given property.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. toctree::
    :maxdepth: 2
    :hidden:

    create_a_mesh_from_scratch.rst
    get_mesh_from_result_file.rst
    read_mesh_metadata.rst
    explore_mesh.rst
    extract_mesh_in_split_parts.rst
    split_mesh.rst
