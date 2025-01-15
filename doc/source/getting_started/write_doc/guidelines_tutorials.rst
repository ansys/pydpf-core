.. _ref_guidelines_tutorials:

=================
Writing tutorials
=================

You can improve the PyDPF-Core documentation by adding a:

- :ref:`New tutorials section<ref_guidelines_add_new_tutorial_section>`;
- :ref:`New tutorial<ref_guidelines_add_new_tutorial>`.

To do so, you must follow the guidelines presented here.

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


Tutorials are located in the ``doc/source/user_guide`` directory.

.. _ref_guidelines_add_new_tutorial_section:

=============================
Adding a new tutorial section
=============================

:download:`Download the new tutorial section template<tutorial_section_template.rst>`

.. note::

    Avoid creating new folders unless absolutely necessary. 
    When in doubt, mention the location of the new section in the pull request for approval. 
    If you must create a new folder, make sure to add an ``index.rst`` file with a reference, a title, and a description of the section. 
    The documentation ignores folders lacking this file.

Location and naming
-------------------

The new tutorial section must reside in a new folder such as ``doc/source/user_guide/tutorials/new_section_name``.

.. code-block::

    .
    ├── doc
    │   ├── source
    │   │    ├── user_guide
    │   │    │   ├── tutorials
    │   │    │        ├── new_section

Structure
---------

The section folder must contain an ``index.rst`` file with:

- a reference tag for referencing this section in other parts of the documentation,
- a title for the tutorial section,
- a general description of the topics covered in the tutorials in this section,
- cards with links to the tutorials, titles, descriptions and applicable solvers,
- a ``Toctree`` for the tutorials in the section to appear in the navigation pane.

.. literalinclude:: tutorial_section_template.rst

You must reference the new section ``index.rst`` file in the main user guide page toctree
for it to appear in the sidebar of the user guide main page. You can find this toctree
at the end of the ``doc/source/user_guide/index.rst`` file.
For example:

.. code-block::

    .. toctree::
        :maxdepth: 2
        :hidden:
        :caption: Tutorials

        tutorials/section_x/index.rst
        tutorials/section_y/index.rst
        tutorials/section_z/index.rst
        tutorials/new_section/index.rst

.. _ref_guidelines_add_new_tutorial:

=====================
Adding a new tutorial
=====================

:download:`Download the tutorial card template<tutorial_card_template.rst>`
:download:`Download the tutorial structure template<tutorial_structure_template.rst>`
:download:`Download the tutorial content formating template<tutorial_content_template.rst>`

Location and naming
-------------------

New tutorials correspond to new ``.rst`` files in tutorial section folders,
for example: ``doc/source/user_guide/tutorials/section/new_tutorial.rst``

.. code-block::

    .
    ├── doc
    │   ├── source
    │   │    ├── user_guide
    │   │    │   ├── tutorials
    │   │    │        ├── section
    │   │    │             ├── new_tutorial.rst

You must also add a new card in the ``index.rst`` file for the tutorial section as well as modify
its toctree. The card must include:

- a tutorial title,
- a short description,
- badges for the applicable solvers,
- a link (in this case, the reference tag) to the tutorial file.

.. topic:: Card example

    .. card:: Tutorial title
       :text-align: center
       :width: 25%

       Short description of the tutorial

       +++
       :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

Structure
---------

The tutorial is divided in two main parts:

- :ref:`Preamble<ref_guidelines_tutorial_header>`
- :ref:`Content<ref_guidelines_tutorial_content>`

.. _ref_guidelines_tutorial_header:

Header
^^^^^^

This first part is essential for clarity, organization and usability of the tutorial. It establishes the purpose 
of the tutorial, making it easier to understand what is going to be explained and reference it within the other parts of
the documentation.

The header must have :

- a reference tag,
- a tutorial title,
- any substitution text for references to the PyDPF-Core library used in the tutorial,
- a short description (same as for the tutorial card in the tutorial section),
- an introduction,
- download buttons for Python script and Jupyter notebook versions of the tutorial.

.. literalinclude:: tutorial_structure_template.rst
    :end-before: First Step

The main PyDPF-Core library references are available in the ``doc/source/links_and_refs.rst`` file.
To add a reference, use the substitution text as usual:

.. code-block::

    .. _ref_tutorial_template:


    ==============
    Tutorial title
    ==============

    Here some text. Here we use the |MeshedRegion| substitution text

For more information about the predefined references, see the
:download:`links and references file <../../links_and_refs.rst>`.

.. _ref_guidelines_tutorial_content:

Content
^^^^^^^

The goal of a tutorial is to present a feature or explain how to perform a common task step by step while explaining a behavior or underlying concepts.
Thus, its structure must prioritize clarity, simplicity, and logical flow.

Sections
~~~~~~~~

A well-organized tutorial breaks down complex tasks into manageable steps, presenting information incrementally
to avoid overwhelming the user. It combines concise explanations with actionable instructions, ensuring users
can follow along easily while building their understanding.

Thus, the sections of the content are the steps themselves. These steps are generally similar to:

#. A first step where you get some data and create DPF objects based on the data;
#. One or more steps where you manipulate the data or the DPF objects;
#. A final step where you reach the objective of the tutorial and obtain the expected result.

For example:

A tutorial explains how to plot a mesh using PyDPF-Core.
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

You must use tabs when a step requires a solver-specific implementation.

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


You can also use tabs if you want to show different approaches to one step and it having the code blocks
in different tabs is clearer. You can see an example of this in the
:ref:`ref_tutorials_animate_time` tutorial.


Code blocks
~~~~~~~~~~~

The tutorials must have code blocks where you show how you actually implement the code.
In addition to the guidelines presented here, you must also follow the `Coding style <dev_guide_coding_style_>`_
guide to ensure that all code looks the same across the project.

- Use the `jupyter sphinx <jupyter_sphinx_ext_>`_ extension to show code blocks. It executes embedded code in
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

- Use comments within a code block to clarify the purpose of a line:

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

- Split your code in several parts to include longer explanations in text format or force showing an intermediate code output:

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

- When using a PyDPF-Core object or method you must name arguments:

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

- When quoting APIs in the code comments you must always use their scripting name. Mind the use of
  a capital letter to name the DPF objects

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            # Define the DataSources object
            ds = dpf.DataSources()

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            # Define the data sources object
            ds = dpf.DataSources()

        .. code-block::

            # Define the Data Sources object
            ds = dpf.DataSources()

- Use blank lines between code lines for better clarity.

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            # Define the result file path
            result_file_path_1 = '/tmp/file.rst'

            # Define the DataSources object
            ds_1 = dpf.DataSources(result_path=result_file_path_1)

            # Create a Model
            model_1 = dpf.Model(data_sources=ds_1)

            # Get the stress results
            stress_fc = model_1.results.stress.eval()

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            # Define the result file path
            result_file_path_1 = '/tmp/file.rst'
            # Define the DataSources object
            ds_1 = dpf.DataSources(result_path=result_file_path_1)
            # Create a Model
            model_1 = dpf.Model(data_sources=ds_1)
            # Get the stress results
            stress_fc = model_1.results.stress.eval()

- Avoid naming the variables with the same name as an argument or an API. You can get inspirations from the
  tutorials available at :ref:`ref_tutorials`.

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            # Define the result file path
            result_file_path = '/tmp/file.rst'

            # Define the DataSources object
            ds = dpf.DataSources(result_path=result_file_path)

            # Create a Model
            my_model = dpf.Model(data_sources=ds)

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            # Define the result file path
            result_path = '/tmp/file.rst'

            # Define the DataSources object
            data_sources = dpf.DataSources(result_path=result_path)

            # Create a Model
            model = dpf.Model(data_sources=data_sources)

Text formating
~~~~~~~~~~~~~~

In addition to the guidelines presented here, you must also follow the `Documentation style <dev_guide_doc_style_>`_
guide to ensure that the tutorials follow a coherent writing style across the project.

- When quoting APIs in the text you must always use a reference to redirect it to the API reference

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

           Here we use the |MeshedRegion| substitution text

        **Rendered text:**

        Here is some text. Here we use the |MeshedRegion| substitution text

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            Here we do not use the MeshedRegion substitution text

        **Rendered text:**

        Here is some text. Here we do not use the MeshedRegion substitution text

- Use bullet lists when enumerating items:

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            This operator accepts as arguments:

            - A Result
            - An Operator
            - A FieldsContainer

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            This operator accepts a Result, an Operator or a
            FieldsContainer as arguments.

- Use a numbered list for ordered items:

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

- If you need to develop explanations for each item of the list, first, enumerate and reference them. Then,
  explore each of them separately in sub headings.

.. grid:: 2
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card::

        :octicon:`check-circle-fill` **Correct**

        .. code-block::

            Section title
            -------------

            This section presents two items:

            - :ref:`Item 1 <ref_tutorial_name_item_1>`
            - :ref:`Content<ref_tutorial_name_item_2>`


            .. _ref_tutorial_name_item_1:

            Item 1
            ^^^^^^

            Presentation of the first item...


            .. _ref_tutorial_name_item_2:

            Item 2
            ^^^^^^

            Presentation of the second item...

    .. grid-item-card::

        :octicon:`x-circle-fill` **Incorrect**

        .. code-block::

            Section title
            -------------

            This section presents two items:

            - Item 1
            - Item 2

            Item 1
            ^^^^^^
            Presentation of the first item...

            Item 2
            ^^^^^^
            Presentation of the second item...


        .. code-block::

            Section title
            -------------

            This section presents two items:

            - Item 1
            Presentation of the first item...


            - Item 2
            Presentation of the second item...
