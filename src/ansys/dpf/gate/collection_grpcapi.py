from typing import NamedTuple
import numpy as np
import weakref

from ansys.dpf.gate.generated import collection_abstract_api
from ansys.dpf.gate import object_handler, data_processing_grpcapi, grpc_stream_helpers, errors
from ansys.dpf.gate.integral_types import MutableListInt32


# -------------------------------------------------------------------------------
# Collection
# -------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(CollectionGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class CollectionGRPCAPI(collection_abstract_api.CollectionAbstractAPI):
    STUBNAME = "collection_stub"

    @staticmethod
    def init_collection_environment(object):
        from ansys.grpc.dpf import collection_message_pb2, collection_pb2_grpc
        if not hasattr(object, "_server"):
            server = object
        elif isinstance(object._server, weakref.ref):
            server = object._server()
        else:
            server = object._server
        server.create_stub_if_necessary(
            CollectionGRPCAPI.STUBNAME, collection_pb2_grpc.CollectionServiceStub)

        object._deleter_func = (
        _get_stub(server).Delete, lambda obj: obj._internal_obj if isinstance(obj, collection_message_pb2.Collection) else None)

    @staticmethod
    def collection_of_scoping_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("SCOPING"))

    @staticmethod
    def collection_of_field_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("FIELD"))

    @staticmethod
    def collection_of_mesh_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("MESHED_REGION"))

    @staticmethod
    def collection_of_int_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("INT"))

    @staticmethod
    def collection_of_double_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("DOUBLE"))

    @staticmethod
    def collection_of_string_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("STRING"))

    @staticmethod
    def collection_new_on_client(client, type):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.CollectionRequest()
        request.type = type
        return _get_stub(client).Create(request)

    @staticmethod
    def collection_of_any_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        return CollectionGRPCAPI.collection_new_on_client(client, base_pb2.Type.Value("ANY"))

    @staticmethod
    def collection_add_label(collection, label):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(collection._internal_obj)
        new_label = collection_pb2.NewLabel(label=label)
        request.labels.extend([new_label])
        _get_stub(collection._server).UpdateLabels(request)

    @staticmethod
    def collection_add_label_with_default_value(collection, label, value):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.UpdateLabelsRequest()
        request.collection.CopyFrom(collection._internal_obj)
        new_label = collection_pb2.NewLabel(label=label)
        new_label.default_value.default_value = value
        request.labels.extend([new_label])
        _get_stub(collection._server).UpdateLabels(request)

    @staticmethod
    def collection_get_num_labels(collection):
        return len(CollectionGRPCAPI._list(collection).labels.labels)

    @staticmethod
    def collection_get_label(collection, labelIndex):
        return CollectionGRPCAPI._list(collection).labels.labels[labelIndex]

    @staticmethod
    def collection_get_name(collection):
        return CollectionGRPCAPI._list(collection).name

    @staticmethod
    def collection_set_name(collection, name):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.UpdateCollectionRequest()
        request.collection.CopyFrom(collection._internal_obj)
        request.string_properties.update({"name": name})
        _get_stub(collection._server).Update(request)

    @staticmethod
    def collection_get_size(collection):
        if isinstance(collection._internal_obj, list):
            return len(collection._internal_obj)
        return CollectionGRPCAPI._list(collection).count_entries

    @staticmethod
    def _list(collection):
        list_stub = _get_stub(collection._server).List(collection._internal_obj)
        return list_stub

    @staticmethod
    def collection_get_num_obj_for_label_space(collection, space):
        return len(CollectionGRPCAPI._collection_get_entries(collection, space))

    @staticmethod
    def collection_fill_obj_indeces_for_label_space(collection, space, indices: MutableListInt32):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(collection._internal_obj)
        request.label_space.CopyFrom(space._internal_obj)

        out = _get_stub(collection._server).GetEntriesIndices(request)
        indices.set(out.indices.rep_int)

    @staticmethod
    def collection_get_obj_by_index_for_label_space(collection, space, index):
        return data_processing_grpcapi.DataProcessingGRPCAPI.data_processing_duplicate_object_reference(
            CollectionGRPCAPI._collection_get_entries(collection, space)[index].entry
        )

    @staticmethod
    def collection_get_obj_by_index(collection, index):
        return data_processing_grpcapi.DataProcessingGRPCAPI.data_processing_duplicate_object_reference(
            CollectionGRPCAPI._collection_get_entries(collection, index)[0].entry
        )

    @staticmethod
    def collection_get_obj_label_space_by_index(collection, index):
        return CollectionGRPCAPI._collection_get_entries(collection, index)[0].label_space

    @staticmethod
    def _collection_get_entries(collection, label_space_or_index):
        from ansys.grpc.dpf import collection_pb2, scoping_pb2, field_pb2, meshed_region_pb2, base_pb2, \
            dpf_any_message_pb2
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(collection._internal_obj)

        if isinstance(label_space_or_index, int):
            request.index = label_space_or_index
        else:
            request.label_space.CopyFrom(label_space_or_index._internal_obj)

        out = _get_stub(collection._server).GetEntries(request)
        list_out = []
        for obj in out.entries:
            label_space = {}
            if obj.HasField("label_space"):
                for key in obj.label_space.label_space:
                    label_space[key] = obj.label_space.label_space[key]
            if obj.HasField("dpf_type"):
                if collection._internal_obj.type == base_pb2.Type.Value("SCOPING"):
                    entry = object_handler.ObjHandler(data_processing_grpcapi.DataProcessingGRPCAPI,
                                                      scoping_pb2.Scoping())
                elif collection._internal_obj.type == base_pb2.Type.Value("FIELD"):
                    entry = object_handler.ObjHandler(data_processing_grpcapi.DataProcessingGRPCAPI, field_pb2.Field())
                elif collection._internal_obj.type == base_pb2.Type.Value("MESHED_REGION"):
                    entry = object_handler.ObjHandler(data_processing_grpcapi.DataProcessingGRPCAPI,
                                                      meshed_region_pb2.MeshedRegion())
                elif collection._internal_obj.type == base_pb2.Type.Value("ANY"):
                    entry = object_handler.ObjHandler(data_processing_grpcapi.DataProcessingGRPCAPI,
                                                      dpf_any_message_pb2.DpfAny())
                else:
                    raise NotImplementedError(
                        f"collection {base_pb2.Type.Name(collection._internal_obj.type)} type is not implemented")
                obj.dpf_type.Unpack(entry._internal_obj)
                entry._server = collection._server
                list_out.append(_CollectionEntry(label_space, entry))

        return list_out

    @staticmethod
    def collection_get_label_scoping(collection, label):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.LabelScopingRequest()
        request.collection.CopyFrom(collection._internal_obj)
        request.label = label
        scoping_message = _get_stub(collection._server).GetLabelScoping(request)
        return scoping_message.label_scoping

    @staticmethod
    def collection_add_entry(collection, labelspace, obj):
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.UpdateRequest()
        request.collection.CopyFrom(collection._internal_obj)
        if hasattr(obj, "_message"):
            # TO DO: remove
            request.entry.dpf_type.Pack(obj._message)
        else:
            request.entry.dpf_type.Pack(obj._internal_obj)
        request.label_space.CopyFrom(labelspace._internal_obj)
        _get_stub(collection._server).UpdateEntry(request)

    @staticmethod
    def _collection_set_data_as_integral_type(collection, data, size):
        from ansys.grpc.dpf import collection_pb2
        metadata = [(u"size_bytes", f"{size * data.itemsize}")]
        request = collection_pb2.UpdateAllDataRequest()
        request.collection.CopyFrom(collection._internal_obj)
        _get_stub(collection._server).UpdateAllData(grpc_stream_helpers._data_chunk_yielder(request, data),
                                                    metadata=metadata)

    @staticmethod
    def collection_set_data_as_int(collection, data, size):
        CollectionGRPCAPI._collection_set_data_as_integral_type(collection, data, size)

    @staticmethod
    def collection_set_data_as_double(collection, data, size):
        CollectionGRPCAPI._collection_set_data_as_integral_type(collection, data, size)

    @staticmethod
    def collection_set_support(collection, label, support):
        from ansys.grpc.dpf import collection_pb2
        from ansys.grpc.dpf import time_freq_support_pb2
        from ansys.grpc.dpf import support_pb2
        request = collection_pb2.UpdateSupportRequest()
        request.collection.CopyFrom(collection._internal_obj)
        if isinstance(support._internal_obj, time_freq_support_pb2.TimeFreqSupport):
            request.time_freq_support.CopyFrom(support._internal_obj)
        else:
            supp = support_pb2.Support(id=support._internal_obj.id)
            request.support.CopyFrom(supp)
        request.label = label
        _get_stub(collection._server).UpdateSupport(request)

    @staticmethod
    def collection_get_support(collection, label):
        from ansys.grpc.dpf import collection_pb2, base_pb2
        request = collection_pb2.SupportRequest()
        request.collection.CopyFrom(collection._internal_obj)
        if collection._server.meet_version("5.0"):
            request.label = label
            request.type = base_pb2.Type.Value("SUPPORT")
        else:
            request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        message = _get_stub(collection._server).GetSupport(request)
        return message

    @staticmethod
    def collection_get_data_as_int(collection, size):
        if not collection._server.meet_version("3.0"):
            raise errors.DpfVersionNotSupported("3.0")
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.GetAllDataRequest()
        request.collection.CopyFrom(collection._internal_obj)
        data_type = u"int"
        dtype = np.int32
        service = _get_stub(collection._server).GetAllData(request, metadata=[(u"float_or_double", data_type)])
        return grpc_stream_helpers._data_get_chunk_(dtype, service)

    @staticmethod
    def collection_get_data_as_double(collection, size):
        if not collection._server.meet_version("3.0"):
            raise errors.DpfVersionNotSupported("3.0")
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.GetAllDataRequest()
        request.collection.CopyFrom(collection._internal_obj)
        data_type = u"double"
        dtype = np.float64
        service = _get_stub(collection._server).GetAllData(request, metadata=[(u"float_or_double", data_type)])
        return grpc_stream_helpers._data_get_chunk_(dtype, service)

    @staticmethod
    def collection_get_string_entry(collection, index):
        if isinstance(collection._internal_obj, list):
            return collection._internal_obj[index]
        from ansys.grpc.dpf import collection_pb2
        request = collection_pb2.EntryRequest()
        request.collection.CopyFrom(collection._internal_obj)
        request.index = index
        response = _get_stub(collection._server).GetEntries(request)
        return response.entries[0]

    @staticmethod
    def collection_of_string_new_local(client):
        return []

    @staticmethod
    def collection_add_string_entry(collection, obj):
        if isinstance(collection._internal_obj, list):
            return collection._internal_obj.append(obj)
        else:
            raise NotImplementedError


class _CollectionEntry(NamedTuple):
    label_space: dict
    entry: object
