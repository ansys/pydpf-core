#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_1 = examples.find_multishells_rst()
# Create the model
model_1 = dpf.Model(data_sources=result_file_path_1)
# Get the mesh
meshed_region_1 = model_1.metadata.meshed_region


# In[2]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_2 = examples.download_d3plot_beam()
# Create the DataSources object
ds_2 = dpf.DataSources()
ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
# Create the model
model_2 = dpf.Model(data_sources=ds_2)
# Get the mesh
meshed_region_2 = model_2.metadata.meshed_region


# In[3]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
# Create the model
model_3 = dpf.Model(data_sources=result_file_path_3)
# Get the mesh
meshed_region_3 = model_3.metadata.meshed_region


# In[4]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_4 = examples.download_cfx_mixing_elbow()
# Create the model
model_4 = dpf.Model(data_sources=result_file_path_4)
# Get the mesh
meshed_region_4 = model_4.metadata.meshed_region


# In[5]:


# Split the mesh by material
meshes_11 = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()

# Print the meshes
print(meshes_11)


# In[6]:


# Split the mesh by material
meshes_21 = ops.mesh.split_mesh(mesh=meshed_region_2, property="mat").eval()

# Print the meshes
print(meshes_21)


# In[7]:


# Split the mesh by material
meshes_31 = ops.mesh.split_mesh(mesh=meshed_region_3, property="mat").eval()

# Print the meshes
print(meshes_31)


# In[8]:


# Split the mesh by material
meshes_41 = ops.mesh.split_mesh(mesh=meshed_region_4, property="mat").eval()
# Print the meshes
print(meshes_41)


# In[9]:


# Define the scoping split by material
split_scoping_1 = ops.scoping.split_on_property_type(mesh=meshed_region_1, label1="mat").eval()
# Get the split meshes
meshes_12 = ops.mesh.from_scopings(scopings_container=split_scoping_1, mesh=meshed_region_1).eval()
# Print the meshes
print(meshes_12)


# In[10]:


# Define the scoping split by material
split_scoping_2 = ops.scoping.split_on_property_type(mesh=meshed_region_2, label1="mat").eval()
# Get the split meshes
meshes_22 = ops.mesh.from_scopings(scopings_container=split_scoping_2, mesh=meshed_region_2).eval()
# Print the meshes
print(meshes_22)


# In[11]:


# Define the scoping split by material
split_scoping_3 = ops.scoping.split_on_property_type(mesh=meshed_region_3, label1="mat").eval()
# Get the split meshes
meshes_32 = ops.mesh.from_scopings(scopings_container=split_scoping_3, mesh=meshed_region_3).eval()
# Print the meshes
print(meshes_32)


# In[12]:


# Define the scoping split by material
split_scoping_4 = ops.scoping.split_on_property_type(mesh=meshed_region_4, label1="mat").eval()
# Get the split meshes
meshes_42 = ops.mesh.from_scopings(scopings_container=split_scoping_4, mesh=meshed_region_4).eval()
# Print the meshes
print(meshes_42)

