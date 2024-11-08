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

    tutorials/basic_tutorial_index.rst
    tutorials/02-import_data/index.rst
    tutorials/03-mesh/index.rst
    tutorials/04-transform_data/index.rst
    tutorials/05-plot/index.rst
    tutorials/06-animate/index.rst
    tutorials/07-export_data/index.rst
    tutorials/08-enriching_dpf_capabilities/index.rst
    tutorials/09-distributed_files/index.rst
    tutorials/10-dpf_server/index.rst
    tutorials/11-licensing/index.rst

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
