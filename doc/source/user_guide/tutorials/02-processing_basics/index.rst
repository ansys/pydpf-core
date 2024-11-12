.. _ref_tutorials_processing_basics:

======================
Processing data basics
======================

When DPF employ operators to manipulate the data,it uses data containers
to store and return it. Therefore, it is important to be aware of how the
data is structured in those containers.

The data containers can be:

    - **Raw data storage structures**: Data arrays (a ``Field`` for example)
      or Data Maps (a ``DataTree`` for example)
    - **Collections**: a group of same labeled objects from one DPF raw data
      storage structure (a ``FieldsContainer`` for example, that is a group of ``Fields``
      with the same label)

The tutorials in this section presents the basics on how to create and manipulate data
with those structures.

If you are not familiarized with those concepts you can check our concepts section: :ref:`ref_concepts`

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Creating DPF raw data storage structures
       :link: ref_tutorials
       :link-type: ref
       :text-align: center

       This tutorial shows how to create and work with some DPF data arrays:
       Field, StringField and PropertyField

    .. grid-item-card:: Creating DPF collections
       :link: ref_tutorials
       :link-type: ref
       :text-align: center

       This tutorial shows how to create and work with some DPF collections:
       FieldsContainer, MeshesContainer, ScopingsContainer

    .. grid-item-card:: Mathematical operations
       :link: ref_tutorials
       :link-type: ref
       :text-align: center

       This tutorial demonstrate some mathematical operations that can be
       performed with PyDPF-Core
