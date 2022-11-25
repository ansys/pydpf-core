.. _user_guide_server_types:

===========================
Client-server communication
===========================

Terminology
-----------

DPF is based on a **client-server** architecture. It allows **local** or **remote**
client-server **communication** capabilities.

The DPF Server is a set of files that enables DPF capabilities.

The different DPF client APIs (CPython, IronPython, C++, and so on) enable the use
of these capabilities.

PyDPF is a term encompassing both the CPython client
(the Python packages such as ansys-dpf-core or ansys-dpf-post, available on PyPI)
and the IronPython client (available within Ansys Mechanical).


Getting started with DPF local server
-------------------------------------

Default use of DPF is local, using :class:`InProcess <ansys.dpf.core.server_types>` class.

.. code-block::
	   
    from ansys.dpf import core as dpf
    local_server = dpf.start_local_server()
    local_server

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    <ansys.dpf.core.server_types.InProcessServer object at ...>

This server can now be used to instantiate Models, Operators, and so on.

.. code-block::
	
    # instantiate an operator
    local_operator = dpf.operators.results.displacement(server=local_server)
	
    # instantiate a model
    from ansys.dpf.core import examples
    local_model = dpf.Model(examples.find_simple_bar(), server=local_server)
	

Getting started with DPF GRPC server
------------------------------------

GRPC communication is enabled using :class:`GrpcServer <ansys.dpf.core.server_types>`. 

.. code-block::
	   
    from ansys.dpf import core as dpf
    grpc_server_config = dpf.AvailableServerConfigs.GrpcServer
    grpc_server = dpf.start_local_server(config=grpc_server_config)
    grpc_server

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    <ansys.dpf.core.server_types.GrpcServer object at ...>

You can obtain the server port and ip:

.. code-block::

    print(grpc_server)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Server: {'server_ip': '127.0.0.1', 'server_port': 50052, 'server_process_id': 9999, 'server_version': '6.0', 'os': 'nt'}
	
From a another machine, you can connect remotly to this server and instantiate Models, Operators, and so on:

.. code-block::
	   
    from ansys.dpf import core as dpf
    grpc_remote_server = dpf.connect_to_server(ip='127.0.0.1', port=50052)
    
    # instantiate an operator
    remote_operator = dpf.operators.results.displacement(server=grpc_remote_server)
    
    # instantiate a model
    from ansys.dpf.core import examples
    remote_model = dpf.Model(examples.find_simple_bar(), server=grpc_remote_server)
	
GRPC server use also enables distributed computation capabilities. To learn more about 
distributed computation with DPF, see :ref:`distributed_post`.
	

Starting a server using a configuration
---------------------------------------

The different DPF server types can be started using one of the 
:class:`AvailableServerConfigs <ansys.dpf.core.server_factory>` configurations. 

.. code-block::
    
    in_process_config = dpf.AvailableServerConfigs.InProcessServer
    in_process_server = dpf.start_local_server(config=in_process_config)
    
    grpc_config = dpf.AvailableServerConfigs.GrpcServer
    grpc_server = dpf.start_local_server(config=grpc_config)
    
    legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer
    legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config)


Advanced concepts and release history
-------------------------------------

The communication logic with a DPF server is defined when starting it using
an instance of the :class:`ServerConfig <ansys.dpf.core.server_factory>` class.
Different predefined server configurations are available in DPF,
each answering a different use-case
(See the :class:`AvailableServerConfigs <ansys.dpf.core.server_factory>` class).

- The :class:`GrpcServer <ansys.dpf.core.server_types>` configuration is available starting 
  with server version 4.0 (Ansys 2022 R2).
  It allows you to remotely connect to a DPF server across a network by telling the client
  to communicate with this server via the gRPC communication protocol.
  Although it can be used to communicate with a DPF server running on the same local machine,
  in that case the next configuration is better for this option.
- The :class:`InProcess <ansys.dpf.core.server_types>` configuration is available starting 
  with server version 4.0 (Ansys 2022 R2).
  It indicates to the client that a DPF server is installed on the local machine, enabling direct 
  calls to the server binaries from within the client's own Python process.
  This removes the need to copy and send data between the client and server, and makes calls
  to the server functionalities much faster as well as using less memory.
- The :class:`LegacyGrpcServer <ansys.dpf.core.server_types>` configuration is the only one 
  available for server versions below 4.0
  (Ansys 2022 R1, Ansys 2021 R2 and Ansys 2021 R1).
  The client communicates with a local or remote DPF server via the gRPC communication protocol.

For DPF with Ansys 2023 R1 and newer, the default configuration is set to :class:`InProcess <ansys.dpf.core.server_types>`,
meaning that servers are launched on the local machine.
To launch a DPF server on a remote machine and communicate with it using gRPC, use
the :class:`GrpcServer <ansys.dpf.core.server_types>` configuration as shown in :ref:`ref_server_types_example`.
