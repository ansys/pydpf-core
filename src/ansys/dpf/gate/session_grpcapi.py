from ansys.dpf.gate.generated import session_abstract_api
from ansys.dpf.gate import grpc_stream_helpers, errors

# -------------------------------------------------------------------------------
# Session
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(SessionGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class SessionGRPCAPI(session_abstract_api.SessionAbstractAPI):
    STUBNAME = "session_stub"

    @staticmethod
    def init_session_environment(object):
        from ansys.grpc.dpf import session_pb2_grpc
        object._server.create_stub_if_necessary(SessionGRPCAPI.STUBNAME,
                                                session_pb2_grpc.SessionServiceStub)
        object._deleter_func = (_get_stub(object._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def session_new_on_client(client):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.CreateSessionRequest()
        return _get_stub(client).Create(request)

    @staticmethod
    def add_external_event_handler(session, event_handler, cb):
        _get_stub(session._server).AddProgressEventSystem(session._internal_obj)

    @staticmethod
    def add_workflow(session, workflow_identifier, workflow):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(session._internal_obj)
        request.wf.CopyFrom(workflow._internal_obj)
        request.identifier = workflow_identifier
        _get_stub(session._server).Add(request)

    @staticmethod
    def add_operator(session, identifier, operator, pin):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(session._internal_obj)
        request.op_output.op.CopyFrom(operator._internal_obj)
        request.op_output.pin = pin
        request.identifier = identifier
        _get_stub(session._server).Add(request)

    @staticmethod
    def start_listening(session, bar, LOG):
        service = _get_stub(session._server).ListenToProgress(session._internal_obj)
        service.initial_metadata()
        bar.start()
        for chunk in service:
            try:
                bar.update(chunk.progress.progress_percentage)
                if len(chunk.state.state):
                    LOG.warning(chunk.state.state)
            except Exception as e:
                pass
        try:
            bar.finish()
        except:
            pass

    @staticmethod
    def flush_workflows(session):
        _get_stub(session._server).FlushWorkflows(session._internal_obj)

    @staticmethod
    def add_event_handler_type(session, type, datatree):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(session._internal_obj)
        request.event_handler_type = type
        if datatree:
            request.properties.CopyFrom(datatree._internal_obj)
        _get_stub(session._server).Add(request)

    @staticmethod
    def add_signal_emitter_type(session, type, identifier, datatree):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(session._internal_obj)
        request.signal_emitter_type = type
        if datatree:
            request.properties.CopyFrom(datatree._internal_obj)
        request.identifier = identifier
        _get_stub(session._server).Add(request)
