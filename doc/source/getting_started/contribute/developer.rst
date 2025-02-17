Contributing as a developer
###########################

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`download` Clone the repository
        :padding: 2 2 2 2
        :link: clone-the-repository
        :link-type: ref

        Download your own copy in your local machine.

    .. grid-item-card:: :fa:`download` Install for developers
        :padding: 2 2 2 2
        :link: install-for-developers
        :link-type: ref

        Install the project in editable mode.

    .. grid-item-card:: :fa:`vial-circle-check` Run the tests
        :padding: 2 2 2 2
        :link: run-tests
        :link-type: ref

        Verify your changes by testing the project.


.. _clone-the-repository:

Clone the repository
====================

Clone the latest version of PyDPF-Core in
development mode by running this code:

.. code-block:: bash

    git clone https://github.com/ansys/pydpf-core

.. _install-for-developers:

Install for developers
======================

Installing PyDPF-Core in development mode allows you to perform changes to the code
and see the changes reflected in your environment without having to reinstall
the library every time you make a change.

Virtual environment
-------------------

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

Development mode
----------------

Now, install PyDPF-Core in editable mode by running:

.. code-block:: text

    python -m pip install --editable .

Verify the installation by checking the version of the library:


.. code-block:: python

    from ansys.dpf.core import __version__


    print(f"PyDPF-Core version is {__version__}")

.. jinja::

    .. code-block:: text

       >>> PyDPF-Core version is {{ PYDPF_CORE_VERSION }}

Install Tox
-----------

Once the project is installed, you can install `Tox`_. This is a cross-platform
automation tool. The main advantage of Tox is that it eases routine tasks like project
testing, documentation generation, and wheel building in separate and isolated Python
virtual environments. To install Tox, run:

.. code-block:: text

    python -m pip install tox tox-uv

Finally, verify the installation by listing all the different environments
(automation rules) for PyDPF-Core:

.. code-block:: text

    python -m tox list

.. jinja:: toxenvs

    .. dropdown:: Default Tox environments
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Description
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            * - {{ name }}
              - {{ description }}
            {% endfor %}

.. _run-tests:

Run the tests
=============

Once you have made your changes, you can run the tests to verify that your
modifications did not break the project. PyDPF-Core tests are organized into groups and require additional steps
during execution to ensure tests run as expected without errors, therefore, PyDPF-Core tox configuration
supports different markers to account for this. These markers are associated with a
dedicated `Tox`_ environment. To also allow flexibity required during development, different DPF Server installation
can also be used as explained in the subsections that follow.

Unified DPF Server installation or specific DPF Server installation using ANSYS_DPF_PATH environment variable
-------------------------------------------------------------------------------------------------------------

These two installation DPF Server installation methods i.e. (unified or via ANSYS_DPF_PATH) require no special handling.
Individual test groups can be simply run with the following commands:

.. jinja:: toxenvs

    .. dropdown:: Testing individual groups
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Command
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            {% if name.startswith("test-")%}
            * - {{ name }}
              - python -m tox -e pretest,{{ name }},posttest,kill-servers
            {% endif %}
            {% endfor %}

Multiple tests can be run in different ways by specifying appropriate tox command:

.. dropdown:: Testing more than one group sequentially
    :animate: fade-in
    :icon: three-bars

    .. list-table::
        :header-rows: 1
        :widths: auto

        * - Command
          - Description
        * - python -m tox
          - Run all test groups sequentially
        * - python -m tox -e pretest,test-api,test-launcher,posttest,kill-servers
          - run specific selection of tests sequentially

To save testing time, the ``--parallel`` flag can be passed when running multiple environments at once.
Some test groups are incompatible for parallel runs by nature of their configuration. Some labels have
been added to the tox configuration for compatible tests to make running them easier.
The following commands are thus recommended when you wish to take advantage of parallel runs.

.. dropdown:: Testing more than one group in parallel
    :animate: fade-in
    :icon: three-bars

    .. list-table::
        :header-rows: 1
        :widths: auto

        * - Command
          - Description
        * - python -m tox -m localparalleltests --parallel
          - Run all compatible test groups in parallel
        * - python -m tox -e othertests
          - Run incompatible test groups sequentially
        * - python -m pretest,test-api,test-launcher,posttest,kill-servers --parallel
          - Run specific selection of tests in parallel

Standalone DPF Server installation
----------------------------------
Standalone DPF Server is usually `installed in editable mode <https://dpf.docs.pyansys.com/version/dev/getting_started/dpf_server.html#install-dpf-server>`_.
Accordingly, tox commands need to be adjusted for installation of standalone DPF Server in the isolated python environments
tox creates to run these tests in. This is achieved by adding ``-x testenv.deps+="-e <path/to/dpf/standalone>"``
to any of the previous tox commands.

For example, to run compatible parallel tests while using a Standalone DPF Server whose path is ``ansys_dpf_server_lin_v2025.1.pre0``, simply run:

.. code-block:: text

    python -m tox -m localparalleltests --parallel -x testenv.deps+="-e ansys_dpf_server_lin_v2025.1.pre0"

.. warning::
    When the ANSYS_DPF_PATH environment variable is set, the server pointed to
    `takes precedence <https://dpf.docs.pyansys.com/version/dev/getting_started/dpf_server.html#manage-multiple-dpf-server-installations>`_
    over any other DPF Server installation method. Therefore, a standalone DPF Server installed in editable mode, in the
    presence of ANSYS_DPF_PATH environment variable, will be ignored.
    
    With tox, a simple workaround is not setting this environment variable at the operating system level but passing it explicitly only when
    required. This is achived by adding ``-x testenv.setenv+="ANSYS_DPF_PATH=<path/to/valid/DPF/Server/installation>"`` to any tox command.
    
    Alternatively, when set at the operating system level, commenting out the line where this environment variable is passed in the tox
    configuration file will ensure that it is ignored within the tox environments.

    .. image:: tox.png

Testing on Linux via WSL
------------------------
Some system dependencies required for VTK to run properly might be missing when running tests on linux via WSL (or even linux in general). 
The identified workaround for this is to install the OSMesa wheel variant that leverages offscreen rendering with OSMesa.
This wheel is being built for both Linux and Windows at this time and bundles all of the necessary libraries into the wheel. This is
achieved by adding ``-x testenv.commands_pre="uv pip install --extra-index-url https://wheels.vtk.org vtk-osmesa==<version>"``

For example, to run all tests sequentially on linux, while using a Standalone DPF Server whose path is ``ansys_dpf_server_lin_v2025.1.pre0``, simply run:

.. code-block:: text

    python -m tox --parallel -x testenv.deps+="-e ansys_dpf_server_lin_v2025.1.pre0" -x testenv.commands_pre="uv pip install --extra-index-url https://wheels.vtk.org vtk-osmesa==9.2.20230527.dev0"
