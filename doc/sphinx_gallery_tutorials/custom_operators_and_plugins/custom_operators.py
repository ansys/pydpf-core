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

# _order: 1
"""
.. _tutorials_custom_operators_and_plugins_custom_operator:

Custom operators
================

.. note::

    This tutorial requires DPF 7.1 or above (2024 R1).

This tutorial shows the basics of creating a custom operator in Python and loading it onto a
server for use.

.. note::

    You can create custom operators in CPython using PyDPF-Core for use with DPF in Ansys 2023 R1
    and later.

It first presents how to create a custom DPF operator in Python using PyDPF-Core. It then shows
how to make a plugin out of this single operator. The next step is to load the plugin on the
server to record its operators. The final step is to instantiate the custom operator from the
client API and use it.

.. note::

    In this tutorial the DPF client API used is PyDPF-Core but, once recorded on the server,
    you can call the operators of the plugin using any of the DPF client APIs
    (C++, CPython, IronPython), as you would any other operator.
"""
###############################################################################
# Create a custom operator
# ------------------------
#
# To create a custom DPF operator using PyDPF-Core, define a custom operator class inheriting
# from the
# :class:`CustomOperatorBase <ansys.dpf.core.custom_operator.CustomOperatorBase>` class
# in a dedicated Python file.
#
# First declare the custom operator class, with necessary imports and a ``name`` property to
# define the operator scripting name.
#
# Next, set the ``specification`` property of your operator with:
#
# - a description of what the operator does
# - a dictionary for each input and output pin, including the name, a list of supported types,
#   a description, and whether it is optional and/or ellipsis
# - a list for operator properties, including name to use in the documentation and the operator
#   category. The optional ``license`` property lets you define a required license to check out
#   when running the operator.
#
# Finally, implement the operator behavior in its ``run`` method: request the inputs with
# ``get_input``, perform operations on the data, set the outputs with ``set_output``,
# and call ``set_succeeded``.
#
# The following code shows the contents of a file named ``custom_operator_example.py`` available
# under :mod:`ansys.dpf.core.examples.python_plugins`.

from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)


class CustomOperator(CustomOperatorBase):
    """Example of a custom DPF operator coded in Python."""

    @property
    def name(self):
        """Return the scripting name of the operator in Snake Case."""
        return "my_custom_operator"

    @property
    def specification(self) -> CustomSpecification:
        """Create the specification of the custom operator."""
        spec = CustomSpecification()
        spec.description = "What the Operator does. You can use MarkDown and LaTeX in descriptions."
        spec.inputs = {
            0: PinSpecification(
                name="input_0",
                type_names=[dpf.Field, dpf.FieldsContainer],
                document="Describe input pin 0.",
            ),
        }
        spec.outputs = {
            0: PinSpecification(
                name="output_0", type_names=[dpf.Field], document="Describe output pin 0."
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="my custom operator",
            category="my_category",
            license="any_dpf_supported_increments",
        )

        # Operator changelog and versioning is only available after DPF 2025R2
        try:
            from ansys.dpf.core.changelog import Changelog

            spec.set_changelog(
                Changelog()
                .patch_bump("Describe a patch bump.")
                .major_bump("Describe a major bump.")
                .minor_bump("Describe a minor bump.")
                .expect_version("1.1.0")
            )
        except ModuleNotFoundError as e:
            if "ansys.dpf.core.changelog" in str(e):
                pass
            else:
                raise e

        return spec

    def run(self):
        """Run the operator and execute the logic implemented here.

        In this example, the operator changes the name of a Field.
        """
        # Get the input as a Field
        field: dpf.Field = self.get_input(0, dpf.Field)
        # If None, try requesting as a FieldsContainer
        if field is None:
            field: dpf.FieldsContainer = self.get_input(0, dpf.FieldsContainer).get_field(0)
        if field is None:
            raise ValueError(
                "my_custom_operator: mandatory input 'input_0' is empty or of an unsupported type."
            )

        # Perform some operations on the data
        field.name = "new_field_name"

        # Set the output and declare success
        self.set_output(0, field)
        self.set_succeeded()


###############################################################################
# Package as a plugin
# -------------------
#
# You must package your custom operator as a *plugin*, which you can then load onto a running
# DPF server or configure to automatically load when starting a server.
#
# A DPF plugin contains Python modules with custom operator declarations. It also defines an
# entry-point for the DPF server to call, which records the operators into the server registry.
#
# This is done by defining a function named ``load_operators`` with signature ``*args`` and a
# call to the
# :func:`record_operator() <ansys.dpf.core.custom_operator.record_operator>` method for each
# custom operator.
#
# The ``CustomOperator`` class defined above, together with the ``load_operators`` function
# below, form a complete single-file DPF Python plugin.
#
# PS: You can declare several custom operator classes in the same file, with as many calls to
# ``record_operator`` as necessary.


def load_operators(*args):
    """Mandatory entry-point for the server to record the operators of the plugin."""
    from ansys.dpf.core.custom_operator import record_operator

    record_operator(CustomOperator, *args)


###############################################################################
# Load the plugin
# ---------------
#
# First, start a server in gRPC mode, which is the only server type supported for custom
# Python plugins.

import ansys.dpf.core as dpf

# Python plugins are not supported in process.
server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)

###############################################################################
# With the server and custom plugin ready, use the
# :func:`load_library() <ansys.dpf.core.core.load_library>` method to load the plugin.
#
# - The first argument is the path to the directory with the plugin.
# - The second argument is ``py_<plugin>``, where ``<plugin>`` is the name identifying the
#   plugin (the name of the Python file for a single-file plugin).
# - The third argument is the name of the function in the plugin which records operators
#   (``load_operators`` by default).

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

# Verify the operator is now in the list of available operators on the server
assert "my_custom_operator" in dpf.dpf_operator.available_operator_names(server=server)

###############################################################################
# Use the custom operator
# -----------------------
#
# Once the plugin is loaded, instantiate the custom operator based on its name,
# as returned by the ``name`` property.

my_custom_op = dpf.Operator(name="my_custom_operator", server=server)
print(my_custom_op)

###############################################################################
# Finally, run it as any other operator.

# Create a field to use as input
in_field = dpf.Field(server=server)
# Give it a name
in_field.name = "initial name"
print(in_field)
# Set it as input of the operator
my_custom_op.inputs.input_0.connect(in_field)
# Run the operator by requesting its output
out_field = my_custom_op.outputs.output_0()
print(out_field)
