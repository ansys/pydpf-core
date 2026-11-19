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
result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
# Create the DataSources object
ds_3 = dpf.DataSources(result_path=result_file_path_3)


# In[2]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the result file path
result_file_path_4 = examples.download_cfx_mixing_elbow()
# Create the DataSources object
ds_4 = dpf.DataSources(result_path=result_file_path_4)


# In[3]:


# Instanciate the meshes_provider operator
meshes_31 =  ops.mesh.meshes_provider(data_sources=ds_3).eval()

# Print the meshes
print(meshes_31)


# In[4]:


# Instanciate the meshes_provider operator
meshes_41 =  ops.mesh.meshes_provider(data_sources=ds_4).eval()

# Print the meshes
print(meshes_41)


# In[5]:


# Instanciate the meshes_provider operator and specify a region
meshes_32 =  ops.mesh.meshes_provider(data_sources=ds_3, region_scoping=[3,12]).eval()

# Print the meshes
print(meshes_32)


# In[6]:


# Instanciate the meshes_provider operator specifying a region
meshes_42 =  ops.mesh.meshes_provider(data_sources=ds_4, region_scoping=[5,8]).eval()

# Print the meshes
print(meshes_42)

