# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

###############################################################################
# Exploring the mesh
# ~~~~~~~~~~~~~~~~~~
# Explore the mesh through the ``MeshInfo``. The ``MeshInfo`` provides metadata
# information about the mesh. For fluid models, it is useful to know the bodies and
# face zones, as well as the topological relationships between them. First get all
# the available information in the ``MeshInfo``.
mesh_info = model.metadata.mesh_info
print(mesh_info)

###############################################################################
# The ``MeshInfo`` exposes several helpers, such as a dictionary of available bodies:
print(mesh_info.bodies)

###############################################################################
# Or the dictionary of available face zones:
print(mesh_info.face_zones)

###############################################################################
# Exploring the results
# ~~~~~~~~~~~~~~~~~~~~~
# Explore the available results through the ``ResultInfo``.
# The ``ResultInfo`` provides metadata information about the results stored in the files.
# First get all the available information in the ``ResultInfo``.
# As you can see above, the ``ResultInfo`` information is also listed when printing the ``Model``.
result_info = model.metadata.result_info
print(result_info)

###############################################################################
# The ``ResultInfo`` class exposes the list of ``AvailableResults``.
print(result_info.available_results)

###############################################################################
# Extracting data
# ~~~~~~~~~~~~~~~
# Extracting the mesh or results is then the same as for any other file type.
