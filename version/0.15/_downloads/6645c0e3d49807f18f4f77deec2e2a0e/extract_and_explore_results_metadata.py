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


# In[2]:


# Define the ResultInfo object
result_info_1 = model_1.metadata.result_info

# Get the analysis type
analysis_type = result_info_1.analysis_type
# Print the analysis type
print("Analysis type: ",analysis_type, "\n")

# Get the physics type
physics_type = result_info_1.physics_type
# Print the physics type
print("Physics type: ",physics_type, "\n")

# Get the number of available results
number_of_results = result_info_1.n_results
# Print the number of available results
print("Number of available results: ",number_of_results, "\n")

# Get the unit system
unit_system = result_info_1.unit_system
# Print the unit system
print("Unit system: ",unit_system, "\n")

# Get the solver version, data and time
solver_version = result_info_1.solver_version
solver_date = result_info_1.solver_date
solver_time = result_info_1.solver_time

# Print the solver version, data and time
print("Solver version: ",solver_version, "\n")
print("Solver date: ", solver_date, "\n")
print("Solver time: ",solver_time, "\n")

# Get the job name
job_name = result_info_1.job_name
# Print the job name
print("Job name: ",job_name, "\n")


# In[3]:


# Extract the displacement results
disp_results = model_1.results.displacement.eval()

# Get the displacement field
disp_field = disp_results[0]


# In[4]:


# Get the location of the displacement data
location = disp_field.location
# Print the location
print("Location: ", location,'\n')

# Get the displacement Field scoping
scoping = disp_field.scoping
# Print the Field scoping
print("Scoping: ", '\n',scoping, '\n')

# Get the displacement Field scoping ids
scoping_ids = disp_field.scoping.ids  # Available entities ids
# Print the Field scoping ids
print("Scoping ids: ", scoping_ids, '\n')

# Get the displacement Field elementary data count
elementary_data_count = disp_field.elementary_data_count
# Print the elementary data count
print("Elementary data count: ", elementary_data_count, '\n')

# Get the displacement Field components count
components_count = disp_field.component_count
# Print the components count
print("Components count: ", components_count, '\n')

# Get the displacement Field size
field_size = disp_field.size
# Print the Field size
print("Size: ", field_size, '\n')

# Get the displacement Field shape
shape = disp_field.shape
# Print the Field shape
print("Shape: ", shape, '\n')

# Get the displacement Field unit
unit = disp_field.unit
# Print the displacement Field unit
print("Unit: ", unit, '\n')

