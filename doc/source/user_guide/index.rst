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

.. include::
   concepts/index.rst

.. include::
   main_entities.rst

.. include::
   how_to.rst


Troubleshooting
---------------

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Server issues
       :link: user_guide_troubleshooting_server_issues
       :link-type: ref
       :text-align: center

    .. grid-item-card:: Model issues
       :link: user_guide_troubleshooting_model_issues
       :link-type: ref
       :text-align: center

    .. grid-item-card::  Plotting issues
       :link: user_guide_troubleshooting_plotting_issues
       :link-type: ref
       :text-align: center

    .. grid-item-card::  Performance issues
       :link: user_guide_troubleshooting_performance_issues
       :link-type: ref
       :text-align: center


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Concepts

   concepts/concepts.rst
   concepts/waysofusing.rst
   concepts/stepbystep.rst


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: DPF most-used entities

    model
    operators
    fields_container


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: How-tos

    plotting.rst
    custom_operators.rst
    dpf_server.rst
    server_types.rst
    server_context.rst
    xmlfiles.rst


.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: Troubleshooting

    troubleshooting
