"""
.. _ref_load_plugin:

Load plugin
~~~~~~~~~~~

This example shows how to load a plugin that is not loaded automatically.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""

###############################################################################
# Import DPF-Core:
from ansys.dpf import core as dpf

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

server = dpf.global_server()

###############################################################################
# Create a base service for loading a plugin:
if server.os == "posix":
    dpf.core.load_library("libAns.Dpf.Math.so", "math_operators")
else:
    dpf.core.load_library("Ans.Dpf.Math.dll", "math_operators")

###############################################################################
# Math operators are now loaded and accessible in ``ansys.dpf.core.operators``:

from ansys.dpf.core import operators as ops

math_op = ops.math.fft_eval()
