.. _ref_tutorials_export_data:

===========
Export data
===========

Data in DPF can be exported to universal file formats, such as VTK, HDF5, and TXT files.
You can use it to generate TH-plots, screenshots, and animations or to create custom result
plots using the `numpy <https://numpy.org/>`_ and `matplotlib <https://matplotlib.org/>`_ packages.

These tutorials explain how to export data from your manipulations with PyDPF-Core.

VTK Export
**********

Learn how to export data to [VTK formats](https://docs.vtk.org/en/latest/vtk_file_formats/index.html). VTK (Visualization Toolkit) is a widely used open-source software system for 3D computer graphics, image processing, and visualization. DPF's VTK export capabilities allow you to save your simulation results in VTK file formats, such as VTU (VTK Unstructured Grid), which can be easily visualized and analyzed using popular tools like ParaView and VisIt.

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Export to VTU format
       :link: ref_tutorials_export_to_vtu
       :link-type: ref
       :text-align: center

       Learn how to export DPF simulation data to VTU format for visualization
       in external tools like ParaView.

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

Other Export Formats
********************

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: HDF5 export
       :text-align: center
       :class-card: sd-bg-light
       :class-header: sd-bg-light sd-text-dark
       :class-footer: sd-bg-light sd-text-dark

       Export data to HDF5 format for efficient storage and processing.

       +++
       Coming soon

.. toctree::
    :maxdepth: 2
    :hidden:

    export_to_vtu.rst

