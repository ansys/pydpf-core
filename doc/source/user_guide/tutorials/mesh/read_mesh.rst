.. _tutorials_read_mesh:

====================================
Read the mesh definition information
====================================

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`

This tutorial explains how to access and read a mesh.

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

Here we we will download a  result file available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path = examples.find_static_rst()
    # Create the model
    my_model = dpf.Model(data_sources=my_data_sources)
    # Get the mesh
    my_meshed_region_1 = my_model.metadata.meshed_region

