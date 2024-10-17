# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

"""Version for ansys-dpf-core"""

# Minimal DPF server version supported
min_server_version = "4.0"


class ServerToAnsysVersion:
    legacy_version_map = {
        "1.0": "2021R1",
        "2.0": "2021R2",
        "3.0": "2022R1",
        "4.0": "2022R2",
        "5.0": "2023R1",
        "6.0": "2023R2",
        "6.1": "2023R2",
        "6.2": "2023R2",
        "7.0": "2024R1",
        "7.1": "2024R1",
        "8.0": "2024R2",
        "8.1": "2024R2",
        "8.2": "2024R2",
        "9.0": "2025R1",
        "9.1": "2025R1",
        "10.0": "2025R2",
    }

    def __getitem__(self, item):
        if len(item) == 3:
            return self.legacy_version_map[item]
        else:
            split = item.split(".")
            return split[0] + "R" + split[1]


server_to_ansys_version = ServerToAnsysVersion()
