"""
change_fc
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "scoping" category
"""

class change_fc(Operator):
    """Rescope / split a fields container to correspond to a scopings container

      available inputs:
        - fields_container (FieldsContainer)
        - scopings_container (ScopingsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.change_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_scopings_container = dpf.ScopingsContainer()
      >>> op.inputs.scopings_container.connect(my_scopings_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.change_fc(fields_container=my_fields_container,scopings_container=my_scopings_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, scopings_container=None, config=None, server=None):
        super().__init__(name="rescope_fc", config = config, server = server)
        self._inputs = InputsChangeFc(self)
        self._outputs = OutputsChangeFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if scopings_container !=None:
            self.inputs.scopings_container.connect(scopings_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope / split a fields container to correspond to a scopings container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "scopings_container", type_names=["scopings_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "rescope_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsChangeFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsChangeFc 
        """
        return super().outputs


#internal name: rescope_fc
#scripting name: change_fc
class InputsChangeFc(_Inputs):
    """Intermediate class used to connect user inputs to change_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.change_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_scopings_container = dpf.ScopingsContainer()
      >>> op.inputs.scopings_container.connect(my_scopings_container)
    """
    def __init__(self, op: Operator):
        super().__init__(change_fc._spec().inputs, op)
        self._fields_container = Input(change_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._scopings_container = Input(change_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scopings_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.change_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def scopings_container(self):
        """Allows to connect scopings_container input to the operator

        Parameters
        ----------
        my_scopings_container : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.change_fc()
        >>> op.inputs.scopings_container.connect(my_scopings_container)
        >>> #or
        >>> op.inputs.scopings_container(my_scopings_container)

        """
        return self._scopings_container

class OutputsChangeFc(_Outputs):
    """Intermediate class used to get outputs from change_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.change_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(change_fc._spec().outputs, op)
        self._fields_container = Output(change_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.scoping.change_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

