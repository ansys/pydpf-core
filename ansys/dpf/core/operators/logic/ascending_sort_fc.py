"""
ascending_sort_fc
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "logic" category
"""

class ascending_sort_fc(Operator):
    """Sort a field (in 0) in ascending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.

      available inputs:
        - fields_container (FieldsContainer)
        - component_priority_table (list) (optional)
        - sort_by_scoping (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.ascending_sort_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_component_priority_table = dpf.list()
      >>> op.inputs.component_priority_table.connect(my_component_priority_table)
      >>> my_sort_by_scoping = bool()
      >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.logic.ascending_sort_fc(fields_container=my_fields_container,component_priority_table=my_component_priority_table,sort_by_scoping=my_sort_by_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, component_priority_table=None, sort_by_scoping=None, config=None, server=None):
        super().__init__(name="ascending_sort_fc", config = config, server = server)
        self._inputs = InputsAscendingSortFc(self)
        self._outputs = OutputsAscendingSortFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if component_priority_table !=None:
            self.inputs.component_priority_table.connect(component_priority_table)
        if sort_by_scoping !=None:
            self.inputs.sort_by_scoping.connect(sort_by_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sort a field (in 0) in ascending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "component_priority_table", type_names=["vector<int32>"], optional=True, document="""component priority table (vector of int)"""), 
                                 2 : PinSpecification(name = "sort_by_scoping", type_names=["bool"], optional=True, document="""if true, uses scoping to sort the field (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ascending_sort_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAscendingSortFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAscendingSortFc 
        """
        return super().outputs


#internal name: ascending_sort_fc
#scripting name: ascending_sort_fc
class InputsAscendingSortFc(_Inputs):
    """Intermediate class used to connect user inputs to ascending_sort_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.ascending_sort_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_component_priority_table = dpf.list()
      >>> op.inputs.component_priority_table.connect(my_component_priority_table)
      >>> my_sort_by_scoping = bool()
      >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(ascending_sort_fc._spec().inputs, op)
        self._fields_container = Input(ascending_sort_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._component_priority_table = Input(ascending_sort_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._component_priority_table)
        self._sort_by_scoping = Input(ascending_sort_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._sort_by_scoping)

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

        >>> op = dpf.operators.logic.ascending_sort_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def component_priority_table(self):
        """Allows to connect component_priority_table input to the operator

        - pindoc: component priority table (vector of int)

        Parameters
        ----------
        my_component_priority_table : list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.ascending_sort_fc()
        >>> op.inputs.component_priority_table.connect(my_component_priority_table)
        >>> #or
        >>> op.inputs.component_priority_table(my_component_priority_table)

        """
        return self._component_priority_table

    @property
    def sort_by_scoping(self):
        """Allows to connect sort_by_scoping input to the operator

        - pindoc: if true, uses scoping to sort the field (default is false)

        Parameters
        ----------
        my_sort_by_scoping : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.ascending_sort_fc()
        >>> op.inputs.sort_by_scoping.connect(my_sort_by_scoping)
        >>> #or
        >>> op.inputs.sort_by_scoping(my_sort_by_scoping)

        """
        return self._sort_by_scoping

class OutputsAscendingSortFc(_Outputs):
    """Intermediate class used to get outputs from ascending_sort_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.ascending_sort_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(ascending_sort_fc._spec().outputs, op)
        self._fields_container = Output(ascending_sort_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.logic.ascending_sort_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

