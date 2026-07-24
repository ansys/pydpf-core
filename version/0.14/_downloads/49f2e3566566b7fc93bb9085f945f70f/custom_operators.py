#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ansys.dpf.core as dpf

# Python plugins are not supported in process.
server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)


# In[2]:


# Get the path to the example plugin
from pathlib import Path
from ansys.dpf.core.examples.python_plugins import custom_operator_example
custom_operator_folder = Path(custom_operator_example.__file__).parent

# Load it on the server
dpf.load_library(
    filename=custom_operator_folder,  # Path to the plugin directory
    name="py_custom_operator_example",  # Look for a Python file named 'custom_operator_example.py'
    symbol="load_operators",  # Look for the entry-point where operators are recorded
    server=server,  # Load the plugin on the server previously started
    generate_operators=False,  # Do not generate the Python module for this operator
)

# You can verify the operator is now in the list of available operators on the server
assert "my_custom_operator" in dpf.dpf_operator.available_operator_names(server=server)


# In[3]:


my_custom_op = dpf.Operator(name="my_custom_operator", server=server) # as returned by the ``name`` property
print(my_custom_op)


# In[4]:


# Create a bogus field to use as input
in_field = dpf.Field(server=server)
# Give it a name
in_field.name = "initial name"
print(in_field)
# Set it as input of the operator
my_custom_op.inputs.input_0.connect(in_field)
# Run the operator by requesting its output
out_field = my_custom_op.outputs.output_0()
print(out_field)

