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


# Get the mesh nodes
nodes_1 = meshed_region_1.nodes

# Print the object type
print("Object type: ",type(nodes_1),'\n')

# Print the nodes
print("Nodes: ", nodes_1)


# In[6]:


# Get the mesh nodes
nodes_2 = meshed_region_2.nodes

# Print the object type
print("Object type: ",type(nodes_2),'\n')

# Print the nodes
print("Nodes: ", nodes_2)


# In[7]:


# Get the mesh nodes
nodes_3 = meshed_region_3.nodes

# Print the object type
print("Object type: ",type(nodes_3),'\n')

# Print the nodes
print("Nodes: ", nodes_3)


# In[8]:


# Get the mesh nodes
nodes_4 = meshed_region_4.nodes

# Print the object type
print("Object type: ",type(nodes_4),'\n')

# Print the nodes
print("Nodes: ", nodes_4)


# In[9]:


# Get the mesh bounding box
bbox_1 = meshed_region_1.bounding_box

# Print the bounding box
print("Bounding box: ", bbox_1)


# In[10]:


# Get the mesh bounding box
bbox_2 = meshed_region_2.bounding_box

# Print the bounding box
print("Bounding box: ", bbox_2)


# In[11]:


# Get the mesh bounding box
bbox_3 = meshed_region_3.bounding_box

# Print the bounding box
print("Bounding box: ", bbox_3)


# In[12]:


# Get the mesh bounding box
bbox_4 = meshed_region_4.bounding_box

# Print the bounding box
print("Bounding box: ", bbox_4)


# In[13]:


# Get the available properties
available_props_1 = meshed_region_1.available_property_fields

# Print the available properties
print("Available properties: ", available_props_1)


# In[14]:


# Get the available properties
available_props_2 = meshed_region_2.available_property_fields

# Print the available properties
print("Available properties: ", available_props_2)


# In[15]:


# Get the available properties
available_props_3 = meshed_region_3.available_property_fields

# Print the available properties
print("Available properties: ", available_props_3)


# In[16]:


# Get the available properties
available_props_4 = meshed_region_4.available_property_fields

# Print the available properties
print("Available properties: ", available_props_4)


# In[17]:


# Get the element types on the mesh
el_types_1 = meshed_region_1.elements.element_types_field

# Print the element types by element
print(el_types_1)


# In[18]:


# Get the element types on the mesh
el_types_2 = meshed_region_2.property_field(property_name="eltype")

# Print the element types by element
print(el_types_2)


# In[19]:


# Get the element types on the mesh
el_types_3 = meshed_region_3.property_field(property_name="eltype")

# Print the element types by element
print(el_types_3)


# In[20]:


# Get the element types on the mesh
el_types_4 = meshed_region_4.property_field(property_name="eltype")

# Print the element types by element
print(el_types_4)

