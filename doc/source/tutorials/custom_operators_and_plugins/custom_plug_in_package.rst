.. _tutorials_others_custom_plug_ins_packages:

=======================================
Plug-in package with multiple operators
=======================================

This tutorial shows how to create, load and use a custom plug-in package with multiple operators or with complex routines

Create the plug-in package
--------------------------

To create a plug-in package with multiple operators or with complex routines, you write a
Python package. The benefits of writing packages rather than simple scripts are:

- **Componentization:** You can split the code into several Python modules or files.
- **Distribution:** You can use standard Python tools to upload and download packages.
- **Documentation:** You can add README files, documentation, tests, and examples to the package.

A plug-in package with dependencies consists of a folder with the necessary files. Assume
that the name of your plug-in package is ``custom_plugin``. A folder with this name would
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


Load the plug-in package
------------------------

Use the :func:`load_library() <ansys.dpf.core.core.load_library>` method to load  plug-in package.

- The first argument is the path to the directory where the plug-in package is located.
- The second argument is ``py_<package>`` where <package> is the name identifying the plug-in package.
- The third argument is the name of the function exposed in the __init__ file for the plug-in package that is used to record operators.

.. code::

    dpf.load_library(
    r"path/to/plugins/custom_plugin",
    "py_my_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin/__init__.py
    "load_operators")


Use the custom operators
------------------------

Once the plugin is loaded, you can instantiate the custom operator:

.. code::

    new_operator = dpf.Operator("custom_operator") # if "custom_operator" is what is returned by the ``name`` property

References
----------
For more information, see :ref:`ref_custom_operator` in the **API reference**
and :ref:`python_operators` in **Examples**.