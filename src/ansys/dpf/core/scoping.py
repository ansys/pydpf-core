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

"""Scoping."""

from __future__ import annotations

import ctypes
import traceback
from typing import TYPE_CHECKING, Union
import warnings

import numpy as np

from ansys.dpf.core import server as server_module, server_types
from ansys.dpf.core.cache import _setter
from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core.common import locations
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
    dpf_vector,
    dpf_vector_abstract_api,
    dpf_vector_capi,
    scoping_capi,
    scoping_grpcapi,
    utils,
)
from ansys.dpf.gate.dpf_array import DPFArray

if TYPE_CHECKING:  # pragma: nocover
    from ctypes import c_void_p as ScopingPointer

    from numpy import typing as np_typing

    from ansys.dpf.core.server_types import AnyServerType
    import ansys.grpc.dpf.scoping_pb2.Scoping as ScopingMessage

    IdVectorType = Union[list[int], range, np_typing.NDArray[np.int32]]


class Scoping:
    """Represents a scoping, which is a subset of a model support.

    Parameters
    ----------
    scoping:
        gRPC message or pointer for an existing scoping on the server.
    server:
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    ids:
        List of entity IDs.
    location:
        Location for this scoping. Defines the type of entities the IDs correspond to.
        For example, if location is :py:attr:`locations.nodal`,
        then the scoping is a list of node IDs.

    Examples
    --------
    Create a scoping for mesh entities.

    >>> from ansys.dpf import core as dpf
    >>> # 1. using the mesh_scoping_factory
    >>> from ansys.dpf.core import mesh_scoping_factory
    >>> # a. scoping with elemental location that targets the elements with id 2, 7 and 11
    >>> my_elemental_scoping = mesh_scoping_factory.elemental_scoping([2, 7, 11])
    >>> # b. scoping with nodal location that targets the elements with id 4 to 6
    >>> my_nodal_scoping = mesh_scoping_factory.nodal_scoping(range(4, 7))
    >>> #2. using the Scoping class directly
    >>> # a. scoping with elemental location that targets the elements with id 2, 7 and 11
    >>> my_elemental_scoping = dpf.Scoping(location=dpf.locations.elemental, ids=[2, 7, 11])
    >>> # b. scoping with nodal  location that targets the elements with id 4 to 6
    >>> my_nodal_scoping = dpf.Scoping(ids=range(4, 7))
    >>> # 3. create a time_freq scoping that targets the second load step
    >>> from ansys.dpf.core import time_freq_scoping_factory
    >>> # a. using the time_freq_scoping_factory
    >>> my_load_step_scoping = time_freq_scoping_factory.scoping_by_load_step(2)
    >>> # b. using the Scoping class directly
    >>> my_load_step_scoping = dpf.Scoping(location=dpf.locations.time_freq_step, ids=[2])

    """

    def __init__(
        self,
        scoping: Union[ScopingMessage, ScopingPointer] = None,
        server: AnyServerType = None,
        ids: IdVectorType = None,
        location: locations = None,
    ):
        """Initialize the scoping with an optional scoping message or by connecting to a stub."""
        # step 1: get server
        self._server = server_module.get_or_create_server(
            scoping._server if isinstance(scoping, Scoping) else server
        )

        self._api = self._server.get_api_for_type(
            capi=scoping_capi.ScopingCAPI, grpcapi=scoping_grpcapi.ScopingGRPCAPI
        )
        # step3: init environment
        self._api.init_scoping_environment(self)  # creates stub when gRPC

        # step2: if object exists, take the instance, else create it
        if scoping is not None:
            if isinstance(scoping, Scoping):
                self._server = scoping._server
                self._api = self._server.get_api_for_type(
                    capi=scoping_capi.ScopingCAPI,
                    grpcapi=scoping_grpcapi.ScopingGRPCAPI,
                )
                # step3: init environment
                self._api.init_scoping_environment(self)  # creates stub when gRPC
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(scoping)
            else:
                # scoping is of type protobuf.message or DPFObject*
                self._internal_obj = scoping
        else:
            if self._server.has_client():
                self._internal_obj = self._api.scoping_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.scoping_new()

        # step5: handle specific calls to set attributes
        if ids is not None:
            self.ids = ids
        if location is not None:
            self.location = location

    def _count(self):
        """Return the number of scoping ids.

        Returns
        -------
        count : int
            Number of scoping IDs.
        """
        return self._api.scoping_get_size(self)

    def _get_location(self):
        """Retrieve the location of the IDs.

        Returns
        -------
        location : str
            Location of the IDs.
        """
        return self._api.scoping_get_location(self)

    def _set_location(self, loc=locations.nodal):
        """Set the location.

        Parameters
        ----------
        loc : str or core.locations enum
            Location needed.

        """
        self._api.scoping_set_location(self, loc)

    @version_requires("2.1")
    def _set_ids(self, ids: IdVectorType):
        """Set the ids.

        Scoping IDs are stored as int32.
        Converts automatically int64 Numpy arrays to int32.

        Parameters
        ----------
        ids:
            Entity IDs to set.

        """
        if isinstance(ids, range):
            ids = list(ids)
        if isinstance(ids, np.ndarray):
            if ids.dtype == np.int64:
                ids = ids.astype(np.int32)
            if ids.dtype != np.int32:
                raise ValueError(
                    f"Accepted dtypes for NumPy arrays when setting scoping IDs are "
                    f"'np.int32' and np.int64' (provided is '{ids.dtype}')."
                )
        if isinstance(self._server, server_types.InProcessServer):
            self._api.scoping_resize(self, len(ids))
            ids_ptr = self._api.scoping_get_ids(self, len(ids))
            ctypes.memmove(
                ids_ptr,
                utils.to_int32_ptr(ids),
                len(ids) * ctypes.sizeof(ctypes.c_int32()),
            )
        else:
            self._api.scoping_set_ids(self, ids, len(ids))

    def _get_ids(self, np_array=None):
        """Return an array of scoping ids.

        Returns
        -------
        ids : list[int], numpy.array (if np_array==True)
            Array of IDs.

        np_array: bool, optional

        Notes
        -----
        Print a progress bar.
        """
        if np_array == None:
            from ansys.dpf.core import settings

            np_array = settings.get_runtime_client_config(self._server).return_arrays
        try:
            vec = dpf_vector.DPFVectorInt(owner=self)
            self._api.scoping_get_ids_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return DPFArray(vec) if np_array else vec.np_array.tolist()

        except NotImplementedError:
            return self._api.scoping_get_ids(self, np_array)

    def get_ids(self, np_array: bool = False) -> Union[list[int], DPFArray]:
        """Return the list of entity IDs in the scoping as a list or as a numpy.ndarray.

        Parameters
        ----------
        np_array:
            Whether to return the list of IDs as a numpy array.

        Returns
        -------
        ids:
            List of entity IDs in the scoping.

        """
        return self._get_ids(np_array=np_array)

    def set_id(self, index: int, scopingid: int):
        """Set the ID of the entity at index in the scoping.

        Parameters
        ----------
        index:
            Index in the scoping.
        scopingid:
            ID of the entity.
        """
        self._api.scoping_set_entity(self, scopingid, index)

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
        return self._api.scoping_id_by_index(self, index)

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
        return self._api.scoping_index_by_id(self, scopingid)

    def id(self, index: int) -> int:
        """Retrieve the entity ID at a given index.

        Parameters
        ----------
        index:
            Index of the entity in the scoping.

        Returns
        -------
        entity_id:
            ID of the entity at index in the scoping.

        """
        return self._get_id(index)

    def index(self, id: int) -> int:
        """Retrieve the index for a given entity ID.

        Parameters
        ----------
        id:
            Entity ID at the index in the scoping.

        Returns
        -------
        index:
            Index in the scoping for the entity ID.

        """
        return self._get_index(id)

    @property
    def ids(self) -> Union[DPFArray, list[int]]:
        """Retrieve the entity IDs in the scoping.

        Returns
        -------
        ids:
            List of IDs in the scoping.
            By default, a mutable DPFArray is returned.
            To change the return type to a list for the complete python session, see
            :func:`ansys.dpf.core.settings.get_runtime_client_config` and
            :func:`ansys.dpf.core.runtime_config.RuntimeClientConfig.return_arrays`.
            To get the list of IDs from a scoping as a Python list without changing a default
            configuration, use :func:`ansys.dpf.core.scoping.Scoping.get_ids` instead.

        """
        return self._get_ids()

    @ids.setter
    def ids(self, value: IdVectorType):
        self._set_ids(value)

    @property
    def location(self) -> str:
        """Location of the scoping as a string.

        This defines the type of entity the IDs correspond to (such as node ID, element ID, face ID, and so on).

        Returns
        -------
        location:
            The location of the scoping.
            One of the values of :class:`~ansys.dpf.core.common.locations`.

        """
        return self._get_location()

    @location.setter
    def location(self, value: locations):
        self._set_location(value)

    def __len__(self):
        """
        Return the number of scoping ids.

        Returns
        -------
        int
            The number of scoping ids.
        """
        return self._count()

    def __del__(self):
        """
        Clean up resources associated with the instance.

        This method calls the deleter function to release resources. If an exception
        occurs during deletion, a warning is issued.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except Exception as e:
            print(str(e.args), str(self._deleter_func[0]))
            warnings.warn(traceback.format_exc())

    def __iter__(self):
        """Return an iterator over the scoping ids."""
        return self.ids.__iter__()

    def __getitem__(self, key):
        """Retrieve the ID at a requested index."""
        return self.id(key)

    def __setitem__(self, index, id):
        """Set the ID at a given index."""
        return self.set_id(index, id)

    @property
    def size(self) -> int:
        """Length of the list of IDs.

        Returns
        -------
        size:
            Size of the scoping.

        """
        return self._count()

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

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
        super(_LocalScoping, self).__init__(scoping=scoping)
        self.__cache_data__(scoping)

    def __cache_data__(self, owner_scoping):
        self._scoping_ids_copy = owner_scoping._get_ids(False)
        self._location = owner_scoping.location
        self.__init_map__()

    def __init_map__(self):
        self._mapper = dict(zip(self._scoping_ids_copy, np.arange(self._count())))

    def _count(self):
        """Return the number of scoping ids.

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
        """Set the location.

        Parameters
        ----------
        loc : str or core.locations enum
            Location needed.

        """
        self._location = loc

    @_setter
    @version_requires("2.1")
    def _set_ids(self, ids):
        """Set scoping ids.

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
        """Return the scoping ids.

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
            for i in range(init_size, index + 1):
                self._scoping_ids_copy.append(-1)
        self._scoping_ids_copy[index] = scopingid
        self._mapper[scopingid] = index

    @_setter
    def append(self, id):
        self._scoping_ids_copy.append(id)
        self._mapper[id] = len(self) - 1

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
        super(_LocalScoping, self).__del__()
        pass
