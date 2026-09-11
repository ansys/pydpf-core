#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf


# In[2]:


# Define a time list that targets the times ids 14, 15, 16, 17
time_list_1 = [14, 15, 16, 17]

# Create the time Scoping object
time_scoping_1 = dpf.Scoping(ids=time_list_1, location=dpf.locations.time_freq)


# In[3]:


# Define a nodes list that targets the nodes with the ids 103, 204, 334, 1802
nodes_ids_1 = [103, 204, 334, 1802]

#  Create the mesh Scoping object
mesh_scoping_1 = dpf.Scoping(ids=nodes_ids_1, location=dpf.locations.nodal)


# In[4]:


# Define a time list that targets the times ids 14, 15, 16, 17
time_list_2 = [14, 15, 16, 17]

# Create the time Scoping object
time_scoping_2 = dpf.time_freq_scoping_factory.scoping_by_sets(cumulative_sets=time_list_2)


# In[5]:


# Define a nodes list that targets the nodes with the ids 103, 204, 334, 1802
nodes_ids_2 = [103, 204, 334, 1802]

# Create the mesh Scoping object
mesh_scoping_2 = dpf.mesh_scoping_factory.nodal_scoping(node_ids=nodes_ids_2)


# In[6]:


# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_1 = examples.download_transient_result()
# Create the DataSources object
ds_1 = dpf.DataSources(result_path=result_file_path_1)
# Create the model
model_1 = dpf.Model(data_sources=ds_1)


# In[7]:


# Get the MeshedRegion
meshed_region_1 = model_1.metadata.meshed_region

# Get a FieldsContainer with the displacement results
disp_fc = model_1.results.displacement.on_all_time_freqs.eval()

# Get a Field from the FieldsContainer
disp_field = disp_fc[0]


# In[8]:


# Extract the TimeFreq support
tfs_1 = model_1.metadata.time_freq_support


# In[9]:


# Extract the time frequencies
t_freqs_1 = tfs_1.time_frequencies

# Extract the time scoping
time_scop_1 = t_freqs_1.scoping

#Print the time scoping
print(time_scop_1)


# In[10]:


# Extract the TimeFreq support
tfs_2 = disp_fc.time_freq_support


# In[11]:


# Extract the time frequencies
t_freqs_2 = tfs_2.time_frequencies

# Extract the time scoping
time_scop_2 = t_freqs_2.scoping

#Print the time scoping
print(time_scop_2)


# In[12]:


# Extract the TimeFreq support
tfs_3 = disp_field.time_freq_support


# In[13]:


# Extract the time frequencies
t_freqs_3 = tfs_1.time_frequencies

# Extract the time scoping
time_scop_3 = t_freqs_3.scoping

#Print the time scoping
print(time_scop_3)


# In[14]:


# Extract the mesh scoping
mesh_scoping_3 = ops.scoping.from_mesh(mesh=meshed_region_1).eval()

# Print the mesh Scoping
print("Scoping from mesh", "\n", mesh_scoping_3, "\n")


# In[15]:


# Extract the mesh scoping
mesh_scoping_4 = meshed_region_1.elements.scoping

# Print the mesh Scoping
print("Scoping from mesh", "\n", mesh_scoping_4, "\n")


# In[16]:


# Extract the mesh scoping
mesh_scoping_5 = meshed_region_1.nodes.scoping

# Print the mesh Scoping
print("Scoping from mesh", "\n", mesh_scoping_5, "\n")


# In[17]:


# Define the extract_scoping operator
extract_scop_fc_op = ops.utility.extract_scoping(field_or_fields_container=disp_fc)

# Get the mesh Scopings from the operators output
mesh_scoping_6 = extract_scop_fc_op.outputs.mesh_scoping_as_scopings_container()

# Print the mesh Scopings
print("Scoping from FieldsContainer", "\n", mesh_scoping_6, "\n")


# In[18]:


# Extract the mesh scoping
mesh_scoping_7 = ops.utility.extract_scoping(field_or_fields_container=disp_field).eval()

# Print the mesh Scoping
print("Scoping from Field ", "\n", mesh_scoping_7, "\n")


# In[19]:


# Extract the mesh scoping
mesh_scoping_8 = disp_field

# Print the mesh Scoping
print("Scoping from Field", "\n", mesh_scoping_8, "\n")


# In[20]:


# Extract and scope the result using the Model.results method
disp_model = model_1.results.displacement(time_scoping=time_scoping_1, mesh_scoping=mesh_scoping_1).eval()

# Extract and scope the results using the result.displacement operator
disp_op = ops.result.displacement(data_sources=ds_1, time_scoping=time_scoping_1, mesh_scoping=mesh_scoping_1).eval()

# Print the displacement results
print("Displacement from Model.results ", "\n", disp_model, "\n")
print("Displacement from result.displacement operator", "\n", disp_op, "\n")


# In[21]:


# Extract the results for the entire mesh
disp_all_mesh = model_1.results.displacement.eval()

# Rescope the displacement results to get the data only for a specific set of nodes
disp_rescope = ops.scoping.rescope(fields=disp_all_mesh, mesh_scoping=mesh_scoping_1).eval()

# Print the displacement results for the entire mesh
print("Displacement results for the entire mesh", "\n", disp_all_mesh, "\n")

# Print the displacement results for the specific set of nodes
print("Displacement results rescoped ", "\n", disp_rescope, "\n")

