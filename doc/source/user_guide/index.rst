.. _ref_user_guide:

==========
User guide
==========

**DPF** provides numerical simulation users and engineers with a toolbox for accessing and
transforming data.

**PyDPF-Core** is a Python client API for accessing DPF
capabilities. The ``ansys.dpf.core`` package makes highly efficient
computation, customization, and remote data processing accessible in Python.

The goals of this section are to:

 - Describe some DPF entities and how they can help you to access and modify solver data.
 - Provide detailed tutorials to demonstrate PyDPF-Core functionalities.
 - Explain how to resolve the most common issues encountered when using PyDPF-Core

.. include::
   tutorials/index.rst

.. include::
   concepts/index.rst

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
    :caption: Tutorials

    tutorials/data_structures/index.rst
    tutorials/language_and_usage/index.rst
    tutorials/post_processing_basics/index.rst
    tutorials/import_data/index.rst
    tutorials/mesh/index.rst
    tutorials/transform_data/index.rst
    tutorials/export_data/index.rst
    tutorials/plot/index.rst
    tutorials/animate/index.rst
    tutorials/enriching_dpf_capabilities/index.rst
    tutorials/distributed_files/index.rst
    tutorials/dpf_server/index.rst
    tutorials/licensing/index.rst
    tutorials/mathematics/index.rst
    tutorials/manipulate_physics_data/index.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Concepts

   concepts/concepts.rst
   concepts/waysofusing.rst
   concepts/stepbystep.rst

.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: Troubleshooting

    troubleshooting
