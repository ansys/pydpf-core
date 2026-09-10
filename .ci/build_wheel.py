# This script generates the different versions of the ansys-dpf-core wheels based on a given input.
# Input can be one of ["any", "win", "manylinux1", "manylinux_2_17"]
#
# It also defines a Hatchling build hook for platform-dependent selection/exclusion of relevant
# binaries whenever wheels are built. To provide a mechanism for generating manylinux1
# wheels (same OS as manylinux_2_17, hence, can not be inferred), the target platform is read
# from the ANSYS_DPF_WHEEL_PLATFORM environment variable by the build hook. This mechanism also
# allows generating "any" wheels on a non-macOS hosts.

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

_ANY = "any"

_PLATFORM_TAGS = {
    "win": "win_amd64",
    "manylinux1": "manylinux1_x86_64",
    "manylinux_2_17": "manylinux_2_17_x86_64",
    _ANY: _ANY,
}

_GATEBIN_DIR = "src/ansys/dpf/gatebin"

_GATEBIN_BINARIES = {
    "win": ["Ans.Dpf.GrpcClient.dll", "DPFClientAPI.dll"],
    "manylinux1": ["libAns.Dpf.GrpcClient.so", "libDPFClientAPI.so"],
    "manylinux_2_17": ["libAns.Dpf.GrpcClient.so", "libDPFClientAPI.so"],
}

# Accommodate tox.ini automatic platform substitutions on the CLI.
_CLI_PLATFORM_ALIASES = {
    "linux": "manylinux_2_17",
    "win32": "win",
    "darwin": _ANY,
}


def _detect_default_platform() -> str:
    """Infer the target platform from the host OS."""
    if sys.platform == "win32":
        return "win"
    if sys.platform == "darwin":
        return _ANY
    return "manylinux_2_17"


class DPFWheelBuildHook(BuildHookInterface):
    """Include only the gatebin binaries matching the requested target platform."""

    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        requested = os.environ.get("ANSYS_DPF_WHEEL_PLATFORM") or _detect_default_platform()
        if requested not in _PLATFORM_TAGS:
            raise ValueError(
                f"Unsupported ANSYS_DPF_WHEEL_PLATFORM={requested!r}. "
                f"Supported values are: {sorted(_PLATFORM_TAGS)}"
            )

        if requested == _ANY:
            # Pure wheel, no platform-specific binaries: the defaults (pure_python=True) already
            # produce the "py3-none-any" tag.
            return

        build_data["pure_python"] = False
        build_data["tag"] = f"py3-none-{_PLATFORM_TAGS[requested]}"

        for binary_name in _GATEBIN_BINARIES[requested]:
            source = f"{_GATEBIN_DIR}/{binary_name}"
            build_data["force_include"][source] = f"ansys/dpf/gatebin/{binary_name}"


def main() -> None:
    supported_platforms = {**{p: p for p in _PLATFORM_TAGS}, **_CLI_PLATFORM_ALIASES}

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--platform", help="platform")
    parser.add_argument("-w", "--wheelhouse", action="store_true", help="build via `pip wheel`")
    args = parser.parse_args()

    if args.platform is not None:
        if args.platform not in supported_platforms:
            raise ValueError(
                f"Platform {args.platform} is not supported. "
                f"Supported platforms are: {list(supported_platforms)}"
            )
        os.environ["ANSYS_DPF_WHEEL_PLATFORM"] = supported_platforms[args.platform]

    if not args.wheelhouse:
        cmd = [sys.executable, "-m", "build", "--wheel"]
    else:
        cmd = [sys.executable, "-m", "pip", "wheel", "-w", "dist", "."]

    subprocess.run(cmd, capture_output=False, text=True, check=True)
    print("Done building the wheel.")


if __name__ == "__main__":
    main()
