"""
Session
========
"""
import abc
import ctypes
import logging
import threading
import traceback
import warnings
import weakref

from ansys.dpf.gate import session_capi, session_grpcapi, capi

from ansys.dpf.core import server as server_module
from ansys.dpf.core import server_types, errors
from ansys.dpf.core.check_version import version_requires, server_meet_version
from ansys.dpf.core.common import _common_percentage_progress_bar, _progress_bar_is_available

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')


@capi.GenericCallBackType
def progress_call_back(obj, nature, arg):
    try:
        obj = ctypes.cast(obj, ctypes.POINTER(ctypes.py_object))
        handler = obj.contents.value
        if nature == 0:
            handler.started_operators += 1
        elif nature == 1:
            handler.finished_operators += 1
            if handler.finished_operators > 0 and handler.bar:
                handler.bar.update(handler.finished_operators / handler.started_operators * 100)
                if handler.finished_operators == handler.started_operators:
                    handler.bar.finish()
        elif nature == 9:
            handler.finished_operators = 0
            handler.started_operators = 0
        elif handler.bar:
            handler.bar.update(0)
    except Exception as e:
        print(e.args)


class EventHandlerBase:
    @abc.abstractmethod
    def add_operator(self, operator, pin, identifier):
        pass

    @abc.abstractmethod
    def start_listening(self):
        pass


class EventHandler(EventHandlerBase):
    def __init__(self, session):
        self._session = weakref.ref(session)
        self.bar = None
        self.started_operators = 0
        self.finished_operators = 0
        self.py_obj = ctypes.py_object(self)
        self._session()._api.add_external_event_handler(
            self._session(), ctypes.cast(ctypes.pointer(self.py_obj),
                                         ctypes.c_void_p), progress_call_back)

    def start_listening(self):
        if not _progress_bar_is_available():
            print("Progress bar is not available, please install progressbar2")
            return
        self.bar = _common_percentage_progress_bar("Workflow running")
        self.started_operators = 0
        self.finished_operators = 0

    def add_operator(self, operator, pin, identifier):
        from ansys.dpf.core import workflow
        wf = workflow.Workflow(server=self._session()._server)
        wf.add_operator(operator)
        wf.set_output_name("out", operator, pin)
        wf._api.work_flow_discover_operators(wf)
        self._session().add_workflow(wf, identifier)


class GrpcEventHandler(EventHandlerBase):
    def __init__(self, session):
        self._session = weakref.ref(session)
        self.bar = None
        self._session()._api.add_external_event_handler(self._session(), self, None)

    def start_listening(self):
        if not _progress_bar_is_available():
            print("Progress bar is not available, please install progressbar2")
            return
        self.bar = _common_percentage_progress_bar("Workflow running")
        thread = threading.Thread(
            target=self._session()._api.start_listening, args=[self._session(), self.bar, LOG]
        )
        return thread

    def add_operator(self, operator, pin, identifier):
        self._session()._api.add_operator(self._session(), identifier, operator, pin)


class Session:
    """A class used to create a user session on the server, it allows to plan events
    call backs from the server when workflows are running.
    A session is started every time a ``'DpfServer'`` is created.

    Notes
    -----
    Class available with server's version starting at 3.0.
    """

    def __init__(self, server=None):
        # step 1: get server
        server = server_module.get_or_create_server(server)
        if not server.meet_version("3.0"):
            raise errors.DpfVersionNotSupported("3.0")
        self._server_weak_ref = weakref.ref(server)
        # step 2: get api
        self._api = server.get_api_for_type(capi=session_capi.SessionCAPI,
                                            grpcapi=session_grpcapi.SessionGRPCAPI)

        # step3: init environment
        self._api.init_session_environment(self)  # creates stub when gRPC

        if self._server.has_client():
            self._internal_obj = self._api.session_new_on_client(self._server.client)
        else:
            self._internal_obj = self._api.session_new()

        self._handler = None
        if server_meet_version("3.0", server):
            self.add_progress_system()

    @property
    def _server(self):
        return self._server_weak_ref()

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
        if self._handler is not None:
            self._api.add_workflow(self, identifier, workflow)

    @version_requires("3.0")
    def add_operator(self, operator, pin, identifier):
        """Creates a workflow made of the input operator and all its ancestors
        to the session. It allows to follow the workflow's
        events while it's running.
        This method is automatically called when an operator's output
        is requested and the property :func:`ansys.dpf.core.dpf_operator.Operator.progress_bar`
        is set to ``'True'``.

        Parameters
        ----------
        operator : Operator

        pin : int
            output pin number requested

        identifier : str
            name given to the workflow
        """
        if self._handler is not None:
            self._handler.add_operator(operator, pin, identifier)

    @version_requires("3.0")
    def listen_to_progress(self):
        """Starts a progress bar and updates it every time an operator is
        finished.
        """
        if self._handler is not None:
            return self._handler.start_listening()

    def _init_handler(self):
        if isinstance(self._server, server_types.InProcessServer):
            self._handler = EventHandler(self)
        elif isinstance(self._server, server_types.LegacyGrpcServer):
            self._handler = GrpcEventHandler(self)

    @version_requires("3.0")
    def add_progress_system(self):
        """Asks the session to start recording progress events.
        Called when the session is started.
        """
        self._init_handler()

    @version_requires("3.0")
    def flush_workflows(self):
        """This removes the handle on the workflow by the ``session`` """
        self._api.flush_workflows(self)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
