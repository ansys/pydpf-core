# -*- coding: utf-8 -*-

"""
ScopingsContainer
=================
Contains classes associated to the DPF ScopingsContainer"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types


class ScopingsContainer(Collection):
    """A class used to represent a ScopingsContainer which contains
    scopings splitted on a given space

    Parameters
    ----------
    scopings_container : ansys.grpc.dpf.collection_pb2.Collection or ansys.dpf.core.ScopingsContainer, optional
        Create a scopings container from a Collection message or create a copy from an existing scopings container

    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    """

    def __init__(self, scopings_container=None, server=None):
        """Initialize the scoping with either optional scoping message,
        or by connecting to a stub.
        """
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()
        
        Collection.__init__(self, types.scoping,  
                            collection=scopings_container, server=self._server)

    def get_scopings(self, label_space_or_index):
        """Returns the scopings at a requested index or label space

        Parameters
        ----------
        label_space_or_index (optional) : dict(string:int) or int
            Scopings correponding to the filter (label space) in input, for example:
            ``{"elshape":1, "body":12}``
            or Index of the scoping.

        Returns
        -------
        scopings : list of scopings or scoping (if only one)
            scopings corresponding to the request
        """
        return super()._get_entries(label_space_or_index)

    def __getitem__(self, key):
        """Returns the scoping at a requested index

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
        label_space : dict(string:int)
            label_space of the requested scopings, ex : {"elshape":1, "body":12}

        scoping : Scoping
            DPF scoping to add.
        """
        return super()._add_entry(label_space, scoping)

    def __str__(self):
        txt = 'DPF Scopings Container with\n'
        txt += "\t%d scoping(s)\n" % len(self)
        txt += f"\tdefined on labels {self.labels} \n\n"
        return txt

    
