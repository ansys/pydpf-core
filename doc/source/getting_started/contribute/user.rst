Contributing as a user
######################

Users can contribute in a variety of ways, such as reporting bugs, requesting
new features, testing in-development features, starting discussions, answering
questions, and sharing their work with the community.

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`bug` Report bugs
        :padding: 2 2 2 2
        :link: report-bugs
        :link-type: ref

        Found a bug? Report it here.

    .. grid-item-card:: :fa:`lightbulb` Request a new feature
        :padding: 2 2 2 2
        :link: request-a-new-feature
        :link-type: ref

        Got an idea for a new feature? Share it!

    .. grid-item-card:: :fa:`vial-circle-check` Test a new feature
        :padding: 2 2 2 2
        :link: test-a-new-feature
        :link-type: ref

        Anxious to try out a new feature? Here's how you can do it.

    .. grid-item-card:: :fa:`comments` Start a discussion
        :padding: 2 2 2 2
        :link: start-a-discussion
        :link-type: ref

        Want to discuss something? Start a discussion here.

    .. grid-item-card:: :fa:`comment-dots` Answer questions
        :padding: 2 2 2 2
        :link: answer-questions
        :link-type: ref

        Help others by answering their questions.

    .. grid-item-card:: :fa:`bullhorn` Share your work
        :padding: 2 2 2 2
        :link: share-your-work
        :link-type: ref

        Share your work with the community.

    .. grid-item-card:: :fa:`book` View documentation
        :padding: 2 2 2 2
        :link: view-documentation
        :link-type: ref

        View project documentation.

.. _report-bugs:

Report bugs
===========

If you encounter a bug or an issue while using the project, please report it.
Your feedback helps to identify problems.

- Search the `PyDPF-Core issues`_ to see if the issue has already been reported.

- Create a new issue if it hasn’t been reported.

  - Include a clear description of the problem.
  - Provide steps to reproduce the issue.
  - Mention the version of the project you're using.
  - Include screenshots or logs if possible.

.. _request-a-new-feature:

Request a new feature
=====================

Do you have an idea for a new feature or an improvement? Your suggestions are
welcome. You can request a new feature by creating an issue in the `PyDPF-Core issues`_
board.

.. _test-a-new-feature:

Test a new feature
==================

It is possible to test a new feature before it is officially released. To do
so, you can install PyDPF-Core from the source code by following the steps below.

Clone the repository
--------------------

Clone and install the latest version of PyDPF-Core by running this code:

.. code-block:: bash

    git clone https://github.com/ansys/pydpf-core

Install for users
-----------------

Installing the latest version of PyDPF-Core allows you to test latest features as
they are being developed without having to wait for releases.

Virtual environment
~~~~~~~~~~~~~~~~~~~

Start by navigating to the project's root directory by running:

.. code-block::

    cd pydpf-core

Then, create a new virtual environment named ``.venv`` to isolate your system's
Python environment by running:

.. code-block:: text

    python -m venv .venv

Finally, activate this environment by running:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    .venv\Scripts\activate.bat

            .. tab-item:: PowerShell

                .. code-block:: text

                    .venv\Scripts\Activate.ps1

    .. tab-item:: macOS/Linux/UNIX

        .. code-block:: text

            source .venv/bin/activate

Latest version installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, install PyDPF-Core in editable mode by running:

.. code-block:: text

    python -m pip install .

Verify the installation by checking the version of the library:


.. code-block:: python

    from ansys.dpf.core import __version__


    print(f"PyDPF-Core version is {__version__}")

.. jinja::

    .. code-block:: text

       >>> PyDPF-Core version is {{ PYDPF_CORE_VERSION }}

.. _start-a-discussion:

Start a discussion
==================

Complex topics may require a discussion. Whether you want to know how to use
PyDPF-Core for solving your specific problem or you have a suggestion for a new
feature, a discussion is a good place to start. You can open a new discussion
in the `PyDPF-Core discussions`_ section.

.. _answer-questions:

Answer questions
================

Another great way to contribute is to help others by answering their questions.
Maintain a positive and constructive attitude while answering questions. If you
don't know the answer, you can still help by pointing the person in the right
direction.

.. _share-your-work:

Share your work
===============

If you have used PyDPF-Core to create something interesting, share it with the rest
of the community. You can share your work in the `PyDPF-Core discussions`_. Include
a brief description of your work and any relevant links that others may find
useful.

.. _view-documentation:

View documentation
==================
Documentation for the latest stable release of PyDPF-Core is hosted at
`PyDPF-Core Documentation`_. 

In the upper right corner of the documentation's title bar, there is an option
for switching from viewing the documentation for the latest stable release
to viewing the documentation for the development version or previously
released versions.