"""
.. _ref_load_plugin:

Load Plugin 
~~~~~~~~~~~
This example shows how to load a plugin that is not loaded automatically. 

"""

###############################################################################
# Import DPF-Core:

from ansys.dpf import core as dpf

###############################################################################
# Create a base service for loading a plugin:

dpf.core.load_library('Ans.Dpf.Math.dll', 'math_operators')

###############################################################################
# Math operators are now loaded and accessible in ``ansys.dpf.core.operators``:

from ansys.dpf.core import operators as ops
math_op = ops.math.fft_eval()
