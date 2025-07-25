.. _contributing_documentation:

Contributing to the documentation
#################################

.. note::

    Overall guidance on contributing to the documentation of a PyAnsys repository appears in
    `Documenting`_ in the *PyAnsys Developer's Guide*.

    You must also follow the `Documentation style`_ guide to
    ensure that all the documentation looks the same across the project.

To contribute on the documentation you must start by setting up the PyDPF-Core repository
by following the steps in :ref:`contributing_as_a_developer` section.

In this page you can check how to :

.. grid:: 1 2 3 3
    :padding: 2 2 2 2

    .. grid-item-card:: :fa:`th` Structure the documentation
        :link: structure-documentation
        :link-type: ref

        How the documentation is structured and where to locate files.

    .. grid-item-card:: :fa:`pencil` Write documentation
        :link: write-product-use-documentation
        :link-type: ref

        Explains and showcases the use of PyDPF-Core.

    .. grid-item-card:: :fa:`book` Build the documentation
        :link: build-documentation
        :link-type: ref

        Render the documentation to see your changes reflected.

.. _structure-documentation:

Structure the documentation
===========================

The documentation generator used in PyDPF-Core is `Sphinx`_. Most of the documents
are written in `reStructuredText`_.

The documentation is located in the ``doc/source`` directory. The landing page
is declared in the ``doc/source/index.rst`` file. The rest of the files contain
the main pages of different sections of the documentation. Finally, the
``doc/source/_static/`` folder contains various assets like images, and CSS
files.

The layout of the ``doc/source`` directory is reflected in the slug of the
online documentation. For example, the
``doc/source/getting_started/contribute/documentarian.rst`` renders as
``https://dpf.docs.pyansys.com/getting_started/contribute/documentarian.html``.

Thus, if you create a new file, it important to follow these rules:

- Use lowercase letters for file and directory names
- Use short and descriptive names
- Play smart with the hierarchy of the files and directories

All files need to be included in a table of contents. No dangling files are
permitted. If a file is not included in the table of contents, Sphinx raises a
warning.

A table of contents can be declared using a directive like this:

.. code-block:: rst

    .. toctree::
        :hidden:
        :maxdepth: 3

        path-to-file-A
        path-to-file-B
        path-to-file-C
        ...

The path to the file is relative to the directory where the table of contents
is declared.

.. _write-product-use-documentation:

Write documentation
===================

Our documentation tries to follow a structure principle that respects four different functions of the documentation.
Each of them fulfills a different need for people working with our tool at different times, in different circumstances.

Here is an overview of how our documentation is organized to help you know where you should include your contributions.
Each section has their own guidelines that must be followed when creating new content.
To check these specific guidelines click on the correspondent card below.

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

       Teach how to perform a task and showcase the underlying concepts,
       providing detailed explanations at each stage. A tutorial is centered around a given feature.

    .. grid-item-card:: **EXAMPLES**
       :link: ref_guidelines_examples
       :link-type: ref
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Use-cases oriented
       ^^^^^^^^^^^^^^^^^^

       **Function:**  Show how to solve specifics key problems

       Showcase a specific key problem or use-case with a complete PyDPF script. They are more advanced than
       tutorials as they present end-to-end engineering workflows and assume basic knowledge of PyDPF-Core.

    .. grid-item-card:: **CONCEPTS**
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Understanding oriented
       ^^^^^^^^^^^^^^^^^^^^^^

       **Function:**  Provide useful theoretical explanations for PyDPF-Core

       Discuss and explain key DPF principles and concepts, for the reader to understand the spirit of the underlying tool.


    .. grid-item-card:: **API REFERENCE**
       :class-title: sd-text-center sd-bg-light
       :class-header: sd-text-center

       Informing oriented
       ^^^^^^^^^^^^^^^^^^

       **Function:** Describe PyDPF-Core APIs

       Provides technical reference on how PyDPF-Core works and how to use it but assume basic
       understanding of key DPF concepts. It is generated automatically along the documentation and
       is based on the source code.

.. _build-documentation:

Build the documentation
=======================

`Tox`_ is used for automating the build of the documentation. To install Tox, run

.. code-block:: text

    python -m pip install tox tox-uv

There are different tox environments for cleaning previous build, building the HTML documentation,
and checking the integrity of external links. The following environments are available:

.. jinja:: toxenvs

    .. dropdown:: Documentation environments
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Description
              - Command
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            {% if name.startswith("doc-")%}
            * - {{ name }}
              - {{ description }}
              - python -m tox -e {{ name }}
            {% endif %}
            {% endfor %}

Two environment variables are available for the documentation build:

- ``BUILD_EXAMPLES``: if set to ``true``, the examples are built. This is the
  default behavior. When set to ``false``, the examples are not built.

- ``BUILD_API``: if set to ``true``, the API documentation is built. This is
  the default behavior. When set to ``false``, the API documentation is not
  built.

By using these environment variables, you can speed up the build process. This
allows to shorten the build time when only certain parts of the documentation
are modified.

.. tip::
    Instead of setting environment variables at the operating system level, you can
    add ``-x testenv:<env_name>.setenv+="<env_var>=<env_var_value>"`` to the
    previous tox commands. This can also be repeated to set multiple environment variables
    through tox. For example, to build HTML documentation while excluding both examples and
    API during the build, you can use the following command:

    .. code-block:: text

        python -m tox -e doc-html -x testenv:doc-html.setenv+="BUILD_API=false" -x testenv:doc-html.setenv+="BUILD_EXAMPLES=false"

.. toctree::
    :hidden:
    :maxdepth: 3

    guidelines_tutorials
    guidelines_examples