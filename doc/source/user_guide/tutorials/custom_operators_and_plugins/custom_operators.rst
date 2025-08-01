.. _tutorials_custom_operators_and_plugins_custom_operator:

================
Custom operators
================

.. note::

    This tutorial requires DPF 7.1 or above (2024 R1).

This tutorial shows the basics of creating a custom operator in Python and loading it ont a server for use.

.. note::

    You can create custom operators in CPython using PyDPF-Core for use with DPF in Ansys 2023 R1 and later.

It first presents how to :ref:`create a custom DPF operator<tutorials_custom_operators_and_plugins_custom_operator_create_custom_operator>`
in Python using PyDPF-Core.

It then shows how to :ref:`make a plugin<tutorials_custom_operators_and_plugins_custom_operator_create_custom_plugin>`
out of this single operator.

The next step is to :ref:`load the plugin on the server<tutorials_custom_operators_and_plugins_custom_operator_load_the_plugin>` to record its operators.

The final step is to instantiate the custom operator from the client API and :ref:`use it<tutorials_custom_operators_and_plugins_custom_operator_use_the_custom_operator>`.

.. note::

    In this tutorial the DPF client API used is PyDPF-Core but, once recorded on the server,
    you can call the operators of the plugin using any of the DPF client APIs
    (C++, CPython, IronPython), as you would any other operator.


:jupyter-download-script:`Download tutorial as Python script<custom_operators>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<custom_operators>`


.. _tutorials_custom_operators_and_plugins_custom_operator_create_custom_operator:

Create a custom operator
------------------------

To create a custom DPF operator using PyDPF-Core, define a custom operator class inheriting from
the :class:`CustomOperatorBase <ansys.dpf.core.custom_operator.CustomOperatorBase>` class in a dedicated Python file.

The following are sections of a file named `custom_operator_example.py` available under ``ansys.dpf.core.examples.python_plugins``:

First declare the custom operator class, with necessary imports and a first property to define the operator scripting name:

.. literalinclude:: /../../src/ansys/dpf/core/examples/python_plugins/custom_operator_example.py
    :end-at: return "my_custom_operator"

Next, set the `specification` property of your operator with:

- a description of what the operator does
- a dictionary for each input and output pin. This dictionary includes the name, a list of supported types, a description,
  and whether it is optional and/or ellipsis (meaning that the specification is valid for pins going from pin
  number *x* to infinity)
- a list for operator properties, including name to use in the documentation and code generation and the
  operator category. The optional ``license`` property lets you define a required license to check out
  when running the operator. Set it equal to ``any_dpf_supported_increments`` to allow any license
  currently accepted by DPF (see :ref:`here<target_to_ansys_license_increments_list>`)

.. literalinclude:: /../../src/ansys/dpf/core/examples/python_plugins/custom_operator_example.py
    :start-after: return "my_custom_operator"
    :end-at: return spec

Next, implement the operator behavior in its `run` method:

.. literalinclude:: /../../src/ansys/dpf/core/examples/python_plugins/custom_operator_example.py
    :start-after: return spec
    :end-at: self.set_succeeded()

The `CustomOperator` class is now ready for packaging into any DPF Python plugin.

.. _tutorials_custom_operators_and_plugins_custom_operator_create_custom_plugin:

Package as a plugin
-------------------

You must package your custom operator as a `plugin`,
which is what you can later load onto a running DPF server,
or configure your installation to automatically load when starting a DPF server.

A DPF plugin contains Python modules with declarations of custom Python operators such as seen above.
However, it also has to define an entry-point for the DPF server to call,
which records the operators of the plugin into the server registry of available operators.

This is done by defining a function (DPF looks for a function named ``load_operators`` by default)
somewhere in the plugin with signature ``*args`` and a call to the
:func:`record_operator() <ansys.dpf.core.custom_operator.record_operator>` method for each custom operator.

In this tutorial, the plugin is made of a single operator, in a single Python file.
You can transform this single Python file into a DPF Python plugin very easily by adding
``load_operators(*args)`` function with a call to the
:func:`record_operator() <ansys.dpf.core.custom_operator.record_operator>` method at the end of the file.

.. literalinclude:: /../../src/ansys/dpf/core/examples/python_plugins/custom_operator_example.py
    :start-at: def load_operators(*args):

PS: You can declare several custom operator classes in the same file, with as many calls to
:func:`record_operator() <ansys.dpf.core.custom_operator.record_operator>` as necessary.

.. _tutorials_custom_operators_and_plugins_custom_operator_load_the_plugin:

Load the plugin
---------------

First, start a server in gRPC mode, which is the only server type supported for custom Python plugins.

.. jupyter-execute::

    import ansys.dpf.core as dpf

    # Python plugins are not supported in process.
    server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)

With the server and custom plugin ready, use the :func:`load_library() <ansys.dpf.core.core.load_library>` method in a PyDPF-Core script to load it.

- The first argument is the path to the directory with the plugin.
- The second argument is ``py_<plugin>``, where <plugin> is the name identifying the plugin (the name of the Python file for a single file).
- The third argument is the name of the function in the plugin which records operators (``load_operators`` by default).

.. jupyter-execute::

    # Get the path to the example plugin
    from pathlib import Path
    from ansys.dpf.core.examples.python_plugins import custom_operator_example
    custom_operator_folder = Path(custom_operator_example.__file__).parent

    # Load it on the server
    dpf.load_library(
        filename=custom_operator_folder,  # Path to the plugin directory
        name="py_custom_operator_example",  # Look for a Python file named 'custom_operator_example.py'
        symbol="load_operators",  # Look for the entry-point where operators are recorded
        server=server,  # Load the plugin on the server previously started
        generate_operators=False,  # Do not generate the Python module for this operator
    )

    # You can verify the operator is now in the list of available operators on the server
    assert "my_custom_operator" in dpf.dpf_operator.available_operator_names(server=server)

.. _tutorials_custom_operators_and_plugins_custom_operator_use_the_custom_operator:

Use the custom operator
-----------------------

Once the plugin is loaded, you can instantiate the custom operator based on its name.

.. jupyter-execute::

    my_custom_op = dpf.Operator(name="my_custom_operator", server=server) # as returned by the ``name`` property
    print(my_custom_op)

Finally, run it as any other operator.

.. jupyter-execute::

    # Create a bogus field to use as input
    in_field = dpf.Field(server=server)
    # Give it a name
    in_field.name = "initial name"
    print(in_field)
    # Set it as input of the operator
    my_custom_op.inputs.input_0.connect(in_field)
    # Run the operator by requesting its output
    out_field = my_custom_op.outputs.output_0()
    print(out_field)

References
----------
For more information, see :ref:`ref_custom_operator` in the **API reference**
and :ref:`python_operators` in **Examples**.
