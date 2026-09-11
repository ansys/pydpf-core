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
result_file_path_1 = examples.find_static_rst()
# Create the DataSources object
ds_1 = dpf.DataSources(result_path=result_file_path_1)


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


# In[3]:


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


# In[4]:


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


# In[5]:


# Create the Model
model_1 = dpf.Model(data_sources=ds_1)
# Get the mesh
meshed_region_11 = model_1.metadata.meshed_region


# In[6]:


# Create the Model
model_2 = dpf.Model(data_sources=ds_2)
# Get the mesh
meshed_region_21 = model_2.metadata.meshed_region


# In[7]:


# Create the Model
model_3 = dpf.Model(data_sources=ds_3)
# Get the mesh
meshed_region_31 = model_3.metadata.meshed_region


# In[8]:


# Create the Model
model_4 = dpf.Model(data_sources=ds_4)
# Get the mesh
meshed_region_41 = model_4.metadata.meshed_region


# In[9]:


# Print the MeshedRegion
print(meshed_region_11)


# In[10]:


# Print the MeshedRegion
print(meshed_region_21)


# In[11]:


# Print the MeshedRegion
print(meshed_region_31)


# In[12]:


# Print the MeshedRegion
print(meshed_region_41)


# In[13]:


# Get the mesh with the mesh_provider operator
meshed_region_12 = ops.mesh.mesh_provider(data_sources=ds_1).eval()


# In[14]:


# Get the mesh with the mesh_provider operator
meshed_region_22 = ops.mesh.mesh_provider(data_sources=ds_2).eval()


# In[15]:


# Get the mesh with the mesh_provider operator
meshed_region_32 = ops.mesh.mesh_provider(data_sources=ds_3).eval()


# In[16]:


# Get the mesh with the mesh_provider operator
meshed_region_42 = ops.mesh.mesh_provider(data_sources=ds_4).eval()


# In[17]:


# Print the MeshedRegion
print(meshed_region_12)


# In[18]:


# Print the MeshedRegion
print(meshed_region_22)


# In[19]:


# Print the MeshedRegion
print(meshed_region_32)


# In[20]:


# Print the MeshedRegion
print(meshed_region_42)

