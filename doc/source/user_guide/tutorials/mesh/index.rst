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

    .. grid-item-card:: Read and get specific information from a mesh
       :link: tutorials_read_mesh
       :link-type: ref
       :text-align: center

       This tutorial explains how to access the mesh data and metadata
       (data about the elements, nodes, faces, region, zone ...)
       so it can be manipulated.

    .. grid-item-card:: Get a mesh split on different parts
       :link: tutorials_split_mesh
       :link-type: ref
       :text-align: center

       This tutorial show how to get meshes split on a given space or time.

    .. grid-item-card:: Split a mesh
       :link: tutorials_split_mesh
       :link-type: ref
       :text-align: center

       This tutorial show how to split a mesh into different meshes.

.. toctree::
    :maxdepth: 2
    :hidden:

    create_a_mesh_from_scratch.rst
    get_mesh_from_result_file.rst
    read_mesh.rst
    get_specific_part_mesh.rst
    split_mesh.rst
