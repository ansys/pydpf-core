"""
.. _ref_dpf_core:

Title
~~~~~


"""
from ansys.dpf import core as dpf_core
from ansys.dpf.core import examples

model = dpf_core.Model(examples.simple_bar)
metadata = model.metadata

# list all results
results = model.results
