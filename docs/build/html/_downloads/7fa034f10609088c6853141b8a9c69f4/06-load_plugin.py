"""
.. _ref_load_plugin:

Load plugin 
~~~~~~~~~~~
This example shows how to load a plugin that is 
not automatically loaded. 

"""

###############################################################################
# Import dpf module 

from ansys.dpf import core as dpf

###############################################################################
# Create a base service that allows to load a plugin

dpf.core.load_library('Ans.Dpf.Math.dll', 'math_operators')

###############################################################################
# Math operators are now loaded and accessible in ansys.dpf.core.operators

from ansys.dpf.core import operators as ops
math_op = ops.math.fft_eval()
