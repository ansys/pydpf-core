.. _ref_write_code:

============
Develop code
============

You can help improve PyDPF-Core by fixing a bug. To do it, you must set up the repository
on your local machine as per the following steps:

- :ref:`ref_write_code_clone`
- :ref:`ref_write_code_check_install`
- :ref:`ref_write_code_develop_code`

.. _ref_write_code_clone:

Clone the repository
--------------------

Before cloning the PyDPF-Core repository, you must install a version control system such as Git.

Then, clone and install the latest version of PyDPF-Core in development mode (using ``pip`` with the ``-e``
development flag) by running this code:

.. code::

    git clone https://github.com/ansys/pydpf-core
    cd pydpf-core
    pip install -e .

.. _ref_write_code_check_install:

Check the installation
----------------------

Run the following Python code to verify your PyDPF-Core installation:

.. code::

   from ansys.dpf.core import Model
   from ansys.dpf.core import examples
   model = Model(examples.find_simple_bar())
   print(model)

.. _ref_write_code_develop_code:

Develop the PyDPF-Core code
---------------------------

Developing code in a repository, particularly when using version control systems like Git,
involves a set of essential guidelines to ensure efficient collaboration, code management, and tracking changes.

Here are the main guidelines for developing code in a repository:

#. **Use branches**: Create branches for different features, bug fixes, or
   experiments. This keeps changes isolated and facilitates parallel
   development. For example, the branch name must start with a prefix and a backslash.

#. **Write descriptive commit messages**: Provide clear and concise commit
   messages that explain the purpose and context of the changes. Follow a
   consistent style.

#. **Commit frequently**: Make small, meaningful commits frequently. Avoid
   making a large number of unrelated changes in a single commit.

#. **Pull before you push**: Always update your local branch with the latest
   changes from the remote repository before pushing your own changes to avoid
   conflicts.

#. **Use pull requests (PRs)**: Use PRs to submit your changes for review.
   This allows for discussion and validation before merging into the main branch.
   Pull requests must follow the same convention as the commit messages.

   The pull requests can also be labeled for easier repository maintenance.
   Those labels are already defined in the repository.

#. **Write good documentation**: Maintain clear and up-to-date documentation for your
   contribution or changes, including comments in code, and relevant project
   documentation in rST or Markdown files.
   If you implement a new feature or change the behaviour of the library in any way,
   remember to mention it somewhere in the documentation (rST files in :file:`doc\source` directory)
   Follow the `numpydoc <numpy_sphinx_ext_doc_>`_ convention for documenting code.

#. **Test your changes**: Thoroughly test your changes to ensure that they work
   as expected. If applicable, create or update the unit tests that run on the
   continuous integration/continuous deployment (CI/CD) pipelines to catch issues early
   and ensure reliable deployments.

#. **Respect code style and standards**: Follow code style
   guidelines and adhere to coding standards specific to your language or
   framework.

#. **Collaborate and communicate**: Communicate with team members, provide
   updates on your progress, and resolve any conflicts promptly.

#. **Ask for help**: To ensure code quality, identify issues, and share knowledge,
   ask PyMAPDL developers to assist you and review your code.
   If you need help or guidance, mention ``@ansys/pydpf-admins`` in a comment
   so they they are notified.

By following these guidelines, you can ensure smooth and organized code
development within a repository, fostering collaboration, code quality, and feature enhancement.