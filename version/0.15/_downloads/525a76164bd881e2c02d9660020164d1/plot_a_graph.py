#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
import ansys.dpf.core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops
# Import the geometry module
from ansys.dpf.core import geometry as geo

# Import the ``matplotlib.pyplot`` module
import matplotlib.pyplot as plt

# Download and get the path to an example result file
result_file_path_1 = examples.find_static_rst()

# Create a model from the result file
model_1 = dpf.Model(data_sources=result_file_path_1)


# In[2]:


# Get the nodal displacement field at the last simulation step (default)
disp_results_1 = model_1.results.displacement.eval()

# Get the norm of the displacement field
norm_disp = ops.math.norm_fc(fields_container=disp_results_1).eval()


# In[3]:


# Create a discretized line for the path
line_1 = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]], n_points=50)
# Plot the line on the original mesh
line_1.plot(mesh=model_1.metadata.meshed_region)


# In[4]:


# Interpolate the displacement norm field at the nodes of the custom path
disp_norm_on_path_fc: dpf.FieldsContainer = ops.mapping.on_coordinates(
    fields_container=norm_disp,
    coordinates=line_1.mesh.nodes.coordinates_field,
).eval()
# Extract the only field in the collection obtained
disp_norm_on_path: dpf.Field = disp_norm_on_path_fc[0]
print(disp_norm_on_path)


# In[5]:


# Get the field of parametric coordinates along the path for the X-axis
line_coordinates = line_1.path

# Define the curve to plot
plt.plot(line_coordinates, disp_norm_on_path.data)

# Add titles to the axes and the graph
plt.xlabel("Position on path")
plt.ylabel("Displacement norm")
plt.title("Displacement norm along the path")

# Display the graph
plt.show()


# In[6]:


# Import the ``ansys.dpf.core`` module
import ansys.dpf.core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Import the ``matplotlib.pyplot`` module
import matplotlib.pyplot as plt

# Download and get the path to an example transient result file
result_file_path_2 = examples.download_transient_result()

# Create a model from the result file
model_2 = dpf.Model(data_sources=result_file_path_2)

# Check the model is transient with its ``TimeFreqSupport``
print(model_2.metadata.time_freq_support)


# In[7]:


# Get the displacement at all time steps
disp_results_2: dpf.FieldsContainer = model_2.results.displacement.on_all_time_freqs.eval()


# In[8]:


# Instantiate the min_max operator and give the output of the norm operator as input
min_max_op = ops.min_max.min_max_fc(fields_container=ops.math.norm_fc(disp_results_2))

# Get the field of maximum values at each time-step
max_disp: dpf.Field = min_max_op.outputs.field_max()
print(max_disp)

# Get the field of minimum values at each time-step
min_disp: dpf.Field = min_max_op.outputs.field_min()
print(min_disp)


# In[9]:


# Get the field of time values
time_steps_1: dpf.Field = disp_results_2.time_freq_support.time_frequencies

# Print the time values
print(time_steps_1)


# In[10]:


# Get the time values
time_data = time_steps_1.data
print(time_data)


# In[11]:


# Define the plot figure
plt.plot(time_data, max_disp.data, "r", label="Max")
plt.plot(time_data, min_disp.data, "b", label="Min")

# Add axis labels and legend
plt.xlabel(f"Time ({time_steps_1.unit})")
plt.ylabel(f"Displacement ({max_disp.unit})")
plt.legend()

# Display the graph
plt.show()

