"""
.. _ref_workflow_apis:

Workflow
========
"""
import logging
import traceback
import warnings

from enum import Enum
from ansys import dpf
from ansys.dpf.core import dpf_operator, inputs, outputs
from ansys.dpf.core.check_version import server_meet_version, version_requires
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    workflow_abstract_api,
    workflow_grpcapi,
    workflow_capi,
    data_processing_capi,
    data_processing_grpcapi,
    dpf_vector,
    object_handler,
)

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")


class Workflow:
    """Represents a workflow.

    A workflow is a black box containing operators and exposing only the necessary operator's
    inputs and outputs to compute a given algorithm.

    Parameters
    ----------
    server : DPFServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    workflow : ctypes.c_void_p, workflow_message_pb2.Workflow, optional

    Examples
    --------
    Create a generic workflow computing the minimum of displacement by chaining the ``'U'``
    and ``'min_max_fc'`` operators.

    >>> from ansys.dpf import core as dpf
    >>> disp_op = dpf.operators.result.displacement()
    >>> max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
    >>> workflow = dpf.Workflow()
    >>> workflow.add_operators([disp_op,max_fc_op])
    >>> workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
    >>> workflow.set_output_name("min", max_fc_op.outputs.field_min)
    >>> workflow.set_output_name("max", max_fc_op.outputs.field_max)


    >>> from ansys.dpf.core import examples
    >>> data_src = dpf.DataSources(examples.multishells_rst)
    >>> workflow.connect("data_sources", data_src)
    >>> min = workflow.get_output("min", dpf.types.field) # doctest: +SKIP
    >>> max = workflow.get_output("max", dpf.types.field) # doctest: +SKIP

    """

    def __init__(self, workflow=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api_instance = None  # see property self._api

        # step3: init environment
        self._api.init_workflow_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if workflow is not None:
            self._internal_obj = workflow
        else:
            if self._server.has_client():
                self._internal_obj = self._api.work_flow_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.work_flow_new()

    @property
    def _api(self) -> workflow_abstract_api.WorkflowAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=workflow_capi.WorkflowCAPI,
                grpcapi=workflow_grpcapi.WorkflowGRPCAPI
            )
        return self._api_instance

    def connect(self, pin_name, inpt, pin_out=0):
        """Connect an input on the workflow using a pin name.

        Parameters
        ----------
        pin_name : str
            Name of the pin to connect. This name should be
            exposed before with wf.set_input_name
        inpt : str, int, double, bool, list of int, list of doubles,
               Field, FieldsContainer, Scoping, ScopingsContainer,
        MeshedRegion, MeshesContainer, DataSources, Operator
            Object to connect to.
        pin_out : int, optional
            If the input is an operator, the output pin of the input operator.
            The default is ``0``.

        Examples
        --------
        Create a generic workflow computing the minimum of displacement by chaining the ``'U'``
        and ``'min_max_fc'`` operators.

        >>> from ansys.dpf import core as dpf
        >>> disp_op = dpf.operators.result.displacement()
        >>> max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
        >>> workflow = dpf.Workflow()
        >>> workflow.add_operators([disp_op,max_fc_op])
        >>> workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
        >>> workflow.set_output_name("min", max_fc_op.outputs.field_min)
        >>> workflow.set_output_name("max", max_fc_op.outputs.field_max)


        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> workflow.connect("data_sources", data_src)
        >>> min = workflow.get_output("min", dpf.types.field) # doctest: +SKIP
        >>> max = workflow.get_output("max", dpf.types.field) # doctest: +SKIP

        """
        if inpt is self:
            raise ValueError("Cannot connect to itself.")
        elif isinstance(inpt, dpf_operator.Operator):
            self._api.work_flow_connect_operator_output(self, pin_name, inpt, pin_out)
        elif isinstance(inpt, dpf_operator.Output):
            self._api.work_flow_connect_operator_output(self, pin_name, inpt._operator, inpt._pin)
        elif isinstance(inpt, list):
            from ansys.dpf.core import collection
            if server_meet_version("3.0", self._server):
                inpt = collection.Collection.integral_collection(inpt, self._server)
                self._api.work_flow_connect_collection_as_vector(self, pin_name, inpt)
            else:
                if all(isinstance(x, int) for x in inpt):
                    self._api.work_flow_connect_vector_int(self, pin_name, inpt, len(inpt))
                else:
                    self._api.work_flow_connect_vector_double(self, pin_name, inpt, len(inpt))
        elif isinstance(inpt, dict):
            from ansys.dpf.core import label_space
            label_space_to_con = label_space.LabelSpace(
                label_space=inpt,
                obj=self,
                server=self._server
            )
            self._api.work_flow_connect_label_space(self, pin_name, label_space_to_con)
        else:
            for type_tuple in self._type_to_input_method:
                if isinstance(inpt, type_tuple[0]):
                    if len(type_tuple) == 3:
                        inpt = type_tuple[2](inpt)
                    return type_tuple[1](self, pin_name, inpt)
            errormsg = f"input type {inpt.__class__} cannot be connected"
            raise TypeError(errormsg)

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
            (bool, self._api.work_flow_connect_bool),
            ((int, Enum), self._api.work_flow_connect_int),
            (str, self._api.work_flow_connect_string),
            (float, self._api.work_flow_connect_double),
            (field.Field, self._api.work_flow_connect_field),
            (property_field.PropertyField, self._api.work_flow_connect_property_field),
            (string_field.StringField, self._api.work_flow_connect_string_field),
            (scoping.Scoping, self._api.work_flow_connect_scoping),
            (collection.Collection, self._api.work_flow_connect_collection),
            (data_sources.DataSources, self._api.work_flow_connect_data_sources),
            (model.Model, self._api.work_flow_connect_data_sources,
             lambda obj: obj.metadata.data_sources),
            (cyclic_support.CyclicSupport, self._api.work_flow_connect_cyclic_support),
            (meshed_region.MeshedRegion, self._api.work_flow_connect_meshed_region),
            # TO DO: (result_info.ResultInfo, self._api.work_flow_connect_result_info),
            (time_freq_support.TimeFreqSupport, self._api.work_flow_connect_time_freq_support),
            (workflow.Workflow, self._api.work_flow_connect_workflow),
            (data_tree.DataTree, self._api.work_flow_connect_data_tree),
        ]

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
            (bool, self._api.work_flow_getoutput_bool),
            (int, self._api.work_flow_getoutput_int),
            (str, self._api.work_flow_getoutput_string),
            (float, self._api.work_flow_getoutput_double),
            (field.Field, self._api.work_flow_getoutput_field, "field"),
            (property_field.PropertyField, self._api.work_flow_getoutput_property_field,
             "property_field"),
            (string_field.StringField, self._api.work_flow_getoutput_string_field,
             "string_field"),
            (scoping.Scoping, self._api.work_flow_getoutput_scoping, "scoping"),
            (fields_container.FieldsContainer, self._api.work_flow_getoutput_fields_container,
             "fields_container"),
            (scopings_container.ScopingsContainer, self._api.work_flow_getoutput_scopings_container,
             "scopings_container"),
            (meshes_container.MeshesContainer, self._api.work_flow_getoutput_meshes_container,
             "meshes_container"),
            (data_sources.DataSources, self._api.work_flow_getoutput_data_sources, "data_sources"),
            (cyclic_support.CyclicSupport, self._api.work_flow_getoutput_cyclic_support,
             "cyclic_support"),
            (meshed_region.MeshedRegion, self._api.work_flow_getoutput_meshed_region, "mesh"),
            (result_info.ResultInfo, self._api.work_flow_getoutput_result_info, "result_info"),
            (time_freq_support.TimeFreqSupport, self._api.work_flow_getoutput_time_freq_support,
             "time_freq_support"),
            (workflow.Workflow, self._api.work_flow_getoutput_workflow, "workflow"),
            (data_tree.DataTree, self._api.work_flow_getoutput_data_tree, "data_tree"),
            (dpf_operator.Operator, self._api.work_flow_getoutput_operator, "operator"),
            (dpf_vector.DPFVectorInt, self._api.work_flow_getoutput_int_collection,
             lambda obj: collection.IntCollection(server=self._server,
                                                  collection=obj).get_integral_entries()),
            (dpf_vector.DPFVectorDouble, self._api.work_flow_getoutput_double_collection,
             lambda obj: collection.FloatCollection(server=self._server,
                                                    collection=obj).get_integral_entries()),
        ]

    def get_output(self, pin_name, output_type):
        """Retrieve the output of the operator on the pin number.
        A progress bar following the workflow state is printed.

        Parameters
        ----------
        pin_name : str
            Name of the pin to retrieve. This name should be
            exposed before with wf.set_output_name
        output_type : core.type enum
            Type of the requested output.
        """
        if server_meet_version("3.0", self._server):
            # handle progress bar
            self._server._session.add_workflow(self, "workflow")
            self._progress_thread = self._server._session.listen_to_progress()
        output_type = dpf_operator._write_output_type_to_type(output_type)
        out = None
        for type_tuple in self._type_to_output_method:
            if output_type is type_tuple[0]:
                if len(type_tuple) >= 3:
                    if isinstance(type_tuple[2], str):
                        parameters = {type_tuple[2]: type_tuple[1](self, pin_name)}
                        out = output_type(**parameters, server=self._server)
                    else:
                        out = type_tuple[2](type_tuple[1](self, pin_name))
                if out is None:
                    try:
                        out = output_type(type_tuple[1](self, pin_name), server=self._server)
                    except TypeError:
                        self._progress_thread = None
                        out = output_type(type_tuple[1](self, pin_name))
        if out is not None:
            self._progress_thread = None
            return out
        raise TypeError(f"{output_type} is not an implemented Operator's output")

    def set_input_name(self, name, *args):
        """Set the name of the input pin of the workflow to expose it for future connection.

        Parameters
        ----------
        name : str
            Name of the pin to connect. This name should be
            exposed before with wf.set_input_name
        *args : core.Operator, core.Input, int
            Operator with its input pin number or input to name.

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> workflow = dpf.Workflow()
        >>> disp_op = dpf.operators.result.displacement()
        >>> max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
        >>> workflow.set_input_name("data_sources", disp_op.inputs.data_sources)

        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> workflow.connect("data_sources", data_src)

        """
        pin = 0
        operator = None
        for arg in args:
            if isinstance(arg, inputs.Input):
                pin = arg._pin
                operator = arg._operator()
            elif isinstance(arg, dpf_operator.Operator):
                operator = arg
            elif isinstance(arg, int):
                pin = arg
        return self._api.work_flow_set_name_input_pin(self, operator, pin, name)

    def set_output_name(self, name, *args):
        """Set the name of the output pin of the workflow to expose it for future connection.

        Parameters
        ----------
        name : str
            Name of the pin to connect. This name should be
            exposed before with wf.set_input_name
        *args : core.Operator, core.Output, int
            Operator with its outpt pin number or output to name.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> workflow = dpf.Workflow()
        >>> model = dpf.Model(examples.simple_bar)
        >>> disp_op = model.results.displacement()
        >>> max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
        >>> workflow.set_output_name("contour", disp_op.outputs.fields_container)
        >>> fc = workflow.get_output("contour", dpf.types.fields_container) # doctest: +SKIP

        """
        pin = 0
        operator = None
        for arg in args:
            if isinstance(arg, outputs.Output):
                pin = arg._pin
                operator = arg._operator
            elif isinstance(arg, dpf_operator.Operator):
                operator = arg
            elif isinstance(arg, int):
                pin = arg
        return self._api.work_flow_set_name_output_pin(self, operator, pin, name)

    def add_operators(self, operators):
        """Add operators to the list of operators of the workflow.

        Parameters
        ----------
        operators : dpf.core.Operator, list of dpf.core.Operator
            Operators to add to the list.

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> workflow = dpf.Workflow()
        >>> disp_op = dpf.Operator("U")
        >>> max_op = dpf.Operator("min_max")
        >>> workflow.add_operators([disp_op, max_op])

        """
        if isinstance(operators, list):
            for op in operators:
                self.add_operator(op)
        elif isinstance(operators, dpf_operator.Operator):
            self.add_operator(operators)
        else:
            raise TypeError(
                "Operators to add to the workflow are expected to be of "
                f"type {type(list).__name__} or {type(dpf_operator.Operator).__name__}"
            )

    def add_operator(self, operator):
        """Add an operator to the list of operators of the workflow.

        Parameters
        ----------
        operator : dpf.core.Operator
            Operator to add to the list.

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> workflow = dpf.Workflow()
        >>> disp_op = dpf.Operator("U")
        >>> workflow.add_operator(disp_op)

        """
        self._api.work_flow_add_operator(self, operator)

    def record(self, identifier="", transfer_ownership=True):
        """Add the workflow to DPF's internal registry with an ID returned by this method.

        The workflow can be recovered by ``dpf.core.Workflow.get_recorded_workflow(id)``.

        Parameters
        ----------
        identifier : str, optional
            Name given to the workflow.
        transfer_ownership : bool
            Whether to transfer the ownership. The default is ``True``. If the ownership is
            not transferred, the workflow is removed from the internal registry
            as soon as the workflow has been recovered by its ID.

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> workflow = dpf.Workflow()
        >>> disp_op = dpf.Operator("U")
        >>> workflow.add_operator(disp_op)
        >>> # ...
        >>> id = workflow.record()
        >>> workflow_copy = dpf.Workflow.get_recorded_workflow(id)

        """
        return self._api.work_flow_record_instance(self, identifier, transfer_ownership)

    @staticmethod
    def get_recorded_workflow(id, server=None):
        """Retrieve a workflow registered (with workflow.record())

        Parameters
        ----------
        id : int
            ID given by the method "record".

        Returns
        ----------
        workflow : core.Workflow()
            workflow registered in dpf's registry (server side)

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> workflow = dpf.Workflow()
        >>> disp_op = dpf.Operator("U")
        >>> workflow.add_operator(disp_op)
        >>> # ...
        >>> id = workflow.record()
        >>> workflow_copy = dpf.Workflow.get_recorded_workflow(id)

        """
        wf = Workflow(workflow="None", server=server)
        if wf._server.has_client():
            wf._internal_obj = wf._api.work_flow_get_by_identifier_on_client(id, wf._server.client)
        else:
            wf._internal_obj = wf._api.work_flow_get_by_identifier(id)
        if wf._internal_obj is None:
            raise Exception("Unable to get this workflow from the registry")
        return wf

    @property
    def info(self):
        """Dictionary with the operator names and the exposed input and output names.

        Returns
        ----------
        info : dictionarry str->list str
            Dictionary with ``"operator_names"``, ``"input_names"``, and ``"output_names"`` key.
        """
        return {
            "operator_names": self.operator_names,
            "input_names": self.input_names,
            "output_names": self.output_names,
        }

    @property
    def operator_names(self):
        """List of the names of operators added in the workflow.

        Returns
        ----------
        names : list str
        """
        num = self._api.work_flow_number_of_operators(self)
        out = []
        for i in range(num):
            out.append(self._api.work_flow_operator_name_by_index(self, i))
        return out

    @property
    def input_names(self):
        """List of the input names exposed in the workflow with set_input_name.

        Returns
        ----------
        names : list str
        """
        num = self._api.work_flow_number_of_input(self)
        out = []
        for i in range(num):
            out.append(self._api.work_flow_input_by_index(self, i))
        return out

    @property
    def output_names(self):
        """List of the output names exposed in the workflow with set_output_name.

        Returns
        ----------
        names : list str
        """
        num = self._api.work_flow_number_of_output(self)
        out = []
        for i in range(num):
            out.append(self._api.work_flow_output_by_index(self, i))
        return out

    @version_requires("3.0")
    def connect_with(self, left_workflow, output_input_names=None):
        """Chain 2 workflows together so that they become one workflow.

        The one workflow contains all the operators, inputs, and outputs
        exposed in both workflows.

        Parameters
        ----------
        left_workflow : core.Workflow
            Second workflow's outputs to chained with this workflow's inputs.
        output_input_names : str tuple, str dict optional
            Input name of the left_workflow to be cained with the output name of this workflow.
            The default is ``None``, in which case the inputs in the left_workflow with the same
            names as the outputs of this workflow are chained.

        Examples
        --------
        ::

            +-------------------------------------------------------------------------------------------------+
            |  INPUT:                                                                                         |
            |                                                                                                 |
            |input_output_names = ("output","field" )                                                         |
            |                      _____________                                  ____________                |
            |  "data_sources"  -> |left_workflow| ->  "stuff"        "field" -> |     this   | -> "contour"   |
            |"time_scoping"    -> |             |             "mesh_scoping" -> |            |                |
            |                     |_____________| ->  "output"                  |____________|                |
            |  OUTPUT                                                                                         |
            |                    ____                                                                         |
            |"data_sources"  -> |this| ->  "stuff"                                                            |
            |"time_scoping" ->  |    | ->  "contour"                                                          |
            |"mesh_scoping" ->  |____| -> "output"                                                            |
            +-------------------------------------------------------------------------------------------------+ # noqa: E501

        Notes
        -----
        Function available with server's version starting at 3.0.

        """
        if output_input_names:
            core_api = self._server.get_api_for_type(
                capi=data_processing_capi.DataProcessingCAPI,
                grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI)
            map = object_handler.ObjHandler(
                data_processing_api=core_api,
                internal_obj=self._api.workflow_create_connection_map_for_object(self)
            )
            if isinstance(output_input_names, tuple):
                self._api.workflow_add_entry_connection_map(
                    map, output_input_names[0], output_input_names[1]
                )
            elif isinstance(output_input_names, dict):
                for key in output_input_names:
                    self._api.workflow_add_entry_connection_map(
                        map, key, output_input_names[key]
                    )
            else:
                raise TypeError("output_input_names argument is expect"
                                "to be either a str tuple or a str dict")
            self._api.work_flow_connect_with_specified_names(self, left_workflow, map)
        else:
            self._api.work_flow_connect_with(self, left_workflow)

    @version_requires("3.0")
    def create_on_other_server(self, *args, **kwargs):
        """Create a new instance of a workflow on another server. The new
        Workflow has the same operators, exposed inputs and output pins as
        this workflow. Connections between operators and between data and
        operators are kept (except for exposed pins).

        Parameters
        ----------
        server : server.LegacyGrpcServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.

        ip : str, optional
            ip address on which the new instance should be created (always put
            a port in args as well)

        port : str, int , optional

        address: str, optional
            address on which the new instance should be created ("ip:port")

        Returns
        -------
        Workflow

        Examples
        --------
        Create a generic Workflow computing the minimum of displacement by chaining the ``'U'``
        and ``'min_max_fc'`` operators.

        >>> from ansys.dpf import core as dpf
        >>> disp_op = dpf.operators.result.displacement()
        >>> max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
        >>> workflow = dpf.Workflow()
        >>> workflow.add_operators([disp_op,max_fc_op])
        >>> workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
        >>> workflow.set_output_name("min", max_fc_op.outputs.field_min)
        >>> workflow.set_output_name("max", max_fc_op.outputs.field_max)
        >>> #other_server = dpf.start_local_server(as_global=False)
        >>> #new_workflow = workflow.create_on_other_server(server=other_server)
        >>> #assert 'data_sources' in new_workflow.input_names

        """
        server = None
        address = None
        for arg in args:
            if isinstance(arg, dpf.core.server_types.BaseServer):
                server = arg
            elif isinstance(arg, str):
                address = arg

        if "ip" in kwargs:
            address = kwargs["ip"] + ":" + str(kwargs["port"])
        if "address" in kwargs:
            address = kwargs["address"]
        if "server" in kwargs:
            server = kwargs["server"]
        if server:
            text_stream = self._api.work_flow_write_to_text(self)
            wf = Workflow(workflow="None", server=server)
            if wf._server.has_client():
                wf._internal_obj = wf._api.work_flow_create_from_text_on_client(
                    text_stream,
                    wf._server.client)
            else:
                wf._internal_obj = wf._api.work_flow_create_from_text(text_stream)
            return wf
        elif address:
            internal_obj = self._api.work_flow_get_copy_on_other_client(self, address, "grpc")
            return Workflow(workflow=internal_obj, server=self._server)
        else:
            raise ValueError("a connection address (either with address input"
                             "or both ip and port inputs) or a server is required")

    def __del__(self):
        try:
            if self._internal_obj is not None and self._internal_obj != "None":
                self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description
        return _description(self._internal_obj, self._server)
