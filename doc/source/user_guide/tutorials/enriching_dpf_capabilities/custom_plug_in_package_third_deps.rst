.. _tutorials_others_custom_plug_ins_packages_third_deps:

=============================================
Plug-in package with third-party dependencies
=============================================

This tutorial shows how to create, load and use a custom plug-in package with third-party dependencies

Create the plug-in package
--------------------------

To create a plug-in package with multiple operators or with complex routines, you write a
Python package.

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


Third-party dependencies
------------------------

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