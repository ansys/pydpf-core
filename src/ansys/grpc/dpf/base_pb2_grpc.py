# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.grpc.dpf.base_pb2 as base__pb2


class BaseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/Initialize',
                request_serializer=base__pb2.InitializationRequest.SerializeToString,
                response_deserializer=base__pb2.InitializationResponse.FromString,
                )
        self.GetServerInfo = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/GetServerInfo',
                request_serializer=base__pb2.ServerInfoRequest.SerializeToString,
                response_deserializer=base__pb2.ServerInfoResponse.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/GetConfig',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=base__pb2.ConfigResponse.FromString,
                )
        self.Load = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/Load',
                request_serializer=base__pb2.PluginRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.Describe = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/Describe',
                request_serializer=base__pb2.DescribeRequest.SerializeToString,
                response_deserializer=base__pb2.DescribeResponse.FromString,
                )
        self.DescribeStreamed = channel.unary_stream(
                '/ansys.api.dpf.base.v0.BaseService/DescribeStreamed',
                request_serializer=base__pb2.DescribeRequest.SerializeToString,
                response_deserializer=base__pb2.DescribeArrayResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/Delete',
                request_serializer=base__pb2.DeleteRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.DeleteStreamed = channel.stream_unary(
                '/ansys.api.dpf.base.v0.BaseService/DeleteStreamed',
                request_serializer=base__pb2.DeleteRequest.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.Serialize = channel.unary_stream(
                '/ansys.api.dpf.base.v0.BaseService/Serialize',
                request_serializer=base__pb2.SerializeRequest.SerializeToString,
                response_deserializer=base__pb2.SerializeResponse.FromString,
                )
        self.DuplicateRef = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/DuplicateRef',
                request_serializer=base__pb2.DuplicateRefRequest.SerializeToString,
                response_deserializer=base__pb2.DuplicateRefResponse.FromString,
                )
        self.CreateTmpDir = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/CreateTmpDir',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=base__pb2.UploadFileResponse.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/ansys.api.dpf.base.v0.BaseService/DownloadFile',
                request_serializer=base__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=base__pb2.DownloadFileResponse.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/ansys.api.dpf.base.v0.BaseService/UploadFile',
                request_serializer=base__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=base__pb2.UploadFileResponse.FromString,
                )
        self.PrepareShutdown = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/PrepareShutdown',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )
        self.ReleaseServer = channel.unary_unary(
                '/ansys.api.dpf.base.v0.BaseService/ReleaseServer',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )


class BaseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Load(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Describe(self, request, context):
        """describes any sharedObjectBase
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeStreamed(self, request, context):
        """describes any sharedObjectBase
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """deletes any sharedObjectBase
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStreamed(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Serialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DuplicateRef(self, request, context):
        """describes any sharedOpbjectBase
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTmpDir(self, request, context):
        """creates a temporary dir server side
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """file from server to client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """file from client to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareShutdown(self, request, context):
        """clears temporary folders allocated during the server runtime
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseServer(self, request, context):
        """removes the handle on the server
        should be used only if the server was started by this client instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=base__pb2.InitializationRequest.FromString,
                    response_serializer=base__pb2.InitializationResponse.SerializeToString,
            ),
            'GetServerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerInfo,
                    request_deserializer=base__pb2.ServerInfoRequest.FromString,
                    response_serializer=base__pb2.ServerInfoResponse.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=base__pb2.ConfigResponse.SerializeToString,
            ),
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=base__pb2.PluginRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'Describe': grpc.unary_unary_rpc_method_handler(
                    servicer.Describe,
                    request_deserializer=base__pb2.DescribeRequest.FromString,
                    response_serializer=base__pb2.DescribeResponse.SerializeToString,
            ),
            'DescribeStreamed': grpc.unary_stream_rpc_method_handler(
                    servicer.DescribeStreamed,
                    request_deserializer=base__pb2.DescribeRequest.FromString,
                    response_serializer=base__pb2.DescribeArrayResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=base__pb2.DeleteRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'DeleteStreamed': grpc.stream_unary_rpc_method_handler(
                    servicer.DeleteStreamed,
                    request_deserializer=base__pb2.DeleteRequest.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'Serialize': grpc.unary_stream_rpc_method_handler(
                    servicer.Serialize,
                    request_deserializer=base__pb2.SerializeRequest.FromString,
                    response_serializer=base__pb2.SerializeResponse.SerializeToString,
            ),
            'DuplicateRef': grpc.unary_unary_rpc_method_handler(
                    servicer.DuplicateRef,
                    request_deserializer=base__pb2.DuplicateRefRequest.FromString,
                    response_serializer=base__pb2.DuplicateRefResponse.SerializeToString,
            ),
            'CreateTmpDir': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTmpDir,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=base__pb2.UploadFileResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=base__pb2.DownloadFileRequest.FromString,
                    response_serializer=base__pb2.DownloadFileResponse.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=base__pb2.UploadFileRequest.FromString,
                    response_serializer=base__pb2.UploadFileResponse.SerializeToString,
            ),
            'PrepareShutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareShutdown,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
            'ReleaseServer': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseServer,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.base.v0.BaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BaseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/Initialize',
            base__pb2.InitializationRequest.SerializeToString,
            base__pb2.InitializationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/GetServerInfo',
            base__pb2.ServerInfoRequest.SerializeToString,
            base__pb2.ServerInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/GetConfig',
            base__pb2.Empty.SerializeToString,
            base__pb2.ConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/Load',
            base__pb2.PluginRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Describe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/Describe',
            base__pb2.DescribeRequest.SerializeToString,
            base__pb2.DescribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeStreamed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ansys.api.dpf.base.v0.BaseService/DescribeStreamed',
            base__pb2.DescribeRequest.SerializeToString,
            base__pb2.DescribeArrayResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/Delete',
            base__pb2.DeleteRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStreamed(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ansys.api.dpf.base.v0.BaseService/DeleteStreamed',
            base__pb2.DeleteRequest.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Serialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ansys.api.dpf.base.v0.BaseService/Serialize',
            base__pb2.SerializeRequest.SerializeToString,
            base__pb2.SerializeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DuplicateRef(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/DuplicateRef',
            base__pb2.DuplicateRefRequest.SerializeToString,
            base__pb2.DuplicateRefResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTmpDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/CreateTmpDir',
            base__pb2.Empty.SerializeToString,
            base__pb2.UploadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ansys.api.dpf.base.v0.BaseService/DownloadFile',
            base__pb2.DownloadFileRequest.SerializeToString,
            base__pb2.DownloadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ansys.api.dpf.base.v0.BaseService/UploadFile',
            base__pb2.UploadFileRequest.SerializeToString,
            base__pb2.UploadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrepareShutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/PrepareShutdown',
            base__pb2.Empty.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.base.v0.BaseService/ReleaseServer',
            base__pb2.Empty.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
