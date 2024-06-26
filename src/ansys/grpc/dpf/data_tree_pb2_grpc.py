# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.data_tree_pb2 as data__tree__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in data_tree_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DataTreeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/Create',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=data__tree__pb2.DataTree.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/Update',
                request_serializer=data__tree__pb2.UpdateRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/List',
                request_serializer=data__tree__pb2.ListRequest.SerializeToString,
                response_deserializer=data__tree__pb2.ListResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/Get',
                request_serializer=data__tree__pb2.GetRequest.SerializeToString,
                response_deserializer=data__tree__pb2.GetResponse.FromString,
                _registered_method=True)
        self.Has = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/Has',
                request_serializer=data__tree__pb2.HasRequest.SerializeToString,
                response_deserializer=data__tree__pb2.HasResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/ansys.api.dpf.data_tree.v0.DataTreeService/Delete',
                request_serializer=data__tree__pb2.DataTree.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                _registered_method=True)


class DataTreeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Has(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataTreeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=data__tree__pb2.DataTree.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=data__tree__pb2.UpdateRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=data__tree__pb2.ListRequest.FromString,
                    response_serializer=data__tree__pb2.ListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=data__tree__pb2.GetRequest.FromString,
                    response_serializer=data__tree__pb2.GetResponse.SerializeToString,
            ),
            'Has': grpc.unary_unary_rpc_method_handler(
                    servicer.Has,
                    request_deserializer=data__tree__pb2.HasRequest.FromString,
                    response_serializer=data__tree__pb2.HasResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=data__tree__pb2.DataTree.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.data_tree.v0.DataTreeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ansys.api.dpf.data_tree.v0.DataTreeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DataTreeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/Create',
            base__pb2.Empty.SerializeToString,
            data__tree__pb2.DataTree.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/Update',
            data__tree__pb2.UpdateRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/List',
            data__tree__pb2.ListRequest.SerializeToString,
            data__tree__pb2.ListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/Get',
            data__tree__pb2.GetRequest.SerializeToString,
            data__tree__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Has(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/Has',
            data__tree__pb2.HasRequest.SerializeToString,
            data__tree__pb2.HasResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ansys.api.dpf.data_tree.v0.DataTreeService/Delete',
            data__tree__pb2.DataTree.SerializeToString,
            base__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
