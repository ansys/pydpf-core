# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.time_freq_support_pb2 as time__freq__support__pb2


class TimeFreqSupportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Create',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=time__freq__support__pb2.TimeFreqSupport.FromString,
                )
        self.Get = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Get',
                request_serializer=time__freq__support__pb2.GetRequest.SerializeToString,
                response_deserializer=time__freq__support__pb2.GetResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Update',
                request_serializer=time__freq__support__pb2.TimeFreqSupportUpdateRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.List = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/List',
                request_serializer=time__freq__support__pb2.ListRequest.SerializeToString,
                response_deserializer=time__freq__support__pb2.ListResponse.FromString,
                )
        self.Count = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Count',
                request_serializer=time__freq__support__pb2.CountRequest.SerializeToString,
                response_deserializer=base__pb2.CountResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Delete',
                request_serializer=time__freq__support__pb2.TimeFreqSupport.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )


class TimeFreqSupportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
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

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeFreqSupportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=time__freq__support__pb2.TimeFreqSupport.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=time__freq__support__pb2.GetRequest.FromString,
                    response_serializer=time__freq__support__pb2.GetResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=time__freq__support__pb2.TimeFreqSupportUpdateRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=time__freq__support__pb2.ListRequest.FromString,
                    response_serializer=time__freq__support__pb2.ListResponse.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=time__freq__support__pb2.CountRequest.FromString,
                    response_serializer=base__pb2.CountResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=time__freq__support__pb2.TimeFreqSupport.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimeFreqSupportService(object):
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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Create',
            base__pb2.Empty.SerializeToString,
            time__freq__support__pb2.TimeFreqSupport.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Get',
            time__freq__support__pb2.GetRequest.SerializeToString,
            time__freq__support__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Update',
            time__freq__support__pb2.TimeFreqSupportUpdateRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/List',
            time__freq__support__pb2.ListRequest.SerializeToString,
            time__freq__support__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Count',
            time__freq__support__pb2.CountRequest.SerializeToString,
            base__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.time_freq_support.v0.TimeFreqSupportService/Delete',
            time__freq__support__pb2.TimeFreqSupport.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)