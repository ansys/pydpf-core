from enum import Enum

from ansys import dpf
from ansys.grpc.dpf import result_info_pb2, result_info_pb2_grpc
from ansys.dpf.core import available_result
from ansys.dpf.core.mapping_types import map_unit_system

names = [m for m in result_info_pb2.PhysicsType.keys()]
physics_types = Enum('physics_types', names)

names = [m for m in result_info_pb2.AnalysisType.keys()]
analysis_types = Enum('analysis_types', names)


class ResultInfo:
    """Class representation the result information.

    Parameters
    ----------
    result_info : ansys.grpc.dpf.result_info_pb2.ResultInfo message

    channel : channel, optional
        Channel connected to the remote or local
        instance. Defaults to the global channel.

    """

    def __init__(self, result_info, channel=None):
        """Initialize with a ResultInfo message"""
        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        self._stub = self._connect()

        if isinstance(result_info, ResultInfo):
            self._message = result_info._message
        else:
            self._message = result_info

        self._names = [item.name for item in self.available_results]

    def __str__(self):
        txt = '%s analysis\n' % self.analysis_type.capitalize() +\
              'Unit system: %s\n' % self.unit_system +\
              'Physics Type: %s\n' % self.physics_type.capitalize() +\
              'Available results:\n'
        for res in self.available_results:
            line = ['', '-', res.name]
            txt += '{0:^4} {1:^2} {2:<30}'.format(*line)+'\n'

        return txt

    def __contains__(self, value):
        return value in self._names

    @property
    def analysis_type(self):
        """Returns the analysis type.

        Returns
        -------
        analysis_type : str
            type of analysis (ex : static, transient...)
        """
        intOut = self._stub.List(self._message).analysis_type
        return result_info_pb2.AnalysisType.Name(intOut).lower()

    @property
    def physics_type(self):
        """Type of physics.

        Examples
        --------
        Mechical result

        >>> scoping.physics_type
        mecanic

        Electrical result

        >>> scoping.physics_type
        electric
        """
        intOut = self._stub.List(self._message).physics_type
        return result_info_pb2.PhysicsType.Name(intOut).lower()

    def get_physics_type(self):
        """
        Returns
        -------
        analysis_type : str
            type of physics (ex : mecanic, electric...)
        """
        intOut = self._stub.List(self._message).physics_type
        return result_info_pb2.PhysicsType.Name(intOut).lower()

    # TODO: Depreciate
    @property
    def n_results(self):
        return self._stub.List(self._message).nresult

    @property
    def unit_system(self):
        """Unit system"""
        val = self._stub.List(self._message).unit_system
        return map_unit_system[val]

    @property
    def available_results(self):
        """Available results"""
        out = []
        for i in range(len(self)):
            out.append(self._get_result(i))
        return out

    def _get_result(self, numres):
        """
        Parameters
        ----------
        numres : int
            Index of the requested result.

        Returns
        -------
        result : Result
        """
        if numres >= len(self):
            raise IndexError('There are only %d results' % len(self))
        elif numres < 0:
            raise IndexError('Result index must be greater than 0')

        request = result_info_pb2.AvailableResultRequest()
        request.result_info.CopyFrom(self._message)
        request.numres = numres
        res = self._stub.ListResult(request)

        return available_result.AvailableResult(res)

    def __len__(self):
        return self._stub.List(self._message).nresult

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, key):
        if isinstance(key, int):
            index = key
        elif isinstance(key, str):
            if key not in self._names:
                raise ValueError('Invalid key "%s"' % key)
            index = self._names.index(key)
        else:
            raise TypeError('"%s" is an invalid keytype' % type(key))

        return self._get_result(index)

    def _connect(self):
        """Connect to the grpc service containing the reader"""
        return result_info_pb2_grpc.ResultInfoServiceStub(self._channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass
