"""
ResultInfo
==========
"""
import traceback
import warnings

from enum import Enum, unique
from types import SimpleNamespace
from ansys.dpf.gate import (
    result_info_capi,
    result_info_grpcapi,
    integral_types,
    label_space_capi,
    label_space_grpcapi,
    object_handler,
    data_processing_grpcapi,
    data_processing_capi,
)

from ansys.dpf.core import collection
from ansys.dpf.core import server as server_module
from ansys.dpf.core import available_result, support
from ansys.dpf.core.cyclic_support import CyclicSupport
from ansys.dpf.core.label_space import LabelSpace
from ansys.dpf.core.check_version import version_requires


@unique
class physics_types(Enum):
    """
    ``'Physics_types'`` enumerates the different types of physics that an analysis can have.
    """
    mechanical = 0
    thermal = 1
    magnetic = 2
    electric = 3
    unknown_physics = 4


@unique
class analysis_types(Enum):
    """``'Analysis_types'`` enumerates the different types of analysis."""
    static = 0
    buckling = 1
    modal = 2
    harmonic = 3
    cms = 4
    transient = 5
    msup = 6
    substruct = 7
    spectrum = 8
    unknown_analysis = 9


class ResultInfo:
    """Represents the result information.

    This class describes the metadata of the analysis and the available results.

    Parameters
    ----------
    result_info : ctypes.c_void_p, ansys.grpc.dpf.result_info_pb2.ResultInfo message

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
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(capi=result_info_capi.ResultInfoCAPI,
                                                  grpcapi=result_info_grpcapi.ResultInfoGRPCAPI)

        # step3: init environment
        self._api.init_result_info_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if result_info is not None:
            if isinstance(result_info, ResultInfo):
                self._internal_obj = result_info._internal_obj
            else:
                self._internal_obj = result_info
        elif result_info is None:
            raise Exception("Result_info given is None")

    def __str__(self):
        try:
            txt = (
                    "%s analysis\n" % self.analysis_type.capitalize()
                    + "Unit system: %s\n" % self.unit_system
                    + "Physics Type: %s\n" % self.physics_type.capitalize()
                    + "Available results:\n"
            )
            for res in self.available_results:
                line = ["", "-", f'{res.name}: {res.native_location} {res.physical_name}']
                txt += "{0:^4} {1:^2} {2:<30}".format(*line) + "\n"

            return txt
        except Exception as e:
            from ansys.dpf.core.core import _description
            return _description(self._internal_obj, self._server)

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
        return self._api.result_info_get_analysis_type_name(self)

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
        'mechanical'

        """
        return self._get_physics_type()

    def _get_physics_type(self):
        """
        Returns
        -------
        physics_type : str
            Type of the physics, such as mechanical or electric.
        """
        return self._api.result_info_get_physics_type_name(self)

    @property
    def n_results(self):
        """Number of results."""
        return self._api.result_info_get_number_of_results(self)

    @property
    def unit_system(self):
        """Unit system of the result."""
        return self._api.result_info_get_unit_system_name(self)
        # return map_unit_system[self._api.result_info_get_ansys_unit_system_enum(self)]

    @property
    def cyclic_symmetry_type(self):
        """Cyclic symmetry type of the result.

        Return
        ------
        cyclic_symmetry_type : str
            Cyclic symmetry type of the results. Options are ``"single_stage"``,
            ``"multi_stage"``, and ``"not_cyclic"``.
        """
        return self._api.result_info_get_cyclic_symmetry_type(self)

    @property
    def has_cyclic(self):
        """Check the result file for cyclic symmetry.

        Return
        ------
        has_cyclic : bool
            Returns ``True`` if the result file has cyclic symmetry or is multistage.
        """
        return self._api.result_info_has_cyclic_symmetry(self)

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
        if self._api.result_info_has_cyclic_symmetry(self):
            cyclic_support = self._api.result_info_get_cyclic_support(self)
            return CyclicSupport(cyclic_support=cyclic_support, server=self._server)

    @property
    def unit_system_name(self):
        """Name of the unit system."""
        return self._api.result_info_get_unit_system_name(self)

    @property
    def solver_version(self):
        """Version of the solver."""
        major = integral_types.MutableInt32()
        minor = integral_types.MutableInt32()
        res = self._api.result_info_get_solver_version(self, major, minor)
        return str(int(major)) + "." + str(int(minor))

    @property
    def solver_date(self):
        """Date of the solver."""
        date = integral_types.MutableInt32()
        time = integral_types.MutableInt32()
        self._api.result_info_get_solve_date_and_time(self, date, time)
        return int(date)

    @property
    def solver_time(self):
        """Time of the solver."""
        date = integral_types.MutableInt32()
        time = integral_types.MutableInt32()
        self._api.result_info_get_solve_date_and_time(self, date, time)
        return int(time)

    @property
    def user_name(self):
        """Name of the user."""
        return self._api.result_info_get_user_name(self)

    @property
    def job_name(self):
        """Name of the job."""
        return self._api.result_info_get_job_name(self)

    @property
    def product_name(self):
        """Name of the product."""
        return self._api.result_info_get_product_name(self)

    @property
    def main_title(self):
        """Main title."""
        return self._api.result_info_get_main_title(self)

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

    @property
    def _data_processing_core_api(self):
        core_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI)
        core_api.init_data_processing_environment(self)
        return core_api

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

        name = self._api.result_info_get_result_name(self, numres)
        physic_name = self._api.result_info_get_result_physics_name(self, numres)
        dimensionality = self._api.result_info_get_result_dimensionality_nature(self, numres)
        n_comp = self._api.result_info_get_result_number_of_components(self, numres)
        unit_symbol = self._api.result_info_get_result_unit_symbol(self, numres)
        homogeneity = self._api.result_info_get_result_homogeneity(self, numres)
        try:
            loc_name = integral_types.MutableString(256)
            self._api.result_info_get_result_location(self, numres, loc_name)
            loc_name = str(loc_name)
        except AttributeError:
            if name in available_result._result_properties:
                loc_name = available_result._result_properties[name]["location"]
            else:
                loc_name = ""
        try:
            scripting_name = self._api.result_info_get_result_scripting_name(self, numres)
        except AttributeError:
            if name in available_result._result_properties:
                scripting_name = available_result._result_properties[name]["scripting_name"]
            else:
                scripting_name = available_result._remove_spaces(physic_name)
        num_sub_res = self._api.result_info_get_number_of_sub_results(self, numres)
        sub_res = {}
        for ires in range(num_sub_res):
            sub_res_name = self._api.result_info_get_sub_result_name(self, numres, ires)
            ssub_res_rec_name = integral_types.MutableString(256)
            self._api.result_info_get_sub_result_operator_name(self, numres,
                                                               ires,
                                                               ssub_res_rec_name)
            ssub_res_rec_name = str(ssub_res_rec_name)
            descr = self._api.result_info_get_sub_result_description(self, numres, ires)
            sub_res[sub_res_name] = [ssub_res_rec_name, descr]

        qualifiers = []
        if self._server.meet_version("5.0"):
            qual_obj = object_handler.ObjHandler(
                data_processing_api=self._data_processing_core_api,
                internal_obj=self._api.result_info_get_qualifiers_for_result(self, numres)
            )
            label_space_api = self._server.get_api_for_type(
                capi=label_space_capi.LabelSpaceCAPI, grpcapi=label_space_grpcapi.LabelSpaceGRPCAPI
            )
            num_qual_obj = label_space_api.list_label_spaces_size(qual_obj)
            for ires in range(num_qual_obj):
                qualifiers.append(
                    LabelSpace(
                        label_space=label_space_api.list_label_spaces_at(qual_obj, ires),
                        obj=self,
                        server=self._server
                    ))

        availableresult = SimpleNamespace(
            name=name, physicsname=physic_name, ncomp=n_comp,
            dimensionality=dimensionality, homogeneity=homogeneity,
            unit=unit_symbol, sub_res=sub_res,
            properties={
                "loc_name": loc_name,
                "scripting_name": scripting_name
            },
            qualifiers=qualifiers
        )
        return available_result.AvailableResult(availableresult)

    @property
    @version_requires("5.0")
    def available_qualifier_labels(self):
        """Returns a list of labels defining result qualifiers

        Returns
        -------
        list[str]

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection.StringCollection(
            collection=
            self._support_api.result_info_get_available_qualifier_labels_as_string_coll(self),
            server=self._server
        )
        return coll_obj.get_integral_entries()

    @version_requires("5.0")
    def qualifier_label_support(self, label):
        """Returns what supports an available qualifier label.

        Parameters
        ----------
        label: str

        Returns
        -------
        Support

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        return support.Support(
            support=self._api.result_info_get_qualifier_label_support(self, label),
            server=self._server
        )

    def __len__(self):
        try:
            return self.n_results
        except Exception as e:
            return 0

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

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
