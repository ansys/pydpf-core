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

# -*- coding: utf-8 -*-

"""
ScopingsContainer.

Contains classes associated to the DPF ScopingsContainer
"""

from ansys.dpf.core import scoping
from ansys.dpf.core.collection_base import CollectionBase


class ScopingsContainer(CollectionBase[scoping.Scoping]):
    """A class used to represent a ScopingsContainer which contains scopings split on a given space.

    Parameters
    ----------
    scopings_container : ansys.grpc.dpf.collection_message_pb2.Collection or
                         ansys.dpf.core.ScopingsContainer, optional
        Create a scopings container from a Collection message or create
        a copy from an existing scopings container

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    """

    entries_type = scoping.Scoping

    def __init__(self, scopings_container=None, server=None):
        super().__init__(collection=scopings_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_scoping_new_on_client(
                    self._server.client
                )
            else:
                self._internal_obj = self._api.collection_of_scoping_new()

    def create_subtype(self, obj_by_copy):
        """Create a Scoping subtype."""
        return scoping.Scoping(scoping=obj_by_copy, server=self._server)

    def get_scopings(self, label_space):
        """Return the scopings at a requested label space.

        Parameters
        ----------
        label_space_or_index : dict[str,int] , int
            Scopings corresponding to the filter (label space) in input, for example:
            ``{"elshape":1, "body":12}``

        Returns
        -------
        scopings : list[Scoping]
            scopings corresponding to the request
        """
        return super()._get_entries(label_space)

    def get_scoping(self, label_space_or_index):
        """Return the scoping at a requested index or label space.

        Throws if the request returns several scoping

        Parameters
        ----------
        label_space_or_index : dict[str,int] , int
            Scopings corresponding to the filter (label space) in input, for example:
            ``{"elshape":1, "body":12}``
            or Index of the scoping.

        Returns
        -------
        scopings : Scoping
            scoping corresponding to the request
        """
        return super()._get_entry(label_space_or_index)

    def __getitem__(self, key):
        """Return the scoping at a requested index.

        Parameters
        ----------
        key : int
            the index

        Returns
        -------
        scoping : Scoping
            scoping corresponding to the request
        """
        return super().__getitem__(key)

    def add_scoping(self, label_space, scoping):
        """Update or add the scoping at a requested label space.

        Parameters
        ----------
        label_space : dict[str,int]
            label_space of the requested scopings, ex : {"elshape":1, "body":12}

        scoping : Scoping
            DPF scoping to add.
        """
        return super()._add_entry(label_space, scoping)
