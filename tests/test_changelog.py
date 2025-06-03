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
import pytest

from ansys.dpf.core.changelog import Changelog
import conftest


@conftest.raises_for_servers_version_under("11.0")
def test_changelog_new(server_type):
    from packaging.version import Version

    changelog = Changelog(server=server_type)
    assert changelog.last_version == Version("0.0.0")
    assert changelog[changelog.last_version] == "Initial version."


@conftest.raises_for_servers_version_under("11.0")
def test_changelog_updates(server_type):
    from packaging.version import Version

    changelog = Changelog(server=server_type)
    changelog.major_bump("Major bump").minor_bump("Minor bump").patch_bump("Patch \nbump")
    with pytest.raises(ValueError):
        changelog.expect_version(Version("0.0.0"))
    changelog.expect_version(Version("1.1.1"))
    assert changelog[changelog.last_version] == "Patch \nbump"
    changelog.patch_bump("Patch 2")
    assert (
        str(changelog)
        == """Changelog:
Version        Changes
-------        -------
0.0.0          Initial version.
1.0.0          Major bump
1.1.0          Minor bump
1.1.1          Patch 
               bump
1.1.2          Patch 2
"""
    )
    assert len(changelog) == 5
    assert changelog[0] == (Version("0.0.0"), "Initial version.")
    assert changelog[-1] == (Version("1.1.2"), "Patch 2")
    for i, v in enumerate(changelog):
        if i == 2:
            assert v == (Version("1.1.0"), "Minor bump")
    with pytest.raises(IndexError):
        _ = changelog[8]
    assert Version("0.0.0") in changelog
    assert Version("1.5.2") not in changelog
