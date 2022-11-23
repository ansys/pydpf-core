"""
extract_sub_fc
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class extract_sub_fc(Operator):
    """Create a new FieldsContainer with all the Fields corresponding to the label space in input 1

      available inputs:
        - fields_container (FieldsContainer)
        - label_space (LabelSpace)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.extract_sub_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.extract_sub_fc(fields_container=my_fields_container,label_space=my_label_space)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, label_space=None, config=None, server=None):
        super().__init__(name="extract_sub_fc", config = config, server = server)
        self._inputs = InputsExtractSubFc(self)
        self._outputs = OutputsExtractSubFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if label_space !=None:
            self.inputs.label_space.connect(label_space)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a new FieldsContainer with all the Fields corresponding to the label space in input 1""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container"""), 
                                 1 : PinSpecification(name = "label_space", type_names=["label_space"], optional=False, document="""label_space""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extract_sub_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractSubFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtractSubFc 
        """
        return super().outputs


#internal name: extract_sub_fc
#scripting name: extract_sub_fc
class InputsExtractSubFc(_Inputs):
    """Intermediate class used to connect user inputs to extract_sub_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_fc._spec().inputs, op)
        self._fields_container = Input(extract_sub_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._label_space = Input(extract_sub_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._label_space)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: fields_container

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

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

        >>> op = dpf.operators.utility.extract_sub_fc()
        >>> op.inputs.label_space.connect(my_label_space)
        >>> #or
        >>> op.inputs.label_space(my_label_space)

        """
        return self._label_space

class OutputsExtractSubFc(_Outputs):
    """Intermediate class used to get outputs from extract_sub_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_fc._spec().outputs, op)
        self._fields_container = Output(extract_sub_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: fields_container

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

