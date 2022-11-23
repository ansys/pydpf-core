"""
extract_sub_sc
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class extract_sub_sc(Operator):
    """Create a new ScopingsContainer with all the Scopings corresponding to the label space in input 1

      available inputs:
        - scopings_container (ScopingsContainer)
        - label_space (LabelSpace)

      available outputs:
        - scopings_container (ScopingsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.extract_sub_sc()

      >>> # Make input connections
      >>> my_scopings_container = dpf.ScopingsContainer()
      >>> op.inputs.scopings_container.connect(my_scopings_container)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.extract_sub_sc(scopings_container=my_scopings_container,label_space=my_label_space)

      >>> # Get output data
      >>> result_scopings_container = op.outputs.scopings_container()"""
    def __init__(self, scopings_container=None, label_space=None, config=None, server=None):
        super().__init__(name="extract_sub_sc", config = config, server = server)
        self._inputs = InputsExtractSubSc(self)
        self._outputs = OutputsExtractSubSc(self)
        if scopings_container !=None:
            self.inputs.scopings_container.connect(scopings_container)
        if label_space !=None:
            self.inputs.label_space.connect(label_space)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a new ScopingsContainer with all the Scopings corresponding to the label space in input 1""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "scopings_container", type_names=["scopings_container"], optional=False, document="""scopings_container"""), 
                                 1 : PinSpecification(name = "label_space", type_names=["label_space"], optional=False, document="""label_space""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "scopings_container", type_names=["scopings_container"], optional=False, document="""scopings_container""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extract_sub_sc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractSubSc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtractSubSc 
        """
        return super().outputs


#internal name: extract_sub_sc
#scripting name: extract_sub_sc
class InputsExtractSubSc(_Inputs):
    """Intermediate class used to connect user inputs to extract_sub_sc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_sc()
      >>> my_scopings_container = dpf.ScopingsContainer()
      >>> op.inputs.scopings_container.connect(my_scopings_container)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_sc._spec().inputs, op)
        self._scopings_container = Input(extract_sub_sc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._scopings_container)
        self._label_space = Input(extract_sub_sc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._label_space)

    @property
    def scopings_container(self):
        """Allows to connect scopings_container input to the operator

        - pindoc: scopings_container

        Parameters
        ----------
        my_scopings_container : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_sc()
        >>> op.inputs.scopings_container.connect(my_scopings_container)
        >>> #or
        >>> op.inputs.scopings_container(my_scopings_container)

        """
        return self._scopings_container

    @property
    def label_space(self):
        """Allows to connect label_space input to the operator

        - pindoc: label_space

        Parameters
        ----------
        my_label_space : LabelSpace, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_sc()
        >>> op.inputs.label_space.connect(my_label_space)
        >>> #or
        >>> op.inputs.label_space(my_label_space)

        """
        return self._label_space

class OutputsExtractSubSc(_Outputs):
    """Intermediate class used to get outputs from extract_sub_sc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_sc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_scopings_container = op.outputs.scopings_container()
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_sc._spec().outputs, op)
        self._scopings_container = Output(extract_sub_sc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._scopings_container)

    @property
    def scopings_container(self):
        """Allows to get scopings_container output of the operator


        - pindoc: scopings_container

        Returns
        ----------
        my_scopings_container : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_sc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scopings_container = op.outputs.scopings_container() 
        """
        return self._scopings_container

