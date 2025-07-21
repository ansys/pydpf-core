Contributing as a user
######################

Users can contribute in a variety of ways, such as reporting bugs, requesting
new features, testing in-development features, starting discussions, answering
questions, and sharing their work with the community.

.. grid:: 1 2 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: :fa:`bug` Report bugs
        :link: report-bugs
        :link-type: ref

        Found a bug? Report it here.

    .. grid-item-card:: :fa:`lightbulb` Request a new feature
        :link: request-a-new-feature
        :link-type: ref

        Got an idea for a new feature? Share it!

    .. grid-item-card:: :fa:`vial-circle-check` Test a new feature
        :link: test-a-new-feature
        :link-type: ref

        Anxious to try out a new feature? Here's how you can do it.

    .. grid-item-card:: :fa:`comments` Start a discussion
        :link: start-a-discussion
        :link-type: ref

        Want to discuss something? Start a discussion here.

    .. grid-item-card:: :fa:`comment-dots` Answer questions
        :link: answer-questions
        :link-type: ref

        Help others by answering their questions.

    .. grid-item-card:: :fa:`bullhorn` Share your work
        :link: share-your-work
        :link-type: ref

        Share your work with the community.

    .. grid-item-card:: :fa:`book` View documentation
        :link: view-documentation
        :link-type: ref

        View project documentation.

----

.. _report-bugs:

Report bugs
===========

If you encounter a bug or an issue while using the project, please report it.
Your feedback helps to identify problems.

- First, search the `PyDPF-Core issues`_ to see if the issue has already been reported.

- If it hasn’t been reported, create a new issue in `PyDPF-Core issues`_ using the ``🐞 bug`` template:

  - Include a clear description of the problem.
  - Provide steps to reproduce the issue.
  - Mention the version of the project you're using.
  - Include screenshots or logs if possible.

.. _request-a-new-feature:

Request a new feature
=====================

Do you have an idea for a new feature or an improvement? Your suggestions are welcome.

You can request a new feature by creating an issue in the `PyDPF-Core issues`_
board using the ``💡 New feature`` template.

.. _test-a-new-feature:
Test a new feature
==================

It is possible to test a new feature before it is officially released.

To do so, you can install PyDPF-Core from the source code by following the steps below.

Clone the repository
--------------------

Clone the latest version of PyDPF-Core by running this code:

.. code-block:: bash

    git clone https://github.com/ansys/pydpf-core

Install PyDPF-Core for users
----------------------------

Installing the latest version of PyDPF-Core allows you to test latest features as
they are being developed without having to wait for releases.

To do so, by following the steps below.

Virtual environment
~~~~~~~~~~~~~~~~~~~

First, set up a new virtual environment.

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
feature, a discussion is a good place to start.

You can open a new discussion in the `PyDPF-Core discussions`_ section.

.. _answer-questions:

Answer questions
================

Another great way to contribute is to help others by answering their questions.
Maintain a positive and constructive attitude while answering questions.

If you don't know the answer, you can still help by pointing the person in the right
direction.

To discover how you can help see the `PyDPF-Core discussions`_.

.. _share-your-work:

Share your work
===============

If you have used PyDPF-Core to create something interesting, share it with the rest
of the community.

You can share your work in the `PyDPF-Core discussions`_. Include
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