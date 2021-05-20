"""
bind_support
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class bind_support(Operator):
    """Tie a support to a field.

      available inputs:
        - field (Field, FieldsContainer)
        - support (MeshedRegion, AbstractFieldSupport)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.bind_support()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_support = dpf.MeshedRegion()
      >>> op.inputs.support.connect(my_support)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.bind_support(field=my_field,support=my_support)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, support=None, config=None, server=None):
        super().__init__(name="BindSupport", config = config, server = server)
        self._inputs = InputsBindSupport(self)
        self._outputs = OutputsBindSupport(self)
        if field !=None:
            self.inputs.field.connect(field)
        if support !=None:
            self.inputs.support.connect(support)

    @staticmethod
    def _spec():
        spec = Specification(description="""Tie a support to a field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "support", type_names=["abstract_meshed_region","abstract_field_support"], optional=False, document="""meshed region or a support of the field""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "BindSupport")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBindSupport 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBindSupport 
        """
        return super().outputs


#internal name: BindSupport
#scripting name: bind_support
class InputsBindSupport(_Inputs):
    """Intermediate class used to connect user inputs to bind_support operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.bind_support()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_support = dpf.MeshedRegion()
      >>> op.inputs.support.connect(my_support)
    """
    def __init__(self, op: Operator):
        super().__init__(bind_support._spec().inputs, op)
        self._field = Input(bind_support._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._support = Input(bind_support._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._support)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def support(self):
        """Allows to connect support input to the operator

        - pindoc: meshed region or a support of the field

        Parameters
        ----------
        my_support : MeshedRegion, AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support()
        >>> op.inputs.support.connect(my_support)
        >>> #or
        >>> op.inputs.support(my_support)

        """
        return self._support

class OutputsBindSupport(_Outputs):
    """Intermediate class used to get outputs from bind_support operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.bind_support()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(bind_support._spec().outputs, op)
        self._field = Output(bind_support._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.bind_support()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

