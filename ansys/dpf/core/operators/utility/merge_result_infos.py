"""
merge_result_infos
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class merge_result_infos(Operator):
    """Take a set of result info and assemble them in a unique one

      available inputs:
        - result_infos1 (ResultInfo)
        - result_infos2 (ResultInfo)

      available outputs:
        - merged_result_infos (ResultInfo)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_result_infos()

      >>> # Make input connections
      >>> my_result_infos1 = dpf.ResultInfo()
      >>> op.inputs.result_infos1.connect(my_result_infos1)
      >>> my_result_infos2 = dpf.ResultInfo()
      >>> op.inputs.result_infos2.connect(my_result_infos2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_result_infos(result_infos1=my_result_infos1,result_infos2=my_result_infos2)

      >>> # Get output data
      >>> result_merged_result_infos = op.outputs.merged_result_infos()"""
    def __init__(self, result_infos1=None, result_infos2=None, config=None, server=None):
        super().__init__(name="merge::result_info", config = config, server = server)
        self._inputs = InputsMergeResultInfos(self)
        self._outputs = OutputsMergeResultInfos(self)
        if result_infos1 !=None:
            self.inputs.result_infos1.connect(result_infos1)
        if result_infos2 !=None:
            self.inputs.result_infos2.connect(result_infos2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of result info and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "result_infos", type_names=["result_info"], optional=False, document="""A vector of result info containers to merge or result infos from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "result_infos", type_names=["result_info"], optional=False, document="""A vector of result info containers to merge or result infos from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_result_infos", type_names=["result_info"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::result_info")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeResultInfos 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeResultInfos 
        """
        return super().outputs


#internal name: merge::result_info
#scripting name: merge_result_infos
class InputsMergeResultInfos(_Inputs):
    """Intermediate class used to connect user inputs to merge_result_infos operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_result_infos()
      >>> my_result_infos1 = dpf.ResultInfo()
      >>> op.inputs.result_infos1.connect(my_result_infos1)
      >>> my_result_infos2 = dpf.ResultInfo()
      >>> op.inputs.result_infos2.connect(my_result_infos2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_result_infos._spec().inputs, op)
        self._result_infos1 = Input(merge_result_infos._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._result_infos1)
        self._result_infos2 = Input(merge_result_infos._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._result_infos2)

    @property
    def result_infos1(self):
        """Allows to connect result_infos1 input to the operator

        - pindoc: A vector of result info containers to merge or result infos from pin 0 to ...

        Parameters
        ----------
        my_result_infos1 : ResultInfo, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_result_infos()
        >>> op.inputs.result_infos1.connect(my_result_infos1)
        >>> #or
        >>> op.inputs.result_infos1(my_result_infos1)

        """
        return self._result_infos1

    @property
    def result_infos2(self):
        """Allows to connect result_infos2 input to the operator

        - pindoc: A vector of result info containers to merge or result infos from pin 0 to ...

        Parameters
        ----------
        my_result_infos2 : ResultInfo, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_result_infos()
        >>> op.inputs.result_infos2.connect(my_result_infos2)
        >>> #or
        >>> op.inputs.result_infos2(my_result_infos2)

        """
        return self._result_infos2

class OutputsMergeResultInfos(_Outputs):
    """Intermediate class used to get outputs from merge_result_infos operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_result_infos()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_result_infos = op.outputs.merged_result_infos()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_result_infos._spec().outputs, op)
        self._merged_result_infos = Output(merge_result_infos._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_result_infos)

    @property
    def merged_result_infos(self):
        """Allows to get merged_result_infos output of the operator


        Returns
        ----------
        my_merged_result_infos : ResultInfo, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_result_infos()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_result_infos = op.outputs.merged_result_infos() 
        """
        return self._merged_result_infos

