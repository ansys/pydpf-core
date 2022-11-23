"""
prns_to_field
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class prns_to_field(Operator):
    """Read the presol of nodal field generated file from mapdl.

      available inputs:
        - filepath (str)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.prns_to_field()

      >>> # Make input connections
      >>> my_filepath = str()
      >>> op.inputs.filepath.connect(my_filepath)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.prns_to_field(filepath=my_filepath)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, filepath=None, config=None, server=None):
        super().__init__(name="PRNS_Reader", config = config, server = server)
        self._inputs = InputsPrnsToField(self)
        self._outputs = OutputsPrnsToField(self)
        if filepath !=None:
            self.inputs.filepath.connect(filepath)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the presol of nodal field generated file from mapdl.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "filepath", type_names=["string"], optional=False, document="""filepath""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PRNS_Reader")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPrnsToField 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPrnsToField 
        """
        return super().outputs


#internal name: PRNS_Reader
#scripting name: prns_to_field
class InputsPrnsToField(_Inputs):
    """Intermediate class used to connect user inputs to prns_to_field operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.prns_to_field()
      >>> my_filepath = str()
      >>> op.inputs.filepath.connect(my_filepath)
    """
    def __init__(self, op: Operator):
        super().__init__(prns_to_field._spec().inputs, op)
        self._filepath = Input(prns_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._filepath)

    @property
    def filepath(self):
        """Allows to connect filepath input to the operator

        - pindoc: filepath

        Parameters
        ----------
        my_filepath : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.prns_to_field()
        >>> op.inputs.filepath.connect(my_filepath)
        >>> #or
        >>> op.inputs.filepath(my_filepath)

        """
        return self._filepath

class OutputsPrnsToField(_Outputs):
    """Intermediate class used to get outputs from prns_to_field operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.prns_to_field()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(prns_to_field._spec().outputs, op)
        self._field = Output(prns_to_field._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.prns_to_field()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

