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

"""Provides classes for changelogs."""

from __future__ import annotations

from packaging.version import Version

import ansys.dpf.core as dpf
from ansys.dpf.core.check_version import version_requires


class Changelog:
    """Changelog of an operator.

    Requires DPF 11.0 (2026 R1) or above.

    Parameters
    ----------
    gdc:
        An optional GenericDataContainer to initialize the changelog with.
    server:
        The server to create the changelog on. Defaults to the current global server.
    """

    def __init__(self, gdc: dpf.GenericDataContainer = None, server=None):
        if gdc is None:
            gdc = dpf.GenericDataContainer(server=server)
            versions_sf = dpf.StringField(server=server)
            versions_sf.append(data=["0.0.0"], scopingid=1)
            changes_sf = dpf.StringField(server=server)
            changes_sf.append(data=["Initial version."], scopingid=1)
            gdc.set_property(property_name="versions", prop=versions_sf)
            gdc.set_property(property_name="changes", prop=changes_sf)
            gdc.set_property(property_name="class", prop="Changelog")
        self.gdc = gdc
        self._server = server

    def append(self, version: Version, changes: str):
        """Append a version and associated changes description to the changelog."""
        versions_sf: dpf.StringField = self.gdc.get_property(
            property_name="versions", output_type=dpf.StringField
        )
        new_id = versions_sf.scoping.size + 1
        versions_sf.append(data=[str(version)], scopingid=new_id)
        changes_sf: dpf.StringField = self.gdc.get_property(
            property_name="changes", output_type=dpf.StringField
        )
        changes_sf.append(data=[changes], scopingid=new_id)

    def patch_bump(self, changes: str) -> Changelog:
        """Bump the patch of the current version with associated changes description.

        Parameters
        ----------
        changes:
            Description of the changes associated to the patch bump.

        Returns
        -------
        changelog:
            Returns the current changelog to allow for chaining calls to bumps.
        """
        current_version = self.last_version
        new_version = Version(
            f"{current_version.major}.{current_version.minor}.{current_version.micro+1}"
        )
        self.append(version=new_version, changes=changes)
        return self

    def minor_bump(self, changes: str) -> Changelog:
        """Bump the minor of the current version with associated changes description.

        Parameters
        ----------
        changes:
            Description of the changes associated to the minor bump.

        Returns
        -------
        changelog:
            Returns the current changelog to allow for chaining calls to bumps.
        """
        current_version = self.last_version
        new_version = Version(f"{current_version.major}.{current_version.minor+1}.0")
        self.append(version=new_version, changes=changes)
        return self

    def major_bump(self, changes: str) -> Changelog:
        """Bump the major of the current version with associated changes description.

        Parameters
        ----------
        changes:
            Description of the changes associated to the major bump.

        Returns
        -------
        changelog:
            Returns the current changelog to allow for chaining calls to bumps.
        """
        current_version = self.last_version
        new_version = Version(f"{current_version.major+1}.0.0")
        self.append(version=new_version, changes=changes)
        return self

    def expect_version(self, version: Version | str) -> Changelog:
        """Check the current latest version of the changelog.

        Useful when chaining version bumps to check the resulting version is as expected.
        Adds readability to the specification of the operator.

        Parameters
        ----------
        version:
            Expected current latest version of the changelog.

        Returns
        -------
        changelog:
            Returns the current changelog to allow for chaining calls to bumps.
        """
        if isinstance(version, str):
            version = Version(version)
        if self.last_version != version:
            raise ValueError(
                f"Last version in the changelog ({self.last_version}) does not match expected version ({version})."
            )
        return self

    @property
    def last_version(self) -> Version:
        """Highest version in the changelog.

        Returns
        -------
        version:
            Highest version in the changelog.
        """
        return self.versions[-1]

    @property
    def versions(self) -> [Version]:
        """List of all versions for which the changelog stores descriptions."""
        versions_sf: dpf.StringField = self.gdc.get_property(
            property_name="versions", output_type=dpf.StringField
        )
        return [Version(version) for version in versions_sf.data_as_list]

    def __getitem__(self, item: Version) -> str:
        """Return changes description for a specific version in the changelog."""
        return self.changes_for_version(item)

    def changes_for_version(self, version: Version) -> str:
        """Return changes description for a specific version in the changelog."""
        versions_sf: dpf.StringField = self.gdc.get_property(
            property_name="versions", output_type=dpf.StringField
        )
        changes_sf: dpf.StringField = self.gdc.get_property(
            property_name="changes", output_type=dpf.StringField
        )
        versions_list = versions_sf.data_as_list
        for i in range(len(versions_sf.scoping.ids)):
            if Version(versions_list[i]) == version:
                return changes_sf.get_entity_data_by_id(versions_sf.scoping.ids[i])[0]
        raise ValueError(f"Changelog has no version '{version}'.")

    def __str__(self):
        """Create string representation of the changelog."""
        string = "Changelog:\n"
        string += "Version        Changes\n"
        string += "-------        -------\n"
        for version in self.versions:
            string += f"{str(version): <15}" + self[version].replace("\n", f"\n{'': >15}") + "\n"
        return string
