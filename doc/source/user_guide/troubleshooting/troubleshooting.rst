.. _user_guide_troubleshooting:

===============
Troubleshooting
===============

This page explains how to resolve the most common issues encountered when
using PyDPF-Core. It also includes suggestions for improving scripts.

.. _ref_server_issues:

==============
Server issues
==============

Start the DPF server
~~~~~~~~~~~~~~~~~~~~~
When using PyDPF-Core to start the server with the
:py:meth:`start_local_server() <ansys.dpf.core.server.start_local_server>` method
or when starting the server manually with the ``Ans.Dpf.Grpc.sh`` or ``Ans.Dpf.Grpc.bat``
file, a Python error might occur: ``TimeoutError: Server did not start in 10 seconds``.
This kind of error might mean that the server or its dependencies were not found. Ensure that
the ``AWP_ROOT{VER}`` environment variable is set when using DPF from an Ansys unified install,
where ``VER`` is the three-digit numeric format for the version, such as ``221`` or ``222``.

Connect to the DPF server
~~~~~~~~~~~~~~~~~~~~~~~~~
If an issue appears while using Py-DPF code to connect to an initialized server with the
:py:meth:`connect_to_server() <ansys.dpf.core.server.connect_to_server>` method, ensure that the
IP address and port number that are set as parameters are applicable for a DPF server started
on the network.

Import the ``pydpf-core`` package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Assume that you are importing the ``PyDPF-Core`` package:

.. code-block:: default

    from ansys.dpf import core as dpf

If an error lists missing modules, see :ref:`ref_compatibility`.
For ``PyDPF-Core``<0.10.0, the `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ module
should always be synchronized with its server version.

.. _ref_model_issues:

============
Model issues
============

Invalid UTF-8 error
~~~~~~~~~~~~~~~~~~~
Assume that you are trying to access the :class:`ansys.dpf.core.model.Model` class.
The following error might be raised:

.. code-block:: default

    [libprotobuf ERROR C:\.conan\897de8\1\protobuf\src\google\protobuf\wire_format_lite.cc:578] 
    String field 'ansys.api.dpf.result_info.v0.ResultInfoResponse.user_name' contains invalid UTF-8 
    data when serializing a protocol buffer. Use the 'bytes' type if you intend to send raw bytes.

Invalid UTF-8 data is preventing the model from being accessed. To avoid this error, ensure that
you are using PyDPF-Core version 0.3.2 or later. While a warning is still raised, the invalid UTF-8
data should not prevent you from using the :class:`ansys.dpf.core.model.Model` class.

Then, with result files reproducing this issue, you can prevent the warning from being raised with:

.. code-block:: default

    from ansys.dpf import core as dpf
    dpf.settings.set_dynamic_available_results_capability(False)
	
However, the preceding code disables the reading and generation of the available results for the model.
Any static results that are available for the model are used instead.

.. _ref_plotting_issues:

===============
Plotting issues
===============

When trying to plot a result with DPF, the following error might be raised:

.. code-block:: default

    ModuleNotFoundError: No module named 'pyvista'

In that case, simply install `PyVista <https://pyvista.org/>`_` with this command:

.. code-block:: default

    pip install pyvista

Another option is to install PyVista along with PyDPF-Core. For more information, see 
:ref:`Install with plotting capabilities<target_to_install_with_plotting_capabilities>`

.. _ref_performance_issues:

==================
Performance issues
==================

Get and set a field's data
~~~~~~~~~~~~~~~~~~~~~~~~~~
Using the :py:class:`Field<ansys.dpf.core.field.Field>` class to get or set field data entity
by entity can be slow if the field's size is large or if the server is far from the Python client.
To improve performance, use the :py:meth:`as_local_field()<ansys.dpf.core.field.Field.as_local_field>`
method in a context manager to bring the field data from the server to your local machine. For an
example, see :ref:`ref_use_local_data_example`.

Autocompletion in notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Autocompletion in Jupyter notebook can sometimes be slow for large models. The interpreter might
evaluate the getters of some properties when the tab key is pressed. To disable this capability, use the
:py:meth:`disable_interpreter_properties_evaluation()<ansys.dpf.core.settings.disable_interpreter_properties_evaluation>`
method:

.. code-block:: default

    from ansys.dpf import core as dpf
    dpf.settings.disable_interpreter_properties_evaluation()

