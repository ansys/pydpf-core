"""Interface to underlying gRPC Operator"""
from textwrap import wrap
import logging
import grpc
import functools

from ansys.grpc.dpf import operator_pb2, operator_pb2_grpc, base_pb2
from ansys.dpf.core import (fields_container, field, scoping,
                            meshed_region, result_info, time_freq_support,
                            operators_helper, collection, data_sources, server)
from ansys.dpf.core.common import types, camel_to_snake_case
from ansys.dpf.core.inputs import Inputs
from ansys.dpf.core.outputs import Outputs
from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.errors import protect_grpc

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')


class Operator:
    """A class used to represent an Operator which is an elementary
    operation.

    A list of existing operators can be asked through the "html_doc"
    operator.

    Parameters
    ----------
    name : str
        Name of the operator.  For example 'U'.

    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.

    Examples
    --------
    Create an operator from a string

    >>> from ansys import dpf
    >>> disp_oper = dpf.core.Operator('U')

    Create an operator from a model

    >>> from ansys import dpf
    >>> model = dpf.core.Model('file.rst')
    >>> disp_oper = model.operator('U')
    """

    def __init__(self, name, channel=None):
        """Initialize the operator with its name by connecting to a
        stub.
        """
        if channel is None:
            channel = server._global_channel()

        self.name = name
        self._channel = channel
        self._stub = self._connect()

        self._message = None
        self._description = None
        self.inputs = None
        self.outputs = None

        self.__send_init_request()

        # add dynamic inputs
        if len(self._message.spec.map_input_pin_spec) > 0:
            self.inputs = Inputs(self._message.spec.map_input_pin_spec, self)
        if len(self._message.spec.map_output_pin_spec) != 0:
            self.outputs = Outputs(self._message.spec.map_output_pin_spec, self)
        self._description = self._message.spec.description

    def _add_sub_res_operators(self, sub_results):
        """Dynamically add operators instantiating for sub-results.

        The new operators subresults are connected to the parent
        operator's inputs when created, but are, then, completely
        independent of the parent operators.

        Examples
        --------
        disp_oper = model.displacement()
        generates: model.displacement().X() model.displacement().Y() model.displacement().Z()
        """
        for result_type in sub_results:
            bound_method = self._sub_result_op.__get__(self, self.__class__)
            method2 = functools.partial(bound_method, name=result_type["operator name"])
            setattr(self, result_type["name"], method2)

    def connect(self, pin, inpt, pin_out=0):
        """Connect an input on the operator using a pin number.

        Parameters
        ----------
        pin : int
            Number of the input pin.

        inpt : str, int, double, Field, FieldsContainer, Scoping, DataSources
            Object you wish to connect to.

        pin_out : int, optional
            In case of the input is an Operator, this is the output
            pin of the input Operator.  Defaults to 0.

        Examples
        --------
        Compute the minimum of displacement by chaining the ``'U'``
        and ``'min_max_fc'`` operators.

        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> print(data_src)
        >>> disp_op = dpf.Operator('U')
        >>> disp_op.inputs.data_sources(data_src)
        >>> max_fc_op = dpf.Operator('min_max_fc')
        >>> max_fc_op.inputs.connect(disp_op.outputs)
        >>> max_field = max_fc_op.outputs.field_max()
        >>> max_field.data
        array([[0.59428386, 0.00201751, 0.0006032 ]])
        """
        request = operator_pb2.UpdateRequest()
        request.op.CopyFrom(self._message)
        request.pin = pin

        if isinstance(inpt, str):
            request.str = inpt
        elif isinstance(inpt, bool):
            request.bool = inpt
        elif isinstance(inpt, int):
            request.int = inpt
        elif isinstance(inpt, float):
            request.double = inpt
        elif isinstance(inpt, list):
            request.vint.rep_int.extend(inpt)
        elif isinstance(inpt, field.Field):
            request.field.CopyFrom(inpt._message)
        elif isinstance(inpt, collection.Collection):
            request.collection.CopyFrom(inpt._message)
        elif isinstance(inpt, scoping.Scoping):
            request.scoping.CopyFrom(inpt._message)
        elif isinstance(inpt, data_sources.DataSources):
            request.data_sources.CopyFrom(inpt._message)
        elif isinstance(inpt, meshed_region.MeshedRegion):
            request.mesh.CopyFrom(inpt._message)
        elif isinstance(inpt, Operator):
            if inpt is self:
                raise ValueError('Cannot connect to itself')
            request.inputop.CopyFrom(inpt._message)
            request.pinOut = pin_out

        self._stub.Update(request)

    @protect_grpc
    def get_output(self, pin=0, output_type=None):
        """Returns the output of the operator on the pin number.  If no
        pin is set, then the operator is run.

        Parameters
        ----------
        pin : int, optional
            Number of the output pin.

        output_type : core.type enum, optional
            The requested type of the output.
        """
        request = operator_pb2.OperatorEvaluationRequest()
        request.op.CopyFrom(self._message)
        request.pin = pin
        subtype=''
        if output_type is not None:
            if hasattr(output_type, 'name'):
                if output_type== types.fields_container:
                    stype='collection'
                    subtype = 'field'
                else :
                    stype = output_type.name
            elif isinstance(output_type,list):
                stype=output_type[0]
                subtype = output_type[1]
            else:
                stype = output_type
            request.type = base_pb2.Type.Value(stype.upper())
            if subtype !="":
                request.subtype = base_pb2.Type.Value(subtype.upper())
            out = self._stub.Get(request)
            if out.HasField("str"):
                return out.str
            elif out.HasField("int"):
                return out.int
            elif out.HasField("double"):
                return out.double
            elif out.HasField("field"):
                toconvert = out.field
                return field.Field(channel=self._channel,field=toconvert)
            elif out.HasField("collection"):
                toconvert = out.collection
                if subtype == "field":
                    return fields_container.FieldsContainer(channel=self._channel,fields_container=toconvert)
            elif out.HasField("scoping"):
                toconvert = out.scoping
                return scoping.Scoping(scoping=toconvert,channel =self._channel)
            elif out.HasField("mesh"):
                toconvert = out.mesh
                return meshed_region.MeshedRegion(toconvert, channel=self._channel)
            elif out.HasField("result_info"):
                toconvert = out.result_info
                return result_info.ResultInfo(result_info=toconvert, channel=self._channel)
            elif out.HasField("time_freq_support"):
                toconvert = out.time_freq_support
                return time_freq_support.TimeFreqSupport(channel=self._channel, time_freq_support=toconvert)
            elif out.HasField("data_sources"):
                toconvert = out.data_sources
                return data_sources.DataSources(channel=self._channel,data_sources=toconvert)
        else:
            request.type = base_pb2.Type.Value('RUN')
            return self._stub.Get(request)

    def _connect(self):
        """Connect to the grpc service"""
        return operator_pb2_grpc.OperatorServiceStub(self._channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __str__(self):
        # return this repr and operator one level up
        txt = f'DPF "{self.name}" Operator\n'
        if self._description:
            txt += '    Description:\n'
            txt += '\n'.join(wrap(self._description, initial_indent='    ',
                                  subsequent_indent='    '))
            txt += '\n\n'
        if self.inputs:
            line = [' ', str(self.inputs)]
            txt += '{:^3} {:^21}'.format(*line)
            txt += '\n'
        if self.outputs:
            line = [' ', str(self.outputs)]
            txt += '{:^3} {:^21}'.format(*line)
            txt += '\n'

        return txt

    def run(self):
        """Evaluate this operator"""
        self.get_output()

    def _find_outputs_corresponding_pins(self, type_names, inpt, pin,
                                         corresponding_pins):
        input_type_name = type(inpt).__name__
        for python_name in type_names:
            if python_name == input_type_name:
                corresponding_pins.append(pin)
            elif input_type_name == "Outputs":
                output_pin_available = inpt._get_given_output([python_name])
                for outputpin in output_pin_available:
                    corresponding_pins.append((pin, outputpin))
            elif input_type_name == "Output":
                for inpttype in inpt._python_expected_types:
                    if inpttype == python_name:
                        corresponding_pins.append(pin)
                if python_name == "Any":
                    corresponding_pins.append(pin)
            elif python_name == "Any":
                corresponding_pins.append(pin)

    @protect_grpc
    def _sub_result_op(self, name):
        op = Operator(name)
        if self.inputs is not None:
            for key in self.inputs._connected_inputs:
                inpt = self.inputs._connected_inputs[key]
                if type(inpt).__name__ == 'dict':
                    for keyout in inpt:
                        op.connect(key,inpt[keyout],keyout)
                else:
                    op.connect(key,inpt)
        return op

    @protect_grpc
    def __send_init_request(self):
        request = operator_pb2.OperatorName()
        request.name = self.name
        self._message = self._stub.Create(request)

    def __mul__(self, inpt):
        if isinstance(inpt, Operator):
            op = Operator("dot")
            op.connect(0, self, 0)
            op.connect(1, inpt, 0)
        elif isinstance(inpt, float):
            op = Operator("scale")
            op.connect(0, self, 0)
            op.connect(1, inpt)
        return op

    def __truediv__(self, inpt):
        if isinstance(inpt, Operator):
            op = Operator("div")
            op.connect(0, self, 0)
            op.connect(1, inpt, 0)
        elif isinstance(inpt, float):
            op = Operator("scale")
            op.connect(0, self, 0)
            op.connect(1, 1.0/inpt)
        return op
