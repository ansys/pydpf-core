"""
.. _ref_scoping:

Scoping
=======
"""

import array
import sys

import numpy as np
from ansys.dpf.core.check_version import server_meet_version, version_requires
from ansys.dpf.core.common import _common_progress_bar, locations
from ansys.dpf.core import misc
from ansys.grpc.dpf import base_pb2, scoping_pb2, scoping_pb2_grpc
from ansys.dpf.core.cache import _setter

class ServerKnowingCtypes:
    def __init__(self, server):
        if server is None:
            self.use_ctypes = True
        else:
            ver = server.info.get("server_version")
            if ver == "4.0":
                self.use_ctypes = True
            else:
                self.use_ctypes = False
            self._server = server
            self._client = None
    
    def use_ctypes(self):
        return self.use_ctypes
    
    def get_client(self, api):
        if self._client is None:
            ip = self._server.ip
            port = self._server.port
            self._client = api.client_new(ip.encode('UTF-8'), str(port).encode('UTF-8'))
        return self._client

class Scoping:
    """Represents a scoping, which is a subset of a model support.

    Parameters
    ----------
    scoping : ansys.grpc.dpf.scoping_pb2.Scoping message, optional
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Attributes
    ----------
    ids : list of int
        List of IDs to include in the scoping.
    location : str
        Location of the IDs, such as ``"Nodal"`` or ``"Elemental"``.

    Examples
    --------
    Create a mesh scoping.

    >>> from ansys.dpf import core as dpf
    >>> # 1. using the mesh_scoping_factory
    >>> from ansys.dpf.core import mesh_scoping_factory
    >>> # a. scoping with elemental location that targets the elements with id 2, 7 and 11
    >>> my_elemental_scoping = mesh_scoping_factory.elemental_scoping([2, 7, 11])
    >>> # b. scoping with nodal location that targets the elements with id 4 and 6
    >>> my_nodal_scoping = mesh_scoping_factory.nodal_scoping([4, 6])
    >>> #2. using the classic API
    >>> my_scoping = dpf.Scoping()
    >>> my_scoping.location = "Nodal" #optional
    >>> my_scoping.ids = list(range(1,11))

    """

    def __init__(self, scoping=None, server=None, ids=None, location=None):
        """Initializes the scoping with an optional scoping message or
        by connecting to a stub.
        """
        self.internal_obj = None
        # different cases, if scoping is None or not
        if scoping is not None:
            self.internal_obj = scoping.internal_obj
            self.api_to_call = scoping.api_to_call
        else:
            # common to dpf_classes : call server
            self._ctypes_server = ServerKnowingCtypes(server)
            # common to dpf_classes : call the API
            use_ctypes = self._ctypes_server.use_ctypes
            if use_ctypes:
                from python_api.api import CTypesAPI
                self.api_to_call = CTypesAPI()
            else:
                from python_api.grpc_ctypes import GrpcAPI
                self.api_to_call = GrpcAPI()
                
            # common to dpf_classes : initialization of the scoping
            self.api_to_call._init_scoping(self, server)
            
            # different cases, if ids, if location ...
            if ids is not None:
                self.api_to_call.scoping_set_ids(self, self.internal_obj, ids, len(ids))
            if location is not None: 
                self.api_to_call.scoping_set_location(self, self.internal_obj, location)

    def _count(self):
        """
        Returns
        -------
        count : int
            Number of scoping IDs.
        """
        request = scoping_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.scoping.CopyFrom(self._message)
        return self._stub.Count(request).count

    def _get_location(self):
        """Retrieve the location of the IDs.

        Returns
        -------
        location : str
            Location of the IDs.
        """
        sloc = self._stub.GetLocation(self._message).loc.location
        return sloc

    def _set_location(self, loc=locations.nodal):
        """
        Parameters
        ----------
        loc : str or core.locations enum
            Location needed.

        """
        request = scoping_pb2.UpdateRequest()
        request.location.location = loc
        request.scoping.CopyFrom(self._message)
        self._stub.Update(request)

    # @version_requires("2.1") # !TO_REMOVE
    def _set_ids(self, ids):
        """
        Parameters
        ----------
        ids : list of int
            IDs to set.

        Notes
        -----
        Print a progress bar.
        """
        from python_api import utils
        self.api_to_call.scoping_set_ids(self, self.internal_obj, utils.list_to_int_array(ids), len(ids))

    def _get_ids(self, np_array=False):
        """
        Returns
        -------
        ids : list[int], numpy.array (if np_array==True)
            List of IDs.

        Notes
        -----
        Print a progress bar.
        """
        if server_meet_version("2.1", self._server):
            service = self._stub.List(self._message)
            dtype = np.int32
            return _data_get_chunk_(dtype, service, np_array)
        else:
            out = []

            service = self._stub.List(self._message)
            for chunk in service:
                out.extend(chunk.ids.rep_int)
            if np_array:
                return np.array(out, dtype=np.int32)
            else:
                return out

    def set_id(self, index, scopingid):
        """Set the ID of a scoping's index.

        Parameters
        ----------
        index : int
            Index of the scoping.
        scopingid : int
            ID of the scoping.
        """
        request = scoping_pb2.UpdateRequest()
        request.index_id.id = scopingid
        request.index_id.index = index
        request.scoping.CopyFrom(self._message)
        self._stub.Update(request)

    def _get_id(self, index):
        """Retrieve the index that the scoping ID is located on.

        Parameters
        ----------
        index : int
            Index of the scoping

        Returns
        -------
        id : int
            ID of the scoping's index.
        """
        return self.api_to_call.scoping_id_by_index(self, self.internal_obj, index)

    def _get_index(self, scopingid):
        """Retrieve an ID corresponding to an ID in the scoping.

        Parameters
        ----------
        id : int
            ID to retrieve.

        Returns
        -------
        index : int
            Index of the ID.
        """
        request = scoping_pb2.GetRequest()
        request.id = scopingid
        request.scoping.CopyFrom(self._message)
        return self._stub.Get(request).index

    def id(self, index: int):
        """Retrieve the ID at a given index.

        Parameters
        ----------
        index : int
            Index for the ID.

        Returns
        -------
        size : int

        """
        return self._get_id(index)

    def index(self, id: int):
        """Retrieve the index of a given ID.

        Parameters
        ----------
        id : int
            ID for the index to retrieve.

        Returns
        -------
        size : int

        """
        return self._get_index(id)

    @property
    def ids(self):
        """Retrieve a list of IDs in the scoping.

        Returns
        -------
        ids : list of int
            List of IDs to retrieve.

        Notes
        -----
        Print a progress bar.
        """
        return self._get_ids()

    @ids.setter
    def ids(self, value):
        self._set_ids(value)

    @property
    def location(self):
        """Location of the IDs as a string, such as ``"nodal"``, ``"elemental"``,
        and ``"time_freq"``.

        Returns
        -------
        location : str

        """
        return self._get_location()

    @location.setter
    def location(self, value):
        self._set_location(value)

    def _connect(self):
        """Connect to the gRPC service containing the reader."""
        return scoping_pb2_grpc.ScopingServiceStub(self._server.channel)

    def __len__(self):
        return self._count()

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __iter__(self):
        return self.ids.__iter__()

    def __getitem__(self, key):
        """Retrieve the ID at a requested index."""
        return self.id(key)

    def __setitem__(self, index, id):
        """Retrieve the ID at a requested index."""
        return self.set_id(index, id)

    @property
    def size(self):
        """Length of the list of IDs.

        Returns
        -------
        size : int

        """
        return self._count()

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

    def deep_copy(self, server=None):
        """Create a deep copy of the scoping's data on a given server.

        This method is useful for passiong data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        scoping_copy : Scoping
        """
        scop = Scoping(server=server)
        scop.ids = self.ids
        scop.location = self.location
        return scop

    def as_local_scoping(self):
        """Create a deep copy of the scoping that can be accessed and modified locally.

        This method allows you to access and modify the local copy of the scoping
        without sending a request to the server. It should be used in a ``with``
        statement so that the local field is released and the data is sent to
        the server in one action. If it is not used in a ``with`` statement,
        :func:`<release_data> Scoping.release_data()` should be used to update the scoping.

        Warning
        -------
        If this `as_local_scoping` method is not used as a context manager in a
        ``with`` statement or if the method `release_data()` is not called,
        the data will not be updated.

        Returns
        -------
        local_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities = 3
        >>> scoping_to_local = dpf.Scoping()
        >>> with scoping_to_local.as_local_scoping() as scoping:
        ...     for i in range(0,num_entities):
        ...         scoping[i] = i+1

        """  # noqa: E501
        return _LocalScoping(self)

class _LocalScoping(Scoping):
    """Caches the internal data of the scoping so that it can be modified locally.

    A single update request is sent to the server when the local scoping is deleted.

    Parameters
    ----------
    scoping : Scoping
        Scoping to copy locally.

    """

    def __init__(self, scoping):
        self._message = scoping._message
        self._server = scoping._server
        self._stub = scoping._stub
        self._owner_scoping = scoping
        self.__cache_data__()

    def __cache_data__(self):
        self._scoping_ids_copy = self._owner_scoping._get_ids(False)
        self._location = self._owner_scoping.location
        self.__init_map__()

    def __init_map__(self):
        self._mapper = dict(zip(self._scoping_ids_copy, np.arange(self._count())))

    def _count(self):
        """
        Returns
        -------
        count : int
            Number of scoping IDs.
        """
        return len(self._scoping_ids_copy)

    def _get_location(self):
        """Retrieve the location of the IDs.

        Returns
        -------
        location : str
            Location of the IDs.
        """
        return self._location

    @_setter
    def _set_location(self, loc=locations.nodal):
        """
        Parameters
        ----------
        loc : str or core.locations enum
            Location needed.

        """
        self._location = loc

    @_setter
    @version_requires("2.1")
    def _set_ids(self, ids):
        """
        Parameters
        ----------
        ids : list of int
            IDs to set.

        Notes
        -----
        Print a progress bar.
        """
        # must convert to a list for gRPC
        if isinstance(ids, range):
            ids = list(ids)
        elif isinstance(ids, (np.ndarray, np.generic)):
            ids = ids.tolist()

        self._scoping_ids_copy = ids
        self.__init_map__()

    def _get_ids(self, np_array=False):
        """
        Returns
        -------
        ids : list[int], numpy.array (if np_array==True)
            List of IDs.

        Notes
        -----
        Print a progress bar.
        """
        if np_array:
            return np.ndarray(self._scoping_ids_copy, dtype=np.int32)
        else:
            return self._scoping_ids_copy

    @_setter
    def set_id(self, index, scopingid):
        """Set the ID of a scoping's index.

        Parameters
        ----------
        index : int
            Index of the scoping.
        scopingid : int
            ID of the scoping.
        """
        init_size = self._count()
        if init_size <= index:
            for i in range(init_size, index+1):
                self._scoping_ids_copy.append(-1)
        self._scoping_ids_copy[index] = scopingid
        self._mapper[scopingid] = index

    @_setter
    def append(self, id):
        self._scoping_ids_copy.append(id)
        self._mapper[id] = len(self)-1

    def _get_id(self, index):
        """Retrieve the index that the scoping ID is located on.

        Parameters
        ----------
        index : int
            Index of the scoping

        Returns
        -------
        id : int
            ID of the scoping's index.
        """
        return self._scoping_ids_copy[index]

    def _get_index(self, scopingid):
        """Retrieve an ID corresponding to an ID in the scoping.

        Parameters
        ----------
        id : int
            ID to retrieve.

        Returns
        -------
        index : int
            Index of the ID.
        """
        return self._mapper[scopingid]

    def release_data(self):
        """Release the data."""
        if hasattr(self, "_is_set") and self._is_set:
            super()._set_ids(self._scoping_ids_copy)
            super()._set_location(self._location)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if tb is None:
            self._is_exited = True
            self.release_data()
        else:
            print(tb)

    def __del__(self):
        if not hasattr(self, "_is_exited") or not self._is_exited:
            self._is_exited = True
            self.release_data()
        pass


def _data_chunk_yielder(request, data, chunk_size=None):
    if not chunk_size:
        chunk_size = misc.DEFAULT_FILE_CHUNK_SIZE

    length = data.size
    need_progress_bar = length > 1e6
    if need_progress_bar:
        bar = _common_progress_bar(
            "Sending data...", unit=data.dtype.name, tot_size=length
        )
        bar.start()
    sent_length = 0
    if length == 0:
        yield request
        return
    unitary_size = int(chunk_size // sys.getsizeof(data[0]))
    if length - sent_length < unitary_size:
        unitary_size = length - sent_length
    while sent_length < length:
        currentcopy = data[sent_length: sent_length + unitary_size]
        request.array = currentcopy.tobytes()
        sent_length = sent_length + unitary_size
        if length - sent_length < unitary_size:
            unitary_size = length - sent_length
        yield request
        try:
            if need_progress_bar:
                bar.update(sent_length)
        except:
            pass
    try:
        if need_progress_bar:
            bar.finish()
    except:
        pass


def _data_get_chunk_(dtype, service, np_array=True):
    tupleMetaData = service.initial_metadata()

    need_progress_bar = False
    for iMeta in range(len(tupleMetaData)):
        if tupleMetaData[iMeta].key == "size_tot":
            size = int(tupleMetaData[iMeta].value)

    itemsize = np.dtype(dtype).itemsize
    need_progress_bar = size // itemsize > 1e6
    if need_progress_bar:
        bar = _common_progress_bar(
            "Receiving data...", unit=dtype.__name__ + "s", tot_size=size // itemsize
        )
        bar.start()

    if np_array:
        arr = np.empty(size // itemsize, dtype)
        i = 0
        for chunk in service:
            curr_size = len(chunk.array) // itemsize
            arr[i : i + curr_size] = np.frombuffer(chunk.array, dtype)
            i += curr_size
            try:
                if need_progress_bar:
                    bar.update(i)
            except:
                pass

    else:
        arr = []
        if dtype == np.float:
            dtype = "d"
        else:
            dtype = "i"
        for chunk in service:
            arr.extend(array.array(dtype, chunk.array))
            try:
                if need_progress_bar:
                    bar.update(len(arr))
            except:
                pass
    try:
        if need_progress_bar:
            bar.finish()
    except:
        pass
    return arr
