"""
scale_fc
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class scale_fc(Operator):
    """Scales a field by a constant factor.

      available inputs:
        - fields_container (FieldsContainer)
        - ponderation (float, Field)
        - boolean (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.scale_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.scale_fc(fields_container=my_fields_container,ponderation=my_ponderation,boolean=my_boolean)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, ponderation=None, boolean=None, config=None, server=None):
        super().__init__(name="scale_fc", config = config, server = server)
        self._inputs = InputsScaleFc(self)
        self._outputs = OutputsScaleFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if ponderation !=None:
            self.inputs.ponderation.connect(ponderation)
        if boolean !=None:
            self.inputs.boolean.connect(boolean)

    @staticmethod
    def _spec():
        spec = Specification(description="""Scales a field by a constant factor.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "ponderation", type_names=["double","field"], optional=False, document="""Double/Field scoped on overall"""), 
                                 2 : PinSpecification(name = "boolean", type_names=["bool"], optional=True, document="""bool(optional, default false) if set to true, output of scale is mane dimensionless""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scale_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScaleFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScaleFc 
        """
        return super().outputs


#internal name: scale_fc
#scripting name: scale_fc
class InputsScaleFc(_Inputs):
    """Intermediate class used to connect user inputs to scale_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.scale_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_ponderation = float()
      >>> op.inputs.ponderation.connect(my_ponderation)
      >>> my_boolean = bool()
      >>> op.inputs.boolean.connect(my_boolean)
    """
    def __init__(self, op: Operator):
        super().__init__(scale_fc._spec().inputs, op)
        self._fields_container = Input(scale_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._ponderation = Input(scale_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._ponderation)
        self._boolean = Input(scale_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._boolean)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def ponderation(self):
        """Allows to connect ponderation input to the operator

        - pindoc: Double/Field scoped on overall

        Parameters
        ----------
        my_ponderation : float, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale_fc()
        >>> op.inputs.ponderation.connect(my_ponderation)
        >>> #or
        >>> op.inputs.ponderation(my_ponderation)

        """
        return self._ponderation

    @property
    def boolean(self):
        """Allows to connect boolean input to the operator

        - pindoc: bool(optional, default false) if set to true, output of scale is mane dimensionless

        Parameters
        ----------
        my_boolean : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale_fc()
        >>> op.inputs.boolean.connect(my_boolean)
        >>> #or
        >>> op.inputs.boolean(my_boolean)

        """
        return self._boolean

class OutputsScaleFc(_Outputs):
    """Intermediate class used to get outputs from scale_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.scale_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(scale_fc._spec().outputs, op)
        self._fields_container = Output(scale_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.scale_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

