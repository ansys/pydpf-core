.. _ref_guide_lines_tutorials:

=============================
Writing tutorials guide lines
=============================

You can improve the Py-DPF-Core documentation by adding:

- :ref:`New tutorials sections<ref_guide_lines_add_new_tutorial_section>`;
- :ref:`New tutorials<ref_guide_lines_add_new_tutorial>`.

To do so, you must follow the guide lines presented here.
You also need to understand the structure of the ``doc`` directory on the PyDPF-Core library:

.. code-block::

    .
    ├── doc
    │   ├── source
    │   │    ├── api
    │   │    ├── examples
    │   │    ├── getting_started
    │   │    ├── images
    │   │    ├── user_guide
    │   │    ├── conf.py
    │   │    ├── index.rst
    │   ├── styles
    │   ├── make.bat


You will be handling only the ``doc/source/user_guide`` directory .

.. _ref_guide_lines_add_new_tutorial_section:

=============================
Adding a new tutorial section
=============================

.. note::

    Avoid creating new folders unless absolutely necessary. If in doubt, its precise location can be advised
    on in the pull request. If you must create a new folder, make sure to add a ``index.rst`` file containing
    a reference, tue section title and a description of the section. Otherwise the new folder will be ignored by Sphinx.

Location and naming
-------------------

The new tutorial section must be organized in a new folder in ``doc/source/user_guide/tutorials/new_section_name``.

.. code-block::

    .
    ├── doc
    │   ├── source
    │   │    ├── user_guide
    │   │    │   ├── tutorials
    │   │    │        ├── new_section

Structure
---------

The new folder must contain at least a ``index.rst`` file. This file has:

- Reference name;
- Section title;
- General description of the content of the tutorials in this section;
- Cards with the tutorial title, description and applicable solvers (the card must have a link to the tutorial file);
- Toctree with the tutorials in the section.

You must also add the ``index.rst`` file. in the main user guide toctree. You can find it at the end of
``doc/source/user_guide/index.rst`` file.

.. rubric:: Templates

:download:`Download the new tutorial section template<tutorial_section_template.rst>`

.. _ref_guide_lines_add_new_tutorial:

=====================
Adding a new tutorial
=====================

Location and naming
-------------------

New tutorials must be added as ``.rst`` files to: ``doc/source/user_guide/tutorials/section_name/tutorial_file.rst``

.. code-block::

    .
    ├── doc
    │   ├── source
    │   │    ├── user_guide
    │   │    │   ├── tutorials
    │   │    │        ├── section
    │   │    │             ├── new_tutorial.rst

You also have to add it to a card and the toctree on the section ``index.rst`` file. The card must have:

- Tutorial title;
- Short description;
- Applicable solvers;
- Link to the tutorial file;

.. card:: Tutorial title
   :text-align: center
   :width: 25%

   Short description of the tutorial

   +++
   :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

.. rubric:: Templates

:download:`Download the card template<tutorial_section_template.rst>`

Structure
---------

The tutorial structure can be divided in two main parts:

- Basis;
- Content.

Basis
^^^^^

This first part must have the following components:

- File reference name;
- Tutorial title;
- Substitution text for the PyDPF-Core library references;
- Short description (same phrase used in the tutorial card in the tutorial section ``index.rst`` file);
- Introduction that explains the context of the tutorial;
- Download script buttons;

.. code-block::

    .. _ref_tutorial_template:


    ==============
    Tutorial title
    ==============


    .. |Examples| replace:: :class:`ansys.dpf.core.examples`


    This sentence resumes the goal of the tutorial


    Introduction to the tutorial


    :jupyter-download-script:`Download tutorial as Python script<file_name>` :jupyter-download-notebook:`Download tutorial as notebook<file_name>`

Content
^^^^^^^

A tutorial goal is to explain how to perform a task step by step and understand the underlying concepts.

Sections
~~~~~~~~

A well-structured tutorial content should be divided by those steps. For example:

A tutorial goal is to explains how to plot a mesh using PyDPF-Core.
The steps to achieve this task are:

- Import a result file;
- Extract the mesh;
- Plot the mesh.

To create those section, underline it with the appropriate characters (here: ``-``).

.. code-block::

    Import result file
    ------------------

    First, you ...


    Extract the mesh
    ----------------

    Then, you extract ...


    Plot the mesh
    -------------

    Finally, you plot ...

Code snippets
~~~~~~~~~~~~~

Text formating
~~~~~~~~~~~~~~







