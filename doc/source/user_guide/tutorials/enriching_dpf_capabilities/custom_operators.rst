.. _user_guide_custom_operators:

================
Custom operators
================

In Ansys 2023 R1 and later, you can create custom operators in CPython. Creating custom operators
consists of wrapping Python routines in a DPF-compliant way so that you can access them in the same way
as you access the native operators in the :class:`Operator <ansys.dpf.core.dpf_operator.Operator>` class in
PyDPF-Core or in any supported client API.

With support for custom operators, PyDPF-Core becomes a development tool offering:

- **Accessibility:** A simple script can define a basic operator plugin.

- **Componentization:** Operators with similar applications can be grouped in Python plug-in packages.

- **Easy distribution:** Standard Python tools can be used to package, upload, and download custom operators.

- **Dependency management:** Third-party Python modules can be added to the Python package.

- **Reusability:** A documented and packaged operator can be reused in an infinite number of workflows.

- **Remotable and parallel computing:** Native DPF capabilities are inherited by custom operators.

The only prerequisite for creating custom operators is to be familiar with native operators.
For more information, see :ref:`ref_user_guide_operators`.

Install module
--------------

Once an Ansys-unified installation is complete, you must install the ``ansys-dpf-core`` module in the Ansys
installer's Python interpreter.

#. Download the script for you operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/tutorials/enriching_dpf_capabilities/install_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/tutorials/enriching_dpf_capabilities/install_ansys_dpf_core_in_ansys.sh>`

#. Run the downloaded script for installing with optional arguments:

   - ``-awp_root``: Path to the Ansys root installation folder. For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.
   - ``-pip_args``: Optional arguments to add to the ``pip`` command. For example, ``--extra-index-url`` or
     ``--trusted-host``.

If you ever want to uninstall the ``ansys-dpf-core`` module from the Ansys installation, you can do so.

#. Download the script for your operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/tutorials/enriching_dpf_capabilities/uninstall_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/tutorials/enriching_dpf_capabilities/uninstall_ansys_dpf_core_in_ansys.sh>`.
  
#. Run the downloaded script for uninstalling with the optional argument:

   - ``-awp_root``: Path to the Ansys root installation folder.  For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.


Create operators
----------------

Creating a basic operator plugin consists of writing a single Python script. An operator implementation
derives from the :class:`CustomOperatorBase <ansys.dpf.core.custom_operator.CustomOperatorBase>` class and a call to
the :func:`record_operator() <ansys.dpf.core.custom_operator.record_operator>` method.

This example script shows how you create a basic operator plugin:

.. literalinclude:: custom_operator_example.py


.. code-block::

        def load_operators(*args):
            record_operator(CustomOperator, *args)


In the various properties for the class, you specify the following:

- Name for the custom operator
- Description of what the operator does
- Dictionary for each input and output pin, which includes the name, a list of supported types, a description,
  and whether it is optional and/or ellipsis (meaning that the specification is valid for pins going from pin
  number *x* to infinity)
- List for operator properties, including name to use in the documentation and code generation and the
  operator category. The optional ``license`` property allows to define a required license to check out
  when running the operator. Set it equal to ``any_dpf_supported_increments`` to allow any license
  currently accepted by DPF (see :ref:`here<target_to_ansys_license_increments_list>`)

For specific examples on writing operator plugins, see :ref:`python_operators`.

Load the plug-in
----------------

Once a custom operator is created, you can use the :func:`load_library() <ansys.dpf.core.core.load_library>` method to load it.

- The first argument is the path to the directory with the plugin.
- The second argument is ``py_<plugin>``, where <plugin> is the name identifying the plug-in (same name of the Python file).
- The third argument is the function name for recording operators.

.. code::

    dpf.load_library(
    r"path/to/plugins",
    "py_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin.py
    "load_operators")

Use custom operators
--------------------

Once the plugin is loaded, you can instantiate the custom operator:

.. code::

    new_operator = dpf.Operator("custom_operator") # if "custom_operator" is what is returned by the ``name`` property

References
----------
For more information, see :ref:`ref_custom_operator` in the **API reference**
and :ref:`python_operators` in **Examples**.
