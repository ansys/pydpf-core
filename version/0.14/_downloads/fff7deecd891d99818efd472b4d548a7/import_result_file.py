#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the .rst result file path
result_file_path_11 = examples.find_static_rst()

# Define the modal superposition harmonic analysis (.mode, .rfrq and .rst) result files paths
result_file_path_12 = examples.download_msup_files_to_dict()


# Print the result files paths
print("Result file path 11:", "\n",result_file_path_11, "\n")
print("Result files paths 12:", "\n",result_file_path_12, "\n")


# In[2]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the .d3plot result files paths
result_file_path_21 = examples.download_d3plot_beam()

# Define the .binout result file path
result_file_path_22 = examples.download_binout_matsum()

# Print the result files paths
print("Result files paths 21:", "\n",result_file_path_21, "\n")
print("Result file path 22:", "\n",result_file_path_22, "\n")


# In[3]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the project .flprj result file path
result_file_path_31 = examples.download_fluent_axial_comp()["flprj"]

# Define the CFF .cas.h5/.dat.h5 result files paths
result_file_path_32 = examples.download_fluent_axial_comp()

# Print the result files paths
print("Result file path 31:", "\n",result_file_path_31, "\n")
print("Result files paths 32:", "\n",result_file_path_32, "\n")


# In[4]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Define the project .res result file path
result_file_path_41 = examples.download_cfx_mixing_elbow()

# Define the CFF .cas.cff/.dat.cff result files paths
result_file_path_42 = examples.download_cfx_heating_coil()

# Print the result files paths
print("Result file path 41:", "\n",result_file_path_41, "\n")
print("Result files paths 42:", "\n",result_file_path_42, "\n")


# In[5]:


# Create the DataSources object
# Use the ``result_path`` argument and give the result file path
ds_11 = dpf.DataSources(result_path=result_file_path_11)


# In[6]:


# Create the main DataSources object
ds_12 = dpf.DataSources()
# Define the main result file path
ds_12.set_result_file_path(filepath=result_file_path_12["rfrq"], key='rfrq')

# Create the upstream DataSources object with the main upstream file path
upstream_ds_12 = dpf.DataSources(result_path=result_file_path_12["mode"])
# Add the additional upstream file path to the upstream DataSources object
upstream_ds_12.add_file_path(filepath=result_file_path_12["rst"])

# Add the upstream DataSources to the main DataSources object
ds_12.add_upstream(upstream_data_sources=upstream_ds_12)


# In[7]:


# Create the DataSources object
ds_21 = dpf.DataSources()

# Define the main result file path
ds_21.set_result_file_path(filepath=result_file_path_21[0], key="d3plot")

# Add the additional file path related to the units
ds_21.add_file_path(filepath=result_file_path_21[3], key="actunits")


# In[8]:


# Create the DataSources object
ds_22 = dpf.DataSources()

# Define the path to the result file
# Use the ``key`` argument and give the file extension key
ds_22.set_result_file_path(filepath=result_file_path_22, key="binout")


# In[9]:


# Create the DataSources object
# Use the ``result_path`` argument and give the result file path
ds_31 = dpf.DataSources(result_path=result_file_path_31)


# In[10]:


# Create the DataSources object
ds_32 = dpf.DataSources()

# Define the path to the main result file
# Use the ``key`` argument and give the first extension key
ds_32.set_result_file_path(filepath=result_file_path_32['cas'][0], key="cas")

# Add the additional result file path to the DataSources
# Use the ``key`` argument and give the first extension key
ds_32.add_file_path(filepath=result_file_path_32['dat'][0], key="dat")


# In[11]:


# Create the DataSources object
# Use the ``result_path`` argument and give the result file path
ds_41 = dpf.DataSources(result_path=result_file_path_41)


# In[12]:


# Create the DataSources object
ds_42 = dpf.DataSources()

# Define the path to the main result file
# Use the ``key`` argument and give the first extension key
ds_42.set_result_file_path(filepath=result_file_path_42["cas"], key="cas")

# Add the additional result file path to the DataSources
# Use the ``key`` argument and give the first extension key
ds_42.add_file_path(filepath=result_file_path_42["dat"], key="dat")


# In[13]:


# Create the model with the result file path
model_11 = dpf.Model(data_sources=result_file_path_11)

# Create the model with the DataSources object
model_12 = dpf.Model(data_sources=ds_11)


# In[14]:


# Create the model with the DataSources object
model_13 = dpf.Model(data_sources=ds_12)


# In[15]:


# Create the model with the DataSources object
model_21 = dpf.Model(data_sources=ds_21)


# In[16]:


# Create the model with the DataSources object
model_22 = dpf.Model(data_sources=ds_22)


# In[17]:


# Create the model with the result file path
model_31 = dpf.Model(data_sources=result_file_path_31)

# Create the model with the DataSources object
model_32 = dpf.Model(data_sources=ds_31)


# In[18]:


# Create the model with the DataSources object
model_33 = dpf.Model(data_sources=ds_32)


# In[19]:


# Create the model with the result file path
model_41 = dpf.Model(data_sources=result_file_path_41)

# Create the model with the DataSources object
model_42 = dpf.Model(data_sources=ds_41)


# In[20]:


# Create the model with the DataSources object
model_43 = dpf.Model(data_sources=ds_42)

