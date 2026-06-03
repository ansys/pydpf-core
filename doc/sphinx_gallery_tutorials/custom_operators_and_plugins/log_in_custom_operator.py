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

# _order: 2
"""
.. _tutorials_custom_operators_and_plugins_log_in_custom_operator:

Add logging to custom operators and plugins
============================================

This tutorial shows how to use the DPF logging API to emit debug and error messages
from within a custom Python operator or plugin.

You will learn how to register a logger with different log levels and output sinks,
and how to emit messages that are captured by the DPF framework's logging system.
This is useful for debugging custom operators and providing visibility into plugin
execution.

.. note::

    This tutorial requires DPF 7.1 or above (2024 R1).
"""
###############################################################################
# Import modules and define a custom operator with logging
# ---------------------------------------------------------
#
# To use logging in a custom operator, import the required DPF modules and the
# logging API from :mod:`ansys.dpf.core.dpf_logger`.
#
# This example creates a custom operator that logs its execution steps.

from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.dpf_logger import (
    LoggerConfig,
    LoggerSink,
    LogLevel,
    register_logger,
)
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)


class LoggingCustomOperator(CustomOperatorBase):
    """Example of a custom DPF operator that uses logging."""

    @property
    def name(self):
        """Return the scripting name of the operator."""
        return "my_logging_operator"

    @property
    def specification(self) -> CustomSpecification:
        """Create the specification of the custom operator."""
        spec = CustomSpecification()
        spec.description = "A custom operator that demonstrates logging."
        spec.inputs = {
            0: PinSpecification(
                name="field_input",
                type_names=[dpf.Field],
                document="Input field to process.",
            ),
        }
        spec.outputs = {
            0: PinSpecification(
                name="result_field", type_names=[dpf.Field], document="Output field."
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="my logging operator",
            category="my_category",
        )
        return spec

    def run(self):
        """Run the operator with logging at different levels."""
        # Register a logger for this operator.
        # Using info level and stdout sink for visibility.
        logger_config = LoggerConfig(
            level=LogLevel.debug,
            sinks=[LoggerSink.stdout],
        )
        my_logger = register_logger(name="my_operator", config=logger_config)

        my_logger.info("Operator execution started")

        # Get the input field
        try:
            field: dpf.Field = self.get_input(0, dpf.Field)
            if field is None:
                my_logger.error("No input field provided")
                self.set_failed()
                return

            my_logger.debug(f"Received field with {field.size} values")
        except Exception as e:
            my_logger.error(f"Failed to retrieve input field: {e}")
            self.set_failed()
            return

        # Process the field
        my_logger.info("Processing field data")

        try:
            # Create a new field as output
            result_field = field.deep_copy()
            my_logger.debug(f"Created output field with {result_field.size} values")

            # Set the output and mark the operator as succeeded
            self.set_output(0, result_field)
            my_logger.info("Operator execution completed successfully")
            self.set_succeeded()
        except Exception as e:
            my_logger.error(f"Error during field processing: {e}")
            self.set_failed()


###############################################################################
# Use multiple log levels
# -----------------------
#
# The DPF logging API supports six log levels (trace, debug, info, warn, error, critical)
# for different severity levels. You can emit messages at any level depending on
# the importance and verbosity desired.

example_logger_config = LoggerConfig(
    level=LogLevel.debug,  # Capture debug and above
    sinks=[LoggerSink.stdout],
)

# In a real operator's run() method, you would do:
# my_logger = register_logger(name="example_operator", config=example_logger_config)
# my_logger.trace("Very detailed tracing information")
# my_logger.debug("Debug information for troubleshooting")
# my_logger.info("Informational message about normal operation")
# my_logger.warn("Warning about potentially problematic condition")
# my_logger.error("Error that occurred during processing")
# my_logger.critical("Critical error requiring immediate attention")

###############################################################################
# Configure logging with file output
# -----------------------------------
#
# Instead of only logging to stdout, you can also write logs to a file
# by including :class:`LoggerSink.file <ansys.dpf.core.dpf_logger.LoggerSink>` in the sinks list.

file_logger_config = LoggerConfig(
    level=LogLevel.info,
    sinks=[LoggerSink.stdout, LoggerSink.file],
)

# In a real operator's run() method, you would do:
# my_logger = register_logger(
#     name="file_logging_operator",
#     config=file_logger_config,
# )
# my_logger.info("This message appears in both stdout and the log file")

###############################################################################
# Retrieve and flush existing loggers
# -------------------------------------------
#
# If you need to access a logger that was already registered,
# use :func:`get_logger <ansys.dpf.core.dpf_logger.get_logger>` instead of
# :func:`register_logger <ansys.dpf.core.dpf_logger.register_logger>`.

# In a real operator's run() method:
# my_logger = get_logger(name="my_operator")
# my_logger.info("Retrieved existing logger")

# To ensure all log messages are written immediately, call
# :func:`flush_all <ansys.dpf.core.dpf_logger.flush_all>` at the end
# of your operator:

# from ansys.dpf.core.dpf_logger import flush_all
# my_logger.info("Final message before flush")
# flush_all()
