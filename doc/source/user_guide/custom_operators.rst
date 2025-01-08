.. _user_guide_custom_operators:

================
Custom operators
================

In Ansys 2023 R1 and later, you can create custom operators in CPython. Creating custom operators
consists of wrapping Python routines in a DPF-compliant way so that you can access them in the same way
as you access the native operators in the :class:`ansys.dpf.core.dpf_operator.Operator` class in
PyDPF-Core or in any supported client API.

With support for custom operators, PyDPF-Core becomes a development tool offering:

- **Accessibility:** A simple script can define a basic operator plug-in.

- **Componentization:** Operators with similar applications can be grouped in Python plug-in packages.

- **Easy distribution:** Standard Python tools can be used to package, upload, and download custom operators.

- **Dependency management:** Third-party Python modules can be added to the Python package.

- **Reusability:** A documented and packaged operator can be reused in an infinite number of workflows.

- **Remotable and parallel computing:** Native DPF capabilities are inherited by custom operators.

The only prerequisite for creating custom operators is to be familiar with native operators.
For more information, see :ref:`ref_user_guide_operators`.

Install module
--------------

Once an Ansys unified installation is complete, you must install the ``ansys-dpf-core`` module in the Ansys
installer's Python interpreter.

#. Download the script for your operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/install_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/install_ansys_dpf_core_in_ansys.sh>`

#. Run the downloaded script for installing with optional arguments:

   - ``-awp_root``: Path to the Ansys root installation folder. For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.
   - ``-pip_args``: Optional arguments to add to the ``pip`` command. For example, ``--extra-index-url`` or
     ``--trusted-host``.

To uninstall the ``ansys-dpf-core`` module from the Ansys installation:

#. Download the script for your operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/uninstall_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/uninstall_ansys_dpf_core_in_ansys.sh>`.
  
3. Run the downloaded script for uninstalling with the optional argument:

   - ``-awp_root``: Path to the Ansys root installation folder.  For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.


Create operators
----------------
You can create a basic operator plugin or a plugin package with multiple operators. 

Basic operator plug-in
~~~~~~~~~~~~~~~~~~~~~~
To create a basic operator plug-in, write a simple Python script. An operator implementation
derives from the :class:`ansys.dpf.core.custom_operator.CustomOperatorBase` class and a call to
the :func:`ansys.dpf.core.custom_operator.record_operator` method.

This example script shows how you create a basic operator plug-in:

.. literalinclude:: custom_operator_example.py


.. code-block::

        def load_operators(*args):
            record_operator(CustomOperator, *args)


In the various properties for the class, specify the following:

- Name for the custom operator
- Description of what the operator does
- Dictionary for each input and output pin. This dictionary includes the name, a list of supported types, a description,
  and whether it is optional and/or ellipsis (meaning that the specification is valid for pins going from pin
  number *x* to infinity)
- List for operator properties, including name to use in the documentation and code generation and the
  operator category. The optional ``license`` property allows you to define a required license to check out
  when running the operator. Set it equal to ``any_dpf_supported_increments`` to allow any license
  currently accepted by DPF (see :ref:`here<target_to_ansys_license_increments_list>`)

For comprehensive examples on writing operator plug-ins, see :ref:`python_operators`.


Plug-in package with multiple operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create a plug-in package with multiple operators or with complex routines, write a
Python package. The benefits of writing packages rather than simple scripts are:

- **Componentization:** You can split the code into several Python modules or files.
- **Distribution:** You can use standard Python tools to upload and download packages.
- **Documentation:** You can add README files, documentation, tests, and examples to the package.

A plugin package with dependencies consists of a folder with the necessary files. Assume
that the name of your plugin package is ``custom_plugin``. A folder with this name would
contain four files:

- ``__init__.py``
- ``operators.py``
- ``operators_loader.py``
- ``common.py``

**__init__.py file**

The ``__init__.py`` file contains this code::

    from operators_loader import load_operators

   
**operators.py file**

The ``operators.py`` file contains code like this:

.. literalinclude:: custom_operator_example.py


**operators_loader.py file**

The ``operators_loader.py`` file contains code like this::

    from custom_plugin import operators
    from ansys.dpf.core.custom_operator import record_operator


    def load_operators(*args):
        record_operator(operators.CustomOperator, *args)


**common.py file**

The ``common.py`` file contains the Python routines as classes and functions::

    #write needed python routines as classes and functions here.

Third-party dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: custom_operators_deps.rst


Assume once again that the name of your plug-in package is ``custom_plugin``.
A folder with this name would contain these files:

- ``__init__.py``
- ``operators.py``
- ``operators_loader.py``
- ``common.py``
- ``winx64.zip``
- ``linx64.zip``
- ``custom_plugin.xml``

**__init__.py file**

The ``__init__.py`` file contains this code::

    from operators_loader import load_operators


**operators.py file**

The ``operators.py`` file contains code like this:

.. literalinclude:: custom_operator_example.py


**operators_loader.py file**

The ``operators_loader.py`` file contains code like this::

    from custom_plugin import operators
    from ansys.dpf.core.custom_operator import record_operator


    def load_operators(*args):
        record_operator(operators.CustomOperator, *args)


    def load_operators(*args):
                record_operator(operators.CustomOperator, *args)

**common.py file**

The ``common.py`` file contains the Python routines as classes and functions::

    #write needed python routines as classes and functions here.


**requirements.txt file**

The ``requirements.txt`` file contains code like this:
    
.. literalinclude:: /examples/07-python-operators/plugins/gltf_plugin/requirements.txt

The ZIP files for Windows and Linux are included as assets:
  
- ``winx64.zip``
- ``linx64.zip``


**custom_plugin.xml file**

The ``custom_plugin.xml`` file contains code like this:
 
.. literalinclude:: custom_plugin.xml
   :language: xml


Use custom operators
--------------------

Once a custom operator is created, you can use the :func:`ansys.dpf.core.core.load_library` method to load it.
The first argument is the path to the directory with the plugin. The second argument is ``py_`` plus any name
identifying the plugin. The last argument is the function name for recording operators.

For a plug-in that is a single script, the second argument should be ``py_`` plus the name of the Python file:

.. code::

    dpf.load_library(
    r"path/to/plugins",
    "py_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin.py
    "load_operators")

For a plug-in package, the second argument should be ``py_`` plus any name:

.. code::

    dpf.load_library(
    r"path/to/plugins/custom_plugin",
    "py_my_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin/__init__.py
    "load_operators")

Once the plug-in is loaded, you can instantiate the custom operator:

.. code::

    new_operator = dpf.Operator("custom_operator") # if "custom_operator" is what is returned by the ``name`` property

References
----------
For more information, see :ref:`ref_custom_operator` in the **API reference**
and :ref:`python_operators` in **Examples**.
