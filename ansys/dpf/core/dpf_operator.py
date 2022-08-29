"""
.. _ref_operator:

Operator
========
"""

import logging
import os
import traceback
import warnings

from enum import Enum
from ansys.dpf.core.check_version import version_requires, server_meet_version
from ansys.dpf.core.config import Config
from ansys.dpf.core.errors import DpfVersionNotSupported
from ansys.dpf.core.inputs import Inputs
from ansys.dpf.core.mapping_types import types
from ansys.dpf.core.common import types_enum_to_types
from ansys.dpf.core.outputs import Output, Outputs, _Outputs
from ansys.dpf.core import server as server_module
from ansys.dpf.core.operator_specification import Specification
from ansys.dpf.gate import operator_capi, operator_abstract_api, operator_grpcapi, \
    data_processing_capi, data_processing_grpcapi, collection_capi, collection_grpcapi, \
    dpf_vector, object_handler

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")


class _SubOperator:
    def __init__(self, op_name, op_to_connect):
        self.op_name = op_name
        self.op = Operator(self.op_name, server=op_to_connect._server)
        if op_to_connect.inputs is not None:
            for key in op_to_connect.inputs._connected_inputs:
                inpt = op_to_connect.inputs._connected_inputs[key]
                if type(inpt).__name__ == "dict":
                    for keyout in inpt:
                        if inpt[keyout]() is not None:
                            self.op.connect(key, inpt[keyout](), keyout)
                else:
                    self.op.connect(key, inpt())

    def __call__(self):
        return self.op


class Operator:
    """Represents an operator, which is an elementary operation.

    The operator is the only object used to create and transform
    data. When the operator is evaluated, it processes the
    input information to compute its output with respect to its
    description.

    Parameters
    ----------
    name : str
        Name of the operator. For example, ``"U"``. You can use the
        ``"html_doc"`` operator to retrieve a list of existing operators.

    config : Config, optional
        The Configuration allows to customize how the operation
        will be processed by the operator. The default is ``None``.

    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create an operator from the library of operators.

    >>> from ansys.dpf import core as dpf
    >>> disp_oper = dpf.operators.result.displacement()

    Create an operator from a model.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> model = Model(examples.static_rst)
    >>> disp_oper = model.results.displacement()

    """

    def __init__(self, name, config=None, server=None):
        """Initialize the operator with its name by connecting to a stub."""
        self.name = name
        self._internal_obj = None
        self._description = None
        self._inputs = None

        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api_instance = None  # see _api property

        # step3: init environment
        self._api.init_operator_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it (server)
        if self._server.has_client():
            self._internal_obj = self._api.operator_new_on_client(self.name, self._server.client)
        else:
            self._internal_obj = self._api.operator_new(self.name)

        if self._internal_obj is None:
            raise KeyError(f"The operator {self.name} doesn't exist in the registry")

        self._spec = Specification(operator_name=self.name, server=self._server)
        # add dynamic inputs
        if len(self._spec.inputs) > 0 and self._inputs is None:
            self._inputs = Inputs(self._spec.inputs, self)

        # step4: if object exists: take instance (config)
        if config:
            self.config = config

        self._description = self._spec.description
        self._progress_bar = False

    @property
    def _api(self) -> operator_abstract_api.OperatorAbstractAPI:
        if self._api_instance is None:
            self._api_instance = self._server.get_api_for_type(
                capi=operator_capi.OperatorCAPI,
                grpcapi=operator_grpcapi.OperatorGRPCAPI
            )
        return self._api_instance

    def _add_sub_res_operators(self, sub_results):
        """Dynamically add operators for instantiating subresults.

        Subresults for new operators are connected to the parent
        operator's inputs when created but are then completely
        independent of them.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> model = Model(examples.static_rst)
        >>> disp_oper = model.results.displacement()
        >>> disp_oper = model.results.displacement()
        >>> disp_x = model.results.displacement().X()
        >>> disp_y = model.results.displacement().Y()
        >>> disp_z = model.results.displacement().Z()

        """

        for result_type in sub_results:
            try:
                setattr(self, result_type["name"], _SubOperator(result_type["operator name"], self))
            except KeyError:
                pass

    @property
    def _outputs(self):
        if self._spec and len(self._spec.outputs) != 0:
            return Outputs(self._spec.outputs, self)

    @_outputs.setter
    def _outputs(self, value):
        # the Operator should not hold a reference on its outputs because outputs hold a reference
        # on the Operator
        pass

    @property
    @version_requires("3.0")
    def progress_bar(self) -> bool:
        """With this property, the user can choose to print a progress bar when
        the operator's output is requested, default is False"""
        return self._progress_bar

    @progress_bar.setter
    def progress_bar(self, value: bool) -> None:
        self._progress_bar = value

    def connect(self, pin, inpt, pin_out=0):
        """Connect an input on the operator using a pin number.

        Parameters
        ----------
        pin : int
            Number of the input pin.

        inpt : str, int, double, bool, list[int], list[float], Field, FieldsContainer, Scoping,
        ScopingsContainer, MeshedRegion, MeshesContainer, DataSources, CyclicSupport, Outputs
            Operator, os.PathLike Object to connect to.

        pin_out : int, optional
            If the input is an operator, the output pin of the input operator. The default is ``0``.

        Examples
        --------
        Compute the minimum of displacement by chaining the ``"U"`` and ``"min_max_fc"`` operators.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> max_fc_op = dpf.operators.min_max.min_max_fc()
        >>> max_fc_op.inputs.connect(disp_op.outputs)
        >>> max_field = max_fc_op.outputs.field_max()
        >>> max_field.data
        DPFArray([[0.59428386, 0.00201751, 0.0006032 ]]...

        """
        if inpt is self:
            raise ValueError("Cannot connect to itself.")
        elif isinstance(inpt, Operator):
            self._api.operator_connect_operator_output(self, pin, inpt, pin_out)
        elif isinstance(inpt, Output):
            self._api.operator_connect_operator_output(self, pin, inpt._operator, inpt._pin)
        elif isinstance(inpt, list):
            from ansys.dpf.core import collection
            if server_meet_version("3.0", self._server):
                inpt = collection.Collection.integral_collection(inpt, self._server)
                self._api.operator_connect_collection_as_vector(self, pin, inpt)
            else:
                if all(isinstance(x, int) for x in inpt):
                    self._api.operator_connect_vector_int(self, pin, inpt, len(inpt))
                else:
                    self._api.operator_connect_vector_double(self, pin, inpt, len(inpt))
        elif isinstance(inpt, dict):
            from ansys.dpf.core import label_space
            label_space_to_con = label_space.LabelSpace(
                label_space=inpt,
                obj=self,
                server=self._server
            )
            self._api.operator_connect_label_space(self, pin, label_space_to_con)
        else:
            if isinstance(inpt, os.PathLike):
                inpt = str(inpt)
            for type_tuple in self._type_to_input_method:
                if isinstance(inpt, type_tuple[0]):
                    if len(type_tuple) == 3:
                        inpt = type_tuple[2](inpt)
                    return type_tuple[1](self, pin, inpt)
            errormsg = f"input type {inpt.__class__} cannot be connected"
            raise TypeError(errormsg)

    @property
    def _type_to_output_method(self):
        from ansys.dpf.core import (
            cyclic_support,
            data_sources,
            field,
            fields_container,
            meshed_region,
            meshes_container,
            property_field,
            string_field,
            result_info,
            scoping,
            scopings_container,
            time_freq_support,
            data_tree,
            workflow,
            collection,
        )
        return [
            (bool, self._api.operator_getoutput_bool),
            (int, self._api.operator_getoutput_int),
            (str, self._api.operator_getoutput_string),
            (float, self._api.operator_getoutput_double),
            (field.Field, self._api.operator_getoutput_field, "field"),
            (property_field.PropertyField, self._api.operator_getoutput_property_field,
             "property_field"),
            (string_field.StringField, self._api.operator_getoutput_string_field,
             "string_field"),
            (scoping.Scoping, self._api.operator_getoutput_scoping, "scoping"),
            (fields_container.FieldsContainer, self._api.operator_getoutput_fields_container,
             "fields_container"),
            (scopings_container.ScopingsContainer, self._api.operator_getoutput_scopings_container,
             "scopings_container"),
            (meshes_container.MeshesContainer, self._api.operator_getoutput_meshes_container,
             "meshes_container"),
            (data_sources.DataSources, self._api.operator_getoutput_data_sources,
             "data_sources"),
            (cyclic_support.CyclicSupport, self._api.operator_getoutput_cyclic_support,
             "cyclic_support"),
            (meshed_region.MeshedRegion, self._api.operator_getoutput_meshed_region, "mesh"),
            (result_info.ResultInfo, self._api.operator_getoutput_result_info, "result_info"),
            (time_freq_support.TimeFreqSupport, self._api.operator_getoutput_time_freq_support,
             "time_freq_support"),
            (workflow.Workflow, self._api.operator_getoutput_workflow, "workflow"),
            (data_tree.DataTree, self._api.operator_getoutput_data_tree, "data_tree"),
            (Operator, self._api.operator_getoutput_operator, "operator"),
            (dpf_vector.DPFVectorInt, self._api.operator_getoutput_int_collection,
             lambda obj: collection.IntCollection(
                 server=self._server, collection=obj
             ).get_integral_entries()),
            (dpf_vector.DPFVectorDouble, self._api.operator_getoutput_double_collection,
             lambda obj: collection.FloatCollection(
                 server=self._server, collection=obj
             ).get_integral_entries()),
        ]

    @property
    def _type_to_input_method(self):
        from ansys.dpf.core import (
            cyclic_support,
            data_sources,
            field,
            collection,
            meshed_region,
            property_field,
            string_field,
            scoping,
            time_freq_support,
            data_tree,
            workflow,
            model,
        )
        return [
            (bool, self._api.operator_connect_bool),
            ((int, Enum), self._api.operator_connect_int),
            (str, self._api.operator_connect_string),
            (float, self._api.operator_connect_double),
            (field.Field, self._api.operator_connect_field),
            (property_field.PropertyField, self._api.operator_connect_property_field),
            (string_field.StringField, self._api.operator_connect_string_field),
            (scoping.Scoping, self._api.operator_connect_scoping),
            (collection.Collection, self._api.operator_connect_collection),
            (data_sources.DataSources, self._api.operator_connect_data_sources),
            (model.Model, self._api.operator_connect_data_sources,
             lambda obj: obj.metadata.data_sources),
            (cyclic_support.CyclicSupport, self._api.operator_connect_cyclic_support),
            (meshed_region.MeshedRegion, self._api.operator_connect_meshed_region),
            # TO DO: (result_info.ResultInfo, self._api.operator_connect_result_info),
            (time_freq_support.TimeFreqSupport, self._api.operator_connect_time_freq_support),
            (workflow.Workflow, self._api.operator_connect_workflow),
            (data_tree.DataTree, self._api.operator_connect_data_tree),
            (Operator, self._api.operator_connect_operator_as_input),
        ]

    def get_output(self, pin=0, output_type=None):
        """Retrieve the output of the operator on the pin number.

        To activate the progress bar for server version higher or equal to 3.0,
        use ``my_op.progress_bar=True``

        Parameters
        ----------
        pin : int, optional
            Number of the output pin. The default is ``0``.
        output_type : :class:`ansys.dpf.core.common.types`, type,  optional
            Requested type of the output. The default is ``None``.

        Returns
        -------
        type
            Output of the operator.
        """
        output_type = _write_output_type_to_type(output_type)
        if self._server.meet_version("3.0") and self.progress_bar:
            self._server._session.add_operator(self, pin, "operator")
            self._progress_thread = self._server._session.listen_to_progress()
        if output_type is None:
            return self._api.operator_run(self)
        out = None
        for type_tuple in self._type_to_output_method:
            if output_type is type_tuple[0]:
                if len(type_tuple) >= 3:
                    if isinstance(type_tuple[2], str):
                        parameters = {type_tuple[2]: type_tuple[1](self, pin)}
                        out = output_type(**parameters, server=self._server)
                    else:
                        out = type_tuple[2](type_tuple[1](self, pin))
                if out is None:
                    try:
                        return output_type(type_tuple[1](self, pin), server=self._server)
                    except TypeError:
                        self._progress_thread = None
                        return output_type(type_tuple[1](self, pin))
        if out is not None:
            self._progress_thread = None
            return out
        raise TypeError(f"{output_type} is not an implemented Operator's output")

    @property
    def config(self):
        """Copy of the operator's current configuration.

        You can modify the copy of the configuration and then use ``operator.config = new_config``
        or create an operator with the new configuration as a parameter.

        Returns
        ----------
        :class:`ansys.dpf.core.config.Config`
            Copy of the operator's current configuration.
        """
        config = self._api.operator_get_config(self)
        return Config(config=config, server=self._server, spec=self._spec)

    @config.setter
    def config(self, value):
        """Change the configuration of the operator.

        If the operator is up to date, changing the configuration
        doesn't make it not up to date.

        Parameters
        ----------
        value : Config
        """
        self._api.operator_set_config(self, value)

    @property
    def inputs(self):
        """Inputs connected to the operator.

        Returns
        --------
        :class:`ansys.dpf.core.inputs`
            Inputs connected to the operator.

        Examples
        --------
        Use the displacement operator.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)

        """

        return self._inputs

    @property
    def outputs(self):
        """Outputs from the operator's evaluation.

        Returns
        --------
        :class:`ansys.dpf.core.outputs`
            Outputs from the operator's evaluation.

        Examples
        --------
        Use the displacement operator.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> disp_fc = disp_op.outputs.fields_container()

        """
        return self._outputs

    @staticmethod
    def default_config(name, server=None):
        """Retrieve the default configuration for an operator.

        You can change the copy of the default configuration to meet your needs
        before instantiating the operator.
        The Configuration allows to customize how the operation
        will be processed by the operator.

        Parameters
        ----------
        name : str
            Name of the operator.  For example ``"U"``. You can use the
            ``"html_doc"`` operator to retrieve a list of existing operators.
        server : server.DPFServer, optional
            Server with the channel connected to the remote or local instance. The
            default is ``None``, in which case an attempt is made to use the global
            server.

        Returns
        -------
        :class"`ansys.dpf.core.config.Config`
            Default configuration for the operator.

        """
        return Config(operator_name=name, server=server)

    def __del__(self):
        try:
            if self._internal_obj is not None:
                self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def run(self):
        """Evaluate this operator."""
        self.get_output()

    def eval(self, pin=None):
        """Evaluate this operator.

        Parameters
        ----------
        pin : int
            Number of the output pin. The default is ``None``.

        Returns
        -------
        output : FieldsContainer, Field, MeshedRegion, Scoping
            Returns the first output of the operator by default and the output of a
            given pin when specified. Or, it only evaluates the operator without output.

        Examples
        --------
        Use the ``eval`` method.

        >>> from ansys.dpf import core as dpf
        >>> import ansys.dpf.core.operators.math as math
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> normfc = math.norm_fc(disp_op).eval()

        """

        if not pin:
            if self.outputs != None and len(self.outputs._outputs) > 0:
                return self.outputs._outputs[0]()
            else:
                self.run()
        else:
            for output in self.outputs._outputs:
                if output._pin == pin:
                    return output()

    def _find_outputs_corresponding_pins(
            self, type_names, inpt, pin, corresponding_pins
    ):
        from ansys.dpf.core.results import Result
        for python_name in type_names:
            # appears to be an issue on Linux.  This check is here
            # because cpp mappings are a single type mapping and
            # sometimes the spec contains 'B' instead of 'bool'
            if python_name == "B":
                python_name = "bool"

            if type(inpt).__name__ == python_name:
                corresponding_pins.append(pin)
            elif isinstance(inpt, (_Outputs, Operator, Result)):
                if isinstance(inpt, Operator):
                    output_pin_available = inpt.outputs._get_given_output([python_name])
                elif isinstance(inpt, Result):
                    output_pin_available = inpt().outputs._get_given_output([python_name])
                else:
                    output_pin_available = inpt._get_given_output([python_name])
                for outputpin in output_pin_available:
                    corresponding_pins.append((pin, outputpin))
            elif isinstance(inpt, Output):
                for inpttype in inpt._python_expected_types:
                    if inpttype == python_name:
                        corresponding_pins.append(pin)
                if python_name == "Any":
                    corresponding_pins.append(pin)
            elif python_name == "Any":
                corresponding_pins.append(pin)

    def __add__(self, fields_b):
        """Add two fields or two fields containers.

        Returns
        -------
        add : operators.math.add_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "add_fc"):
            op = operators.math.add_fc(self, fields_b, server=self._server)
        else:
            op = dpf_operator.Operator("add_fc", server=self._server)
            op.connect(0, self)
            op.connect(1, fields_b)
        return op

    def __sub__(self, fields_b):
        """Subtract two fields or two fields containers.

        Returns
        -------
        minus : operators.math.minus_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "minus_fc"):
            op = operators.math.minus_fc(server=self._server)
        else:
            op = dpf_operator.Operator("minus_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, fields_b)
        return op

    def __pow__(self, value):
        if value != 2:
            raise ValueError('Only the value "2" is supported.')
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "sqr_fc"):
            op = operators.math.sqr_fc(server=self._server)
        else:
            op = dpf_operator.Operator("sqr_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    def __mul__(self, value):
        """Multiply two fields or two fields containers.

        Returns
        -------
        mul : operators.math.generalized_inner_product_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(
                operators.math, "generalized_inner_product_fc"
        ):
            op = operators.math.generalized_inner_product_fc(server=self._server)
        else:
            op = dpf_operator.Operator(
                "generalized_inner_product_fc", server=self._server
            )
        op.connect(0, self)
        op.connect(1, value)
        return op

    @staticmethod
    def operator_specification(op_name, server=None):
        """Documents an Operator with its description (what the Operator does),
        its inputs and outputs and some properties"""
        return Specification(operator_name=op_name, server=server)

    @property
    def specification(self):
        """Returns the Specification (or documentation) of this Operator

        Returns
        -------
        Specification
        """
        if isinstance(self._spec, Specification):
            return self._spec
        else:
            return Specification(operator_name=self.name, server=self._server)

    def __truediv__(self, inpt):
        if isinstance(inpt, Operator):
            op = Operator("div")
            op.connect(0, self, 0)
            op.connect(1, inpt, 0)
        elif isinstance(inpt, float):
            op = Operator("scale")
            op.connect(0, self, 0)
            op.connect(1, 1.0 / inpt)
        return op


def available_operator_names(server=None):
    """Returns the list of operator names available in the server.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
    list

    Notes
    -----
    Function available with server's version starting at 3.0. Not available for server
    of type GrpcServer.

    """
    if server is None:
        server = server_module._global_server()

    if not server.meet_version("3.0"):
        raise DpfVersionNotSupported("3.0")

    api = server.get_api_for_type(
        capi=data_processing_capi.DataProcessingCAPI,
        grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI
    )
    api.init_data_processing_environment(server)  # creates stub when gRPC
    coll_api = server.get_api_for_type(
        capi=collection_capi.CollectionCAPI,
        grpcapi=collection_grpcapi.CollectionGRPCAPI)
    coll_api.init_collection_environment(server)

    if server.has_client():
        coll_obj = object_handler.ObjHandler(
            data_processing_api=api,
            internal_obj=api.data_processing_list_operators_as_collection_on_client(
                server.client
            ))
    else:
        coll_obj = object_handler.ObjHandler(
            data_processing_api=api,
            internal_obj=api.data_processing_list_operators_as_collection()
        )
    num = coll_api.collection_get_size(coll_obj)
    out = []
    for i in range(num):
        out.append(coll_api.collection_get_string_entry(coll_obj, i))
    return out


def _write_output_type_to_type(output_type):
    if isinstance(output_type, str):
        output_type = types[output_type]

    if isinstance(output_type, types):
        try:
            return types_enum_to_types()[output_type]
        except KeyError as e:
            raise TypeError(f"{output_type} is not an implemented Operator's output")
    return output_type
