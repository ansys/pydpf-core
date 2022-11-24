.. _user_guide_server_types:

===========================
Client-server communication
===========================

DPF is based on a client-server architecture.

The DPF Server acts as a server, while the different client APIs (CPython, IronPython, C++, and so on)
act as clients connecting to it.
PyDPF is a term encompassing both the CPython client
(the Python packages such as ansys-dpf-core or ansys-dpf-post, available on PyPI)
and the IronPython client (available within Ansys Mechanical).

The communication logic with a DPF server is defined when starting it using
an instance of the :class:`ServerConfig <ansys.dpf.core.server_factory>` class.
Different predefined server configurations are available in DPF,
each answering a different use-case
(See the :class:`AvailableServerConfigs <ansys.dpf.core.server_factory>` class).

- The :class:`GrpcServer <ansys.dpf.core.server_types>` configuration is available starting with server version 4.0 (Ansys 2022 R2).
  It allows you to remotely connect to a DPF server across a network by telling the client
  to communicate with this server via the gRPC communication protocol.
  Although it can be used to communicate with a DPF server running on the same local machine,
  in that case the next configuration is better for this option.
- The :class:`InProcess <ansys.dpf.core.server_types>` configuration is available starting with server version 4.0 (Ansys 2022 R2).
  It indicates to the client that a DPF server is installed on the local machine, enabling direct calls
  to the server binaries from within the client's own Python process.
  This removes the need to copy and send data between the client and server, and makes calls
  to the server functionalities much faster as well as using less memory.
- The :class:`LegacyGrpcServer <ansys.dpf.core.server_types>` configuration is the only one available for server versions below 4.0
  (Ansys 2022 R1, Ansys 2021 R2 and Ansys 2021 R1).
  The client communicates with a local or remote DPF server via the gRPC communication protocol.

For DPF with Ansys 2023 R1 and newer, the default configuration is set to :class:`InProcess <ansys.dpf.core.server_types>`,
meaning that servers are launched on the local machine.
To launch a DPF server on a remote machine and communicate with it using gRPC, use
the :class:`GrpcServer <ansys.dpf.core.server_types>` configuration as shown in :ref:`_ref_server_types_example`.
