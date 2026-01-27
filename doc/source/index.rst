.. title:: PyDPF-Core

.. figure:: _static/pydpf-core.svg
    :align: center
    :width: 640px

PyDPF-Core is a Python client library for the Ansys Data Processing Framework (DPF). You are looking at the documentation for version |version|

.. grid:: 1 2 3 3
    :gutter: 1 2 3 3
    :padding: 1 2 3 3

    .. grid-item-card:: Introduction :fa:`circle-info`
        :link: introduction
        :link-type: doc

        Understand what PyDPF-Core is and how it provides a Python interface to Ansys Data Processing Framework.

    .. grid-item-card:: Getting started :fa:`person-running`
        :link: getting_started/index
        :link-type: doc

        Learn how to install and start using PyDPF-Core.

    .. grid-item-card:: User guide :fa:`book-open-reader`
        :link: user_guide/index
        :link-type: doc

        Learn about core DPF concepts, the basic steps of using DPF to transform data, and
        the different ways of using DPF.

    .. jinja:: toctree

        {% if build_tutorials %}
        .. grid-item-card:: Tutorials :fa:`person-chalkboard`
            :link: tutorials/index
            :link-type: doc

            Understand fundamental PyDPF-Core functionalities through simple yet comprehensive
            tutorials.
        {% endif %}

        {% if build_examples %}
        .. grid-item-card:: Examples :fa:`scroll`
            :link: examples/index
            :link-type: doc

            Explore a wide range of examples that show how to use PyDPF-Core to access and
            transform simulation data.
        {% endif %}

        {% if build_api %}
        .. grid-item-card:: API reference :fa:`book-bookmark`
            :link: api/index
            :link-type: doc

            Understand PyDPF-Core API endpoints, their capabilities,
            and how to interact with them programmatically.
        {% endif %}

    .. grid-item-card:: Operators :fa:`chart-diagram`
        :link: operator_reference
        :link-type: doc

        Learn about the available operators in PyDPF-Core.

    .. grid-item-card:: Contributing :fa:`people-group`
        :link: contribute/index
        :link-type: doc

        Learn how to contribute to the PyDPF-Core codebase
        or documentation.



.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   introduction
   getting_started/index
   user_guide/index
   tutorials/index
   examples/index
   api/index
   operator_reference
   contribute/index