"""
ResultInfo
==========
"""
from enum import Enum

from ansys import dpf
from ansys.grpc.dpf import result_info_pb2, result_info_pb2_grpc
from ansys.dpf.core import available_result
from ansys.dpf.core.mapping_types import map_unit_system
from ansys.dpf.core.cyclic_support import CyclicSupport
from ansys.dpf.core.common import __write_enum_doc__
from ansys.dpf.core.cache import class_handling_cache


names = [m for m in result_info_pb2.PhysicsType.keys()]
physics_types = Enum("physics_types", names)
physics_types.__doc__ = __write_enum_doc__(
    physics_types,
    "``'Physics_types'`` enumerates the different types of physics that an analysis can have.",
)

names = [m for m in result_info_pb2.AnalysisType.keys()]
analysis_types = Enum("analysis_types", names)
analysis_types.__doc__ = __write_enum_doc__(
    physics_types, "``'Analysis_types'`` enumerates the different types of analysis."
)


@class_handling_cache
class ResultInfo:
    """Represents the result information.

    This class describes the metadata of the analysis and the available results.

    Parameters
    ----------
    result_info : ansys.grpc.dpf.result_info_pb2.ResultInfo message

     server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Explore the result info from the model

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> result_info = model.metadata.result_info # printable result_info

    >>> result_info.available_results[0].name
    'displacement'
    >>> result_info.available_results[0].homogeneity
    'length'

    """

    def __init__(self, result_info, server=None):
        """Initialize with a ResultInfo message"""
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()

        if isinstance(result_info, ResultInfo):
            self._message = result_info._message
        else:
            self._message = result_info

    def __str__(self):
        txt = (
            "%s analysis\n" % self.analysis_type.capitalize()
            + "Unit system: %s\n" % self.unit_system
            + "Physics Type: %s\n" % self.physics_type.capitalize()
            + "Available results:\n"
        )
        for res in self.available_results:
            line = ["", "-", res.name]
            txt += "{0:^4} {1:^2} {2:<30}".format(*line) + "\n"

        return txt

    @property
    def _names(self):
        return [item.name for item in self.available_results]

    def __contains__(self, value):
        return value in self._names

    @property
    def analysis_type(self):
        """Retrieves the analysis type.

        Returns
        -------
        analysis_type : str
            Type of the analysis, such as static or transient.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> result_info = model.metadata.result_info
        >>> result_info.analysis_type
        'static'

        """
        intOut = self._get_list().analysis_type
        return result_info_pb2.AnalysisType.Name(intOut).lower()

    @property
    def physics_type(self):
        """Type of the physics.

        Examples
        --------
        Mechanical result

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> result_info = model.metadata.result_info
        >>> result_info.physics_type
        'mecanic'

        """
        return self._get_physics_type()

    def _get_physics_type(self):
        """
        Returns
        -------
        physics_type : str
            Type of the physics, such as mechanical or electric.
        """
        intOut = self._get_list().physics_type
        return result_info_pb2.PhysicsType.Name(intOut).lower()

    # TODO: Depreciate
    @property
    def n_results(self):
        """Number of results."""
        return self._get_list().nresult

    @property
    def unit_system(self):
        """Unit system of the result."""
        val = self._get_list().unit_system
        return map_unit_system[val]

    @property
    def cyclic_symmetry_type(self):
        """Cyclic symmetry type of the result.

        Return
        ------
        cyclic_symmetry_type : str
            Cyclic symmetry type of the results. Options are ``"single_stage"``,
            ``"multi_stage"``, and ``"not_cyclic"``.
        """
        return self._get_list().cyc_info.cyclic_type

    @property
    def has_cyclic(self):
        """Check the result file for cyclic symmetry.

        Return
        ------
        has_cyclic : bool
            Returns ``True`` if the result file has cyclic symmetry or is multistage.
        """
        return self._get_list().cyc_info.has_cyclic

    @property
    def cyclic_support(self):
        """Cyclic expansion information for a result file that has cyclic symmetry or is multistage.

        Return
        ------
        cyclic_support : CyclicSupport

        Examples
        --------
        Get a cyclic support from a model.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> model = Model(multi_stage)
        >>> result_info = model.metadata.result_info
        >>> cyc_support = result_info.cyclic_support

        """
        tmp = self._get_list().cyc_info.cyc_support
        return CyclicSupport(cyclic_support=tmp, server=self._server)

    @property
    def unit_system_name(self):
        """Name of the unit system."""
        return self._get_list().unit_system_name

    @property
    def solver_version(self):
        """Version of the solver."""
        major = self._stub.List(self._message).solver_major_version
        minor = self._stub.List(self._message).solver_minor_version
        version = str(major) + "." + str(minor)
        return version

    @property
    def solver_date(self):
        """Date of the solver."""
        return self._get_list().solver_date

    @property
    def solver_time(self):
        """Time of the solver."""
        return self._get_list().solver_time

    @property
    def user_name(self):
        """Name of the user."""
        return self._get_list().user_name

    @property
    def job_name(self):
        """Name of the job."""
        return self._get_list().job_name

    @property
    def product_name(self):
        """Name of the product."""
        return self._get_list().product_name

    @property
    def main_title(self):
        """Main title."""
        return self._get_list().main_title

    @property
    def available_results(self):
        """Available results, containing all information about results
        present in the result files.

        Returns
        -------
        available_result : list[AvailableResult]
        """
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
            raise IndexError("There are only %d results" % len(self))
        elif numres < 0:
            raise IndexError("Result index must be greater than 0")

        request = result_info_pb2.AvailableResultRequest()
        request.result_info.CopyFrom(self._message)
        request.numres = numres
        res = self._stub.ListResult(request)

        return available_result.AvailableResult(res)

    def __len__(self):
        return self._get_list().nresult

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
        """Connect to the gRPC service containing the reader."""
        return result_info_pb2_grpc.ResultInfoServiceStub(self._server.channel)

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def _get_list(self):
        return self._stub.List(self._message)

    _to_cache = {_get_list: None, _get_result: None}
