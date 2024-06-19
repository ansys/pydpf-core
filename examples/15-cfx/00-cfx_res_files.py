"""
.. _ref_cfx_res_files:

Read CFX `.res` files
---------------------

This example demonstrates how to read Ansys CFX `.res` files.

.. note::
    This example requires DPF 7.0 (ansys-dpf-server-2024-1-pre0) or above.
    For more information, see :ref:`ref_compatibility`.

"""

###############################################################################
# Exploring an Ansys CFX `.res` file
# ----------------------------------
# The first part of the example demonstrates how you can load an
# Ansys CFX `.res` file in a model.

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

path = examples.download_cfx_mixing_elbow()
model = dpf.Model(path)
print(model)
