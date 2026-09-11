.. _user_guide_custom_operators:

================
Custom Operators
================

Starting with Ansys 2022 R2, DPF offers the capability to create user-defined Operators in CPython.
Writing Operators allows to wrap python routines in a DPF compliant way so that it can be accessed
the same way as a native :class:`ansys.dpf.core.dpf_operator.Operator` in pyDPF or in any supported
client API.
With this feature, DPF can be used as a development tool offering:

- Accessibility: a single script defines an Operator and its documentation.

- Componentization: Operators with similar applications can be grouped in python packages named ``Plugins``.

- Easy Distribution: standard python tools can be used to package, upload and download the user-defined operators.

- Dependencies management: third party python modules can be added to the python package.

- Reusability: a documented and packaged Operator can be reused in an infinite number of workflows.

- Remotable and parallel computing: native DPF's capabilities are inherited by the user-defined Operators.


A prerequisite to writing user-defined Operators is to be comfortable with the concept of Operator (:ref:`ref_user_guide_operators`).


Installation
------------

Once Ansys unified installation completed, ansys-dpf-core module needs to be installed in the Ansys installer's Python
interpreter. Run this :download:`powershell script </user_guide/install_ansys_dpf_core_in_ansys.ps1>` for windows
or this :download:`shell script </user_guide/install_ansys_dpf_core_in_ansys.sh>` for linux with the optional
arguments:

- -awp_root : path to Ansys root installation path (usually ending with Ansys Inc/v222), defaults to environment variable AWP_ROOT222
- -pip_args : optional arguments that add to pip command (ie. --extra-index-url, --trusted-host,...)

If you wish to uninstall ansys-dpf-core module of the Ansys installation, run this :download:`powershell script </user_guide/uninstall_ansys_dpf_core_in_ansys.ps1>` for windows
or this :download:`shell script </user_guide/uninstall_ansys_dpf_core_in_ansys.sh>` for linux with the optional
argument:

- -awp_root : path to Ansys root installation path (usually ending with Ansys Inc/v222), defaults to environment variable AWP_ROOT222


Writing the Operator
--------------------

Basic Implementation
~~~~~~~~~~~~~~~~~~~~

To write the simplest DPF python plugins, a single python script is necessary.
An Operator implementation deriving from :class:`ansys.dpf.core.custom_operator.CustomOperatorBase`
and a call to :py:func:`ansys.dpf.core.custom_operator.record_operator` are the 2 necessary steps to create a plugin.


.. literalinclude:: custom_operator_example.py

.. code-block::

        def load_operators(*args):
            record_operator(CustomOperator, *args)


Input and output pins descriptions take a dictionary mapping pin numbers to their
:class:`ansys.dpf.core.operator_specification.PinSpecification`. PinSpecification takes a name (used in the documentation,
and in the code generation), a list of supported types, a document, whether the pin is optional and/or ellipsis (meaning
the pin specification is valid for pins going from pin number to infinity).
:class:`ansys.dpf.core.operator_specification.SpecificationProperties` allows to specify other properties of the
Operator like its user name (mandatory) or its category (used in the documentation,
and in the code generation).

See example of Custom Operators implementations in the Examples section :ref:`python_operators`.


Package Custom Operators
~~~~~~~~~~~~~~~~~~~~~~~~

To create a DPF plugin with several Operators or with complex routines, python packages of Operators can be created.
The benefits of writing packages instead of simple scripts are:

- componentization (split the code in several python modules or files).
- distribution (with packages, standard python tools can be used to upload and download packages).
- documentation (READMEs, docs, tests and examples can be added to the package).

A plugin as a package can be a folder with a structure like:


.. card:: custom_plugin

   .. dropdown:: __init__.py

      .. code-block:: default

        from operators_loader import load_operators

   .. dropdown:: operators.py

        .. literalinclude:: custom_operator_example.py

   .. dropdown:: operators_loader.py

      .. code-block:: default

        from custom_plugin import operators
        from ansys.dpf.core.custom_operator import record_operator


        def load_operators(*args):
            record_operator(operators.CustomOperator, *args)

   .. dropdown:: common.py

      .. code-block:: default

        #write needed python routines as classes and functions here.

Add Third Party Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: custom_operators_deps.rst

A plugin as a package with dependencies can be a folder with a structure like:

.. card:: plugins

    .. card:: custom_plugin

       .. dropdown:: __init__.py

          .. code-block:: default

            from operators_loader import load_operators

       .. dropdown:: operators.py

            .. literalinclude:: custom_operator_example.py

       .. dropdown:: operators_loader.py

          .. code-block:: default

            from custom_plugin import operators
            from ansys.dpf.core.custom_operator import record_operator


            def load_operators(*args):
                record_operator(operators.CustomOperator, *args)

       .. dropdown:: common.py

          .. code-block:: default

            #write needed python routines as classes and functions here.

       .. dropdown:: requirements.txt

           .. literalinclude:: /examples/07-python-operators/plugins/gltf_plugin/requirements.txt

       .. dropdown:: assets

           - winx64.zip
           - linx64.zip

   .. dropdown:: custom_plugin.xml

      .. literalinclude:: custom_plugin.xml
         :language: xml


Use the Custom Operators
------------------------

Once a python plugin is written, it can be loaded with the function :func:`ansys.dpf.core.core.load_library`
taking as first argument the path to the directory of the plugin, as second argument ``py_`` + any name identifying the plugin,
and as last argument the function’s name used to record operators.

If a single script has been used to create the plugin, then the second argument should be ``py_`` + name of the python file:

.. code::

    dpf.load_library(
    r"path/to/plugins",
    "py_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin.py
    "load_operators")

If a python package was written, then the second argument should be ``_py`` + any name:

.. code::

    dpf.load_library(
    r"path/to/plugins/custom_plugin",
    "py_my_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin/__init__.py
    "load_operators")

Once the plugin loaded, the Operator can be instantiated with:

.. code::

    new_operator = dpf.Operator("custom_operator") # if "custom_operator" is what is returned by the ``name`` property



References
----------
See the API reference at :ref:`ref_custom_operator` and examples of Custom Operators implementations in :ref:`python_operators`.
