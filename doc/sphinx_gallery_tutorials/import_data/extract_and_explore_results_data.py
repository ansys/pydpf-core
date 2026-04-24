# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# _order: 4
"""
.. _ref_tutorials_extract_and_explore_results_data:

Extract and explore results data
=================================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

This tutorial shows how to extract and explore results data from a result file.

When you extract a result from a result file, DPF stores it in a
:class:`Field<ansys.dpf.core.field.Field>`. This ``Field`` contains the data of
the result associated with it.

.. note::

    When DPF-Core returns the ``Field`` object, what Python actually has is a
    client-side representation of the ``Field``, not the entirety of the ``Field``
    itself. This means all the data is stored within the DPF service. When building
    your workflows, the most efficient way of interacting with result data is to
    minimize the exchange of data between Python and DPF, either by using operators
    or by accessing exclusively the data that is needed.
"""
###############################################################################
# Get the result file
# -------------------
#
# Import a result file. For this tutorial, use one available in the
# :mod:`examples<ansys.dpf.core.examples>` module. For more information about how
# to import your own result file in DPF, see the
# :ref:`ref_tutorials_import_result_file` tutorial.
#
# .. tip::
#
#     If you need to evaluate many result operators against the same file,
#     consider using a ``StreamsContainer`` to reuse open file handles and
#     avoid redundant mesh loads. See
#     :ref:`ref_tutorials_import_data_streams_for_multiple_operators`.
#
# Extract the displacement results. The displacement
# :class:`Result<ansys.dpf.core.results.Results>` object gives a
# :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>` when
# evaluated. Get a ``Field`` from this ``FieldsContainer``.

# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf

# Import the operators and examples module
from ansys.dpf.core import examples, operators as ops

# Define the result file path
result_file_path_1 = examples.download_transient_result()

# Create the model
model_1 = dpf.Model(data_sources=result_file_path_1)

# Extract the displacement results for the last time step
disp_results = model_1.results.displacement.on_last_time_freq.eval()

# Get the displacement field for the last time step
disp_field = disp_results[0]
print(disp_field)

###############################################################################
# Extract all the data from a ``Field``
# --------------------------------------
#
# Extract the entire data in a ``Field`` as an array or a list.
#
# Get the data as an array (Numpy array)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

data_array = disp_field.data
print("Displacement data as an array: ", "\n", data_array)

###############################################################################
# Note that this array is a genuine, local, numpy array (overloaded by the DPFArray).

print("Array type: ", type(data_array))

###############################################################################
# Get the data as a list
# ~~~~~~~~~~~~~~~~~~~~~~~~

data_list = disp_field.data_as_list
print("Displacement data as a list: ", "\n", data_list)

###############################################################################
# Extract specific data from a field
# ------------------------------------
#
# If you need to access data for specific entities (node, element, ...), you can
# extract it with two approaches:
#
# - Based on its index (position in the ``Field``) using the
#   :func:`get_entity_data()<ansys.dpf.core.field.Field.get_entity_data>` method
# - Based on the entity id using the
#   :func:`get_entity_data_by_id()<ansys.dpf.core.field.Field.get_entity_data_by_id>`
#   method
#
# The ``Field`` data is organized with respect to its scoping ids. Note that the
# element with ``id=533`` would correspond to an ``index=2`` within the ``Field``.

# Get the index of the entity with id=533
index_533_entity = disp_field.scoping.index(id=533)
print("Index entity id=533: ", index_533_entity)

###############################################################################
# Note that scoping IDs are not sequential. Get the id of the element at index 533.

id_533_entity = disp_field.scoping.id(index=533)
print("Id entity index=533: ", id_533_entity)

###############################################################################
# .. _ref_extract_specific_data_by_index:
#
# Get the data by the entity index
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

data_3_entity = disp_field.get_entity_data(index=3)
print("Data entity index=3: ", data_3_entity)

###############################################################################
# .. _ref_extract_specific_data_by_id:
#
# Get the data by the entity id
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

data_533_entity = disp_field.get_entity_data_by_id(id=533)
print("Data entity id=533: ", data_533_entity)

###############################################################################
# Extract specific data using a loop over the array
# --------------------------------------------------
#
# While the methods above are acceptable when requesting data for a few elements
# or nodes, they should not be used when looping over the entire array. For
# efficiency, a ``Field`` data can be recovered locally before sending a large
# number of requests.

# Create a deep copy of the field that can be accessed and modified locally.
with disp_field.as_local_field() as f:
    for i in disp_field.scoping.ids[2:50]:
        f.get_entity_data_by_id(i)

print(f)
