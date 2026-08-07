#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
import ansys.dpf.core as dpf
# Import the examples module
from ansys.dpf.core import examples
# Import the operators module
from ansys.dpf.core import operators as ops

# Download and get the path to an example result file
result_file_path_1 = examples.download_piston_rod()

# Create a model from the result file
model_1 = dpf.Model(data_sources=result_file_path_1)


# In[2]:


# Plot the mesh
model_1.plot()


# In[3]:


# Extract the mesh
meshed_region_1 = model_1.metadata.meshed_region


# In[4]:


# Plot the mesh object
meshed_region_1.plot()


# In[5]:


# Create a DpfPlotter instance
plotter_1 = dpf.plotter.DpfPlotter()

# Add the mesh to the scene
plotter_1.add_mesh(meshed_region=meshed_region_1)

# Display the scene
plotter_1.show_figure()


# In[6]:


# Split the mesh based on material property
meshes = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()

# Show the result
print(meshes)


# In[7]:


# Plot the collection of meshes
meshes.plot()


# In[8]:


model_1.plot(title="Mesh",
             text="this is a mesh",  # Adds the given text at the bottom of the plot
             off_screen=True,
             screenshot="mesh_plot_1.png",  # Save a screenshot to file with the given name
             window_size=[450,350])
# Notes:
# - To save a screenshot to file, use "screenshot=figure_name.png" ( as well as "notebook=False" if on a Jupyter notebook).
# - The "off_screen" keyword only works when "notebook=False". If "off_screen=True" the plot is not displayed when running the code.

