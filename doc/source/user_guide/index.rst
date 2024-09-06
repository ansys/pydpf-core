.. _ref_user_guide:

==========
User guide
==========

PyDPF-Core is a Python client API for accessing DPF postprocessing
capabilities. The ``ansys.dpf.core`` package makes highly efficient 
computation, customization, and remote postprocessing accessible in Python.

The goals of this section are to:

 - Describe the most-used DPF entities and how they can help you to access and modify solver data.
 - Provide simple how-tos for tackling the most common use cases.

Concepts
~~~~~~~~

.. card-carousel:: 2

    .. card:: Concepts and terminology
       :link: user_guide_concepts
       :link-type: ref
       :width: 25%
       :text-align: center

       .. image:: ../images/drawings/book-logo.png

    .. card:: Ways of using DPF
       :link: user_guide_waysofusing
       :link-type: ref
       :width: 25%
       :text-align: center

       .. image:: ../images/drawings/using-dpf.png

    .. card:: Using DPF: Step by step
       :link: user_guide_stepbystep
       :link-type: ref
       :width: 25%
       :text-align: center

       .. image:: ../images/drawings/checklist.png


.. include::
   main_entities.rst

.. include::
   how_to.rst


Troubleshooting
~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Concepts

    concepts.rst
    waysofusing.rst
    stepbystep.rst

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Tutorials

    model
    operators
    fields_container
    plotting
    custom_operators
    server_context
    server_types
    xmlfiles

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Troubleshooting

    troubleshooting
