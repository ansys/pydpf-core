.. _ref_tutorials_data_structures:

===================
DPF data structures
===================

DPF uses two main data structures to handle data: Fields and Collections.
Therefore, it is important to be aware of how the data is
structured in those containers.

The data containers can be:

    - **Raw data storage structures**: Data arrays (a ``Field`` for example) or Data Maps (a ``DataTree`` for example)
    - **Collections**: a group of same labeled objects from one DPF raw data storage structure (a ``FieldsContainer`` for example, that is a group of ``Fields`` with the same label)

These tutorials explains how these structures work and how you can manipulate data within.

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: DPF raw data storage structures
       :link: ref_tutorials
       :link-type: ref
       :text-align: center

       This tutorial shows how to create and work with some DPF data arrays:
       Field, StringField and PropertyField


    .. grid-item-card:: DPF collections
       :link: ref_tutorials_language_and_usage
       :link-type: ref
       :text-align: center

       This tutorial shows how to create and work with some DPF collections:
       FieldsContainer, MeshesContainer and ScopingContainer
