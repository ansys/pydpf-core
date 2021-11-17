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
If an issue appeared while using the dpf python API to connect to an initialized server with :py:meth:`connect_to_server()
<ansys.dpf.core.server.connect_to_server>`, please make sure that the IP address and port number set as parameters
are applicable for a DPF server started on the network.

Importing DPF python module
~~~~~~~~~~~~~~~~~~~~~~~~~~~
If while doing:

.. code-block:: default

    from ansys.dpf import core as dpf

missing modules are listed as an error, please refer to the compatibility paragraph of :ref:`_ref_getting_started`.
The module `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ should always be synchronized with its server
version.


Performance issues
------------------

Getting and Setting Field's data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Accessing or modifying field's data :py:class:`Field<ansys.dpf.core.field.Field>` entity by entity can
be slow if the field's size is large or if the server is far from the python client. To improve performances,
please use :py:meth:`as_local_field()<ansys.dpf.core.field.Field.as_local_field>` in a context manager.
An example of usage can be found in :ref:`_ref_use_local_data_example`.

Slow autocompletion on notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Autocompletion in Jupyter notebook can sometimes be slow for large models. The interpreter might
evaluate some properties getters when the tab key is pressed. To unable this capability please use
:py:meth:`disable_interpreter_properties_evaluation()<ansys.dpf.core.settings.disable_interpreter_properties_evaluation>`:

.. code-block:: default

    from ansys.dpf import core as dpf
    dpf.settings.disable_interpreter_properties_evaluation()


