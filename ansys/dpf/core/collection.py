"""
Collection
===========
Contains classes associated to the DPF Collection

"""

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
from ansys.dpf.core.scoping import Scoping


class Collection:
    """A class used to represent a Collection which contains
    entries ordered in labels and ids.

    Parameters
    ----------
    collection : ansys.grpc.dpf.collection_pb2.Collection, optional
        Create a collection from a Collection message.

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
        
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> coll = dpf.Collection(dpf.types.field)

    """

    def __init__(self, dpf_type, collection=None, server: server.DpfServer=None ):
        if server is None:
            server = dpf.core._global_server()

        self._server = server
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
            self._collection = collection #keep the base collection used for copy
        else:
            self._message = collection

    def set_labels(self, labels):
        """set the requested labels to scope the collection

        Parameters
        ----------
        labels : list[str], optional
            labels on which the entries will be scoped, for example:
                ['time','complex']

        """
        if len(self._info['labels'])!=0:
            print("the collection has already labels :",self._info['labels'],'deleting existing labels is  not implemented yet')
            return
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(self._message)
        request.labels.extend([collection_pb2.NewLabel(label=lab) for lab in labels])
        self._stub.UpdateLabels(request)

    def add_label(self, label, default_value =None):
        """Add the requested label to scope the collection

        Parameters
        ----------
        label : str
            Labels on which the entries will be scoped, for example ``'time'``.
            
        default_value : int , optional
            default value set for existing fields in the collection

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
            new_label.default_value.default_value=default_value
        request.labels.extend([new_label])
        self._stub.UpdateLabels(request)

    def _get_labels(self):
        """get the labels scoping the collection

        Returns
        -------
        labels: list[str]
            labels on which the entries are scoped, for example:
                ``['time', 'complex']``
        """
        return self._info['labels']

    labels = property(_get_labels, set_labels, "labels")
    
    def has_label(self, label):
        """Check if a collection has a specified label

        Parameters
        ----------
        label: str
            Labels that must be searched, for example ``'time'``.
            
        Returns
        -------
        bool
            ``True`` if the specified value has been found in the collection. 

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
        """Returns the entries at a requested index or label space

        Parameters
        ----------
        label_space_or_index : dict[str,int]
            Label space of the requested entry, for example:
            ``{"time": 1, "complex": 0}`` or index of the field.

        Returns
        -------
        entries : list[Scoping], list[Field], list[MeshedRegion]
            entries corresponding to the request
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
                    list_out.append(Scoping(scoping=unpacked_msg, server=self._server))
                elif self._type == types.field:
                    unpacked_msg = field_pb2.Field()
                    obj.dpf_type.Unpack(unpacked_msg)
                    list_out.append(Field(field=unpacked_msg, server=self._server))
                elif self._type == types.meshed_region:
                    unpacked_msg = meshed_region_pb2.MeshedRegion()
                    obj.dpf_type.Unpack(unpacked_msg)
                    list_out.append(MeshedRegion(mesh=unpacked_msg, server=self._server))
        if len(list_out)==0:
            list_out=None
        return list_out  
    
    
    def _get_entry(self, label_space_or_index):
        """Returns the entry at a requested index or label space

        Parameters
        ----------
        label_space_or_index : dict[str,int]
            Label space of the requested entry, for example:
            ``{"time": 1, "complex": 0}`` or index of the field.

        Returns
        -------
        entry : Scoping, Field, MeshedRegion
            entry corresponding to the request
        """
        entries = self._get_entries(label_space_or_index)
        if isinstance(entries, list):
            if len(entries)==1:
                return entries[0]
            else :
                raise KeyError(f"{label_space_or_index} has {len(entries)} entries")
        else:
            return entries
        
            
    def get_label_space(self, index):
        """Returns the label space of an entry at a requested index

        Parameters
        ----------
        index: int, optional
            Index of the entry.

        Returns
        -------
        label_space : dict(str:int)
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

    def get_available_ids_for_label(self, label="time"):
        """Get the IDs corresponding to the input label.


        Parameters
        ----------
        label : str
            name of the requested ids

        Returns
        -------
        ids : list[int]
            ids corresponding to the input label
        """
        ids = []
        for i in range(len(self)):
            current_scop = self.get_label_space(i)
            if label in current_scop and current_scop[label] not in ids:
                ids.append(current_scop[label])
        return ids
    
    def get_label_scoping(self, label = "time"):
        """Get the scoping corresponding to the input label. This method
        allows to get the list of available ids for a given label in the 
        Collection. 
        For example, if the label "el_type" is available in the collection,
        the get_lable_scoping method, will return the list element type ids 
        available in it. Those ids can then be used to request a given entity 
        inside the collection.
        
        Parameters
        ----------
        label: str
            name of the requested ids
        
        Returns
        -------
        scoping: Scoping
            scoping containing the ids of the input label
        """
        request = collection_pb2.LabelScopingRequest()
        request.collection.CopyFrom(self._message)
        request.label = label
        scoping_message = self._stub.GetLabelScoping(request)
        scoping = Scoping(scoping_message.label_scoping)
        return scoping

    def __getitem__(self, index):
        """Returns the entry at a requested index

        Parameters
        ----------
        key : int
            the index

        Returns
        -------
        entry : Field , Scoping
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

        return self._get_entries(index)[0]

    def _add_entry(self, label_space, entry):
        """Update or add the entry at a requested label space

        parameters
        ----------
        label_space : list[str,int]
            label space of the requested fields, ex : {"time":1, "complex":0}

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


    def _set_time_freq_support(self, time_freq_support):
        """
        Set the time_freq_support of a collection. 
        """
        request = collection_pb2.UpdateSupportRequest()
        request.collection.CopyFrom(self._message)
        request.time_freq_support.CopyFrom(time_freq_support._message)
        request.label = "time"
        self._stub.UpdateSupport(request)
    

    def _connect(self):
        """Connect to the grpc service"""
        return collection_pb2_grpc.CollectionServiceStub(self._server.channel)

    @property
    @protect_grpc
    def _info(self):
        """Length and labels of this container"""
        list_stub = self._stub.List(self._message)
        return {"len": list_stub.count_entries, "labels": list_stub.labels.labels}
    
    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        request = base_pb2.DescribeRequest()
        request.dpf_type_id = self._message.id
        return self._stub.Describe(request).description

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
