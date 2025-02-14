Contributing as a documentarian
###############################

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`pencil` Write documentation
        :padding: 2 2 2 2
        :link: write-documentation
        :link-type: ref

        Explain how to get started, use, and contribute to the project.

    .. grid-item-card:: :fa:`laptop-code` Add a new example
        :padding: 2 2 2 2
        :link: write-examples
        :link-type: ref

        Showcase the capabilities of PyDPF-Core by adding a new example. 

    .. grid-item-card:: :fa:`book` Build the documentation
        :padding: 2 2 2 2
        :link: build-documentation
        :link-type: ref

        Render the documentation to see your changes reflected.

.. _write-documentation:

Write documentation
===================

The documentation generator used in PyDPF-Core is `Sphinx`_. Most of the documents
are written in `reStructuredText`_. Some parts of the documentation, like the
:ref:`examples <Examples>`, uses a mix of `reStructuredText`_ and Python, thanks to `Sphinx-Gallery`_.
If you are interested in writing examples, see the :ref:`writing examples <write-examples>` 
section.

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

.. _write-examples:

Write a new example
===================

The :ref:`examples <Examples>` section of the documentation showcases different
capabilities of PyDPF-Core. Each example (grouped into folders of related examples)
is a standalone Python script. Despite being ``*.py`` files, they are written in a mix
of `reStructuredText`_ and Python. This is possible thanks to the `Sphinx-Gallery`_
Sphinx extension.

Documentarians writing new examples are encouraged to familiarize themselves with
`structuring Python scripts for Sphinx-Gallery <https://sphinx-gallery.github.io/stable/syntax.html>`_.
Once the ``.py`` file for a new example is properly set up, Sphinx-Gallery automatically
generates `Sphinx`_ `reStructuredText`_ files from it. The rendering of the resulting reST will provide
users with ``.ipynb`` (Jupyter notebook) and ``.py`` files of each example, which users can download.

Finally, here are some tips for writing examples:

- Start the example with an explanation of the main topic. Try to use as many relevant
  keywords as possible in this section to optimize for Search Engine Optimization.

- Include an explanation with each code cell. The explanations should
  be included before, not after, the corresponding code.

- The examples are built with the documentation. As part of the build process,
  screenshots of rendered graphics are inserted in the document. You do not need
  to include the screenshots yourself.

- When creating a new folder where more than one related example will be included, ensure
  a ``README.txt`` file is also included. This file should contain reST to be used as the header
  for the index page corresponding to the subsection for these examples in the generated documentation.

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
