# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import errors
import ansys.dpf.core.dpf_logger as dpf_logger

import conftest


class _FakeDataTree:
    def __init__(self, server=None):
        self.server = server
        self.attrs = {}

    def add(self, data):
        self.attrs.update(data)


class _FakeAPI:
    """Mock CAPI backend for in-process logger testing."""

    def __init__(self):
        self.last_registered_params = None
        self.last_retrieved_params = None
        self.logged_calls = []
        self.flush_all_called = False
        self.flushed_impl = None

    def init_data_processing_environment(self, server):
        self.server = server

    def data_processing_logging_register_logger(self, register_logger_params):
        self.last_registered_params = register_logger_params
        return "logger-impl"

    def data_processing_logging_get_logger(self, get_logger_params):
        self.last_retrieved_params = get_logger_params
        return "logger-impl"

    def data_processing_logging_log_message(self, logger_impl, message, log_level):
        self.logged_calls.append((logger_impl, message, log_level))

    def data_processing_logging_flush(self, logger_impl):
        self.flushed_impl = logger_impl

    def data_processing_logging_flush_all(self):
        self.flush_all_called = True


class _FakeServer:
    def __init__(self, api):
        self.api = api

    def get_api_for_type(self, capi=None, grpcapi=None):
        return self.api


def _patch_server_and_tree(monkeypatch, api):
    """Patch server factory and DataTree for testing."""
    fake_server = _FakeServer(api)
    monkeypatch.setattr(dpf_logger.server_module, "get_or_create_server", lambda _: fake_server)
    monkeypatch.setattr(dpf_logger, "DataTree", _FakeDataTree)


def test_register_logger_builds_expected_payload(monkeypatch):
    """Test that register_logger constructs correct param tree."""
    api = _FakeAPI()
    _patch_server_and_tree(monkeypatch, api)

    logger = dpf_logger.register_logger(
        "custom.plugin",
        dpf_logger.LoggerConfig(
            level=dpf_logger.LogLevel.debug,
            sinks=[dpf_logger.LoggerSink.stdout, dpf_logger.LoggerSink.file],
        ),
    )

    assert isinstance(logger, dpf_logger.DPFLogger)
    assert api.last_registered_params.attrs == {
        "logger_name": "custom.plugin",
        "log_level": 1,
        "sinks": [0, 1],
    }


def test_get_logger_and_log_message(monkeypatch):
    """Test get_logger, message emission, and flush chain."""
    api = _FakeAPI()
    _patch_server_and_tree(monkeypatch, api)

    logger = dpf_logger.get_logger("custom.plugin")
    logger.log("test message", dpf_logger.LogLevel.warn)
    logger.flush()
    dpf_logger.flush_all()

    assert api.last_retrieved_params.attrs == {"logger_name": "custom.plugin"}
    assert api.logged_calls == [("logger-impl", "test message", 3)]
    assert api.flushed_impl == "logger-impl"
    assert api.flush_all_called


def test_unsupported_backend_raises_server_type_error(monkeypatch):
    """Test that NotImplementedError is converted to ServerTypeError."""

    class _NotImplementedAPI(_FakeAPI):
        def data_processing_logging_register_logger(self, register_logger_params):
            raise NotImplementedError()

    api = _NotImplementedAPI()
    _patch_server_and_tree(monkeypatch, api)

    try:
        dpf_logger.register_logger("custom.plugin")
        assert False, "Expected a ServerTypeError"
    except errors.ServerTypeError as exc:
        assert "custom Python plugin" in str(exc)
        assert "implement" in str(exc).lower()


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_0,
    reason="Requires DPF server >= 8.0",
)
def test_logger_with_real_global_inprocess_server():
    """Validate logger API against the real global InProcess server."""
    server = dpf._global_server()
    if not isinstance(server, dpf.server_types.InProcessServer):
        pytest.skip("Global server is not InProcess in this environment")

    logger_name = "custom.plugin.real.integration_test"

    logger = dpf_logger.register_logger(
        name=logger_name,
        config=dpf_logger.LoggerConfig(
            level=dpf_logger.LogLevel.debug,
            sinks=[dpf_logger.LoggerSink.stdout],
        ),
        server=server,
    )

    assert isinstance(logger, dpf_logger.DPFLogger)

    logger.debug("debug message from real in-process logger test")
    logger.info("info message from real in-process logger test")

    same_logger = dpf_logger.get_logger(name=logger_name, server=server)
    assert isinstance(same_logger, dpf_logger.DPFLogger)

    same_logger.warn("warn message from real in-process logger test")
    same_logger.flush()
    dpf_logger.flush_all(server=server)
