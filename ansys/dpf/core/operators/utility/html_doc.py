"""
html_doc
========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class html_doc(Operator):
    """Create dpf's html documentation. Only on windows, use deprecated doc for linux

      available inputs:
        - output_path (str) (optional)

      available outputs:


      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.html_doc()

      >>> # Make input connections
      >>> my_output_path = str()
      >>> op.inputs.output_path.connect(my_output_path)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.html_doc(output_path=my_output_path)

      >>> # Get output data"""
    def __init__(self, output_path=None, config=None, server=None):
        super().__init__(name="html_doc", config = config, server = server)
        self._inputs = InputsHtmlDoc(self)
        self._outputs = OutputsHtmlDoc(self)
        if output_path !=None:
            self.inputs.output_path.connect(output_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create dpf's html documentation. Only on windows, use deprecated doc for linux""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "output_path", type_names=["string"], optional=True, document="""default is {working directory}/dataProcessingDoc.html""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "html_doc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsHtmlDoc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsHtmlDoc 
        """
        return super().outputs


#internal name: html_doc
#scripting name: html_doc
class InputsHtmlDoc(_Inputs):
    """Intermediate class used to connect user inputs to html_doc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.html_doc()
      >>> my_output_path = str()
      >>> op.inputs.output_path.connect(my_output_path)
    """
    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().inputs, op)
        self._output_path = Input(html_doc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._output_path)

    @property
    def output_path(self):
        """Allows to connect output_path input to the operator

        - pindoc: default is {working directory}/dataProcessingDoc.html

        Parameters
        ----------
        my_output_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.html_doc()
        >>> op.inputs.output_path.connect(my_output_path)
        >>> #or
        >>> op.inputs.output_path(my_output_path)

        """
        return self._output_path

class OutputsHtmlDoc(_Outputs):
    """Intermediate class used to get outputs from html_doc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.html_doc()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(html_doc._spec().outputs, op)
        pass 

