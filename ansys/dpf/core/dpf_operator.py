"""
Operator
===============
Interface to underlying gRPC Operator
"""
from textwrap import wrap
import logging
import grpc
import functools

from ansys import dpf
from ansys.grpc.dpf import operator_pb2, operator_pb2_grpc, base_pb2, operator_config_pb2, operator_config_pb2_grpc
from ansys.dpf.core import (fields_container, field, scopings_container, scoping,
                            meshes_container, meshed_region, result_info, time_freq_support,
                            operators_helper, collection, data_sources)
from ansys.dpf.core.common import types, camel_to_snake_case
from ansys.dpf.core.inputs import Inputs, _Inputs, Input
from ansys.dpf.core.outputs import Outputs, _Outputs, Output
from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.core import BaseService

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

    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    Create an operator from a string

    >>> from ansys.dpf import core
    >>> disp_oper = core.Operator('U')

    Create an operator from a model

    >>> from ansys.dpf import core    
    >>> from ansys.dpf.core import examples
    >>> model = core.Model(examples.static_rst)
    >>> disp_oper = model.operator('U')
    """

    def __init__(self, name, config = None, server=None):
        """Initialize the operator with its name by connecting to a
        stub.
        """
        if server is None:
            server = dpf.core._global_server()

        self._server = server

        self.name = name
        self._stub = self._connect()

        self._message = None
        self._description = None
        self.inputs = None
        self.outputs = None

        self.__send_init_request(config)

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

        
    @protect_grpc
    def connect(self, pin, inpt, pin_out=0):
        """Connect an input on the operator using a pin number.

        Parameters
        ----------
        pin : int
            Number of the input pin.

        inpt :  str, int, double, bool, list of int, list of doubles, Field, FieldsContainer, Scoping, ScopingsContainer, 
        MeshedRegion, MeshesContainer, DataSources, Operator
            Object you wish to connect.

        pin_out : int, optional
            In case of the input is an Operator, this is the output
            pin of the input Operator.  Defaults to 0.

        Examples
        --------
        Compute the minimum of displacement by chaining the ``'U'``
        and ``'min_max_fc'`` operators.

        >>> from ansys.dpf import core as dpf
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
        _fillConnectionRequestMessage(request, inpt, pin_out)
        if inpt is self:
            raise ValueError('Cannot connect to itself')
        self._stub.Update(request)
    
        
    @protect_grpc
    def get_output(self, pin=0, output_type=None):
        """Returns the output of the operator on the pin number.

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
        
        if output_type is not None:
            _write_output_type_to_proto_style(output_type, request)
            out = self._stub.Get(request)
            return _convertOutputMessageToPythonInstance(out, output_type, self._server)
        else:
            request.type = base_pb2.Type.Value('RUN')
            return self._stub.Get(request)
            
    
    @property
    def config(self):
        """Returns a copy of the current config of the operator
        To use the config that you modify, please use operator.config = new_config
        
        Returns
        ----------
        config : core.Config        
        """
        out = self._stub.List(self._message)
        config = out.config
        return Config(config =config, server = self._server)
    
    
    @config.setter
    def config(self,value):
        """Change the configuration of the operator 
        (if the operator is up to date, changing the config doesn't make it not up to date)
         
        Parameters
        ----------
        value : dpf.core.Config
        """
        request = operator_pb2.UpdateConfigRequest()
        request.op.CopyFrom(self._message)
        request.config.CopyFrom(value._message)
        self._stub.UpdateConfig(request)
        
      
    @staticmethod
    def default_config(name, server=None):
        """Returns the default config for a given operator.
        This config can then be changed to the user needs and be used to
        instanciate the given operator
        
        Parameters
        ----------
        name : str
            Name of the operator.  For example 'U'.
    
        server : DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the the global server.
        """
        return Config(operator_name = name, server =server)
        
    def _connect(self):
        """Connect to the grpc service"""
        return operator_pb2_grpc.OperatorServiceStub(self._server.channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        return BaseService(self._server)._description(self._message)

    def run(self):
        """Evaluate this operator"""
        self.get_output()

    def _find_outputs_corresponding_pins(self, type_names, inpt, pin,
                                         corresponding_pins):
        for python_name in type_names:
            # appears to be an issue on Linux.  This check is here
            # because cpp mappings are a single type mapping and
            # sometimes the spec contains 'B' instead of 'bool'
            if python_name == 'B':
                python_name = 'bool'

            if  type(inpt).__name__ == python_name:
                corresponding_pins.append(pin)
            elif isinstance(inpt, _Outputs) or isinstance(inpt,Operator):
                if isinstance(inpt,Operator):
                    output_pin_available = inpt.outputs._get_given_output([python_name])
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
    def __send_init_request(self, config = None):
        request = operator_pb2.CreateOperatorRequest()
        request.name = self.name
        if config:
            request.config.CopyFrom(config._message)
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
    
class Config:
    """A class used to represent an operator's configuration.
        With configurations the user can optionnaly choose how the operator will run.
        This is an advanced feature used for deep customization. 
        The different options can change the way loops are done, 
        it can change whether the operator needs to make check on the input or not.
    """
    def __init__(self,operator_name=None, config=None, server=None):
        if server is None:
          server = dpf.core._global_server()

        self._server = server

        self._stub = self._connect()
        
        if config:
            self._message = config
        else:
            self.__send_init_request(operator_name)
        
        if hasattr(self._message, "spec"):
            self._config_help=self._message.spec
        
        opt = self.options
        for name in opt : 
            bound_method = self.config_option_value.__get__(self, self.__class__)
            method2 = functools.partial(bound_method,
                                        config_name=name)
            setattr(self, "get_"+name+"_option", method2)
            
            bound_method = self.__set_config_option__.__get__(self, self.__class__)
            method2 = functools.partial(bound_method,
                                        config_name=name)
            setattr(self, "set_"+name+"_option", method2)
        
    def _connect(self):
        """Connect to the grpc service"""
        return operator_config_pb2_grpc.OperatorConfigServiceStub(self._server.channel)


    @protect_grpc
    def __send_init_request(self, operator_name=None):
        request = operator_config_pb2.CreateRequest()
        if operator_name:
            request.operator_name.operator_name = operator_name
        self._message = self._stub.Create(request)
    
    @property
    def options(self):
        """Returns a list of the different config options and their values"""
        tmp= self._stub.List(self._message)
        out ={}
        for opt in tmp.options:
            out[opt.option_name]=opt.value_str
        return out
    
    
    
    def __set_config_option__(self,config_value, config_name):
        """Change the value of a config option

        Parameters
        ----------
        config_name : str
            Name of the config option to change

        config_value : bool, int, float
            The value to give to this config option
        """
        request = operator_config_pb2.UpdateRequest()
        request.config.CopyFrom(self._message)
        option_request = operator_config_pb2.ConfigOption()
        option_request.option_name = config_name
        if isinstance(config_value, bool):
            option_request.bool = config_value
        elif isinstance(config_value, int):
            option_request.int = config_value
        elif isinstance(config_value, float):
            option_request.double = config_value
        else:
            raise TypeError("str, int, float are the accepted type for config options")            
        
        request.options.extend([option_request])
        self._stub.Update(request)
        
        
    def set_config_option(self, config_name, config_value):
        """Change the value of a config option

        Parameters
        ----------
        config_name : str
            Name of the config option to change

        config_value : bool, int, float
            The value to give to this config option
        """
        return self.__set_config_option__(config_value, config_name)
        
        
    def config_option_value(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        value : str
        """
        opt = self.options
        if config_name in opt:
            return opt[config_name]
        else:
            raise KeyError(f"{config_name} option doesn't exist")
            
        
    def __try_get_option__(self,config_name):
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option
        return None
    
    
    def config_option_documentation(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        documentation : str
        """
        option =self.__try_get_option__(config_name)
        if option:
            return option.document
        return ""
    
    
    def config_option_accepted_types(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        types : list str
        """
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option.type_names
        return ""
    
    def config_option_default_value(self, config_name):
        """Description of the given config_name and how it impacts the operator
        
        Parameters
        ----------
        config_name : str
            Name of the config option to change
            
        Returns
        ----------
        default value : str
        """
        if self._config_help:
            for option in self._config_help.config_options_spec:
                if option.name==config_name:
                    return option.default_value_str
        return ""
    
    
    @property
    def available_config_options(self):
        """Returns the list of available config options for this operator
        
        Returns
        ----------
        types : list str
        """
        tmp= self._stub.List(self._message)
        out =[]
        for opt in tmp.options:
            out.append(opt.option_name)
        return out

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        return BaseService(self._server)._description(self._message)
        

def _write_output_type_to_proto_style(output_type, request):
    subtype=''
    stype=''
    if hasattr(output_type, 'name'):
        if output_type == types.fields_container:
            stype='collection'
            subtype = 'field'
        elif output_type== types.scopings_container:
            stype='collection'
            subtype = 'scoping'
        elif output_type== types.meshes_container:
            stype='collection'
            subtype = 'meshed_region'
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
            

def _convertOutputMessageToPythonInstance(out, output_type, server):
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
        return field.Field(server=server,field=toconvert)
    elif out.HasField("collection"):
        toconvert = out.collection
        if output_type == types.fields_container:
            return fields_container.FieldsContainer(server=server,fields_container=toconvert)
        elif output_type == types.scopings_container:
            return scopings_container.ScopingsContainer(server=server,scopings_container=toconvert)
        elif output_type == types.meshes_container:
            return meshes_container.MeshesContainer(server=server,meshes_container=toconvert)
    elif out.HasField("scoping"):
        toconvert = out.scoping
        return scoping.Scoping(scoping=toconvert,server=server)
    elif out.HasField("mesh"):
        toconvert = out.mesh
        return meshed_region.MeshedRegion(mesh=toconvert, server=server)
    elif out.HasField("result_info"):
        toconvert = out.result_info
        return result_info.ResultInfo(result_info=toconvert, server=server)
    elif out.HasField("time_freq_support"):
        toconvert = out.time_freq_support
        return time_freq_support.TimeFreqSupport(server=server, time_freq_support=toconvert)
    elif out.HasField("data_sources"):
        toconvert = out.data_sources
        return data_sources.DataSources(server=server,data_sources=toconvert)
    
def _fillConnectionRequestMessage(request, inpt, pin_out=0):
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
                request.vint.rep_int.extend(inpt)
            elif all(isinstance(x, float) for x in inpt):
                request.vdouble.rep_double.extend(inpt)
        elif isinstance(inpt, field.Field):
            request.field.CopyFrom(inpt._message)
        elif isinstance(inpt, collection.Collection):
            request.collection.CopyFrom(inpt._message)
        elif isinstance(inpt, scoping.Scoping):
            request.scoping.CopyFrom(inpt._message)
        elif isinstance(inpt, data_sources.DataSources):
            request.data_sources.CopyFrom(inpt._message)        
        elif isinstance(inpt, dpf.core.Model):
            request.data_sources.CopyFrom(inpt.metadata.data_sources._message)
        elif isinstance(inpt, meshed_region.MeshedRegion):
            request.mesh.CopyFrom(inpt._message)
        elif isinstance(inpt, Operator):
            request.inputop.inputop.CopyFrom(inpt._message)
            request.inputop.pinOut = pin_out
        elif isinstance(inpt, Output):
            request.inputop.inputop.CopyFrom(inpt._operator._message)
            request.inputop.pinOut = inpt._pin
        else:
            errormsg = f"input type {inpt.__class__} cannot be connected"
            raise TypeError(errormsg)
        