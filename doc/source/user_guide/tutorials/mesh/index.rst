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
       :link: tutorials_create_a_mesh_from_scratch
       :link-type: ref
       :text-align: center

       This tutorial demonstrates how to build a mesh from the scratch

    .. grid-item-card:: Get a mesh from a result file
       :link: tutorials_get_mesh_from_result_file
       :link-type: ref
       :text-align: center

       This tutorial explains how to extract the models mesh from a result file
       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Read a mesh metadata
       :link: ref_tutorials_read_mesh_metadata
       :link-type: ref
       :text-align: center

       This tutorial explains how to read a mesh metadata
       (data about the elements, nodes, faces, region, zone ...) before
       extracting the mesh.

       +++
       :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`


    .. grid-item-card:: Explore a mesh
       :link: tutorials_explore_mesh
       :link-type: ref
       :text-align: center

       This tutorial explains how to access the mesh data and metadata
       (data about the elements, nodes, faces, region, zone ...)
       so it can be manipulated.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Extract a mesh in split parts
       :link: tutorials_get_specific_part_mesh
       :link-type: ref
       :text-align: center

       This tutorial show how to get meshes split on a given space or time for Fluent,
       or CFX result files.

       +++
       :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

    .. grid-item-card:: Split a mesh
       :link: tutorials_split_mesh
       :link-type: ref
       :text-align: center

       This tutorial show how to split a mesh into different meshes.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. toctree::
    :maxdepth: 2
    :hidden:

    create_a_mesh_from_scratch.rst
    get_mesh_from_result_file.rst
    read_mesh_metadata.rst
    explore_mesh.rst
    get_specific_part_mesh.rst
    split_mesh.rst
