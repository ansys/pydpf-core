import os
import logging
import time

import grpc

from ansys import dpf
from ansys.grpc.dpf import base_pb2, base_pb2_grpc

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')


if 'DPF_CONFIGURATION' in os.environ:
    CONFIGURATION = os.environ['DPF_CONFIGURATION']
else:
    CONFIGURATION = 'release'


class BaseService():
    """Base service connection to dpf server.  Used to load operators.

    Parameters
    ----------
    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.

    timeout : float, optional
        Fails when a connection takes longer than ``timeout`` seconds
        to initialize.

    Examples
    --------
    Connect to an existing DPF server
    >>> from ansys import dpf
    >>> dpf.core.BaseService(grpc.insecure_channel('127.0.0.1:50054'))
    """

    def __init__(self, channel=None, load_operators=True, timeout=5):
        """Initialize base service"""

        # internal flag to detect if server is running linux
        self._is_linux = False

        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        self._stub = self._connect(timeout)

        if load_operators:
            self._load_mapdl_operators()
            self._load_mesh_operators()
            # self._load_native_operators()

    def _connect(self, timeout=5):
        """Connect to dpf service within a given timeout"""
        stub = base_pb2_grpc.BaseServiceStub(self._channel)

        # verify connected
        if timeout is not None:
            state = grpc.channel_ready_future(self._channel)
            tstart = time.time()
            while (time.time() - tstart) < timeout and not state._matured:
                time.sleep(0.01)

            if not state._matured:
                raise IOError(f'Unable to connect to DPF instance at {self._channel}')

        return stub

    def load_library(self, filename, name='', symbol="LoadOperators"):
        """Dynamically load an operators library for dpf.core.

        Parameters
        ----------
        filename : str
            Filename of the operator library.

        name : str, optional
            Library name.  Probably optional

        Examples
        --------
        Load the mapdl operators for linux
        >>> from ansys import dpf
        >>> base = dpf.core.BaseService()
        >>> base.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')

        Load a new operators libary
        >>> base.load_library('someNewOperators.so', 'new_operators')

        """
        request = base_pb2.PluginRequest()
        request.name = name
        request.dllPath = filename
        request.symbol = symbol
        try:
            self._stub.Load(request)
        except Exception as e:
            raise IOError(f'Unable to load library "{filename}". File may not exist or'
                          f' is missing dependencies:\n{str(e)}')

    def _load_mapdl_operators(self):
        """Load the mapdl operators library"""
        if self._is_linux or self._is_linux is None:
            try:
                self.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')
                self._is_linux = True
                return
            except:
                self._is_linux = False

        if CONFIGURATION == "release":
            self.load_library('mapdlOperatorsCore.dll', 'mapdl_operators')
        else:
            self.load_library('mapdlOperatorsCoreD.dll', 'mapdl_operators')

    def _load_mesh_operators(self):
        """Load the mesh operators library"""
        if self._is_linux or self._is_linux is None:
            try:
                self.load_library('libmeshOperatorsCore.so', 'mesh_operators')
                self._is_linux = True
                return
            except:
                self._is_linux = False

        if CONFIGURATION == "release":
            self.load_library('meshOperatorsCore.dll', 'mesh_operators')
        else:
            self.load_library('meshOperatorsCoreD.dll', 'mesh_operators')

    # def _load_native_operators(self):
    #     """This is normally loaded at the start of the server"""
    #     if self._is_linux or self._is_linux is None:
    #         try:
    #             self.load_library('libAns.Dpf.Native.so', 'native')
    #             self._is_linux = True
    #             return
    #         except:
    #             self._is_linux = False

        # TODO: Add this
        # if CONFIGURATION == "release":
        #     self.load_library('meshOperatorsCore.dll', 'mesh_operators')
        # else:
        #     self.load_library('meshOperatorsCoreD.dll', 'mesh_operators')

    def _load_hdf5(self):
        """Load HDF5 operators"""
        operator_name = 'hdf5'

        if self._is_linux or self._is_linux is None:
            try:
                self.load_library('libAns.Dpf.Hdf5.so', operator_name)
                self._is_linux = True
                return
            except:
                self._is_linux = False

        self.load_library('Ans.Dpf.Hdf5.dll', operator_name)
