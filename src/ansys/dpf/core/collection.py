# -*- coding: utf-8 -*-
"""
Collection
===============
"""
from __future__ import annotations
from ansys.dpf.core.any import Any
from ansys.dpf.core.collection_base import CollectionBase, TYPE
from ansys.dpf.core.common import create_dpf_instance
from ansys.dpf.core import server as server_module, errors


class Collection(CollectionBase[TYPE]):
    """Represents a collection of dpf objects organised by label spaces.

    Parameters
    ----------
    collection : ansys.grpc.dpf.collection_pb2.Collection or
                ansys.dpf.core.Collection, optional
        Create a collection from a collection message or create a copy from an
        existing collection. The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    entries_type: type
        Type of the entries in the collection.

    Notes
    -----
    Class available with server's version starting at 8.1 (Ansys 2024 R2 pre1).
    """

    def __init__(self, collection=None, server=None, entries_type: type = None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            collection._server if isinstance(collection, Collection) else server
        )
        if not self._server.meet_version("8.1"):
            raise errors.DpfVersionNotSupported("8.1")

        super().__init__(collection=collection, server=server)
        if entries_type is not None:
            self.entries_type = entries_type
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_any_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.collection_of_any_new()

    def create_subtype(self, obj_by_copy):
        return create_dpf_instance(Any, obj_by_copy, self._server).cast(self.entries_type)

    def get_entries(self, label_space):
        """Retrieve the entries at a label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Entries corresponding to a filter (label space) in the input. For example:
            ``{"elshape":1, "body":12}``

        Returns
        -------
        entries : list[self.type]
            Entries corresponding to the request.
        """
        return super()._get_entries(label_space)

    def get_entry(self, label_space_or_index) -> TYPE:
        """Retrieve the entry at a requested index or label space.

        Raises an exception if the request returns more than one entry.

        Parameters
        ----------
        label_space_or_index : dict[str,int] , int
            Scoping of the requested entry, such as ``{"time": 1, "complex": 0}``
            or the index of the mesh.

        Returns
        -------
        entry : self.type
            Entry corresponding to the request.
        """
        return super()._get_entry(label_space_or_index)

    def add_entry(self, label_space, entry):
        """Add or update the entry at a requested label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Label space of the requested meshes. For example, {"elshape":1, "body":12}.

        entry : self.type
            DPF entry to add or update.
        """
        return super()._add_entry(label_space, Any.new_from(entry, server=self._server))


def CollectionFactory(subtype, BaseClass=Collection):
    """Creates classes deriving from Collection at runtime for a given subtype."""
    def __init__(self, **kwargs):
        BaseClass.__init__(self, **kwargs)

    new_class = type(str(subtype.__name__) + "sCollection", (BaseClass,), {"__init__": __init__, "entries_type": subtype})
    return new_class
