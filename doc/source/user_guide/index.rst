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
   tutorials/index.rst

.. include::
   how-to/index.rst

.. include::
   troubleshooting/index.rst


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
    :caption: Tutorials

    tutorials/model.rst
    tutorials/operators.rst
    tutorials/fields_container.rst

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Accessing and enriching DPF capabilities

    how-to/plotting.rst
    how-to/custom_operators.rst
    how-to/server_context.rst
    how-to/server_types.rst
    how-to/xmlfiles.rst

.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: Troubleshooting

    troubleshooting/troubleshooting.rst
