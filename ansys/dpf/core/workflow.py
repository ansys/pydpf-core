"""
Workflow
========
Interface to underlying gRPC workflow.
"""
import logging

from ansys import dpf
from ansys.dpf.core import dpf_operator, inputs, outputs
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.check_version import server_meet_version, version_requires
from ansys.dpf.core.common import types

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")


class Workflow:
    """Represents a workflow.

    A workflow is a black box containing operators and exposing only the necessary operator's
    inputs and outputs to compute a given algorithm.

    Parameters
    ----------
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    workflow :  workflow_message_pb2.Workflow

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
    >>> min = workflow.get_output("min", dpf.types.field)
    >>> max = workflow.get_output("max", dpf.types.field)

    """

    def __init__(self, workflow=None, server=None):
        """Initialize the workflow by connecting to a stub."""
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()

        self._message = workflow

        from ansys.grpc.dpf import workflow_pb2
        remote_copy_needed = server_meet_version("3.0", self._server) \
                             and isinstance(workflow, workflow_pb2.RemoteCopyRequest)
        if isinstance(workflow, str):
            self.__create_from_stream(workflow)
        elif workflow is None or remote_copy_needed:
            self.__send_init_request(workflow)

    @protect_grpc
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
        >>> min = workflow.get_output("min", dpf.types.field)
        >>> max = workflow.get_output("max", dpf.types.field)

        """
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdateConnectionRequest()
        request.wf.CopyFrom(self._message)
        request.pin_name = pin_name
        tmp = _fillConnectionRequestMessage(request, inpt, self._server, pin_out)
        self._stub.UpdateConnection(request)

    @protect_grpc
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
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.WorkflowEvaluationRequest()
        request.wf.CopyFrom(self._message)
        request.pin_name = pin_name

        if output_type is not None:
            _write_output_type_to_proto_style(output_type, request)
            if server_meet_version("3.0", self._server):
                # handle progress bar
                self._server._session.add_workflow(self, "workflow")
                out_future = self._stub.Get.future(request)
                while out_future.is_active():
                    self._server._session.listen_to_progress()
                out = out_future.result()
            else:
                out = self._stub.Get(request)
            return _convertOutputMessageToPythonInstance(
                out,
                output_type,
                self._server
            )
        else:
            raise ValueError(
                "please specify an output type to get the workflow's output"
            )

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
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(self._message)
        input_request = workflow_pb2.OperatorNaming()
        input_request.name = name
        input_request.pin = 0
        for arg in args:
            if isinstance(arg, inputs.Input):
                input_request.pin = arg._pin
                input_request.operator.CopyFrom(arg._operator._internal_obj)
            elif isinstance(arg, dpf_operator.Operator):
                input_request.operator.CopyFrom(arg._internal_obj)
            elif isinstance(arg, int):
                input_request.pin = arg
        request.inputs_naming.extend([input_request])
        self._stub.UpdatePinNames(request)

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
        >>> fc = workflow.get_output("contour", dpf.types.fields_container)

        """
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(self._message)
        output_request = workflow_pb2.OperatorNaming()
        output_request.name = name
        output_request.pin = 0
        for arg in args:
            if isinstance(arg, outputs.Output):
                output_request.pin = arg._pin
                output_request.operator.CopyFrom(arg._operator._internal_obj)
            elif isinstance(arg, dpf_operator.Operator):
                output_request.operator.CopyFrom(arg._internal_obj)
            elif isinstance(arg, int):
                output_request.pin = arg
        request.outputs_naming.extend([output_request])
        self._stub.UpdatePinNames(request)

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
        >>> workflow.add_operator([disp_op,max_op])

        """
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.AddOperatorsRequest()
        request.wf.CopyFrom(self._message)
        if isinstance(operators, list):
            request.operators.extend([op._internal_obj for op in operators])
        elif isinstance(operators, dpf_operator.Operator):
            request.operators.extend([operators._internal_obj])
        else:
            raise TypeError(
                "Operators to add to the workflow are expected to be of "
                f"type {type(list).__name__} or {type(dpf_operator.Operator).__name__}"
            )
        self._stub.AddOperators(request)

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
        self.add_operators(operator)

    def record(self, identifier=None, transfer_ownership=True):
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
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.RecordInInternalRegistryRequest()
        request.wf.CopyFrom(self._message)
        if identifier:
            request.identifier = identifier
        request.transferOwnership = transfer_ownership
        return self._stub.RecordInInternalRegistry(request).id

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
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.WorkflowFromInternalRegistryRequest()
        request.registry_id = id
        wf = Workflow(server=server)
        wf._message.CopyFrom(wf._stub.GetFromInternalRegistry(request))
        return wf

    @property
    def info(self):
        """Dictionary with the operator names and the exposed input and output names.

        Returns
        ----------
        info : dictionarry str->list str
            Dictionary with ``"operator_names"``, ``"input_names"``, and ``"output_names"`` key.
        """
        tmp = self._stub.List(self._message)
        out = {"operator_names": [], "input_names": [], "output_names": []}
        for name in tmp.operator_names:
            out["operator_names"].append(name)
        for name in tmp.input_pin_names.pin_names:
            out["input_names"].append(name)
        for name in tmp.output_pin_names.pin_names:
            out["output_names"].append(name)
        return out

    @property
    def operator_names(self):
        """List of the names of operators added in the workflow.

        Returns
        ----------
        names : list str
        """
        return self.info["operator_names"]

    @property
    def input_names(self):
        """List of the input names exposed in the workflow with set_input_name.

        Returns
        ----------
        names : list str
        """
        return self.info["input_names"]

    @property
    def output_names(self):
        """List of the output names exposed in the workflow with set_output_name.

        Returns
        ----------
        names : list str
        """
        return self.info["output_names"]

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


        """
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.ConnectRequest()
        request.right_wf.CopyFrom(self._message)
        request.left_wf.CopyFrom(left_workflow._message)
        if output_input_names:
            if isinstance(output_input_names, tuple):
                request.input_to_output.append(
                    workflow_pb2.InputToOutputChainRequest(
                        output_name=output_input_names[0],
                        input_name=output_input_names[1]))
            elif isinstance(output_input_names, dict):
                for key in output_input_names:
                    request.input_to_output.append(
                        workflow_pb2.InputToOutputChainRequest(
                            output_name=key,
                            input_name=output_input_names[key]))
            else:
                raise TypeError("output_input_names argument is expect"
                                "to be either a str tuple or a str dict")

        self._stub.Connect(request)

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
        from ansys.grpc.dpf import workflow_pb2

        server = None
        address = None
        for arg in args:
            if isinstance(arg, dpf.core.server_types.LegacyGrpcServer):
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
            text_stream = self._stub.WriteToStream(self._message)
            return Workflow(workflow=text_stream.stream, server=server)
        elif address:
            request = workflow_pb2.RemoteCopyRequest()
            request.wf.CopyFrom(self._message)
            request.address = address
            return Workflow(workflow=request, server=self._server)
        else:
            raise ValueError("a connection address (either with address input"
                             "or both ip and port inputs) or a server is required")

    def _connect(self):
        """Connect to the gRPC service."""
        from ansys.grpc.dpf import workflow_pb2_grpc
        return workflow_pb2_grpc.WorkflowServiceStub(self._server.channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

    @protect_grpc
    def __send_init_request(self, workflow):
        from ansys.grpc.dpf import workflow_pb2, base_pb2

        if server_meet_version("3.0", self._server) \
                and isinstance(workflow, workflow_pb2.RemoteCopyRequest):
            request = workflow_pb2.CreateRequest()
            request.remote_copy.CopyFrom(workflow)
        else:
            request = base_pb2.Empty()
            if hasattr(workflow_pb2, "CreateRequest"):
                request = workflow_pb2.CreateRequest(empty=request)
        self._message = self._stub.Create(request)

    @protect_grpc
    def __create_from_stream(self, string):
        from ansys.grpc.dpf import workflow_pb2

        request = workflow_pb2.TextStream(stream=string)
        self._message = self._stub.LoadFromStream(request)


def _write_output_type_to_proto_style(output_type, request):
    from ansys.grpc.dpf import base_pb2

    subtype = ""
    stype = ""
    if hasattr(output_type, "name"):
        if output_type == types.fields_container:
            stype = "collection"
            subtype = "field"
        elif output_type == types.scopings_container:
            stype = "collection"
            subtype = "scoping"
        elif output_type == types.meshes_container:
            stype = "collection"
            subtype = "meshed_region"
        elif hasattr(types, "vec_int") and output_type == types.vec_int:
            stype = 'collection'
            subtype = 'int'
        elif hasattr(types, "vec_double") and output_type == types.vec_double:
            stype = 'collection'
            subtype = 'double'
        else:
            stype = output_type.name
    elif isinstance(output_type, list):
        stype = output_type[0]
        subtype = output_type[1]
    else:
        stype = output_type
    request.type = base_pb2.Type.Value(stype.upper())
    if subtype != "":
        request.subtype = base_pb2.Type.Value(subtype.upper())


def _convertOutputMessageToPythonInstance(out, output_type, server):
    from ansys.dpf.core import (
        cyclic_support,
        data_sources,
        field,
        fields_container,
        collection,
        meshed_region,
        meshes_container,
        property_field,
        result_info,
        scoping,
        scopings_container,
        time_freq_support,
        data_tree,
        workflow,
    )

    if out.HasField("str"):
        return out.str
    elif out.HasField("int"):
        return out.int
    elif out.HasField("double"):
        return out.double
    elif out.HasField("bool"):
        return out.bool
    elif out.HasField("field"):
        toconvert = out.field
        if toconvert.datatype == "int":
            return property_field.PropertyField(server=server, property_field=toconvert)
        else:
            return field.Field(server=server, field=toconvert)
    elif out.HasField("collection"):
        toconvert = out.collection
        if output_type == types.fields_container:
            return fields_container.FieldsContainer(
                server=server, fields_container=toconvert
            )
        elif output_type == types.scopings_container:
            return scopings_container.ScopingsContainer(
                server=server, scopings_container=toconvert
            )
        elif output_type == types.meshes_container:
            return meshes_container.MeshesContainer(
                server=server, meshes_container=toconvert
            )
        elif output_type == types.vec_int:
            return collection.IntCollection(server=server,
                                         collection=toconvert
                                         ).get_integral_entries()
        elif output_type == types.vec_double:
            return collection.FloatCollection(server=server,
                                         collection=toconvert
                                         ).get_integral_entries()
    elif out.HasField("scoping"):
        toconvert = out.scoping
        return scoping.Scoping(scoping=toconvert, server=server)
    elif out.HasField("mesh"):
        toconvert = out.mesh
        return meshed_region.MeshedRegion(mesh=toconvert, server=server)
    elif out.HasField("result_info"):
        toconvert = out.result_info
        return result_info.ResultInfo(result_info=toconvert, server=server)
    elif out.HasField("time_freq_support"):
        toconvert = out.time_freq_support
        return time_freq_support.TimeFreqSupport(
            server=server, time_freq_support=toconvert
        )
    elif out.HasField("data_sources"):
        toconvert = out.data_sources
        return data_sources.DataSources(server=server, data_sources=toconvert)
    elif out.HasField("cyc_support"):
        toconvert = out.cyc_support
        return cyclic_support.CyclicSupport(server=server, cyclic_support=toconvert)
    elif out.HasField("workflow"):
        toconvert = out.workflow
        return workflow.Workflow(server=server, workflow=toconvert)
    elif out.HasField("data_tree"):
        toconvert = out.data_tree
        return data_tree.DataTree(server=server, data_tree=toconvert)


def _fillConnectionRequestMessage(request, inpt, server, pin_out=0):
    from ansys.dpf.core import (
        collection,
        cyclic_support,
        data_sources,
        field_base,
        meshed_region,
        model,
        scoping,
        workflow,
        time_freq_support,
        data_tree,
    )

    if isinstance(inpt, str):
        request.str = inpt
    elif isinstance(inpt, bool):
        request.bool = inpt
    elif isinstance(inpt, int):
        request.int = inpt
    elif isinstance(inpt, float):
        request.double = inpt
    elif isinstance(inpt, list):
        if all(isinstance(x, int) for x in inpt):
            if server_meet_version("3.0", server):
                inpt = collection.Collection.integral_collection(inpt, server)
                request.collection.CopyFrom(inpt._internal_obj)
                return inpt
            else:
                request.vint.rep_int.extend(inpt)
        elif all(isinstance(x, float) for x in inpt):
            if server_meet_version("3.0", server):
                inpt = collection.Collection.integral_collection(inpt, server)
                request.collection.CopyFrom(inpt._internal_obj)
                return inpt
            else:
                request.vdouble.rep_double.extend(inpt)
        else:
            errormsg = f"input type {inpt.__class__} cannot be connected"
            raise TypeError(errormsg)
    elif isinstance(inpt, field_base._FieldBase):
        if isinstance(inpt._internal_obj, int):
            raise NotImplementedError("Operator must be switched to pygate")
        # TODO: inpt._internal_obj is a pointer in the case of CLayer
        request.field.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, collection.Collection):
        request.collection.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, scoping.Scoping):
        request.scoping.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, data_sources.DataSources):
        if isinstance(inpt._internal_obj, int):
            raise NotImplementedError("Operator must be switched to pygate")
            # TODO: inpt._internal_obj is a pointer in the case of CLayer
        request.data_sources.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, model.Model):
        request.data_sources.CopyFrom(inpt.metadata.data_sources._internal_obj)
    elif isinstance(inpt, meshed_region.MeshedRegion):
        request.mesh.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, cyclic_support.CyclicSupport):
        request.cyc_support.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, workflow.Workflow):
        request.workflow.CopyFrom(inpt._message)
    elif isinstance(inpt, data_tree.DataTree):
        request.data_tree.CopyFrom(inpt._message)
    elif isinstance(inpt, time_freq_support.TimeFreqSupport):
        request.time_freq_support.CopyFrom(inpt._internal_obj)
    elif isinstance(inpt, dpf_operator.Operator):
        request.inputop.inputop.CopyFrom(inpt._internal_obj)
        request.inputop.pinOut = pin_out
    elif isinstance(inpt, outputs.Output):
        request.inputop.inputop.CopyFrom(inpt._operator._internal_obj)
        request.inputop.pinOut = inpt._pin
    else:
        errormsg = f"input type {inpt.__class__} cannot be connected"
        raise TypeError(errormsg)
