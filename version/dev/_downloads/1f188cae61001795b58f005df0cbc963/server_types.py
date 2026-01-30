#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf

# Import the examples module
from ansys.dpf.core import examples


# In[2]:


# Start a local DPF server with default InProcess configuration
local_server = dpf.start_local_server()

# Display the server object
print(local_server)


# In[3]:


# Instantiate a displacement Operator on the local server
local_operator = dpf.operators.result.displacement(server=local_server)

# Display the Operator
print(local_operator)


# In[4]:


# Define the result file path using an example file
result_file = examples.find_simple_bar()

# Instantiate a Model on the local server
local_model = dpf.Model(result_file, server=local_server)

# Display basic information about the Model
print(local_model)


# In[5]:


# Get the GrpcServer configuration
grpc_server_config = dpf.AvailableServerConfigs.GrpcServer

# Start a local server with gRPC configuration
grpc_server = dpf.start_local_server(config=grpc_server_config)

# Display the server object
print(grpc_server)


# In[6]:


# Get the server IP address
server_ip = grpc_server.ip

# Get the server port
server_port = grpc_server.port

# Display connection information
print(f"Server IP: {server_ip}")
print(f"Server Port: {server_port}")


# In[7]:


# Connect to the remote gRPC server
remote_server = dpf.connect_to_server(ip=server_ip, port=server_port, as_global=False)

# Display the connected server object
print(remote_server)


# In[8]:


# Instantiate an Operator on the remote server
remote_operator = dpf.operators.result.displacement(server=remote_server)

# Display the remote Operator
print(remote_operator)


# In[9]:


# Instantiate a Model on the remote server
remote_model = dpf.Model(result_file, server=remote_server)

# Display basic information about the remote Model
print(remote_model)


# In[10]:


# Set the environment variable on Windows (run in PowerShell or Command Prompt)
# os.environ['ANSYS_GRPC_CERTIFICATES'] = r'C:\path\to\certificates'
pass


# In[11]:


# Set the environment variable on Linux (run in terminal)
# export ANSYS_GRPC_CERTIFICATES=/path/to/certificates
pass


# In[12]:


# Disable mTLS on Windows (not recommended for production)
# os.environ['DPF_DEFAULT_GRPC_MODE'] = 'insecure'
pass


# In[13]:


# Disable mTLS on Linux (not recommended for production)
# export DPF_DEFAULT_GRPC_MODE=insecure
pass


# In[14]:


# Get InProcessServer configuration
in_process_config = dpf.AvailableServerConfigs.InProcessServer

# Start an InProcess server
in_process_server = dpf.start_local_server(config=in_process_config, as_global=False)

# Display the InProcess server
print(f"InProcess server: {in_process_server}")


# In[15]:


# Get GrpcServer configuration
grpc_config = dpf.AvailableServerConfigs.GrpcServer

# Start a gRPC server
grpc_server_2 = dpf.start_local_server(config=grpc_config, as_global=False)

# Display the gRPC server
print(f"gRPC server: {grpc_server_2}")


# In[16]:


# Get LegacyGrpcServer configuration (for compatibility with older versions)
legacy_grpc_config = dpf.AvailableServerConfigs.LegacyGrpcServer

# Start a legacy gRPC server
legacy_grpc_server = dpf.start_local_server(config=legacy_grpc_config, as_global=False)

# Display the legacy gRPC server
print(f"Legacy gRPC server: {legacy_grpc_server}")

