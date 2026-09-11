#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data for the scalar Fields (lists with 1 and 2 dimensions)
data_1 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
data_2 = [[12.0, 7.0, 8.0], [ 9.0, 31.0, 1.0]]

# Data for the vector Fields (lists with 1 and 2 dimensions)
data_3 = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]
data_4 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 9.0, 7.0, 8.0, 10.0]
data_5 = [[8.0, 4.0, 3.0], [31.0, 5.0, 7.0]]

# Data for the matrix Fields
data_6 = [3.0, 2.0, 1.0, 7.0]
data_7 = [15.0, 3.0, 9.0, 31.0, 1.0, 42.0, 5.0, 68.0, 13.0]
data_8 = [[12.0, 7.0, 8.0], [ 1.0, 4.0, 27.0], [98.0, 4.0, 6.0]]


# In[2]:


# Data for the scalar Fields
data_9 = [24.0]

# Data for the vector Fields
data_10 = [47.0, 33.0, 5.0]

# Data for the matrix Fields
data_11 = [8.0, 2.0, 4.0, 64.0, 32.0, 47.0, 11.0, 23.0, 1.0]


# In[3]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf


# In[4]:


# Define the number of entities
num_entities_1 = 6


# In[5]:


# Define the number of entities
num_entities_2 = 2


# In[6]:


# Define the number of entities
num_entities_3 = 1


# In[7]:


# Define the number of entities
num_entities_1 = 6


# In[8]:


# Instanciate the Field
field_11 = dpf.Field(nentities=num_entities_1, nature=dpf.common.natures.scalar)

# Set the scoping ids
field_11.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field: ", '\n',field_11, '\n')


# In[9]:


# Instanciate the Field
field_12 = dpf.Field(nentities=num_entities_1)

# Use the Field.dimensionality method
field_12.dimensionality = dpf.Dimensionality([1])

# Set the scoping ids
field_12.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field : ", '\n',field_12, '\n')


# In[10]:


# Define the number of entities
num_entities_2 = 2


# In[11]:


# Instantiate the Field
field_21 = dpf.Field(nentities=num_entities_2)

# Set the scoping ids
field_21.scoping.ids = range(num_entities_2)

# Print the Field
print("3D vector Field : ", '\n',field_21, '\n')


# In[12]:


# Instantiate the Field
field_31 = dpf.Field(nentities=num_entities_2)

# Use the Field.dimensionality method
field_31.dimensionality = dpf.Dimensionality([5])

# Set the scoping ids
field_31.scoping.ids = range(num_entities_2)

# Print the Field
print("5D vector Field (5D): ", '\n',field_31, '\n')


# In[13]:


# Create the scalar Field
field_13 = dpf.fields_factory.create_scalar_field(num_entities=num_entities_1)

# Set the scoping ids
field_13.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field: ", '\n',field_13, '\n')


# In[14]:


# Use the field_from_array function
field_14 = dpf.fields_factory.field_from_array(arr=data_1)

# Set the scoping ids
field_14.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field: ", '\n',field_14, '\n')


# In[15]:


# Use the field_from_array function
field_15 = dpf.fields_factory.field_from_array(arr=data_2)

# Use the |Field.dimensionality| method
field_15.dimensionality = dpf.Dimensionality([1])

# Set the scoping ids
field_15.scoping.ids = range(num_entities_1)

# Print the Field
print("Scalar Field (b): ", '\n',field_15, '\n')


# In[16]:


# Use the create_vector_field function
field_22 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=3)

# Set the scoping ids
field_22.scoping.ids = range(num_entities_2)

# Print the Field
print("3D vector Field : ", '\n',field_22, '\n')


# In[17]:


# Use the create_vector_field function
field_32 = dpf.fields_factory.create_vector_field(num_entities=num_entities_2, num_comp=5)

# Set the scoping ids
field_32.scoping.ids = range(num_entities_2)

# Print the Field
print("5D vector Field : ", '\n',field_32, '\n')


# In[18]:


# Create the 3d vector Field
field_25 = dpf.fields_factory.create_3d_vector_field(num_entities=num_entities_2)
# Set the scoping ids
field_25.scoping.ids = range(num_entities_2)

# Print the Field
print("Vector Field (3D): ", '\n',field_25, '\n')


# In[19]:


# Use the field_from_array function
field_23 = dpf.fields_factory.field_from_array(arr=data_3)

# Use the Field.dimensionality method
field_23.dimensionality = dpf.Dimensionality([3])

# Set the scoping ids
field_23.scoping.ids = range(num_entities_2)

# Print the Field
print("3D vector Field: ", '\n',field_23, '\n')


# In[20]:


# Use the field_from_array function
field_24 = dpf.fields_factory.field_from_array(arr=data_5)

# Set the scoping ids
field_24.scoping.ids = range(num_entities_2)

# Print the Field
print("3D vector Field: ", '\n',field_24, '\n')


# In[21]:


# Use the create_matrix_field function
field_41 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=2, num_col=2)

# Set the scoping ids
field_41.scoping.ids = range(num_entities_3)

# Print the Field
print("Matrix Field (2,2) : ", '\n',field_41, '\n')


# In[22]:


# Use the create_matrix_field function
field_51 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=3, num_col=3)
field_52 = dpf.fields_factory.create_matrix_field(num_entities=num_entities_3, num_lines=3, num_col=3)

# Set the scoping ids
field_51.scoping.ids = range(num_entities_3)
field_52.scoping.ids = range(num_entities_3)

# Print the Field
print("Matrix Field 1 (3,3) : ", '\n',field_51, '\n')
print("Matrix Field 2 (3,3) : ", '\n',field_52, '\n')


# In[23]:


# Set the data
field_11.data = data_1

# Print the Field
print("Scalar Field : ", '\n',field_11, '\n')

# Print the Fields data
print("Data scalar Field : ", '\n',field_11.data, '\n')


# In[24]:


# Set the data
field_12.data = data_2

# Print the Field
print("Scalar Field : ", '\n',field_12, '\n')

# Print the Fields data
print("Data scalar Field : ", '\n',field_12.data, '\n')


# In[25]:


# Set the data
field_21.data = data_3

# Print the Field
print("Vector Field : ", '\n',field_21, '\n')

# Print the Fields data
print("Data vector Field: ", '\n',field_21.data, '\n')


# In[26]:


# Set the data
field_31.data = data_4

# Print the Field
print("Vector Field: ", '\n',field_31, '\n')

# Print the Fields data
print("Data vector Field : ", '\n',field_31.data, '\n')


# In[27]:


# Set the data
field_22.data = data_5

# Print the Field
print("Vector Field: ", '\n',field_22, '\n')

# Print the Fields data
print("Data vector Field: ", '\n',field_22.data, '\n')


# In[28]:


# Set the data
field_41.data = data_6

# Print the Field
print("Matrix Field: ", '\n',field_41, '\n')

# Print the Fields data
print("Data matrix Field: ", '\n',field_41.data, '\n')


# In[29]:


# Set the data
field_51.data = data_7

# Print the Field
print("Matrix Field: ", '\n',field_51, '\n')

# Print the Fields data
print("Data matrix Field: ", '\n',field_51.data, '\n')


# In[30]:


# Set the data
field_52.data = data_8

# Print the Field
print("Matrix Field: ", '\n',field_51, '\n')

# Print the Fields data
print("Data matrix Field: ", '\n',field_51.data, '\n')


# In[31]:


# Append the data
field_11.append(scopingid=6, data=data_9)

# Print the Field
print("Scalar Field : ", '\n',field_11, '\n')

# Print the Fields data
print("Data scalar Field: ", '\n',field_11.data, '\n')


# In[32]:


# Append the data
field_21.append(scopingid=2, data=data_10)

# Print the Field
print("Vector Field : ", '\n',field_21, '\n')

# Print the Fields data
print("Data vector Field: ", '\n',field_21.data, '\n')


# In[33]:


# Append the data
field_51.append(scopingid=1, data=data_11)

# Print the Field
print("VMatrix Field : ", '\n',field_51, '\n')

# Print the Fields data
print("Data Matrix Field: ", '\n',field_51.data, '\n')


# In[34]:


# Create the FieldsContainer object
fc_1 = dpf.FieldsContainer()

# Define the labels
fc_1.add_label(label="time")

# Add the Fields
fc_1.add_field(label_space={"time": 0}, field=field_21)
fc_1.add_field(label_space={"time": 1}, field=field_31)

# Print the FieldsContainer
print(fc_1)


# In[35]:


# Create the FieldsContainer
fc_2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field_21, field_31])

# Print the FieldsContainer
print(fc_2)

