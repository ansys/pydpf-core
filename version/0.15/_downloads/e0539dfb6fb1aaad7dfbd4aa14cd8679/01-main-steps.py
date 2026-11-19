#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops


# In[2]:


# Define the DataSources object
my_data_sources = dpf.DataSources(result_path=examples.find_simple_bar())


# In[3]:


# Define the Model object
my_model = dpf.Model(data_sources=my_data_sources)
print(my_model)


# In[4]:


# Define the displacement results through the models property `results`
my_displacements = my_model.results.displacement.eval()
print(my_displacements)


# In[5]:


# Extract the data of the displacement field
my_displacements_0 = my_displacements[0].data
print(my_displacements_0)


# In[6]:


# Define the norm operator (here for a fields container) for the displacement
my_norm = ops.math.norm_fc(fields_container=my_displacements).eval()
print(my_norm[0].data)


# In[7]:


# Define the maximum operator and chain it to the norm operator
my_max= ops.min_max.min_max_fc(fields_container=my_norm).outputs.field_max()
print(my_max)


# In[8]:


# Define the support of the plot (here we plot the displacement over the mesh)
my_model.metadata.meshed_region.plot(field_or_fields_container=my_displacements)

