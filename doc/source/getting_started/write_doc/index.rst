.. _ref_write_doc:

=============
Documentation
=============

Overall guidance on contributing to the documentation a PyAnsys repository appears in
`Documenting <dev_guide_documenting_>`_ in the *PyAnsys Developer's Guide*.

You must also follow the `Documentation style <dev_guide_doc_style_>`_ guide to
ensure that all the documentation looks the same across the project.

To improve the documentation you need to:

- Start by `cloning the repository <Clone the repository>`_;
- Follow the `guidelines <Guide Lines>`_ to the corresponding documentation part you want to develop;
- Check the new documentation by `viewing the documentaion <View the documentation>`_

Clone the repository
--------------------

Clone and install the latest version of PyDPF-Core in
development mode by running this code:

.. code::

    git clone https://github.com/ansys/pydpf-core
    cd pydpf-core
    pip install -e .


Guidelines
----------

Our documentation tries to follow a structure principle that respects four different functions of the documentation
that fulfils the possible needs of people working with our tool at different times, in different circumstances.

Here is an overview of how our documentation is organized to help you know where you should include your contributions.
Each section has their own guidelines that must be followed when creating new content.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: **TUTORIALS**
       :link: ref_guidelines_tutorials
       :link-type: ref
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Learning oriented
       ^^^^^^^^^^^^^^^^^

       **Function:**  Teach how to get started and use PYDPF-core step by step

       They are designed to teach how to perform a task and understand the underlying concepts,
       providing detailed explanations at each stage.

       +++
       .. rubric:: Guidelines

       Here you find guidelines and templates to write new tutorials.

    .. grid-item-card:: **EXAMPLES**
       :link: ref
       :link-type: ref
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Use-cases oriented
       ^^^^^^^^^^^^^^^^^^

       **Function:**  Show how to solve specifics key problems

       They showcase specific key problems and use-cases. They are more advanced than
       tutorials and assume some knowledge on PyDPF-Core.

       +++
       .. rubric:: Guidelines

       Here you find guidelines and templates to write new examples.

    .. grid-item-card:: **CONCEPTS**
       :link: ref
       :link-type: ref
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Understanding oriented
       ^^^^^^^^^^^^^^^^^^^^^^

       **Function:**  Provide useful background explanation on PyDPF-Core

       They discuss and explain key topics and concepts providing enabling the reader to understand our
       tool.

       +++
       .. rubric:: Guidelines

       Here you find guidelines and templates to write more concepts.


    .. grid-item-card:: **API REFERENCE**
       :link: ref
       :link-type: ref
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Informing oriented
       ^^^^^^^^^^^^^^^^^^

       **Function:** Describe PyDPF-Core APIs

       They contain technical reference on how PyDPF-Core works and how to use it but assume that you have
       a basic understanding of key concepts.

       +++
       .. rubric:: Guidelines

       Here you find guidelines and templates to improve the API reference.

View the documentation
----------------------

Documentation for the latest stable release of PyDPF-Core is hosted at
`PyDPF-Core Documentation <https://dpf.docs.pyansys.com/>`_.

In the upper right corner of the documentation's title bar, there is an option
for switching from viewing the documentation for the latest stable release
to viewing the documentation for the development version or previously
released versions.

.. toctree::
    :maxdepth: 2
    :hidden:

    guide_lines_tutorials.rst
