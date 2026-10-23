#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples

# Define the result file path
result_file_path_2 = examples.download_d3plot_beam()


# In[2]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples

# Define the result file path
result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]


# In[3]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples

# Define the result file path
result_file_path_4 = examples.download_cfx_mixing_elbow()


# In[4]:


# Create the DataSources object
ds_2 = dpf.DataSources()
ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
# Create the Model
model_2 = dpf.Model(data_sources=ds_2)


# In[5]:


# Create the Model
model_3 = dpf.Model(data_sources=result_file_path_3)


# In[6]:


# Create the Model
model_4 = dpf.Model(data_sources=result_file_path_4)


# In[7]:


# Get the mesh metadata information
mesh_info_2 = model_2.metadata.mesh_info

# Print the mesh metadata information
print(mesh_info_2)


# In[8]:


# Get the mesh metadata information
mesh_info_3 = model_3.metadata.mesh_info

# Print the mesh metadata information
print(mesh_info_3)


# In[9]:


# Get the mesh metadata information
mesh_info_4 = model_4.metadata.mesh_info

# Print the mesh metadata information
print(mesh_info_4)


# In[10]:


# Get the part names
cell_zones_2 = mesh_info_2.get_property("part_names")

# Print the part names
print(cell_zones_2)


# In[11]:


# Get the cell zone names
cell_zones_3 = mesh_info_3.get_property("cell_zone_names")

# Print the cell zone names
print(cell_zones_3)


# In[12]:


# Get the cell zone names
cell_zones_4 = mesh_info_4.get_property("cell_zone_names")

# Print the cell zone names
print(cell_zones_4)

