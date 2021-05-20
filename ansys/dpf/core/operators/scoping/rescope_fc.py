"""
rescope_fc
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "scoping" category
"""

class rescope_fc(Operator):
    """Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh_scoping (Scoping, list)
        - default_value (float, list)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.rescope_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_default_value = float()
      >>> op.inputs.default_value.connect(my_default_value)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.rescope_fc(fields_container=my_fields_container,mesh_scoping=my_mesh_scoping,default_value=my_default_value)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh_scoping=None, default_value=None, config=None, server=None):
        super().__init__(name="Rescope_fc", config = config, server = server)
        self._inputs = InputsRescopeFc(self)
        self._outputs = OutputsRescopeFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping","vector<int32>"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "default_value", type_names=["double","vector<double>"], optional=False, document="""if a the pin 2 is used, the ids not found in the fields are added with this default value""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Rescope_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRescopeFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRescopeFc 
        """
        return super().outputs


#internal name: Rescope_fc
#scripting name: rescope_fc
class InputsRescopeFc(_Inputs):
    """Intermediate class used to connect user inputs to rescope_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.rescope_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_default_value = float()
      >>> op.inputs.default_value.connect(my_default_value)
    """
    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().inputs, op)
        self._fields_container = Input(rescope_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh_scoping = Input(rescope_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._default_value = Input(rescope_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._default_value)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope_fc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def default_value(self):
        """Allows to connect default_value input to the operator

        - pindoc: if a the pin 2 is used, the ids not found in the fields are added with this default value

        Parameters
        ----------
        my_default_value : float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope_fc()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> #or
        >>> op.inputs.default_value(my_default_value)

        """
        return self._default_value

class OutputsRescopeFc(_Outputs):
    """Intermediate class used to get outputs from rescope_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.rescope_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(rescope_fc._spec().outputs, op)
        self._fields_container = Output(rescope_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.scoping.rescope_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

