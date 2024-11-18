.. _tutorials_create_a_mesh_from_scratch:

==========================
Create a mesh from scratch
==========================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`

The mesh object in DPF is a |MeshedRegion|. You can create your own |MeshedRegion| object to use DPF operators
with your own data. The ability to use scripting to create any DPF entity means
that you are not dependent on result files and can connect the DPF environment
with any Python tool.

This tutorial demonstrates how to build a |MeshedRegion| from the scratch.

Here we create a parallel piped mesh made of linear hexa elements.

Import the necessary modules
----------------------------

Import the ``ansys.dpf.core`` module, including the operators subpackage

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as ops

Define the mesh dimensions
--------------------------

.. code-block:: python

    length = 0.1
    width = 0.05
    depth = 0.1
    num_nodes_in_length = 10
    num_nodes_in_width = 5
    num_nodes_in_depth = 10
    my_meshed_region = dpf.MeshedRegion()



