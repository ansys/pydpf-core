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
result_file_path_1 = examples.download_transient_result()

# Create the model
model_1 = dpf.Model(data_sources=result_file_path_1)

# Extract the displacement results for the last time step
disp_results = model_1.results.displacement.on_last_time_freq.eval()

# Get the displacement field for the last time step
disp_field = disp_results[0]

# Print the displacement Field
print(disp_field)


# In[2]:


# Get the displacement data as an array
data_array = disp_field.data

# Print the data as an array
print("Displacement data as an array: ", '\n', data_array)


# In[3]:


# Print the array type
print("Array type: ", type(data_array))


# In[4]:


# Get the displacement data as a list
data_list = disp_field.data_as_list
# Print the data as a list
print("Displacement data as a list: ", '\n', data_list)


# In[5]:


# Get the index of the entity with id=533
index_533_entity = disp_field.scoping.index(id=533)
# Print the index
print("Index entity id=533: ",index_533_entity)


# In[6]:


# Get the id of  the entity with index=533
id_533_entity = disp_field.scoping.id(index=533)
print("Id entity index=533: ",id_533_entity)


# In[7]:


# Get the data from the third entity in the field
data_3_entity = disp_field.get_entity_data(index=3)
# Print the data
print("Data entity index=3: ", data_3_entity)


# In[8]:


# Get the data from the entity with id=533
data_533_entity = disp_field.get_entity_data_by_id(id=533)
# Print the data
print("Data entity id=533: ", data_533_entity)


# In[9]:


# Create a deep copy of the field that can be accessed and modified locally.
with disp_field.as_local_field() as f:
    for i in disp_field.scoping.ids[2:50]:
        f.get_entity_data_by_id(i)

# Print the field
print(f)

