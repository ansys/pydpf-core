#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ansys.dpf.core module as ``dpf``
from ansys.dpf import core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Create a data source targeting the example file
my_data_sources = dpf.DataSources(result_path=examples.download_fluent_axial_comp()["flprj"])
# Create a model from the data source
my_model = dpf.Model(data_sources=my_data_sources)
# Print information available for the analysis
print(my_model)


# In[2]:


# Get the mesh metadata
my_mesh_info = my_model.metadata.mesh_info
print(my_mesh_info)


# In[3]:


# Request the collection of temperature result fields from the model and take the first one.
my_temp_field = my_model.results.temperature.eval()[0]
# Print the field
print(my_temp_field)


# In[4]:


# Request the name of the face zones in the fluid analysis
my_string_field = my_mesh_info.get_property(property_name="face_zone_names")
# Print the field of strings
print(my_string_field)


# In[5]:


# Get the body_face_topology property field
my_property_field = my_mesh_info.get_property(property_name="body_face_topology")
# Print the field of integers
print(my_property_field)


# In[6]:


# Create a 3D vector field ready to hold data for two entities
# The constructor creates 3D vector fields by default
my_field = dpf.Field(nentities=2)
# Set the data values as a flat vector
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
# Associate the data to nodes
my_field.location = dpf.locations.nodal
# Set the IDs of the nodes the data applies to
my_field.scoping.ids = [1, 2]
# Define the unit (only available for the Field type)
my_field.unit = "m"
# Print the field
print(my_field)


# In[7]:


# Set the nature to symmatrix
my_field = dpf.Field(nentities=1, nature=dpf.natures.symmatrix)
# The symmatrix dimensions defaults to 3x3
# Set the data values as a flat vector
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
# Associate the data to elements
my_field.location = dpf.locations.elemental
# Set the IDs of the nodes the data applies to
my_field.scoping.ids = [1]
# Define the unit (only available for the Field type)
my_field.unit = "Pa"
# Print the field
print(my_field)


# In[8]:


# Set the nature to matrix and the location to elemental
my_field = dpf.Field(nentities=1, nature=dpf.natures.matrix)
# Set the matrix dimensions to 2x3
my_field.dimensionality = dpf.Dimensionality(dim_vec=[2, 3], nature=dpf.natures.matrix)
# Set the data values as a flat vector
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
# Associate the data to faces
my_field.location = dpf.locations.faces
# Set the IDs of the face the data applies to
my_field.scoping.ids = [1]
# Define the unit (only available for the Field type)
my_field.unit = "mm"
# Print the field
print(my_field)


# In[9]:


# Create a string field with data for two elements
my_string_field = dpf.StringField(nentities=2)
# Set the string values
my_string_field.data = ["string_1", "string_2"]
# Set the location
my_string_field.location = dpf.locations.elemental
# Set the element IDs
my_string_field.scoping.ids = [1, 2]
# Print the string field
print(my_string_field)


# In[10]:


# Create a property field with data for two modes
my_property_field = dpf.PropertyField(nentities=2)
# Set the data values
my_property_field.data = [12, 25]
# Set the location
# For DPF 26R1 and above, directly set the location of the PropertyField
from ansys.dpf.core.check_version import meets_version
if meets_version(dpf.SERVER.version, "11.0"):
    my_property_field.location = dpf.locations.modal
# For DPF older than 26R1, you must set the location with a Scoping
else:
    my_property_field.scoping = dpf.Scoping(location=dpf.locations.modal)
# Set the mode IDs
my_property_field.scoping.ids = [1, 2]
# Print the property field
print(my_property_field)


# In[11]:


# Create a scalar field ready to hold data for two entities
# The field is nodal by default
my_field = dpf.fields_factory.create_scalar_field(num_entities=2)
my_field.data = [1.0, 2.0]
my_field.scoping.ids = [1, 2]
# Print the field
print(my_field)


# In[12]:


# Create a 2D vector field ready to hold data for two entities
# The field is nodal by default
my_field = dpf.fields_factory.create_vector_field(num_entities=2, num_comp=2)
my_field.data = [1.0, 2.0, 3.0, 4.0]
my_field.scoping.ids = [1, 2]
# Print the field
print(my_field)


# In[13]:


# Create a 3D vector field ready to hold data for two entities
# The field is nodal by default
my_field = dpf.fields_factory.create_3d_vector_field(num_entities=2)
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_field.scoping.ids = [1, 2]
# Print the field
print(my_field)


# In[14]:


# Create a 2x3 matrix field ready to hold data for two entities
# The field is nodal by default
my_field = dpf.fields_factory.create_matrix_field(num_entities=2, num_lines=2, num_col=3)
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_field.scoping.ids = [1, 2]
# Print the field
print(my_field)


# In[15]:


# Create a 3x3 matrix field ready to hold data for two entities
# The field is nodal by default
my_field = dpf.fields_factory.create_tensor_field(num_entities=2)
my_field.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
my_field.scoping.ids = [1, 2]
# Print the field
print(my_field)


# In[16]:


# Create a field storing a value applied to every node in the support
my_field = dpf.fields_factory.create_overall_field(value=1.0)
# Print the field
print(my_field)


# In[17]:


# Create a scalar field from a 1D array or a list
arr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
my_field = dpf.fields_factory.field_from_array(arr=arr)
# Print the field
print(my_field)


# In[18]:


# Create a 3D vector field from an array or a list
arr = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
my_field = dpf.fields_factory.field_from_array(arr=arr)
# Print the field
print(my_field)


# In[19]:


# Create a symmetric matrix field from an array or a list
arr = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]]
my_field = dpf.fields_factory.field_from_array(arr=arr)
# Print the field
print(my_field)


# In[20]:


# Location of the fields data
my_location = my_temp_field.location
print("location", '\n', my_location,'\n')

# Fields scoping
my_scoping = my_temp_field.scoping  # Location entities type and number
print("scoping", '\n',my_scoping, '\n')

my_scoping_ids = my_temp_field.scoping.ids  # Available ids of locations components
print("scoping.ids", '\n', my_scoping_ids, '\n')

# Elementary data count
# Number of the location entities (how many data vectors we have)
my_elementary_data_count = my_temp_field.elementary_data_count
print("elementary_data_count", '\n', my_elementary_data_count, '\n')

# Components count
# Vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z)
my_component_count = my_temp_field.component_count
print("components_count", '\n', my_component_count, '\n')

# Size
# Length of the data entire vector (equal to the number of elementary data times the number of components.)
my_field_size = my_temp_field.size
print("size", '\n', my_field_size, '\n')

# Fields shape
# Gives a tuple with the elementary data count and the components count
my_shape = my_temp_field.shape
print("shape", '\n', my_shape, '\n')

# Units
my_unit = my_temp_field.unit
print("unit", '\n', my_unit, '\n')


# In[21]:


# Location of the fields data
my_location = my_string_field.location
print("location", '\n', my_location,'\n')

# StringFields scoping
my_scoping = my_string_field.scoping  # Location entities type and number
print("scoping", '\n',my_scoping, '\n')

my_scoping_ids = my_string_field.scoping.ids  # Available ids of locations components
print("scoping.ids", '\n', my_scoping_ids, '\n')

# Elementary data count
# Number of the location entities (how many data vectors we have)
my_elementary_data_count = my_string_field.elementary_data_count
print("elementary_data_count", '\n', my_elementary_data_count, '\n')

# Components count
# Data dimension, here we expect one name by zone
my_component_count = my_string_field.component_count
print("components_count", '\n', my_component_count, '\n')

# Size
# Length of the data entire array (equal to the number of elementary data times the number of components.)
my_field_size = my_string_field.size
print("size", '\n', my_field_size, '\n')

# Fields shape
# Gives a tuple with the elementary data count and the components count
my_shape = my_string_field.shape
print("shape", '\n', my_shape, '\n')


# In[22]:


# Location of the fields data
my_location = my_property_field.location
print("location", '\n', my_location,'\n')

# Fields scoping
my_scoping = my_property_field.scoping  # Location entities type and number
print("scoping", '\n',my_scoping, '\n')

my_scoping_ids = my_property_field.scoping.ids  # Available ids of locations components
print("scoping.ids", '\n', my_scoping_ids, '\n')

# Elementary data count
# Number of the location entities (how many data vectors we have)
my_elementary_data_count = my_property_field.elementary_data_count
print("elementary_data_count", '\n', my_elementary_data_count, '\n')

# Components count
# Data dimension, we expect to have one id by face that makes part of a body
my_component_count = my_property_field.component_count
print("components_count", '\n', my_component_count, '\n')

# Size
# Length of the data entire array (equal to the number of elementary data times the number of components.)
my_field_size = my_property_field.size
print("size", '\n', my_field_size, '\n')

# Fields shape
# Gives a tuple with the elementary data count and the components count
my_shape = my_property_field.shape
print("shape", '\n', my_shape, '\n')


# In[23]:


my_data_array = my_temp_field.data
print(my_data_array)


# In[24]:


print(type(my_data_array))


# In[25]:


my_data_array = my_string_field.data
print(my_data_array)


# In[26]:


my_data_array = my_property_field.data
print(my_data_array)


# In[27]:


# Get the data from the third element in the field
my_temp_field.get_entity_data(index=3)


# In[28]:


# Get the data from the element with id 533
my_temp_field.get_entity_data_by_id(id=533)


# In[29]:


# Get index of the element with id 533
my_temp_field.scoping.index(id=533)


# In[30]:


# Create a deep copy of the field that can be accessed and modified locally.
with my_temp_field.as_local_field() as f:
    for i in range(1,100):
        f.get_entity_data_by_id(i)

