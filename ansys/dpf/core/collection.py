"""Contains classes associated to the DPF Collection"""

from ansys import dpf
from ansys.grpc.dpf import collection_pb2, collection_pb2_grpc
from ansys.dpf.core.core import base_pb2
from ansys.dpf.core.common import types
from ansys.dpf.core.scoping import Scoping, scoping_pb2
from ansys.dpf.core.field import Field, field_pb2
from ansys.dpf.core.time_freq_support import TimeFreqSupport
from ansys.dpf.core.errors import protect_grpc


class Collection:
    """A class used to represent a Collection which contains
    entries ordered in labels and ids.

    Parameters
    ----------
    collection : ansys.grpc.dpf.collection_pb2.Collection, optional
        Create a collection from a Collection message.

    channel : channel, optional
        Channel connected to the remote or local instance. When
        ``None``, attempts to use the the global channel.

    """

    def __init__(self, dpf_type, collection=None, channel=None):
        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._type = dpf_type
        # self.__info = None  # cached info

        if collection is None:
            request = collection_pb2.CollectionRequest()
            if hasattr(dpf_type, 'name'):
                stype = dpf_type.name
            else:
                stype = dpf_type
            request.type = base_pb2.Type.Value(stype.upper())
            self._message = self._stub.Create(request)
        elif hasattr(collection, '_message'):
            self._message = collection._message
        else:
            self._message = collection

    def set_labels(self, labels):
        """set the requested labels to scope the collection

        Parameters
        ----------
        labels (optional) : list(string)
            labels on which the entries will be scoped, for example:
                ['time','complex']

        """
        if len(self._info['labels'])!=0:
            print("the collection has already labels :",self._info['labels'],'deleting existing abels is  not implemented yet')
            return
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(self._message)
        request.labels.labels.extend(labels)
        self._stub.UpdateLabels(request)

    def add_label(self, label):
        """Add the requested label to scope the collection

        Parameters
        ----------
        label (optional) : string
            Labels on which the entries will be scoped, for example ``'time'``.

        Examples
        --------
        >>> coll.add_label('time')
        """
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(self._message)
        request.labels.labels.extend([label])
        self._stub.UpdateLabels(request)

    def _get_labels(self):
        """get the labels scoping the collection

        Returns
        -------
        labels: list(string)
            labels on which the entries are scoped, for example:
                ``['time', 'complex']``
        """
        return self._info['labels']

    labels = property(_get_labels, set_labels, "labels")

    def _get_entries(self, label_space_or_index):
        """Returns the entry at a requested index or label space

        Parameters
        ----------
        label_space (optional) : dict(string:int)
            Label space of the requested entry, for example:
            ``{"time": 1, "complex": 0}``

        index: int, optional
            Index of the field.

        Returns
        -------
        entry : scoping or field
            entry corresponding to the request
        """
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(self._message)

        if isinstance(label_space_or_index, dict):
            for key in label_space_or_index:
                request.label_space.label_space[key] = label_space_or_index[key]
        elif isinstance(label_space_or_index, int):
            request.index = label_space_or_index

        out = self._stub.GetEntries(request)
        list_out =[]
        for obj in out.entries :
            if obj.HasField("dpf_type"):
                if self._type == types.scoping:
                    unpacked_msg = scoping_pb2.Scoping()
                    obj.dpf_type.Unpack(unpacked_msg)
                    if len(out.entries)==1:
                        return Scoping(scoping=unpacked_msg, channel=self._channel)
                    else:
                        list_out.append(Scoping(scoping=unpacked_msg, channel=self._channel))
                elif self._type == types.field:
                    unpacked_msg = field_pb2.Field()
                    obj.dpf_type.Unpack(unpacked_msg)
                    if len(out.entries)==1:
                        return Field(field=unpacked_msg, channel=self._channel)
                    else:
                        list_out.append(Field(field=unpacked_msg, channel=self._channel))
        if len(list_out)==0:
            list_out=None
        return list_out
            
    def get_label_space(self, index):
        """Returns the label space of an entry at a requested index

        Parameters
        ----------
        index: int, optional
            Index of the entry.

        Returns
        -------
        label_space (optional) : dict(string:int)
            Scoping of the requested entry, for example:
            ``{"time": 1, "complex": 0}``
        """
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(self._message)
        request.index = index
        out = self._stub.GetEntries(request).entries
        out = out[0].label_space.label_space
        dictOut ={}
        for key in out:
            dictOut[key]=out[key]

        return dictOut

    def get_ids(self, label="time"):
        """Get the IDs corresponding to the input label.


        Parameters
        ----------
        label : str
            name of the requested ids

        Returns
        -------
        ids : list of int
            ids corresponding to the input label
        """
        ids = []
        for i in range(len(self)):
            current_scop = self.get_label_space(i)
            if label in current_scop and current_scop[label] not in ids:
                ids.append(current_scop[label])
        return ids

    def __getitem__(self, index):
        """Returns the entry at a requested index

        Parameters
        ----------
        key : int
            the index

        Returns
        -------
        entry : Field or Scoping
            Entry at the index corresponding to the request.
        """
        self_len = len(self)
        if index < 0:
            # convert to a positive index
            index = self_len + index

        if not self_len:
            raise IndexError('This collection contains no items')
        if index >= self_len:
            raise IndexError(f'This collection contains only {self_len} entrie(s)')

        return self._get_entries(index)

    def _add_entry(self, label_space, entry):
        """Update or add the entry at a requested label space

        parameters
        ----------
        label_space : dict(string:int)
            label space of the requested fields, ex : {"time":1, "complex":0}

        entry : Field or Scoping
            DPF entry to add.
        """
        request = collection_pb2.UpdateRequest()
        request.collection.CopyFrom(self._message)
        if self._type == types.scoping:
            request.entry.dpf_type.Pack(entry._message)
        elif self._type == types.field:
            request.entry.dpf_type.Pack(entry._message)

        for key in label_space:
            request.label_space.label_space[key] = label_space[key]
        self._stub.UpdateEntry(request)

    def _get_time_freq_support(self):
        """
        Returns
        -------
        time_freq_support : TimeFreqSupport
        """
        request = collection_pb2.SupportRequest()
        request.collection.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        message = self._stub.GetSupport(request)
        return TimeFreqSupport(time_freq_support=message)

    def _connect(self):
        """Connect to the grpc service"""
        return collection_pb2_grpc.CollectionServiceStub(self._channel)

    @property
    @protect_grpc
    def _info(self):
        """Length and labels of this container"""
        list_stub = self._stub.List(self._message)
        return {"len": list_stub.count_entries, "labels": list_stub.labels.labels}

    def __len__(self):
        """Return number of entries"""
        return self._info["len"]

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
