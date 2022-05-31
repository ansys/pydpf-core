"""
Session
========
"""

import logging
import weakref

from ansys import dpf
from ansys.dpf.core.check_version import version_requires, server_meet_version
from ansys.dpf.core.common import _common_percentage_progress_bar, _progress_bar_is_available
from ansys.dpf.core.errors import protect_grpc

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')


class Session:
    """A class used to a user session on the server, it allows to plan events
    call backs from the server when workflows are running.
    A session is started every time a ``'DpfServer'`` is created.
    """

    def __init__(self, server=None):
        if server is None:
            server = dpf.core._global_server()

        self._server_weak_ref = weakref.ref(server)
        if server_meet_version("3.0", self._server):
            self._stub = self._connect()
            self.__send_init_request()
            self.add_progress_system()

    @property
    def _server(self):
        return self._server_weak_ref()

    @version_requires("3.0")
    def _connect(self):
        """Connect to the grpc service"""
        from ansys.grpc.dpf import session_pb2_grpc
        return session_pb2_grpc.SessionServiceStub(self._server.channel)

    @protect_grpc
    def __send_init_request(self):
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.CreateSessionRequest()
        self._message = self._stub.Create(request)

    @version_requires("3.0")
    def add_workflow(self, workflow, identifier):
        """Add a workflow to the session. It allows to follow the workflow's
        events while it's running.
        This method is automatically called when a workflow's output
        is requested.

        Parameters
        ----------
        workflow : Workflow

        identifier : str
            name given to the workflow
        """
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(self._message)
        request.wf.CopyFrom(workflow._internal_obj)
        request.identifier = identifier
        self._stub.Add(request)

    @version_requires("3.0")
    def add_operator(self, operator, pin, identifier):
        """Add a workflow made of the input operator and all his ancestors
        to the session. It allows to follow the workflow's
        events while it's running.
        This method is automatically called when an operator's output
        is requested and the opetion op.progress_bar is set to ``'True'``.

        Parameters
        ----------
        operator : Operator

        pin : int
            output pin number requested

        identifier : str
            name given to the workflow
        """
        from ansys.grpc.dpf import session_pb2
        request = session_pb2.AddRequest()
        request.session.CopyFrom(self._message)
        request.op_output.op.CopyFrom(operator._internal_obj)
        request.op_output.pin = pin
        request.identifier = identifier
        self._stub.Add(request)

    @version_requires("3.0")
    def listen_to_progress(self):
        """Starts a progress bar and update it every time an operator is
        finished.
        """
        service = self._stub.ListenToProgress(self._message)
        if not _progress_bar_is_available():
            print("Progress bar is not available, please install progressbar2")
            return
        bar = _common_percentage_progress_bar("Workflow running")
        bar.start()
        for chunk in service:
            try:
                bar.update(chunk.progress.progress_percentage)
                if len(chunk.state.state):
                    LOG.warning(chunk.state.state)
            except Exception as e:
                raise e
                pass
        try:
            bar.finish()
        except:
            pass

    @version_requires("3.0")
    def add_progress_system(self):
        """Asks the session to start recording progress events.
        Called when the session is started.
        """
        self._stub.AddProgressEventSystem(self._message)

    @version_requires("3.0")
    def flush_workflows(self):
        """This removes the handle on the workflow by the session"""
        self._stub.FlushWorkflows(self._message)

    def __del__(self):
        try:
            if server_meet_version("3.0", self._server):
                self._stub.Delete(self._message)
        except:
            pass
