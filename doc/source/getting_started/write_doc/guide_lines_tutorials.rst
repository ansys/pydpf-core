.. _ref_guide_lines_tutorials:

============================
Writing tutorials guidelines
============================

You can improve the Py-DPF-Core documentation by adding a:

- :ref:`New tutorials section<ref_guide_lines_add_new_tutorial_section>`;
- :ref:`New tutorial<ref_guide_lines_add_new_tutorial>`.

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

:download:`Download the new tutorial section template<tutorial_section_template.rst>`

.. note::

    Avoid creating new folders unless it is absolutely necessary. If you are in doubt, its precise location can be
    advised on the pull request. If you must create a new folder, make sure to add a ``index.rst`` file containing
    a reference, a title and a description of the section. Otherwise the new folder will be ignored by Sphinx.

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

.. code-block::

    .. _ref_tutorial_new_section_template:

    =============
    Section title
    =============

    These tutorials demonstrate how to ...

    .. grid:: 1 1 3 3
        :gutter: 2
        :padding: 2
        :margin: 2

        .. grid-item-card:: Tutorial title
           :link: ref
           :link-type: ref
           :text-align: center

           This tutorial ...

           +++
           :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

    .. toctree::
        :maxdepth: 2
        :hidden:

        tutorial_file.rst

You must also add the ``index.rst`` file in the main user guide page toctree. You can find it at the end of
``doc/source/user_guide/index.rst`` file.

.. _ref_guide_lines_add_new_tutorial:

=====================
Adding a new tutorial
=====================

:download:`Download the tutorial card template<tutorial_card_template.rst>` :download:`Download the tutorial template<tutorial_template.rst>`

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

You also have to add it to a card and the toctree on the tutorial section ``index.rst`` file. The card must have:

- Tutorial title;
- Short description;
- Badges with the applicable solvers;
- Link to the tutorial file;

.. topic:: Card example

    .. card:: Tutorial title
       :text-align: center
       :width: 25%

       Short description of the tutorial

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

Structure
---------

The tutorial structure can be divided in two main parts:

- :ref:`Preamble<ref_guide_lines_tutorial_preamble>`;
- :ref:`Content<ref_guide_lines_tutorial_content>`.

.. _ref_guide_lines_tutorial_preamble:

Preamble
^^^^^^^^

This first part is essential for clarity, organization and usability of the tutorial. It establishes the tutorials
purpose, making it easy to understand what is going to be explained and reference it within the other parts of
the documentation.

Components
~~~~~~~~~~

The preamble must have the following components:

- File reference name;
- Tutorial title;
- Substitution text for the PyDPF-Core library references that will be used across the tutorial;
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

The main PyDPF-Core library references are available already defined in the ``doc/source/links_and_refs.rst`` file.
To employ them, you use the ``include`` directive and use the substitution text as usual:

.. code-block::

    .. _ref_tutorial_template:


    ==============
    Tutorial title
    ==============

    .. include:: ../../../links_and_refs.rst

    Here some text. Here we use the |MeshedRegion| substitution text

For more information on those references check the :download:`links and references file<../../links_and_refs.rst>`.

.. _ref_guide_lines_tutorial_content:

Content
^^^^^^^

A tutorial goal is to explain how to perform a task step by step and understand the underlying concepts.
Thus, its structure must prioritize clarity, simplicity, and logical flow.

Sections
~~~~~~~~

A well-organized tutorial breaks down complex tasks into manageable steps, presenting information incrementally
to avoid overwhelming the user. It combines concise explanations with actionable instructions, ensuring users
can follow along easily while building their understanding.

Thus, the sections of the content are the steps themselves. Globally those steps looks like:

#. Get data, define DPF objects that contains the data;
#. One or more steps where you manipulate, handles the data/ DPF objects;
#. Conclusion, here is the final step where the tutorial goal is accomplished.

For example:

A tutorial goal is to explains how to plot a mesh using PyDPF-Core.
The steps to achieve this task are:

#. Import a result file;
#. Extract the mesh;
#. Plot the mesh.

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

Tabs
~~~~

You must use tabs in the case the tutorial is applicable fore more then one solver and the implementations are
different for each of them.

These tabs looks like:

.. tab-set::

    .. tab-item:: MAPDL

        Explanation 1 ...

        .. jupyter-execute::

            # Code block 1

    .. tab-item:: LSDYNA

        Explanation 2 ...

        .. jupyter-execute::

            # Code block 2

    .. tab-item:: Fluent

        Explanation 3 ...

        .. jupyter-execute::

            # Code block 3

    .. tab-item:: CFX

        Explanation 4 ...

        .. jupyter-execute::

            # Code block 4


You can also use tabs if you want to show different approaches to one step and it would be more clear
to have the code blocks in different tabs. You can see an example of this case in the
:ref:`ref_tutorials_animate_time` tutorial.


Code blocks
~~~~~~~~~~~

The tutorials must have code blocks where you show how you actually implement the coode.
The guidelines for the code snippets are:

- Use the `jupyter sphinx<jupyter_sphinx_ext>`_ extension to show code blocks. Its executes embedded code in
  a Jupyter kernel and embeds outputs of that code in the document:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            .. jupyter-execute::

                # This is a executable code block
                from ansys.dpf import core as dpf

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            .. code-block::

                # This is a simple code block
                from ansys.dpf import core as dpf

- Every code implementation must be commented:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            # Define the model
            model = dpf.Model()
            # Get the stress results
            stress_fc = model.results.stress.eval()

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            model = dpf.Model()
            stress_fc = model.results.stress.eval()

- You must split your code in several parts so you can make explanations between them:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        First explanation

        .. code-block::

            # Code comment 1
            code1

        Second explanation

        .. code-block::

            # Code comment 2
            code2

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            # First explanation
            # Code comment 1
            code1

            # Second explanation
            # Code comment 2
            code2

- When using a PyDPF-Core object or method you must use key arguments:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            # Get the stress results
            stress_fc = model.results.stress(time_scoping=time_steps).eval()

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            # Get the stress results
            stress_fc = model.results.stress(time_steps).eval()

Text formating
~~~~~~~~~~~~~~

- When enumerating something you must use bullet lists:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            This operator accepts as arguments:

            - A Result;
            - An Operator;
            - A FieldsContainer.

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            This operator accepts a Result, an Operator or a
            FieldsContainer as arguments.

- If the enumeration represent a order of topics the list must be numbered:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            To extract the mesh you need to follow those steps:

            #. Get the result file;
            #. Create a Model;
            #. Get the MeshedRegion.

        The ``#.`` renders as a numbered list.

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            To extract the mesh you need to follow those steps:

            - Get the result file;
            - Create a Model;
            - Get the MeshedRegion.

- If you need to put code blocks between the list items first you enumerate and reference them in a list. Then, you
  explore each of them separately in sub headings.
