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

"""Version for ansys-dpf-core."""

from packaging.version import parse as parse_version

# Minimal DPF server version supported
min_server_version = "4.0"


class ServerToAnsysVersion:
    def __getitem__(self, item):
        version = parse_version(item)
        # The current DPF versioning scheme is MAJOR.MINOR.PATCH
        # Compute release version equivalent (YEAR+'R'+REVISION)
        # The revision is 'R1' for any odd major DPF version, 'R2' for even major versions.
        ansys_revision = 2 - version.major % 2
        # The year is 2021 for DPF 1.0, and bumped every two releases.
        ansys_year = 2020 + version.major // 2 + version.major % 2
        # Return the corresponding Ansys release
        return f"{ansys_year}R{ansys_revision}"


server_to_ansys_version = ServerToAnsysVersion()
