"""
Workflow
========
Interface to underlying gRPC workflow.
"""
from textwrap import wrap
import logging
import functools

from ansys import dpf
from ansys.grpc.dpf import workflow_pb2, workflow_pb2_grpc, base_pb2
from ansys.dpf.core import dpf_operator, inputs, outputs
from ansys.dpf.core.common import types
from ansys.dpf.core.errors import protect_grpc

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
    workflow :  workflow_pb2.Workflow

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

        if workflow is None:
            self.__send_init_request()

    @protect_grpc
    def connect(self, pin_name, inpt, pin_out=0):
        """Connect an input on the workflow using a pin name.

        Parameters
        ----------
        pin_name : str
            Name of the pin to connect. This name should be
            exposed before with wf.set_input_name
        inpt : str, int, double, bool, list of int, list of doubles, Field, FieldsContainer, Scoping, ScopingsContainer,
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
        request = workflow_pb2.UpdateConnectionRequest()
        request.wf.CopyFrom(self._message)
        request.pin_name = pin_name
        dpf_operator._fillConnectionRequestMessage(request, inpt, pin_out)
        self._stub.UpdateConnection(request)

    @protect_grpc
    def get_output(self, pin_name, output_type):
        """Retrieve the output of the operator on the pin number.

        Parameters
        ----------
        pin_name : str
            Name of the pin to retrieve. This name should be
            exposed before with wf.set_output_name
        output_type : core.type enum
            Type of the requested output.
        """

        request = workflow_pb2.WorkflowEvaluationRequest()
        request.wf.CopyFrom(self._message)
        request.pin_name = pin_name

        if output_type is not None:
            dpf_operator._write_output_type_to_proto_style(output_type, request)
            out = self._stub.Get(request)
            return dpf_operator._convertOutputMessageToPythonInstance(
                out, output_type, self._server
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
        >>> workflow.add_operators([disp_op,max_fc_op])
        >>> workflow.set_input_name("data_sources", disp_op.inputs.data_sources)

        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> workflow.connect("data_sources", data_src)

        """
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(self._message)
        input_request = workflow_pb2.OperatorNaming()
        input_request.name = name
        input_request.pin = 0
        for arg in args:
            if isinstance(arg, inputs.Input):
                input_request.pin = arg._pin
                input_request.operator.CopyFrom(arg._operator._message)
            elif isinstance(arg, dpf_operator.Operator):
                input_request.operator.CopyFrom(arg._message)
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

        >>> workflow = dpf.Workflow()
        >>> workflow.add_operators([disp_op,max_fc_op])
        >>> workflow.set_output_name("contour", disp_op.outputs.fields_container)

        >>> fc = workflow.get_output("contour", dpf.types.fields_container)

        """
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(self._message)
        output_request = workflow_pb2.OperatorNaming()
        output_request.name = name
        output_request.pin = 0
        for arg in args:
            if isinstance(arg, outputs.Output):
                output_request.pin = arg._pin
                output_request.operator.CopyFrom(arg._operator._message)
            elif isinstance(arg, dpf_operator.Operator):
                output_request.operator.CopyFrom(arg._message)
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
        request = workflow_pb2.AddOperatorsRequest()
        request.wf.CopyFrom(self._message)
        if isinstance(operators, list):
            request.operators.extend([op._message for op in operators])
        elif isinstance(operators, dpf_operator.Operator):
            request.operators.extend([operators._message])
        else:
            raise TypeError(
                f"operators to add to the workflow are expected to be of type {type(list).__name__} or {type(dpf_operator.Operator).__name__}"
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

    def chain_with(self, workflow, input_output_names=None):
        """Chain two workflows together so that they become one workflow.

        The one workflow contains all the operators, inputs, and outputs
        exposed in both workflows.

        Parameters
        ----------
        workflow : core.Workflow
            Second workflow's inputs to chained with this workflow's outputs.
        input_output_names : str tuple, optional
            Input name of the workflow to chain with the output name of the second workflow.
            The default is ``None``, in which case this outputs in this workflow with the same
            names as the inputs in the second workflow are chained.

        Examples
        --------
        ::

            +-------------------------------------------------------------------------------------------------+
            |  INPUT:                                                                                         |
            |                                                                                                 |
            |input_output_names = ("output","field" )                                                         |
            |                      ____                                  ______________________               |
            |  "data_sources"  -> |this| ->  "stuff"        "field" -> |workflow_to_chain_with| -> "contour"  |
            |"time_scoping"    -> |    |             "mesh_scoping" -> |                      |               |
            |                     |____| ->  "output"                  |______________________|               |
            |  OUTPUT                                                                                         |
            |                    ____                                                                         |
            |"data_sources"  -> |this| ->  "stuff"                                                            |
            |"time_scoping" ->  |    | ->  "contour"                                                          |
            |"mesh_scoping" ->  |____| -> "output"                                                            |
            +-------------------------------------------------------------------------------------------------+


        """
        request = workflow_pb2.ChainRequest()
        request.wf.CopyFrom(self._message)
        request.wf_to_chain_with.CopyFrom(workflow._message)
        if input_output_names:
            request.input_to_output.output_name = input_output_names[0]
            request.input_to_output.input_name = input_output_names[1]
        self._stub.Chain(request)

    def _connect(self):
        """Connect to the gRPC service."""
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
    def __send_init_request(self):
        request = base_pb2.Empty()
        self._message = self._stub.Create(request)
