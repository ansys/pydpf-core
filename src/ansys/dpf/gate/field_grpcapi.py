import types
import numpy as np
from ansys.dpf.gate.generated import field_abstract_api
from ansys.dpf.gate import grpc_stream_helpers, errors

# -------------------------------------------------------------------------------
# Field
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(FieldGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class FieldGRPCAPI(field_abstract_api.FieldAbstractAPI):
    STUBNAME = "field_stub"

    @staticmethod
    def init_field_environment(object):
        from ansys.grpc.dpf import field_pb2_grpc
        if hasattr(object, "_server"):
            server = object._server
        else:
            server = object
        server.create_stub_if_necessary(FieldGRPCAPI.STUBNAME, field_pb2_grpc.FieldServiceStub)
        object._deleter_func = (_get_stub(server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def field_new_with1_ddimensionnality_on_client(client, fieldDimensionality, numComp,
                                                 numEntitiesToReserve, location):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.FieldRequest()
        request.nature = fieldDimensionality
        request.location.location = location
        request.size.scoping_size = fieldDimensionality
        request.dimensionality.size.append(numComp)
        return _get_stub(client).Create(request)

    @staticmethod
    def field_new_with2_ddimensionnality_on_client(client, fieldDimensionality, numCompN, numCompM,
                                                 numEntitiesToReserve, location):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.FieldRequest()
        request.nature = fieldDimensionality
        request.location.location = location
        request.size.scoping_size = fieldDimensionality
        request.dimensionality.size.append(numCompN)
        request.dimensionality.size.append(numCompM)
        return _get_stub(client).Create(request)

    @staticmethod
    def csfield_get_number_elementary_data(field):
        from ansys.grpc.dpf import base_pb2, field_pb2
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.field.CopyFrom(field._internal_obj)
        return _get_stub(field._server).Count(request).count

    @staticmethod
    def csfield_get_number_of_components(field):
        from ansys.grpc.dpf import base_pb2, field_pb2
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_COMPONENT
        request.field.CopyFrom(field._internal_obj)
        return _get_stub(field._server).Count(request).count

    @staticmethod
    def csfield_get_data_size(field):
        from ansys.grpc.dpf import base_pb2, field_pb2
        if field._server.meet_version("4.0"):
            request = field_pb2.CountRequest()
            request.entity = base_pb2.NUM_DATA
            request.field.CopyFrom(field._internal_obj)
            return _get_stub(field._server).Count(request).count
        else:
            return FieldGRPCAPI.csfield_get_number_of_components(field) * \
                   FieldGRPCAPI.csfield_get_number_elementary_data(field)

    @staticmethod
    def csfield_set_cscoping(field, scoping):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.UpdateScopingRequest()
        request.scoping.CopyFrom(scoping._internal_obj)
        request.field.CopyFrom(field._internal_obj)
        _get_stub(field._server).UpdateScoping(request)

    @staticmethod
    def csfield_get_cscoping(field):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.GetRequest()
        request.field.CopyFrom(field._internal_obj)
        return _get_stub(field._server).GetScoping(request).scoping

    @staticmethod
    def csfield_get_entity_data(field, EntityIndex):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.GetElementaryDataRequest()
        request.field.CopyFrom(field._internal_obj)
        request.index = EntityIndex
        list_message =_get_stub(field._server).GetElementaryData(
            request, metadata=[(b"float_or_double", b"double")]
        )
        data = []
        if list_message.elemdata_containers.data.HasField("datadouble"):
            data = list_message.elemdata_containers.data.datadouble.rep_double
        elif list_message.elemdata_containers.data.HasField("dataint"):
            data = list_message.elemdata_containers.data.dataint.rep_int
        elif list_message.elemdata_containers.data.HasField("datastring"):
            data = list_message.elemdata_containers.data.datastring.rep_string
        elif list_message.elemdata_containers.data.HasField("databyte"):
            return list_message.elemdata_containers.data.databyte.rep_bytes

        return np.array(data)

    @staticmethod
    def csfield_push_back(field, EntityId, size, data):
        from ansys.grpc.dpf import field_pb2
        if isinstance(data, (np.ndarray, np.generic)):
            data = data.reshape(data.size)
        elif not hasattr(data, "__iter__"):
            data = np.array([data])
        elif size > 0 and isinstance(data[0], list):
            data = np.array(data).flatten()
        request = field_pb2.AddDataRequest()
        if field._internal_obj.datatype == "int":
            request.elemdata_containers.data.dataint.rep_int.extend(
                data.tolist() if not isinstance(data, list) else data
            )
        elif field._internal_obj.datatype == "string":
            request.elemdata_containers.data.datastring.rep_string.extend(data.tolist())
        elif field._internal_obj.datatype == "custom":
            request.elemdata_containers.data.databyte.rep_bytes= bytes(data.view(np.byte))
        else:
            request.elemdata_containers.data.datadouble.rep_double.extend(
                data.tolist() if not isinstance(data, list) else data
            )
        request.elemdata_containers.scoping_id = EntityId

        request.field.CopyFrom(field._internal_obj)
        _get_stub(field._server).AddData(request)

    @staticmethod
    def csfield_get_data_pointer(field, np_array):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.ListRequest()
        request.field.CopyFrom(field._internal_obj)
        service = _get_stub(field._server).ListDataPointer(request)
        dtype = np.int32
        return grpc_stream_helpers._data_get_chunk_(dtype, service, np_array)

    @staticmethod
    def csfield_set_data_pointer(field, size, data):
        from ansys.grpc.dpf import field_pb2
        if isinstance(data, (np.ndarray, np.generic)):
            data = np.array(data.reshape(data.size), dtype=np.int32)
        else:
            data = np.array(data, dtype=np.int32)
        if data.size == 0:
            return
        metadata = [("size_int", f"{size}")]
        request = field_pb2.UpdateDataRequest()
        request.field.CopyFrom(field._internal_obj)
        _get_stub(field._server).UpdateDataPointer(
            grpc_stream_helpers._data_chunk_yielder(request, data), metadata=metadata)

    @staticmethod
    def csfield_get_data(field, np_array):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.ListRequest()
        request.field.CopyFrom(field._internal_obj)
        data_type=""
        if field._internal_obj.datatype == "int":
            data_type = "int"
            dtype = np.int32
        elif field._internal_obj.datatype == "custom":
            dtype = field._type
        else:
            data_type = "double"
            dtype = np.float64
        service = _get_stub(field._server).List(request, metadata=[("float_or_double", data_type)])
        return grpc_stream_helpers._data_get_chunk_(dtype, service, np_array)

    @staticmethod
    def csfield_raw_set_data(field, data, metadata):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.UpdateDataRequest()
        request.field.CopyFrom(field._internal_obj)
        _get_stub(field._server).UpdateData(
            grpc_stream_helpers._data_chunk_yielder(request, data), metadata=metadata
        )

    @staticmethod
    def csfield_set_data(field, size, data):
        from ansys.grpc.dpf import field_pb2
        if isinstance(data, (np.ndarray, np.generic)):
            data = np.array(data.reshape(data.size), dtype=float)
        else:
            data = np.array(data, dtype=float)
        metadata = [("float_or_double", "double"), ("size_double", f"{size}")]
        FieldGRPCAPI.csfield_raw_set_data(field, data, metadata)

    @staticmethod
    def csfield_resize(field, dataSize, scopingSize):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.UpdateSizeRequest()
        request.field.CopyFrom(field._internal_obj)
        request.size.scoping_size = scopingSize
        request.size.data_size = dataSize
        _get_stub(field._server).UpdateSize(request)

    @staticmethod
    def csfield_get_shared_field_definition(field):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.GetRequest()
        request.field.CopyFrom(field._internal_obj)
        return _get_stub(field._server).GetFieldDefinition(request).field_definition

    @staticmethod
    def csfield_set_field_definition(field, field_definition):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.UpdateFieldDefinitionRequest()
        request.field_def.CopyFrom(field_definition._internal_obj)
        request.field.CopyFrom(field._internal_obj)
        _get_stub(field._server).UpdateFieldDefinition(request)

    @staticmethod
    def csfield_get_support_as_meshed_region(field):
        from ansys.grpc.dpf import field_pb2, base_pb2, meshed_region_pb2
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(field._internal_obj)
        request.type = base_pb2.Type.Value("MESHED_REGION")
        try:
            message = _get_stub(field._server).GetSupport(request)
            out = meshed_region_pb2.MeshedRegion()
            if isinstance(out.id, int):
                out.id = message.id
            else:
                out.id.CopyFrom(message.id)
            return out
        except:
            raise RuntimeError(
                "The field's support is not a mesh. "
                "Try to retrieve the time frequency support."
            )

    @staticmethod
    def csfield_get_support(field):
        from ansys.grpc.dpf import field_pb2, base_pb2
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(field._internal_obj)
        request.type = base_pb2.Type.Value("SUPPORT")
        try:
            message = _get_stub(field._server).GetSupport(request)
            return message
        except:
            raise RuntimeError(
                "Could not get the field's support."
            )


    @staticmethod
    def csfield_get_support_as_time_freq_support(field):
        from ansys.grpc.dpf import field_pb2, base_pb2
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(field._internal_obj)
        request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        try:
            message = _get_stub(field._server).GetSupport(request)
            return message
        except:
            raise RuntimeError(
                "The field's support is not a timefreqsupport.  Try a mesh."
            )

    @staticmethod
    def csfield_set_meshed_region_as_support(field, support):
        from ansys.grpc.dpf import field_pb2, base_pb2
        request = field_pb2.SetSupportRequest()
        request.field.CopyFrom(field._internal_obj)
        request.support.type = base_pb2.Type.Value("MESHED_REGION")
        if isinstance(request.support.id, int):
            request.support.id = support._internal_obj.id
        else:
            request.support.id.id = support._internal_obj.id.id
        _get_stub(field._server).SetSupport(request)

    @staticmethod
    def csfield_set_support(field, support):
        from ansys.grpc.dpf import field_pb2, base_pb2
        request = field_pb2.SetSupportRequest()
        request.field.CopyFrom(field._internal_obj)
        request.support.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        if isinstance(request.support.id, int):
            request.support.id = support._internal_obj.id
        else:
            request.support.id.id = support._internal_obj.id.id
        _get_stub(field._server).SetSupport(request)

    @staticmethod
    def csfield_get_name(field):
        from ansys.grpc.dpf import field_pb2
        from ansys.dpf.gate import data_processing_grpcapi
        request = field_pb2.GetRequest()
        request.field.CopyFrom(field._internal_obj)
        out = _get_stub(field._server).GetFieldDefinition(request)
        return out.name
