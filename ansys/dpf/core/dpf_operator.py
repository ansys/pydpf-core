"""
.. _ref_operator:
    
Operator
===============
Interface to underlying gRPC Operator
"""
from textwrap import wrap
import logging
import grpc
import functools

from ansys.grpc.dpf import operator_pb2, operator_pb2_grpc, base_pb2
from ansys.dpf.core.inputs import Inputs, _Inputs, Input
from ansys.dpf.core.outputs import Outputs, _Outputs, Output
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.config import Config
from ansys.dpf.core.mapping_types import types
from ansys.dpf.core import server as serverlib

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

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    Create an operator from the library of operators

    >>> from ansys.dpf import core as dpf
    >>> disp_oper = dpf.operators.result.displacement()

    Create an operator from a model

    >>> from ansys.dpf.core import Model 
    >>> from ansys.dpf.core import examples
    >>> model = Model(examples.static_rst)
    >>> disp_oper = model.results.displacement()
    
    """

    def __init__(self, name, config = None, server=None):
        """Initialize the operator with its name by connecting to a
        stub.
        """
        if server is None:
            server = serverlib._global_server()

        self._server = server

        self.name = name
        self._stub = self._connect()

        self._message = None
        self._description = None
        self._inputs = None
        self._outputs = None

        self.__send_init_request(config)
        
        # add dynamic inputs
        if len(self._message.spec.map_input_pin_spec) > 0 and self._inputs==None:
            self._inputs = Inputs(self._message.spec.map_input_pin_spec, self)
        if len(self._message.spec.map_output_pin_spec) != 0 and self._outputs==None:
            self._outputs = Outputs(self._message.spec.map_output_pin_spec, self)
        
        self._description = self._message.spec.description

    def _add_sub_res_operators(self, sub_results):
        """Dynamically add operators instantiating for sub-results.

        The new operators subresults are connected to the parent
        operator's inputs when created, but are, then, completely
        independent of the parent operators.

        Examples
        --------
        >>> disp_oper = model.results.displacement()
        >>> disp_x = model.results.displacement().X()
        >>> disp_y = model.results.displacement().Y()
        >>> disp_z = model.results.displacement().Z()
        
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

        inpt :  str, int, double, bool, list of int, list of doubles, Field, FieldsContainer, Scoping, ScopingsContainer, MeshedRegion, MeshesContainer, DataSources, Operator
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
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> max_fc_op = dpf.operators.min_max.min_max_fc()
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
        """Returns a copy of the current config of the operator.
        To use the config that you modify, please use operator.config = new_config
        or create an operator with the new config as a parameter.
        
        Returns
        ----------
        config : Config        
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
        value : Config
        """
        request = operator_pb2.UpdateConfigRequest()
        request.op.CopyFrom(self._message)
        request.config.CopyFrom(value._message)
        self._stub.UpdateConfig(request)
        
    @property
    def inputs(self):
        """Enables to connect inputs to the operator 
        
        Returns
        --------
        inputs : Inputs
        
        Examples
        --------
        Use the displacement operator

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.multishells_rst)
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        
        """
        return self._inputs
    
    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it
        
        Returns
        --------
        outputs : Output
        
        Examples
        --------
        CUse the displacement operator

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
        """Returns the default config for a given operator.
        This config can then be changed to the user needs and be used to
        instanciate the given operator
        
        Parameters
        ----------
        name : str
            Name of the operator.  For example 'U'.
    
        server : server.DPFServer, optional
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
        from ansys.dpf.core.core import _description
        return _description(self._message, self._server)

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

    def __add__(self, fields_b):
        """Adds two fields or fields containers together
                
        Returns
        -------
        add : operators.math.add_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "add_fc") :
            op= operators.math.add_fc(self, fields_b)
        else :
            op= dpf_operator.Operator("add_fc")
            op.connect(0,self)        
            op.connect(1, fields_b)
        return op
    
    
    def __sub__(self, fields_b):
        """Substract two fields or fields containers together
                
        Returns
        -------
        minus : operators.math.minus_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "minus_fc") :
            op= operators.math.minus_fc()
        else :
            op= dpf_operator.Operator("minus_fc")
        op.connect(0,self)        
        op.connect(1, fields_b)
        return op
    

    def __pow__(self, value):
        if value != 2:
            raise ValueError('DPF only the value is "2" suppported')
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "sqr_fc") :
            op= operators.math.sqr_fc()
        else :
            op= dpf_operator.Operator("sqr_fc")
        op.connect(0,self)        
        op.connect(1, value)
        return op
    
    def __mul__(self, value):
        """Multiplies two fields or fields containers together
        
        Returns
        -------
        mul : operators.math.generalized_inner_product_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "generalized_inner_product_fc") :
            op= operators.math.generalized_inner_product_fc()
        else :
            op= dpf_operator.Operator("generalized_inner_product_fc")
        op.connect(0,self)        
        op.connect(1, value)
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
    from ansys.dpf.core import (fields_container, field, property_field, field_base, scopings_container, scoping,
                            meshes_container, meshed_region, result_info, time_freq_support, collection, data_sources,
                            collection, data_sources, cyclic_support)
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
        if toconvert.datatype == u"int":
            return property_field.PropertyField(server=server,property_field=toconvert)
        else:   
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
    elif out.HasField("cyc_support"):
        toconvert = out.cyc_support
        return cyclic_support.CyclicSupport(server=server,cyclic_support=toconvert)
    
def _fillConnectionRequestMessage(request, inpt, pin_out=0):
    from ansys.dpf.core import (fields_container, field, property_field, field_base, scopings_container, scoping,
                            meshes_container, meshed_region, result_info, time_freq_support, collection, data_sources,
                            collection, data_sources, cyclic_support, model)
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
    elif isinstance(inpt, field_base._FieldBase):
        request.field.CopyFrom(inpt._message)
    elif isinstance(inpt, collection.Collection):
        request.collection.CopyFrom(inpt._message)
    elif isinstance(inpt, scoping.Scoping):
        request.scoping.CopyFrom(inpt._message)
    elif isinstance(inpt, data_sources.DataSources):
        request.data_sources.CopyFrom(inpt._message)      
    elif isinstance(inpt, model.Model):
        request.data_sources.CopyFrom(inpt.metadata.data_sources._message)
    elif isinstance(inpt, meshed_region.MeshedRegion):
        request.mesh.CopyFrom(inpt._message)
    elif isinstance(inpt, cyclic_support.CyclicSupport):
        request.cyc_support.CopyFrom(inpt._message)
    elif isinstance(inpt, Operator):
        request.inputop.inputop.CopyFrom(inpt._message)
        request.inputop.pinOut = pin_out
    elif isinstance(inpt, Output):
        request.inputop.inputop.CopyFrom(inpt._operator._message)
        request.inputop.pinOut = inpt._pin
    else:
        errormsg = f"input type {inpt.__class__} cannot be connected"
        raise TypeError(errormsg)
        
    