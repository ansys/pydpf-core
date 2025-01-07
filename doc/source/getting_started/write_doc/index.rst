.. _ref_write_doc:

=============
Documentation
=============

Writing good documentation for a GitHub repository is crucial to ensure that
users and contributors can understand, use, and contribute to PyDPF-Core
effectively.

Here's a short summary of how to write good documentation:

#. **Use a consistent structure**: Organize your documentation with a clear and
   consistent structure. Use headings, subheadings, and a table of contents if
   necessary to help users navigate your documentation easily.

#. **Use Sphinx properly**: Sphinx has multiple features and directives. Before
   starting to write documentation, you should get familiar with it. For guidance,
   see these Sphinx and DocUtils topics: `Directives <sphinx_directives_>`_,
   `reStructuredText Primer <sphinx_basics_>`_ and
   `reStructuredText Directives <docutils_directives_>`_.

#. **Usage Examples**: Include real-world usage examples, code snippets, and
   explanations to demonstrate how users can make the most of PyDPF-Core.

#. **Document the API and code**: Thoroughly document each function, class, and method. Include
   parameter descriptions, return values, and usage examples. Follow the
   `numpydoc <numpy_sphinx_ext_doc_>`_ convention for documenting code.

#. **Tutorials and guides**: Create tutorials or guides to help users achieve
   specific tasks or workflows with PyDPF-Core.

#. **Troubleshooting**: Anticipate common issues and provide solutions
   in a troubleshooting section.

#. **Maintain and update**: Keep your documentation up to date as the project
   evolves. New features, changes, and bug fixes should be reflected in the
   documentation.

#. **Solicit Feedback**: Invite users and contributors to provide feedback on
   the documentation and be responsive to their suggestions and questions.

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
