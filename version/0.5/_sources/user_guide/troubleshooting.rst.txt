.. _user_guide_troubleshooting:

===============
Troubleshooting
===============
This section explains how to resolve the most common issues encountered with ``pydpf-core``.
It also includes suggestions for improving scripts.

Using the Server
----------------

Starting DPF Server
~~~~~~~~~~~~~~~~~~~
While using the DPF-Python API to start the server with :py:meth:`start_local_server()
<ansys.dpf.core.server.start_local_server>` or while starting the server manually (with ``Ans.Dpf.Grpc.sh``
or ``Ans.Dpf.Grpc.bat``), a Python error might occur: "TimeoutError: Server did not start in 10 seconds".
This kind of error might mean that the server or its dependencies were not found. Ensure that
the environment variable ``AWP_ROOT{VER}`` is set, where VER=212, 221, ....

Connecting to DPF Server
~~~~~~~~~~~~~~~~~~~~~~~~
If an issue appears while using the ``pydpf-core`` API to connect to an initialized server with :py:meth:`connect_to_server()
<ansys.dpf.core.server.connect_to_server>`, ensure that the IP address and port number that are set as parameters
are applicable for a DPF server started on the network.

Importing pydpf-core module
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Assume that you are importing the ``pydpf-core`` module:

.. code-block:: default

    from ansys.dpf import core as dpf

If an error lists missing modules, see the compatibility paragraph of :ref:`ref_getting_started`.
The module `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ should always be synchronized with its server
version.

Using the Model
---------------

Invalid UTF-8 Error
~~~~~~~~~~~~~~~~~~~
Assume that you are trying to access the :class:`ansys.dpf.core.model.Model`.
The following error can be raised:

.. code-block:: default

    [libprotobuf ERROR C:\.conan\897de8\1\protobuf\src\google\protobuf\wire_format_lite.cc:578] 
    String field 'ansys.api.dpf.result_info.v0.ResultInfoResponse.user_name' contains invalid UTF-8 
    data when serializing a protocol buffer. Use the 'bytes' type if you intend to send raw bytes.

This will prevent the model from being accessed. To avoid this error, ensure that you are using
a PyDPF-Core version higher than 0.3.2. In this case, a warning will still be raised, but it should not 
prevent the use of the Model. 

Then, with result files reproducing this issue, to avoid the warning to pop up, you can use:

.. code-block:: default

    from ansys.dpf import core as dpf
    dpf.settings.set_dynamic_available_results_capability(False)
	
However, this will disable the reading and generation of the available results of the model: static prewritten 
available results will be used instead.



Performance Issues
------------------

Getting and Setting a Field's Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Accessing or modifying field data :py:class:`Field<ansys.dpf.core.field.Field>` entity by entity can
be slow if the field's size is large or if the server is far from the Python client. To improve performance,
use :py:meth:`as_local_field()<ansys.dpf.core.field.Field.as_local_field>` in a context manager.
An example can be found in :ref:`ref_use_local_data_example`.

Slow Autocompletion in Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Autocompletion in Jupyter notebook can sometimes be slow for large models. The interpreter might
evaluate getters of some properties when the tab key is pressed. To disable this capability use
:py:meth:`disable_interpreter_properties_evaluation()<ansys.dpf.core.settings.disable_interpreter_properties_evaluation>`:

.. code-block:: default

    from ansys.dpf import core as dpf
    dpf.settings.disable_interpreter_properties_evaluation()


