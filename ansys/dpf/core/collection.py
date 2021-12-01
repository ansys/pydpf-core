"""
Collection
===========
Contains classes associated with the DPF collection.

"""
import numpy as np
from ansys import dpf
from ansys.grpc.dpf import collection_pb2, collection_pb2_grpc
from ansys.dpf.core.core import base_pb2
from ansys.dpf.core.common import types
from ansys.dpf.core.scoping import Scoping, scoping_pb2
from ansys.dpf.core.field import Field, field_pb2
from ansys.dpf.core.meshed_region import MeshedRegion, meshed_region_pb2
from ansys.dpf.core.time_freq_support import TimeFreqSupport
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core import server
from ansys.dpf.core import scoping


class Collection:
    """Represents a collection of entries ordered by labels and IDs.

    Parameters
    ----------
    dpf_type :

    collection : ansys.grpc.dpf.collection_pb2.Collection, optional
        Collection to create from the collection message. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> coll = dpf.Collection(dpf.types.field)

    """

    def __init__(self, dpf_type=None, collection=None, server: server.DpfServer=None):
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()
        self._type = dpf_type
        # self.__info = None  # cached info

        if collection is None:
            request = collection_pb2.CollectionRequest()
            if hasattr(dpf_type, "name"):
                stype = dpf_type.name
            else:
                stype = dpf_type
            request.type = base_pb2.Type.Value(stype.upper())
            self._message = self._stub.Create(request)
        elif hasattr(collection, "_message"):
            self._message = collection._message
            self._collection = collection  # keep the base collection used for copy

        else:
            self._message = collection

        if self._type == None:
            self._type = types(int(self._message.type) + 1)

    @staticmethod
    def integral_collection(inpt, server: server.DpfServer = None):
        """Creates a collection of integral type with a list.
        The collection of integral is the equivalent of an array of
        data sent server side. It can be used to efficiently stream
        large data to the server.

        Notes
        -----
        Used by default by the ``'Operator'`` and the``'Workflow'`` when a
        list is connected or returned.

        Parameters
        ----------
        inpt : list[float], list[int], numpy.array
            list to transfert server side

        Returns
        -------
        Collection

        """
        if all(isinstance(x, int) for x in inpt):
            dpf_type = types.int
        elif all(isinstance(x, float) for x in inpt):
            dpf_type = types.double
        out = Collection(dpf_type=dpf_type, server=server)
        out._set_integral_entries(inpt)
        return out

    def set_labels(self, labels):
        """Set labels for scoping the collection.

        Parameters
        ----------
        labels : list[str], optional
            Labels to scope entries to. For example, ``["time", "complex"]``.

        """
        if len(self._info["labels"]) != 0:
            print(
                "The collection already has labels :",
                self._info["labels"],
                "deleting existing labels is not implemented yet.",
            )
            return
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(self._message)
        request.labels.extend([collection_pb2.NewLabel(label=lab) for lab in labels])
        self._stub.UpdateLabels(request)

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
        >>> coll = dpf.Collection(dpf.types.field)
        >>> coll.add_label('time')

        """
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(self._message)
        new_label = collection_pb2.NewLabel(label=label)
        if default_value is not None:
            new_label.default_value.default_value = default_value
        request.labels.extend([new_label])
        self._stub.UpdateLabels(request)

    def _get_labels(self):
        """Retrieve labels scoping the collection.

        Returns
        -------
        labels: list[str]
            List of labels that entries are scoped to. For example, ``["time", "complex"]``.
        """
        return self._info["labels"]

    labels = property(_get_labels, set_labels, "labels")

    def has_label(self, label):
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
        >>> coll = dpf.Collection(dpf.types.field)
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
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(self._message)

        if isinstance(label_space_or_index, dict):
            for key in label_space_or_index:
                request.label_space.label_space[key] = label_space_or_index[key]
        elif isinstance(label_space_or_index, int):
            request.index = label_space_or_index

        out = self._stub.GetEntries(request)
        list_out = []
        for obj in out.entries:
            if obj.HasField("dpf_type"):
                if self._type == types.scoping:
                    unpacked_msg = scoping_pb2.Scoping()
                    obj.dpf_type.Unpack(unpacked_msg)
                    list_out.append(Scoping(scoping=unpacked_msg, server=self._server))
                elif self._type == types.field:
                    unpacked_msg = field_pb2.Field()
                    obj.dpf_type.Unpack(unpacked_msg)
                    list_out.append(Field(field=unpacked_msg, server=self._server))
                elif self._type == types.meshed_region:
                    unpacked_msg = meshed_region_pb2.MeshedRegion()
                    obj.dpf_type.Unpack(unpacked_msg)
                    list_out.append(
                        MeshedRegion(mesh=unpacked_msg, server=self._server)
                    )
        if len(list_out) == 0:
            list_out = None
        return list_out

    def _get_entry(self, label_space_or_index):
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
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(self._message)
        request.index = index
        out = self._stub.GetEntries(request).entries
        out = out[0].label_space.label_space
        dictOut = {}
        for key in out:
            dictOut[key] = out[key]

        return dictOut

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
        ids = []
        for i in range(len(self)):
            current_scop = self.get_label_space(i)
            if label in current_scop and current_scop[label] not in ids:
                ids.append(current_scop[label])
        return ids

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
            IDs scopped to the input label.
        """
        request = collection_pb2.LabelScopingRequest()
        request.collection.CopyFrom(self._message)
        request.label = label
        scoping_message = self._stub.GetLabelScoping(request)
        scoping = Scoping(scoping_message.label_scoping)
        return scoping

    def __getitem__(self, index):
        """Retrieves the entry at a requested index value.

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
            raise IndexError("This collection contains no items")
        if index >= self_len:
            raise IndexError(f"This collection contains only {self_len} entrie(s)")

        return self._get_entries(index)[0]

    def _add_entry(self, label_space, entry):
        """Update or add an entry at a requested label space.

        parameters
        ----------
        label_space : list[str,int]
            Label space of the requested fields. For example, ``{"time":1, "complex":0}``.
        entry : Field or Scoping
            DPF entry to add.
        """
        request = collection_pb2.UpdateRequest()
        request.collection.CopyFrom(self._message)
        request.entry.dpf_type.Pack(entry._message)
        for key in label_space:
            request.label_space.label_space[key] = label_space[key]
        self._stub.UpdateEntry(request)

    def _get_time_freq_support(self):
        """Retrieve time frequency support.

        Returns
        -------
        time_freq_support : TimeFreqSupport
        """
        request = collection_pb2.SupportRequest()
        request.collection.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        message = self._stub.GetSupport(request)
        return TimeFreqSupport(time_freq_support=message)

    def _set_time_freq_support(self, time_freq_support):
        """Set the time frequency support of the collection."""
        request = collection_pb2.UpdateSupportRequest()
        request.collection.CopyFrom(self._message)
        request.time_freq_support.CopyFrom(time_freq_support._message)
        request.label = "time"
        self._stub.UpdateSupport(request)

    def _set_integral_entries(self, input):
        if self._type == types.int:
            dtype = np.int32
        else:
            dtype = np.float

        if isinstance(input, range):
            input = np.array(list(input), dtype=dtype)
        elif not isinstance(input, (np.ndarray, np.generic)):
            input = np.array(input, dtype=dtype)
        else:
            input = np.array(list(input), dtype=dtype)

        metadata = [(u"size_bytes", f"{input.size * input.itemsize}")]
        request = collection_pb2.UpdateAllDataRequest()
        request.collection.CopyFrom(self._message)

        self._stub.UpdateAllData(scoping._data_chunk_yielder(request, input), metadata=metadata)

    def _get_integral_entries(self):
        request = collection_pb2.GetAllDataRequest()
        request.collection.CopyFrom(self._message)
        if self._type == types.int:
            data_type = u"int"
            dtype = np.int32
        else:
            data_type = u"double"
            dtype = np.float
        service = self._stub.GetAllData(request, metadata=[(u"float_or_double", data_type)])
        return scoping._data_get_chunk_(dtype, service)

    def _connect(self):
        """Connect to the gRPC service."""
        return collection_pb2_grpc.CollectionServiceStub(self._server.channel)

    @property
    @protect_grpc
    def _info(self):
        """Length and labels of this container."""
        list_stub = self._stub.List(self._message)
        return {"len": list_stub.count_entries, "labels": list_stub.labels.labels}

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
            Description of the entity.
        """
        request = base_pb2.DescribeRequest()
        if isinstance(self._message.id, int):
            request.dpf_type_id = self._message.id
        else:
            request.dpf_type_id = self._message.id.id
        return self._stub.Describe(request).description

    def __len__(self):
        """Retrieve the number of entries."""
        return self._info["len"]

    def __del__(self):
        """Delete the entry."""
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
