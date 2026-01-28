.. _ref_tutorials:

Tutorials
---------

The tutorials cover specifics features with detailed demonstrations to help
understanding the fundamental PyDPF-Core functionalities and clarify some concepts.
They are designed to teach how to perform a task, providing explanations at each stage.

It helps to have a Python interpreter for hands-on experience, but all code examples are
executed, so the tutorial can be read off-line as well.

For a complete description of all the objects and modules, see the :doc:`API reference <../../api/index>`
section.

:fa:`person-running` Beginner's guide
*************************************

New to PyDPF-Core? Check our beginner's tutorials. They offer an overview
of basic features and concepts so you can start coding right away.

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Data structures
        :link: ref_tutorials_data_structures
        :link-type: ref
        :text-align: center

        Learn about the different data structures available in DPF.

    .. grid-item-card::  Post-processing data basics
        :link: ref_tutorials_processing_basics
        :link-type: ref
        :text-align: center

        Follow a basic post-processing procedure with data transformation,
        visualization and analysis using PyDPf-Core.

:fa:`book-open-reader` Common topics
************************************

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Importing data
        :link: ref_tutorials_import_data
        :link-type: ref
        :text-align: center

        Understand how to represent data in DPF: either from manual input either form result files.

    .. grid-item-card:: Meshes
        :link: ref_tutorials_mesh
        :link-type: ref
        :text-align: center

        Learn how to interact with meshes in PyDPF-Core.

    .. grid-item-card:: Processing data with operators and workflows
        :text-align: center
        :class-card: sd-bg-light
        :class-header: sd-bg-light sd-text-dark
        :class-footer: sd-bg-light sd-text-dark

        Learn how to use operators to process your data and build workflows.

        +++
        Coming soon

    .. grid-item-card:: Exporting data
        :text-align: center
        :class-card: sd-bg-light
        :class-header: sd-bg-light sd-text-dark
        :class-footer: sd-bg-light sd-text-dark

        Discover the best ways to export data from your manipulations with PyDPF-Core.

        +++
        Coming soon

    .. grid-item-card:: Plotting
        :link: ref_tutorials_plot
        :link-type: ref
        :text-align: center

        Explore the different approaches to visualise the data in plots.

    .. grid-item-card:: Animations
        :link: ref_tutorials_animate
        :link-type: ref
        :text-align: center

        Explore the different approaches to visualise the data in an animation.

    .. grid-item-card:: Mathematical operations
        :link: ref_tutorials_mathematics
        :link-type: ref
        :text-align: center

        Learn how to perform mathematical operations on data structures.

    .. grid-item-card:: Custom Python operator and plugin
        :link: ref_tutorials_custom_operators_and_plugins
        :link-type: ref
        :text-align: center

        Discover how to enhance DPF capabilities with custom operators and plugins.

    .. grid-item-card:: Processing distributed files
        :text-align: center
        :class-card: sd-bg-light
        :class-header: sd-bg-light sd-text-dark
        :class-footer: sd-bg-light sd-text-dark

        Learn how to use PyDPF-Core with distributed result files.

        +++
        Coming soon

    .. grid-item-card:: Managing local and remote servers
        :link: ref_tutorials_dpf_server
        :link-type: ref
        :text-align: center

        Learn about the DPF client-server architecture and management of local and remote servers.

    .. grid-item-card:: Manage licensing
        :text-align: center
        :class-card: sd-bg-light
        :class-header: sd-bg-light sd-text-dark
        :class-footer: sd-bg-light sd-text-dark

        Learn how to manage licensing in PyDPF-Core.

        +++
        Coming soon

.. toctree::
    :maxdepth: 2
    :hidden:

    data_structures/index.rst
    post_processing_basics/index.rst
    import_data/index.rst
    mesh/index.rst
    plot/index.rst
    animate/index.rst
    mathematics/index.rst
    custom_operators_and_plugins/index.rst
    dpf_server/index.rst