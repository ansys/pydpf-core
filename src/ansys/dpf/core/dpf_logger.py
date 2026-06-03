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

"""High-level access to DPF framework logging APIs.

This module provides a Python wrapper around the native DPF logging APIs.
It is designed for use in custom Python plugins, where code executes in-process
with the DPF server and has direct access to native C-layer logging functions
through the CAPI.

Note: This API is only available in custom Python plugins. Remote or
client-side Python environments cannot access these logging functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Optional

from ansys.dpf.core import errors, server as server_module
from ansys.dpf.core.data_tree import DataTree
from ansys.dpf.gate import data_processing_capi


class LogLevel(Enum):
    """DPF logging levels."""

    trace = 0
    debug = 1
    info = 2
    warn = 3
    error = 4
    critical = 5
    off = 6


class LoggerSink(Enum):
    """DPF logging sinks."""

    stdout = 0
    file = 1


@dataclass
class LoggerConfig:
    """Configuration used when registering a DPF logger."""

    level: LogLevel = LogLevel.info
    sinks: Optional[Iterable[LoggerSink]] = None

    def sink_values(self) -> list[int]:
        """Return sink values as integers expected by C-layer APIs."""
        if self.sinks is None:
            return [int(LoggerSink.stdout.value)]
        return [_enum_or_int(value, LoggerSink, "sinks") for value in self.sinks]


class DPFLogger:
    """Wrapper around a native DPF logger implementation pointer."""

    def __init__(self, implementation, core_api):
        self._implementation = implementation
        self._core_api = core_api

    def log(self, message: str, level: LogLevel = LogLevel.info) -> None:
        """Log one message with the given level."""
        self._core_api.data_processing_logging_log_message(
            self._implementation,
            message,
            _enum_or_int(level, LogLevel, "level"),
        )

    def trace(self, message: str) -> None:
        """Log message at trace level."""
        self.log(message, LogLevel.trace)

    def debug(self, message: str) -> None:
        """Log message at debug level."""
        self.log(message, LogLevel.debug)

    def info(self, message: str) -> None:
        """Log message at info level."""
        self.log(message, LogLevel.info)

    def warn(self, message: str) -> None:
        """Log message at warn level."""
        self.log(message, LogLevel.warn)

    def error(self, message: str) -> None:
        """Log message at error level."""
        self.log(message, LogLevel.error)

    def critical(self, message: str) -> None:
        """Log message at critical level."""
        self.log(message, LogLevel.critical)

    def flush(self) -> None:
        """Flush this logger sinks."""
        self._core_api.data_processing_logging_flush(self._implementation)


def register_logger(name: str, config: Optional[LoggerConfig] = None, server=None) -> DPFLogger:
    """Register and return a DPF logger instance.

    Intended for use in custom Python plugins.

    Parameters
    ----------
    name : str
        Logger name to register.
    config : LoggerConfig, optional
        Logger configuration (level, sinks). Default is Info level, stdout sink.
    server : DPFServer, optional
        DPF server instance. If None, uses global server.

    Returns
    -------
    DPFLogger
        Logger wrapper bound to native DPF logger implementation.

    Raises
    ------
    ServerTypeError
        If called outside a custom Python plugin context or from a remote client.
    """
    if config is None:
        config = LoggerConfig()
    server_instance, core_api = _server_and_api(server)
    params = _build_logger_params(
        server=server_instance,
        logger_name=name,
        log_level=_enum_or_int(config.level, LogLevel, "config.level"),
        sinks=config.sink_values(),
    )
    implementation = _call_api(
        core_api.data_processing_logging_register_logger,
        params,
        operation="register_logger",
    )
    return DPFLogger(implementation, core_api)


def get_logger(name: str, server=None) -> DPFLogger:
    """Get an existing DPF logger by name.

    Intended for use in custom Python plugins.

    Parameters
    ----------
    name : str
        Logger name to retrieve.
    server : DPFServer, optional
        DPF server instance. If None, uses global server.

    Returns
    -------
    DPFLogger
        Logger wrapper bound to native DPF logger implementation.

    Raises
    ------
    ServerTypeError
        If called outside a custom Python plugin context or from a remote client.
    """
    server_instance, core_api = _server_and_api(server)
    params = _build_logger_params(server=server_instance, logger_name=name)
    implementation = _call_api(
        core_api.data_processing_logging_get_logger,
        params,
        operation="get_logger",
    )
    return DPFLogger(implementation, core_api)


def flush_all(server=None) -> None:
    """Flush all currently registered DPF loggers.

    Intended for use in custom Python plugins.

    Parameters
    ----------
    server : DPFServer, optional
        DPF server instance. If None, uses global server.

    Raises
    ------
    ServerTypeError
        If called outside a custom Python plugin context or from a remote client.
    """
    _, core_api = _server_and_api(server)
    _call_api(core_api.data_processing_logging_flush_all, operation="flush_all")


def _build_logger_params(server, **kwargs) -> DataTree:
    params = DataTree(server=server)
    params.add(kwargs)
    return params


def _server_and_api(server):
    server_instance = server_module.get_or_create_server(server)
    core_api = server_instance.get_api_for_type(
        capi=data_processing_capi.DataProcessingCAPI,
        grpcapi=None,  # Custom operators are always in-process, no gRPC support needed
    )
    core_api.init_data_processing_environment(server_instance)
    return server_instance, core_api


def _call_api(function, *args, operation: str):
    """Call a logging API function, converting NotImplementedError to ServerTypeError."""
    try:
        return function(*args)
    except NotImplementedError as exc:
        raise errors.ServerTypeError(
            "DPF logger API is only available in custom Python plugins. "
            f"The backend does not implement logging (during '{operation}'). "
            "Ensure this code is executing within a custom Python plugin context."
        ) from exc


def _enum_or_int(value, enum_type, argument_name: str) -> int:
    """Convert enum or int to int, validating type."""
    if isinstance(value, enum_type):
        return int(value.value)
    if isinstance(value, int):
        return value
    raise TypeError(f"{argument_name} must be an int or {enum_type.__name__}.")
