.. _user_guide_server_types:

===========================
Client-server communication
===========================

Terminology
-----------

DPF is based on a **client-server** architecture. 

A DPF Server is a set of files that enables DPF capabilities.

PyDPF-Core is a Python client API communicating with a DPF Server, either
directly **in the same process** or through the network using **gRPC**.


DPF Server in the same process
------------------------------

Default use of a PyDPF-Core client and a DPF Server is in the same process,
using the :class:`InProcess <ansys.dpf.core.server_types.InProcessServer>` class.

.. code-block::
	   
    from ansys.dpf import core as dpf
    local_server = dpf.start_local_server()
    local_server

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    <ansys.dpf.core.server_types.InProcessServer object at ...>

This DPF Server can now be used to instantiate models, operators, and more.

.. code-block::
	
    # instantiate an operator
    local_operator = dpf.operators.results.displacement(server=local_server)
	
    # instantiate a model
    from ansys.dpf.core import examples
    local_model = dpf.Model(examples.find_simple_bar(), server=local_server)
	

DPF Server through the network using gRPC
-----------------------------------------

The :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` class is used
to enable gRPC communication: 

.. code-block::
	   
    from ansys.dpf import core as dpf
    grpc_server_config = dpf.AvailableServerConfigs.GrpcServer
    grpc_server = dpf.start_local_server(config=grpc_server_config)
    grpc_server

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    <ansys.dpf.core.server_types.GrpcServer object at ...>

You can obtain the server port and IP address:

.. code-block::

    print(grpc_server)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Server: {'server_ip': '127.0.0.1', 'server_port': 50052, 'server_process_id': 9999, 'server_version': '6.0', 'os': 'nt'}
	
From another machine, you can connect remotely to this DPF Server and instantiate models, operators, and more:

.. code-block::
	   
    from ansys.dpf import core as dpf
    grpc_remote_server = dpf.connect_to_server(ip='127.0.0.1', port=50052)
    
    # instantiate an operator
    remote_operator = dpf.operators.results.displacement(server=grpc_remote_server)
    
    # instantiate a model
    from ansys.dpf.core import examples
    remote_model = dpf.Model(examples.find_simple_bar(), server=grpc_remote_server)
	
Through the network using gRPC, a DPF sever enables distributed computation capabilities.
For more information, see :ref:`distributed_post`.
	

DPF Server startup using a configuration
----------------------------------------

The different DPF server types can be started using one of the 
:class:`AvailableServerConfigs <ansys.dpf.core.server_factory.AvailableServerConfigs>`
configurations. 

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
an instance of the :class:`ServerConfig <ansys.dpf.core.server_factory.ServerConfig>` class.
Different predefined server configurations are available in DPF,
each answering a different use case. For more information, see the
:class:`AvailableServerConfigs <ansys.dpf.core.server_factory.AvailableServerConfigs>` class.

- The :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` configuration is available in 
  server version 4.0 (Ansys 2022 R2) and later. It allows you to remotely connect to a DPF server
  across a network by telling the client to communicate with this server via the gRPC communication protocol.
  Although it can be used to communicate with a DPF server running on the same local machine, the next
  configuration is better for this option.
- The :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>` configuration is available
  in server version 4.0 (Ansys 2022 R2) and later. It indicates to the client that a DPF server is
  installed on the local machine, enabling direct calls to the server binaries from within the client's
  own Python process. This removes the need to copy and send data between the client and server, and it
  makes calls to the server functionalities much faster and uses less memory.
- The :class:`LegacyGrpcServer <ansys.dpf.core.server_types.LegacyGrpcServer>` configuration is
  the only one available for server versions 4.0 and earlier (Ansys 2022 R1, 2021 R2, and 2021 R1).
  The client communicates with a local or remote DPF server via the gRPC communication protocol.

For DPF with Ansys 2023 R1 and later, :class:`InProcessServer <ansys.dpf.core.server_types.InProcessServer>`
is the default configuration, which means that servers are launched on the local machine.
To launch a DPF server on a remote machine and communicate with it using gRPC, use
the :class:`GrpcServer <ansys.dpf.core.server_types.GrpcServer>` configuration as shown in :ref:`ref_server_types_example`.
