#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ansys.dpf.core module
import ansys.dpf.core as dpf

# Import the examples module
from ansys.dpf.core import examples

# Load a transient analysis with multiple time steps
result_file_path = examples.find_msup_transient()

# Create a DataSources object
data_sources = dpf.DataSources(result_path=result_file_path)

# Create a Model from the data sources
model = dpf.Model(data_sources=data_sources)

# Display basic model information
print(model)


# In[2]:


# Get displacement results for all time steps
displacement_fc = model.results.displacement.on_all_time_freqs.eval()

# Display FieldsContainer information
print(displacement_fc)


# In[3]:


# Access field by index (first time step)
first_field = displacement_fc[0]
print(f"First field info:")
print(first_field)

# Access field by label (specific time step)
second_time_field = displacement_fc.get_field({"time": 2})
# Equivalent to:
second_time_field = displacement_fc.get_field_by_time_id(2)
print(f"\nSecond time step field:")
print(second_time_field)


# In[4]:


# Create an empty FieldsContainer
custom_fc = dpf.FieldsContainer()

# Set up labels for the container
custom_fc.labels = ["time", "zone"]

# Create sample fields for different time steps and zones
field1 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field2 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field3 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
field4 = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)

# Add some sample nodes and data
field1.scoping.ids = [1, 2, 3, 4, 5]
field1.data = [float(1 * i) for i in range(1, 6)]
field2.scoping.ids = [1, 2, 3, 4, 5]
field2.data = [float(2 * i) for i in range(1, 6)]
field3.scoping.ids = [1, 2, 3, 4, 5]
field3.data = [float(3 * i) for i in range(1, 6)]
field4.scoping.ids = [1, 2, 3, 4, 5]
field4.data = [float(4 * i) for i in range(1, 6)]

# Add field to container with labels
custom_fc.add_field({"time": 1, "zone": 1}, field1)
custom_fc.add_field({"time": 2, "zone": 1}, field2)
custom_fc.add_field({"time": 1, "zone": 2}, field3)
custom_fc.add_field({"time": 2, "zone": 2}, field4)

# Display the custom FieldsContainer
print(custom_fc)


# In[5]:


# Get the mesh from our model
mesh = model.metadata.meshed_region

# Create a ScopingsContainer
scopings_container = dpf.ScopingsContainer()

# Set labels for different selections
scopings_container.labels = ["selection_type"]

# Selection 1: First 10 nodes
first_nodes = dpf.Scoping(location=dpf.locations.nodal)
first_nodes.ids = list(range(1, 11))
scopings_container.add_scoping(label_space={"selection_type": 0}, scoping=first_nodes)

# Selection 2: Every 10th node (sample)
all_node_ids = mesh.nodes.scoping.ids
every_tenth = dpf.Scoping(location=dpf.locations.nodal)
every_tenth.ids = all_node_ids[::10]  # Every 10th node
scopings_container.add_scoping(label_space={"selection_type": 1}, scoping=every_tenth)

# Selection 3: Last 10 nodes
last_nodes = dpf.Scoping(location=dpf.locations.nodal)
last_nodes.ids = all_node_ids[-10:]
scopings_container.add_scoping(label_space={"selection_type": 2}, scoping=last_nodes)

# Display ScopingsContainer information
print(scopings_container)


# In[6]:


# Create an operator to extract displacement on specific node sets
displacement_op = dpf.operators.result.displacement()
# Connect the data source
displacement_op.inputs.data_sources(data_sources)
# Connect the scopings container which defines the node selections
displacement_op.inputs.mesh_scoping(scopings_container)

# Evaluate to get results for all scopings
scoped_displacements = displacement_op.eval()

print(f"Displacement results for different node selections:")
print(scoped_displacements)


# In[7]:


# Create a MeshesContainer
meshes_container = dpf.MeshesContainer()

# Set labels for different mesh variations
meshes_container.labels = ["variation"]

# Get the original mesh
original_mesh = model.metadata.meshed_region

# Add original mesh
meshes_container.add_mesh({"variation": 0}, original_mesh)

# Create a modified mesh (example: subset of elements)
# Get element scoping for first half of elements
all_element_ids = original_mesh.elements.scoping.ids
subset_element_ids = all_element_ids[:len(all_element_ids)//2]

# Create element scoping for subset
element_scoping = dpf.Scoping(location=dpf.locations.elemental)
element_scoping.ids = subset_element_ids

# Extract subset mesh using an operator
mesh_extract_op = dpf.operators.mesh.from_scoping()
mesh_extract_op.inputs.mesh(original_mesh)
mesh_extract_op.inputs.scoping(element_scoping)
subset_mesh = mesh_extract_op.eval()

# Add subset mesh to container
meshes_container.add_mesh({"variation": 1}, subset_mesh)

# Display MeshesContainer information
print(meshes_container)


# In[8]:


# Iterate through a FieldsContainer
print("Iterating through displacement fields by index:")
for i in range(3):  # Show the first three fields in the collection
    # Get the field at index i
    field = displacement_fc[i]
    # Get the label space for the field at index i
    label_space = displacement_fc.get_label_space(i)
    # Print field information
    max_value = field.data.max()
    print(f"  Field {i}: {label_space}, max value: {max_value:.6f}")

# Enumerate the scopings in a ScopingsContainer
print("\nEnumerate the scopings in a ScopingsContainer:")
for i, scoping in enumerate(scopings_container):
    # Get the label space for the scoping at index i
    label_space = scopings_container.get_label_space(i)
    # Print scoping information
    print(f"  Scoping {i}: {label_space}, size: {scoping.size}")


# In[9]:


# Get specific fields from a FieldsContainer with criteria on label values
# Get all fields of ``custom_fc`` where ``zone=1``
zone_1_fields = custom_fc.get_fields({"zone": 1})
print(f"\nFields in custom_fc with zone=1:")
for field in zone_1_fields:
    print(field)


# In[10]:


from ansys.dpf.core import DataSources
from ansys.dpf.core import examples
from ansys.dpf.core.collection import Collection

# Create a collection class for DataSources
DataSourcesCollection = Collection.collection_factory(DataSources)
ds_collection = DataSourcesCollection()
ds_collection.labels = ["case"]

# Add DataSources objects to the collection
ds1 = DataSources("path/to/first/result/file.rst")
ds2 = DataSources("path/to/second/result/file.rst")
ds_collection.add_entry({"case": 0}, ds1)
ds_collection.add_entry({"case": 1}, ds2)

# Show the collection
print(ds_collection)

