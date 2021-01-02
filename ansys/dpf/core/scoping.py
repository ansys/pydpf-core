from ansys import dpf
from ansys.grpc.dpf import scoping_pb2, scoping_pb2_grpc, base_pb2
from ansys.dpf.core.common import locations


class Scoping:
    """A class used to represent a Scoping which is a subset of a
    model support.

    Parameters
    ----------
    scoping : ansys.grpc.dpf.scoping_pb2.Scoping message, optional

    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.

    Attributes
    ----------
    ids : list of int

    location : str
        Location of the ids.  For example ``"Nodal"`` or ``"Elemental"``.
    """

    def __init__(self, scoping=None, channel=None):
        """Initialize the scoping with either optional scoping message, or
        by connecting to a stub.
        """
        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        self._stub = self._connect()

        if scoping is None:
            request = base_pb2.Empty()
            self._message = self._stub.Create(request)
        else:
            self._message = scoping

    def _count(self):
        """
        Returns
        -------
        count : int
            The number of scoping ids
        """
        request = scoping_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.scoping.CopyFrom(self._message)
        return self._stub.Count(request).count

    def _get_location(self):
        """
        Returns
        -------
        location : str
            location of the ids
        """
        sloc = self._stub.GetLocation(self._message).loc.location
        return sloc

    def _set_location(self, loc=locations.nodal):
        """
        Parameters
        ----------
        loc : str or core.locations enum
            The location needed

        """
        request = scoping_pb2.UpdateRequest()
        request.location.location = loc
        request.scoping.CopyFrom(self._message)
        self._stub.Update(request)

    def _set_ids(self, ids):
        """
        Parameters
        ----------
        ids : list of int
            The ids to set
        """
        # must convert to a list for gRPC
        if isinstance(ids, range):
            ids = list(ids)

        request = scoping_pb2.UpdateRequest()
        request.ids.ids.rep_int.extend(ids)
        request.scoping.CopyFrom(self._message)
        self._stub.Update(request)

    def _get_ids(self):
        """
        Returns
        -------
        ids : list[int]
            List of ids.
        """
        service = self._stub.List(self._message)

        # Get total size, removed as it's unnecessary since Python has
        # to create a list from the ids
        #
        # tupleMetaData = service.initial_metadata()
        # for iMeta in range(len(tupleMetaData)):
        #     if (tupleMetaData[iMeta].key == 'size_tot'):
        #         totsize = int(tupleMetaData[iMeta].value)

        out = []
        for chunk in service:
            out.extend(chunk.ids.rep_int)
        return out


    def set_id(self, index, scopingid):
        """Set the id of an index of the scoping

        Parameters
        ----------
        index : int
        id : int
        """
        request = scoping_pb2.UpdateRequest()
        request.index_id.id = scopingid
        request.index_id.index = index
        request.scoping.CopyFrom(self._message)
        self._stub.Update(request)

    def _get_id(self, index):
        """Returns on which index is located an id in the scoping

        Parameters
        ----------
        index : int

        Returns
        -------
        id : int
        """
        request = scoping_pb2.GetRequest()
        request.index = index
        request.scoping.CopyFrom(self._message)
        return self._stub.Get(request).id

    def _get_index(self, scopingid):
        """Returns on which id is corresponding to an id in the
        scoping.

        Parameters
        ----------
        id : int

        Returns
        -------
        index : int
        """
        request = scoping_pb2.GetRequest()
        request.id = scopingid
        request.scoping.CopyFrom(self._message)
        return self._stub.Get(request).index

    def id(self, index):
        return self._get_id(index)

    def index(self, id):
        return self._get_index(id)

    @property
    def ids(self):
        return self._get_ids()

    @ids.setter
    def ids(self, value):
        self._set_ids(value)

    @property
    def location(self):
        """The location of the ids as a string (e.g. nodal, elemental,
        time_freq, etc...)"""
        return self._get_location()

    @location.setter
    def location(self, value):
        self._set_location(value)

    def _connect(self):
        """Connect to the grpc service containing the reader"""
        return scoping_pb2_grpc.ScopingServiceStub(self._channel)

    def __len__(self):
        return self._count()

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __getitem__(self, key):
        """Returns the id at a requested index"""
        return self.id(key)

    @property
    def size(self):
        return self._count()

    def __str__(self):
        txt = 'DPF Scoping Object\n'
        txt += f'Size: {self.size}\n'
        txt += f'Location: {self.location}\n'
        return txt
