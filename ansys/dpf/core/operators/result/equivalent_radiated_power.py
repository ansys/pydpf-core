"""
equivalent_radiated_power
=========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "result" category
"""

class equivalent_radiated_power(Operator):
    """Compute the Equivalent Radiated Power (ERP)

      available inputs:
        - fields_container (FieldsContainer)
        - meshed_region (MeshedRegion, MeshesContainer) (optional)
        - time_scoping (int, list, Scoping) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.equivalent_radiated_power()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_time_scoping = int()
      >>> op.inputs.time_scoping.connect(my_time_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.equivalent_radiated_power(fields_container=my_fields_container,meshed_region=my_meshed_region,time_scoping=my_time_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, meshed_region=None, time_scoping=None, config=None, server=None):
        super().__init__(name="ERP", config = config, server = server)
        self._inputs = InputsEquivalentRadiatedPower(self)
        self._outputs = OutputsEquivalentRadiatedPower(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the Equivalent Radiated Power (ERP)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin have to be boundary or skin mesh"""), 
                                 2 : PinSpecification(name = "time_scoping", type_names=["int32","vector<int32>","scoping"], optional=True, document="""load step number (if it's specified, the ERP is computed only on the substeps of this step) or time scoping""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ERP")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEquivalentRadiatedPower 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsEquivalentRadiatedPower 
        """
        return super().outputs


#internal name: ERP
#scripting name: equivalent_radiated_power
class InputsEquivalentRadiatedPower(_Inputs):
    """Intermediate class used to connect user inputs to equivalent_radiated_power operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.equivalent_radiated_power()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_time_scoping = int()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().inputs, op)
        self._fields_container = Input(equivalent_radiated_power._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._meshed_region = Input(equivalent_radiated_power._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._meshed_region)
        self._time_scoping = Input(equivalent_radiated_power._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._time_scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def meshed_region(self):
        """Allows to connect meshed_region input to the operator

        - pindoc: the mesh region in this pin have to be boundary or skin mesh

        Parameters
        ----------
        my_meshed_region : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.meshed_region.connect(my_meshed_region)
        >>> #or
        >>> op.inputs.meshed_region(my_meshed_region)

        """
        return self._meshed_region

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: load step number (if it's specified, the ERP is computed only on the substeps of this step) or time scoping

        Parameters
        ----------
        my_time_scoping : int, list, Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

class OutputsEquivalentRadiatedPower(_Outputs):
    """Intermediate class used to get outputs from equivalent_radiated_power operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.equivalent_radiated_power()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(equivalent_radiated_power._spec().outputs, op)
        self._fields_container = Output(equivalent_radiated_power._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.equivalent_radiated_power()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

