# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Tests for the DPF Server discovery order (issue 3527).
# DPF Server discovery: test cases

Tests live in `tests/test_server_discovery.py`. Everything runs on fake folders created under
`tmp_path` and on `monkeypatch` (environment variables, `load_api.__file__`, and the
`ansys-dpf-server` package lookup). No DPF binaries are needed.

## Priority order under test

| Rank | Source | Function | Route A `misc.get_ansys_path()` | Route B `load_api._find_latest_ansys_versions()` |
|---|---|---|---|---|
| 0 | Explicit `ansys_path` argument | caller | yes | yes (caller) |
| 1 | `ANSYS_DPF_PATH` | `_path_to_dpf_from_env_variable` | yes | yes |
| 2 | Latest pip-installed `ansys-dpf-server` | `_paths_to_dpf_server_library_installs` | yes | yes |
| 3 | Unified Install hosting `load_api.py` | `_path_to_dpf_in_hosting_unified_install` | yes | yes |
| 4 | Latest `AWP_ROOTXXX` | `_paths_to_dpf_in_unified_installs` | yes | yes |
| 5 | Latest `vXXX` in the default install folder | `misc.find_ansys` | yes | no |

## Fake machine (`_make_layout`, `_setup`)

| Key | Fake location under `tmp_path` |
|---|---|
| `v261`, `v271` | `ANSYS Inc/v261`, `ANSYS Inc/v271` (with `aisol/...` and `dpf/...` sub-folders) |
| `standalone` | `AnsysDev/dpf_standalone_win_v35.2.pre3/ansys/dpf/server_2035_2_pre3` |
| `package` | `venv/Lib/site-packages/ansys/dpf/server_2035_2_pre3` (pip `ansys-dpf-server` 2035.2.pre3) |
| `pydpf_cpython_vXXX` | `ANSYS Inc/vXXX/commonfiles/CPython/3_10/winx64/Release/Ansys/PyDPF/ansys/dpf/gate/load_api.py` (v261, v271) |
| `pydpf_zip_vXXX` | `ANSYS Inc/vXXX/dpf/python/original/dpf-site.zip/ansys/dpf/gate/load_api.py` (v261, v271) |
| `pydpf_standalone` | `AnsysDev/dpf_standalone_win_v35.2.pre3/ansys/dpf/gate/load_api.py` |
| `pydpf_external` | `venv/Lib/site-packages/ansys/dpf/gate/load_api.py` (pip-installed PyDPF) |

The `clean_discovery_env` fixture removes `ANSYS_DPF_PATH`, every `AWP_ROOT*` variable and any
real server package, so each test only enables the sources it needs.

`_setup(deployment, pydpf, venv, env)` builds one machine:

- `deployment="unified"`: creates `v261` and `v271`, sets `AWP_ROOT261`, `AWP_ROOT271` and a
  non-numeric `AWP_ROOTDV_DEV` (must be ignored).
- `deployment="standalone"`: creates the standalone server and sets `AWP_ROOT271` to it.
- `pydpf`: where `load_api.py` lives.
- `venv`: whether the `ansys-dpf-server` package is installed.
- `env`: target of `ANSYS_DPF_PATH` (`None`, `v261`, `v271` or `standalone`).


## Priority matrix (`test_discovery_priority`)

| Code | Deployment | `load_api.py` from | Server package | `ANSYS_DPF_PATH` | Expected | Capability covered |
|---|---|---|---|---|---|---|
| U01 | Unified v261 + v271 | `commonfiles/CPython` (v261) | no | - | v261 | Hosting (3) beats newer `AWP_ROOT271` (4), issue 3527; non-numeric `AWP_ROOT` ignored |
| U02 | Unified v261 + v271 | `dpf-site.zip` (v261) | no | - | v261 | Same as U01 for the zip layout |
| U03 | Unified v261 + v271 | external venv | no | - | v271 | No hosting: latest `AWP_ROOTXXX` (4) wins |
| U04 | Unified v261 + v271 | `commonfiles/CPython` (v261) | yes | - | package | Package (2) beats hosting (3) |
| U05 | Unified v261 + v271 | external venv | yes | - | package | Package (2) beats `AWP_ROOTXXX` (4) |
| U06 | Unified v261 + v271 | `dpf-site.zip` (v261) | yes | v271 | v271 | `ANSYS_DPF_PATH` (1) beats package (2) and hosting (3) |
| U07 | Unified v261 + v271 | external venv | yes | v261 | v261 | `ANSYS_DPF_PATH` (1) beats package (2) and a newer `AWP_ROOTXXX` (4) |
| S01 | Standalone (`AWP_ROOT271`) | standalone | no | - | standalone | `AWP_ROOTXXX` pointing to a standalone (4); standalone is not seen as hosting |
| S02 | Standalone (`AWP_ROOT271`) | standalone | yes | - | package | Package (2) beats standalone `AWP_ROOTXXX` (4) |
| S03 | Standalone (`AWP_ROOT271`) | standalone | yes | standalone | standalone | `ANSYS_DPF_PATH` to a standalone (1) beats package (2) |

## Supporting tests

| Code | Test | Capability covered |
|---|---|---|
| H01 | `test_hosting_detection[H01]` | `_unified_install_root_of` finds `v261` from `commonfiles/CPython` |
| H02 | `test_hosting_detection[H02]` | Same from inside `dpf-site.zip` (path does not exist on disk) |
| H03 | `test_hosting_detection[H03]` | Standalone folder `v35.2.pre3` is not a `vXXX` Unified Install |
| H04 | `test_hosting_detection[H04]` | External venv PyDPF is not hosted |
| H05 | `test_hosting_detection_vxxx_without_aisol` | A `vXXX` folder without `aisol/...` is ignored |
| E01 | `test_ansys_dpf_path_trailing_separator` | Trailing separator in `ANSYS_DPF_PATH` is normalized, for Unified and standalone targets, on both routes |
| E02 | `test_ansys_dpf_path_not_a_directory` | `ANSYS_DPF_PATH` to a missing folder raises `ValueError`; there is no silent fallback |
| A01 | `test_explicit_ansys_path_wins` | Explicit `ansys_path` (0) beats `ANSYS_DPF_PATH`, package and hosting |
| A02 | `test_default_folder_scan` | Route A only: default install folder scan (5) when no other source exists (Windows only) |
| A03 | `test_nothing_found` | Route B returns `None`; route A raises a clear `ValueError` |
| W01 | `test_start_local_server_passes_discovered_path` | `start_local_server` passes the discovered path to the InProcess, gRPC and LegacyGrpc servers |
| W02 | `test_load_client_api_uses_discovery` | `load_client_api(None)` (InProcess and gRPC) uses the discovery chain |
| W03 | `test_load_grpc_client_uses_discovery` | `load_grpc_client(None)` (gRPC) uses the discovery chain |

"""

import os
from pathlib import Path
import shutil

from packaging.version import Version
import pytest

from ansys.dpf.core import misc, server, server_types
from ansys.dpf.core.server_factory import AvailableServerConfigs, ServerFactory
from ansys.dpf.gate import load_api
from conftest import running_docker

PACKAGE_VERSION = Version("2035.2.pre3")


# ---------------------------------------------------------------------------------------------
# Fake file system helpers
# ---------------------------------------------------------------------------------------------


def _make_unified_install(root: Path, version: str) -> Path:
    """Create a minimal fake Unified Install ``root/v<version>`` and return it."""
    install = root / f"v{version}"
    (install / load_api._get_path_in_install()).mkdir(parents=True)
    (install / load_api._get_dpf_path_in_install()).mkdir(parents=True)
    return install


def _make_server_package(site_packages: Path, suffix: str) -> Path:
    """Create a minimal fake pip-installed ``ansys-dpf-server`` and return its root."""
    server_root = site_packages / "ansys" / "dpf" / f"server_{suffix}"
    (server_root / load_api._get_path_in_install()).mkdir(parents=True)
    return server_root


def _make_layout(tmp_path: Path) -> dict:
    """Return every location used by the tests. Only the folders a test needs are created."""
    ansys_inc = tmp_path / "ANSYS Inc"
    standalone_dir = tmp_path / "AnsysDev" / "dpf_standalone_win_v35.2.pre3"
    site_packages = tmp_path / "venv" / "Lib" / "site-packages"
    gate = Path("ansys") / "dpf" / "gate" / "load_api.py"
    return {
        "ansys_inc": ansys_inc,
        "v261": ansys_inc / "v261",
        "v271": ansys_inc / "v271",
        "standalone": standalone_dir / "ansys" / "dpf" / "server_2035_2_pre3",
        "site_packages": site_packages,
        "package": site_packages / "ansys" / "dpf" / "server_2035_2_pre3",
        # Possible locations of load_api.py (only used as strings, never created)
        "pydpf_cpython": ansys_inc / "v261" / "commonfiles" / "CPython" / "3_10" / "winx64"
        / "Release" / "Ansys" / "PyDPF" / gate,
        "pydpf_zip": ansys_inc / "v261" / "dpf" / "python" / "original" / "dpf-site.zip" / gate,
        "pydpf_standalone": standalone_dir / gate,
        "pydpf_external": site_packages / gate,
    }

# deletes each test's fake folders when the test ends
@pytest.fixture(autouse=True)
def _delete_fake_layout(request):
    """Delete the fake folders of a test as soon as it ends.

    Every folder is created under ``tmp_path``, which pytest only purges on later runs
    (it keeps the last three). Remove it right after each test instead.
    """
    tmp_path = request.getfixturevalue("tmp_path") if "tmp_path" in request.fixturenames else None
    yield
    if tmp_path is not None:
        shutil.rmtree(tmp_path, ignore_errors=True)
        assert not tmp_path.exists(), f"Fake layout not deleted: {tmp_path}"

# removes any real ANSYS_DPF_PATH, AWP_ROOT* variables and server packages, so each test only sees the sources it sets up.
@pytest.fixture()
def clean_discovery_env(monkeypatch):
    """Remove every discovery source so each test enables only the ones it needs."""
    monkeypatch.delenv("ANSYS_DPF_PATH", raising=False)
    for key in list(os.environ.keys()):
        if "AWP_ROOT" in key:
            monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(load_api, "_paths_to_dpf_server_library_installs", lambda: {})
    monkeypatch.setattr(load_api, "__file__", str(Path(os.sep) / "not_an_install" / "load_api.py"))


def _setup(tmp_path, monkeypatch, deployment, pydpf, venv, env):
    """Build a fake machine and enable the requested discovery sources.

    Parameters
    ----------
    deployment : "unified" | "standalone"
        ``unified``: ``v261`` and ``v271`` exist, ``AWP_ROOT261``/``AWP_ROOT271`` are set.
        ``standalone``: a DPF standalone exists, ``AWP_ROOT271`` points to it.
    pydpf : "cpython_v261" | "cpython_v271" | "zip_v261" | "zip_v271" | "standalone" | "external"
        Location of ``load_api.py``.
    venv : bool
        Whether an ``ansys-dpf-server`` package is pip-installed in the Python environment.
    env : None | "v261" | "v271" | "standalone"
        Target of ``ANSYS_DPF_PATH``.
    """
    layout = _make_layout(tmp_path)
    if deployment == "unified":
        _make_unified_install(layout["ansys_inc"], "261")
        _make_unified_install(layout["ansys_inc"], "271")
        monkeypatch.setenv("AWP_ROOT261", str(layout["v261"]))
        monkeypatch.setenv("AWP_ROOT271", str(layout["v271"]))
        monkeypatch.setenv("AWP_ROOTDV_DEV", str(layout["v271"]))  # ignored: suffix not numeric
    else:
        (layout["standalone"] / load_api._get_path_in_install()).mkdir(parents=True)
        (layout["standalone"] / load_api._get_dpf_path_in_install()).mkdir(parents=True)
        monkeypatch.setenv("AWP_ROOT271", str(layout["standalone"]))
    monkeypatch.setattr(load_api, "__file__", str(layout[f"pydpf_{pydpf}"]))
    if venv:
        _make_server_package(layout["site_packages"], "2035_2_pre3")
        monkeypatch.setattr(
            load_api,
            "_paths_to_dpf_server_library_installs",
            lambda: {PACKAGE_VERSION: str(layout["package"])},
        )
    if env is not None:
        monkeypatch.setenv("ANSYS_DPF_PATH", str(layout[env]))
    return layout


# ---------------------------------------------------------------------------------------------
# Priority matrix (route A and route B must agree)
# ---------------------------------------------------------------------------------------------

MATRIX = [
    # code,  deployment,   pydpf,        venv,  env,          expected
    ("U01", "unified", "cpython", False, None, "v261"), #PyDPF is shipped inside v261 (the CPython). v261 wins over the newer AWP_ROOT271
    ("U02", "unified", "zip", False, None, "v261"), #PyDPF is shipped inside v261 (dpf-site.zip layout). v261 wins over the newer AWP_ROOT271
    ("U03", "unified", "external", False, None, "v271"), #PyDPF comes from an external venv, so no install hosts it. The latest AWP_ROOTXXX (v271) wins
    ("U04", "unified", "cpython", True, None, "package"),#a pip-installed server package wins over the hosting install.
    ("U05", "unified", "external", True, None, "package"),#a pip-installed server package wins over the hosting install.
    ("U06", "unified", "zip", True, "v271", "v271"),#ANSYS_DPF_PATH wins over everything else
    ("U07", "unified", "external", True, "v261", "v261"),#ANSYS_DPF_PATH wins over everything else
    ("S01", "standalone", "standalone", False, None, "standalone"),#DPF standalone setup. AWP_ROOT271 points to the standalone, and the standalone folder isn't mistaken for a Unified Install.
    ("S02", "standalone", "standalone", True, None, "package"),#a pip-installed package wins over the standalone
    ("S03", "standalone", "standalone", True, "standalone", "standalone"),# ANSYS_DPF_PATH pointing to the standalone wins over the package.
]


@pytest.mark.parametrize(
    "deployment, pydpf, venv, env, expected",
    [case[1:] for case in MATRIX],
    ids=[case[0] for case in MATRIX],
)
def test_discovery_priority(
    tmp_path, monkeypatch, clean_discovery_env, deployment, pydpf, venv, env, expected
):
    layout = _setup(tmp_path, monkeypatch, deployment, pydpf, venv, env)
    # Route B: client libraries loaded with ansys_path=None
    assert load_api._find_latest_ansys_versions() == str(layout[expected])
    # Route A: start_local_server() and DataProcessingCore
    assert misc.get_ansys_path() == str(layout[expected])
    dll_path = server_types._get_dll_path("DataProcessingCore")
    assert dll_path.parent == layout[expected] / load_api._get_path_in_install()


# ---------------------------------------------------------------------------------------------
# Hosting detection: _unified_install_root_of()
# ---------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "pydpf, expected",
    [
        ("pydpf_cpython", "v261"), #v261 is found from the CPython path.
        ("pydpf_zip", "v261"),# v261 is found from inside dpf-site.zip
        ("pydpf_standalone", None),  # "v35.2.pre3" is not a vXXX folder
        ("pydpf_external", None),# a PyDPF in an external venv has no hosting install
    ],
    ids=["H01", "H02", "H03", "H04"],
)
def test_hosting_detection(tmp_path, pydpf, expected):
    layout = _make_layout(tmp_path)
    _make_unified_install(layout["ansys_inc"], "261")
    (layout["standalone"] / load_api._get_path_in_install()).mkdir(parents=True)
    result = load_api._unified_install_root_of(layout[pydpf])
    assert result == (str(layout[expected]) if expected else None)

# A folder named like v123 that has no aisol subfolder isn't treated as an install.
def test_hosting_detection_vxxx_without_aisol(tmp_path):  # H05
    fake = tmp_path / "v123" / "some" / "folder"
    fake.mkdir(parents=True)
    assert load_api._unified_install_root_of(fake) is None


# ---------------------------------------------------------------------------------------------
# ANSYS_DPF_PATH validation
# ---------------------------------------------------------------------------------------------

# ANSYS_DPF_PATH ending in \ or / still works on both lookups, for a Unified Install and for a standalone target.
@pytest.mark.parametrize("target", ["v271", "standalone"], ids=["E01-unified", "E01-standalone"])
def test_ansys_dpf_path_trailing_separator(tmp_path, monkeypatch, clean_discovery_env, target):
    layout = _make_layout(tmp_path)
    (layout[target] / load_api._get_path_in_install()).mkdir(parents=True)
    monkeypatch.setenv("ANSYS_DPF_PATH", str(layout[target]) + os.sep)
    assert load_api._find_latest_ansys_versions() == str(layout[target])
    assert misc.get_ansys_path() == str(layout[target])

# . If ANSYS_DPF_PATH points to a missing folder, you get a clear ValueError instead of a silent switch to another install.
def test_ansys_dpf_path_not_a_directory(tmp_path, monkeypatch, clean_discovery_env):  # E02
    _setup(tmp_path, monkeypatch, "unified", "cpython", True, None)
    monkeypatch.setenv("ANSYS_DPF_PATH", str(tmp_path / "ANSYS Inc" / "v999"))
    with pytest.raises(ValueError, match="ANSYS_DPF_PATH"):
        load_api._find_latest_ansys_versions()


# ---------------------------------------------------------------------------------------------
# Route A specifics: explicit argument, default folder scan, nothing found
# ---------------------------------------------------------------------------------------------

# A path passed explicitly to get_ansys_path(path) wins over every automatic source.
def test_explicit_ansys_path_wins(tmp_path, monkeypatch, clean_discovery_env):  # A01
    layout = _setup(tmp_path, monkeypatch, "unified", "cpython", True, "v271")
    assert misc.get_ansys_path(str(layout["v261"])) == str(layout["v261"])

#  When nothing else is found, find_ansys() falls back to the newest vXXX folder under Program Files\ANSYS Inc
@pytest.mark.skipif(os.name != "nt", reason="Default folder is hard-coded on Linux")
def test_default_folder_scan(tmp_path, monkeypatch, clean_discovery_env):  # A02
    _make_unified_install(tmp_path / "ANSYS INC", "261")
    latest = _make_unified_install(tmp_path / "ANSYS INC", "271")
    monkeypatch.setenv("PROGRAMFILES", str(tmp_path))
    assert load_api._find_latest_ansys_versions() is None
    assert misc.find_ansys() == str(latest)

# With no source at all, the low-level lookup returns None and get_ansys_path() raises a clear "Unable to locate any Ansys installation" error.
def test_nothing_found(monkeypatch, clean_discovery_env):  # A03
    assert load_api._find_latest_ansys_versions() is None
    monkeypatch.setattr(misc, "find_ansys", lambda: None)
    with pytest.raises(ValueError, match="Unable to locate any Ansys installation"):
        misc.get_ansys_path()


# ---------------------------------------------------------------------------------------------
# Wiring: every server type consumes the discovered path
# ---------------------------------------------------------------------------------------------


@pytest.mark.skipif(running_docker, reason="ansys_path is not resolved in Docker mode")
@pytest.mark.parametrize(
    "config",
    [
        AvailableServerConfigs.InProcessServer,
        AvailableServerConfigs.GrpcServer,
        AvailableServerConfigs.LegacyGrpcServer,
    ],
    ids=["W01-in-process", "W01-grpc", "W01-legacy-grpc"],
)
# start_local_server() passes the discovered path to the in-process, gRPC and legacy gRPC server types. These cases are skipped in Docker.
def test_start_local_server_passes_discovered_path(monkeypatch, config):
    received = {}

    class FakeServer:
        def __init__(self, ansys_path, *args, **kwargs):
            received["ansys_path"] = ansys_path

    monkeypatch.setattr(server, "get_ansys_path", lambda path=None: "discovered_install")
    monkeypatch.setattr(
        ServerFactory, "get_server_type_from_config", staticmethod(lambda *args: FakeServer)
    )
    server.start_local_server(config=config, as_global=False)
    assert received["ansys_path"] == "discovered_install"


def _capture_api_path(monkeypatch, received):
    monkeypatch.setattr(load_api, "_find_latest_ansys_versions", lambda: "discovered_install")

    def fake_api_path(ansys_path, is_posix):
        received["ansys_path"] = ansys_path
        return "api_folder"

    monkeypatch.setattr(load_api, "_get_api_path_from_installer_or_package", fake_api_path)

#  load_client_api() called without a path uses the discovery order to find the client library.
def test_load_client_api_uses_discovery(monkeypatch):  # W02
    received = {}
    _capture_api_path(monkeypatch, received)
    monkeypatch.setattr(load_api, "_try_load_api", lambda path, name: path)
    load_api.load_client_api()
    assert received["ansys_path"] == "discovered_install"

# The same check for load_grpc_client(), which loads the gRPC client library.
def test_load_grpc_client_uses_discovery(monkeypatch):  # W03
    received = {}
    _capture_api_path(monkeypatch, received)
    monkeypatch.setattr(load_api.utils, "data_processing_core_load_api", lambda path, api: None)
    load_api.load_grpc_client()
    assert received["ansys_path"] == "discovered_install"

