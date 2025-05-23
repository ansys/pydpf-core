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

"""Contains classes associated with the DPF collection."""

from __future__ import annotations

import abc
import traceback
from typing import TYPE_CHECKING, Generic, List, Optional, TypeVar
import warnings

import numpy as np

from ansys.dpf.core import server as server_module
from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core.label_space import LabelSpace
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.core.server_types import BaseServer
from ansys.dpf.gate import (
    collection_capi,
    collection_grpcapi,
    data_processing_capi,
    data_processing_grpcapi,
    dpf_array,
    dpf_vector,
)

if TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.core.support import Support

from ansys.dpf.gate.integral_types import MutableListInt32

TYPE = TypeVar("TYPE")


class CollectionBase(Generic[TYPE]):
    """Represents a collection of entries ordered by labels and IDs.

    Parameters
    ----------
    collection : ansys.grpc.dpf.collection_message_pb2.Collection, optional
        Collection to create from the collection message. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    """

    entries_type: Optional[type[TYPE]]  # type of the entries in the collection.

    def __init__(self, collection=None, server: BaseServer = None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            collection._server if isinstance(collection, CollectionBase) else server
        )

        # step2: if object exists, take the instance, else create it
        self._internal_obj = None
        if collection is not None:
            if isinstance(collection, CollectionBase):
                self._server = collection._server
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(collection)
            else:
                self._internal_obj = collection
        self.owned = False

    @property
    def _server(self):
        return self._server_instance

    @_server.setter
    def _server(self, value):
        self._server_instance = value
        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=collection_capi.CollectionCAPI,
            grpcapi=collection_grpcapi.CollectionGRPCAPI,
        )
        # step3: init environment
        self._api.init_collection_environment(self)  # creates stub when gRPC

    @property
    @version_requires("8.0")
    def name(self):
        """Name of the Collection.

        Notes
        -----
        Available starting with DPF 2024 R2 pre0.

        Returns
        -------
        str
        """
        out = self._api.collection_get_name(self)
        return out if out != "" else None

    @name.setter
    @version_requires("8.0")
    def name(self, name: str):
        """Set the name of the Collection.

        Notes
        -----
        Available starting with DPF 2024 R2 pre0.
        """
        self._api.collection_set_name(self, name=name)

    @abc.abstractmethod
    def create_subtype(self, obj_by_copy):
        """Must be implemented by subclasses."""
        pass

    @staticmethod
    def integral_collection(inpt, server: BaseServer = None):
        """Create a collection of integral type with a list.

        The collection of integral is the equivalent of an array of
        data sent server side. It can be used to efficiently stream
        large data to the server.

        Parameters
        ----------
        inpt : list[float], list[int], numpy.array
            list to transfer server side

        Returns
        -------
        IntegralCollection

        Notes
        -----
        Used by default by the ``'Operator'`` and the``'Workflow'`` when a
        list is connected or returned.

        """
        if isinstance(inpt, np.ndarray):
            inpt = inpt.flatten()
        if all(isinstance(x, (int, np.int32)) for x in inpt):
            return IntCollection(inpt, server=server)
        if all(isinstance(x, (float, np.float64)) for x in inpt):
            return FloatCollection(inpt, server=server)
        if all(isinstance(x, str) for x in inpt):
            return StringCollection(inpt, server=server)
        else:
            raise NotImplementedError(
                f"{IntegralCollection.__name__} is only "
                "implemented for int and float values "
                f"and not {type(inpt[0]).__name__}"
            )

    def set_labels(self, labels):
        """Set labels for scoping the collection.

        Parameters
        ----------
        labels : list[str], optional
            Labels to scope entries to. For example, ``["time", "complex"]``.

        """
        current_labels = self.labels
        if len(current_labels) != 0:
            print(
                "The collection already has labels :",
                current_labels,
                "deleting existing labels is not implemented yet.",
            )
            return
        for label in labels:
            self.add_label(label)

    def add_label(self, label, default_value=None):
        """Add the requested label to scope the collection.

        Parameters
        ----------
        label : str
            Labels to scope the entries to. For example, ``"time"``.

        default_value : int, optional
            Default value for existing fields in the collection. The default
            is ``None``.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> coll = dpf.FieldsContainer()
        >>> coll.add_label('time')

        """
        if default_value is not None:
            self._api.collection_add_label_with_default_value(self, label, default_value)
        else:
            self._api.collection_add_label(self, label)

    def _get_labels(self) -> list:
        """Retrieve labels scoping the collection.

        Returns
        -------
        labels: list[str]
            List of labels that entries are scoped to. For example, ``["time", "complex"]``.
        """
        num = self._api.collection_get_num_labels(self)
        out = []
        for i in range(0, num):
            out.append(self._api.collection_get_label(self, i))
        return out

    @property
    def labels(self) -> List[str]:
        """Provides for getting scoping labels as a property.

        Returns
        -------
        List[str]
            List of labels scoping the collection.
        """
        return self._get_labels()

    @labels.setter
    def labels(self, labels: List[str]):
        self.set_labels(labels=labels)

    def has_label(self, label) -> bool:
        """Check if a collection has a specified label.

        Parameters
        ----------
        label: str
            Label to search for. For example, ``"time"``.

        Returns
        -------
        bool
           ``True`` when successful, ``False`` when failed.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> coll = dpf.FieldsContainer()
        >>> coll.add_label('time')
        >>> coll.has_label('time')
        True

        >>> coll.has_label('complex')
        False

        """
        return label in self.labels

    def _get_entries(self, label_space_or_index):
        """Retrieve the entries at a requested label space or index.

        Parameters
        ----------
        label_space_or_index : dict[str,int]
            Label space or index. For example,
            ``{"time": 1, "complex": 0}`` or the index of the field.

        Returns
        -------
        entries : list[Scoping], list[Field], list[MeshedRegion]
            Entries corresponding to the request.
        """
        if isinstance(label_space_or_index, dict):
            client_label_space = LabelSpace(
                label_space=label_space_or_index, obj=self, server=self._server
            )
            num = self._api.collection_get_num_obj_for_label_space(self, client_label_space)
            out = []
            for i in range(0, num):
                out.append(
                    self.create_subtype(
                        self._api.collection_get_obj_by_index_for_label_space(
                            self, client_label_space, i
                        )
                    )
                )
            return out
        else:
            return self.create_subtype(
                self._api.collection_get_obj_by_index(self, label_space_or_index)
            )

    @version_requires("9.0")
    def get_entries_indices(self, label_space):
        """Retrieve the indices of the entries corresponding a requested label space .

        Notes
        -----
        Available starting with DPF 2025R1.

        Parameters
        ----------
        label_space : dict[str,int]
            Label space or index. For example,
            ``{"time": 1, "complex": 0}`` or the index of the field.

        Returns
        -------
        indices : list[int], list[Field], list[MeshedRegion]
            Indices of the entries corresponding to the request.
        """
        client_label_space = LabelSpace(label_space=label_space, obj=self, server=self._server)
        num = self._api.collection_get_num_obj_for_label_space(self, client_label_space)
        int_list = MutableListInt32(num)
        self._api.collection_fill_obj_indeces_for_label_space(self, client_label_space, int_list)
        return int_list.tolist()

    def _get_entry(self, label_space_or_index) -> TYPE:
        """Retrieve the entry at a requested label space or index.

        Parameters
        ----------
        label_space_or_index : dict[str,int]
            Label space or index of the requested entry. For example,
            ``{"time": 1, "complex": 0}`` or the index of the field.

        Returns
        -------
        entry : Scoping, Field, MeshedRegion
            Entry at the requested label space or index.
        """
        entries = self._get_entries(label_space_or_index)
        if isinstance(entries, list):
            if len(entries) == 1:
                return entries[0]
            elif len(entries) == 0:
                return None
            else:
                raise KeyError(f"{label_space_or_index} has {len(entries)} entries")
        else:
            return entries

    def get_label_space(self, index):
        """Retrieve the label space of an entry at a requested index.

        Parameters
        ----------
        index: int
            Index of the entry.

        Returns
        -------
        label_space : dict(str:int)
            Scoping of the requested entry. For example,
            ``{"time": 1, "complex": 0}``.
        """
        return LabelSpace(
            label_space=self._api.collection_get_obj_label_space_by_index(self, index),
            server=self._server,
        ).__dict__()

    def get_available_ids_for_label(self, label="time"):
        """Retrieve the IDs assigned to an input label.

        Parameters
        ----------
        label : str
            Name of the input label. The default is ``"time"``.

        Returns
        -------
        ids : list[int]
            List of IDs assigned to the input label.
        """
        return self.get_label_scoping(label)._get_ids(False)

    def get_label_scoping(self, label="time"):
        """Retrieve the scoping for an input label.

        This method allows you to retrieve a list of IDs for a given input label in the
        collection. For example, if the label ``el_type`` exists in the collection, you
        can use the `get_lable_scoping` method to retrieve a list of IDS with this label.
        You can then use these IDs to request a given entity inside the collection.

        Parameters
        ----------
        label: str
            Name of the input label.

        Returns
        -------
        scoping: Scoping
            IDs scoped to the input label.
        """
        scoping = Scoping(self._api.collection_get_label_scoping(self, label), server=self._server)
        return scoping

    def __getitem__(self, index):
        """Retrieve the entry at a requested index value.

        Parameters
        ----------
        index : int
            Index value.

        Returns
        -------
        entry : Field , Scoping
            Entry at the index value.
        """
        self_len = len(self)
        if index < 0:
            # convert to a positive index
            index = self_len + index

        if not self_len:
            raise IndexError("This collection contains no items.")
        if index >= self_len:
            word = "entry" if self_len == 1 else "entries"
            raise IndexError(f"This collection contains only {self_len} {word}.")

        return self._get_entries(index)

    @property
    def _data_processing_core_api(self):
        core_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        core_api.init_data_processing_environment(self)
        return core_api

    def _add_entry(self, label_space, entry):
        """Update or add an entry at a requested label space.

        Parameters
        ----------
        label_space : list[str,int]
            Label space of the requested fields. For example, ``{"time":1, "complex":0}``.
        entry : Field or Scoping
            DPF entry to add.
        """
        client_label_space = LabelSpace(label_space=label_space, obj=self, server=self._server)
        self._api.collection_add_entry(self, client_label_space, entry)

    def _get_time_freq_support(self):
        """Retrieve time frequency support.

        Returns
        -------
        time_freq_support : TimeFreqSupport
        """
        from ansys.dpf.core.time_freq_support import TimeFreqSupport
        from ansys.dpf.gate import (
            object_handler,
            support_capi,
            support_grpcapi,
        )

        data_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        internal_obj = None
        # LegacyGrpcServer throws UNAVAILABLE when retrieving nullptr
        # This is all to obtain a None instead of throwing
        import ansys.dpf.gate.errors as err

        try:
            internal_obj = self._api.collection_get_support(self, "time")
        except err.DPFServerException as e:
            str_to_ignore = "The collection does not have a support."
            if str_to_ignore not in str(e):
                raise e
        if not internal_obj:
            return None

        support = object_handler.ObjHandler(
            data_processing_api=data_api,
            internal_obj=internal_obj,
            server=self._server,
        )
        support_api = self._server.get_api_for_type(
            capi=support_capi.SupportCAPI, grpcapi=support_grpcapi.SupportGRPCAPI
        )

        time_freq = support_api.support_get_as_time_freq_support(support)
        res = TimeFreqSupport(time_freq_support=time_freq, server=self._server)
        return res

    def _set_time_freq_support(self, time_freq_support):
        """Set the time frequency support of the collection."""
        self._api.collection_set_support(self, "time", time_freq_support)

    @version_requires("5.0")
    def set_support(self, label: str, support: Support) -> None:
        """Set the support of the collection for a given label.

        Notes
        -----
        Available starting with DPF 2023 R1.

        """
        self._api.collection_set_support(self, label, support)

    @version_requires("5.0")
    def get_support(self, label: str) -> Support:
        """Get the support of the collection for a given label.

        Notes
        -----
        Available starting with DPF 2023 R1.

        """
        from ansys.dpf.core.support import Support

        return Support(support=self._api.collection_get_support(self, label), server=self._server)

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def __len__(self):
        """Retrieve the number of entries."""
        return self._api.collection_get_size(self)

    def __del__(self):
        """Delete the entry."""
        try:
            # delete
            if not self.owned:
                obj = self._deleter_func[1](self)
                if obj is not None:
                    self._deleter_func[0](obj)
        except:
            warnings.warn(traceback.format_exc())

    def _get_ownership(self):
        self.owned = True
        return self._internal_obj

    def __iter__(self):
        """Provide for looping through entry items."""
        for i in range(len(self)):
            yield self[i]


class IntegralCollection(CollectionBase):
    """Creates a collection of integral type with a list.

    The collection of integral is the equivalent of an array of
    data sent server side. It can be used to efficiently stream
    large data to the server.

    Parameters
    ----------
    list : list[float], list[int], numpy.array
        list to transfer server side

    Notes
    -----
    Used by default by the ``'Operator'`` and the``'Workflow'`` when a
    list is connected or returned.
    """

    def __init__(self, server=None, collection=None):
        super().__init__(server=server, collection=collection)

    @abc.abstractmethod
    def create_subtype(self, obj_by_copy):
        """Must be implemented by subclasses."""
        pass

    @abc.abstractmethod
    def _set_integral_entries(self, input):
        pass

    def get_integral_entries(self):
        """Must be implemented by subclasses."""
        pass


class IntCollection(CollectionBase[int]):
    """Creates a collection of integers with a list.

    The collection of integral is the equivalent of an array of
    data sent server side. It can be used to efficiently stream
    large data to the server.

    Parameters
    ----------
    list : list[int], numpy.array
        list to transfer server side

    Notes
    -----
    Used by default by the ``'Operator'`` and the``'Workflow'`` when a
    list is connected or returned.
    """

    entries_type = int

    def __init__(self, list=None, server=None, collection=None):
        super().__init__(server=server, collection=collection)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_int_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.collection_of_int_new()
        if list is not None:
            self._set_integral_entries(list)

    def create_subtype(self, obj_by_copy):
        """Create a sub type."""
        return int(obj_by_copy)

    def _set_integral_entries(self, input):
        dtype = np.int32
        if isinstance(input, range):
            input = np.array(list(input), dtype=dtype)
        elif not isinstance(input, (np.ndarray, np.generic)):
            input = np.array(input, dtype=dtype)
        else:
            input = np.array(list(input), dtype=dtype)

        self._api.collection_set_data_as_int(self, input, input.size)

    def get_integral_entries(self):
        """Get integral entries."""
        try:
            vec = dpf_vector.DPFVectorInt(owner=self)
            self._api.collection_get_data_as_int_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return dpf_array.DPFArray(vec)
        except NotImplementedError:
            return self._api.collection_get_data_as_int(self, 0)


class FloatCollection(CollectionBase[float]):
    """Creates a collection of floats (double64) with a list.

    The collection of integral is the equivalent of an array of
    data sent server side. It can be used to efficiently stream
    large data to the server.

    Parameters
    ----------
    list : list[float], numpy.array
        list to transfer server side

    Notes
    -----
    Used by default by the ``'Operator'`` and the``'Workflow'`` when a
    list is connected or returned.
    """

    entries_type = float

    def __init__(self, list=None, server=None, collection=None):
        super().__init__(server=server, collection=collection)
        self._sub_type = float
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_double_new_on_client(
                    self._server.client
                )
            else:
                self._internal_obj = self._api.collection_of_double_new()
        if list is not None:
            self._set_integral_entries(list)

    def create_subtype(self, obj_by_copy):
        """Create a sub type."""
        return float(obj_by_copy)

    def _set_integral_entries(self, input):
        dtype = np.float64
        if isinstance(input, range):
            input = np.array(list(input), dtype=dtype)
        elif not isinstance(input, (np.ndarray, np.generic)):
            input = np.array(input, dtype=dtype)
        else:
            input = np.array(list(input), dtype=dtype)

        self._api.collection_set_data_as_double(self, input, input.size)

    def get_integral_entries(self):
        """Get integral entries."""
        try:
            vec = dpf_vector.DPFVectorDouble(owner=self)
            self._api.collection_get_data_as_double_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return dpf_array.DPFArray(vec)
        except NotImplementedError:
            return self._api.collection_get_data_as_double(self, 0)


class StringCollection(CollectionBase[str]):
    """Creates a collection of strings with a list.

    The collection of integral is the equivalent of an array of
    data sent server side. It can be used to efficiently stream
    large data to the server.

    Parameters
    ----------
    list : list[float], numpy.array
        list to transfer server side

    Notes
    -----
    Used by default by the ``'Operator'`` and the``'Workflow'`` when a
    list is connected or returned.
    """

    entries_type = str

    def __init__(self, list=None, server=None, collection=None, local: bool = False):
        super().__init__(server=server, collection=collection)
        self._sub_type = str
        if self._internal_obj is None:
            if self._server.has_client():
                if local:
                    self._internal_obj = self._api.collection_of_string_new_local(
                        self._server.client
                    )
                else:
                    self._internal_obj = self._api.collection_of_string_new_on_client(
                        self._server.client
                    )
            else:
                self._internal_obj = self._api.collection_of_string_new()
        if list is not None:
            self._set_integral_entries(list)

    def create_subtype(self, obj_by_copy):
        """Create a sub type."""
        return str(obj_by_copy)

    def _set_integral_entries(self, input):
        for s in input:
            self._api.collection_add_string_entry(self, s)

    def get_integral_entries(self):
        """Get integral entries."""
        num = self._api.collection_get_size(self)
        out = []
        for i in range(num):
            out.append(self._api.collection_get_string_entry(self, i))
        return out
