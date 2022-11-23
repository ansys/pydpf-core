"""
prepare_mapping_workflow
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mapping" category
"""

class prepare_mapping_workflow(Operator):
    """Generate a workflow that can map results from a support to another one.

      available inputs:
        - input_support (Field, MeshedRegion)
        - output_support (Field, MeshedRegion)
        - filter_radius (float)
        - influence_box (float) (optional)

      available outputs:
        - mapping_workflow (Workflow)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.prepare_mapping_workflow()

      >>> # Make input connections
      >>> my_input_support = dpf.Field()
      >>> op.inputs.input_support.connect(my_input_support)
      >>> my_output_support = dpf.Field()
      >>> op.inputs.output_support.connect(my_output_support)
      >>> my_filter_radius = float()
      >>> op.inputs.filter_radius.connect(my_filter_radius)
      >>> my_influence_box = float()
      >>> op.inputs.influence_box.connect(my_influence_box)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.prepare_mapping_workflow(input_support=my_input_support,output_support=my_output_support,filter_radius=my_filter_radius,influence_box=my_influence_box)

      >>> # Get output data
      >>> result_mapping_workflow = op.outputs.mapping_workflow()"""
    def __init__(self, input_support=None, output_support=None, filter_radius=None, influence_box=None, config=None, server=None):
        super().__init__(name="prepare_mapping_workflow", config = config, server = server)
        self._inputs = InputsPrepareMappingWorkflow(self)
        self._outputs = OutputsPrepareMappingWorkflow(self)
        if input_support !=None:
            self.inputs.input_support.connect(input_support)
        if output_support !=None:
            self.inputs.output_support.connect(output_support)
        if filter_radius !=None:
            self.inputs.filter_radius.connect(filter_radius)
        if influence_box !=None:
            self.inputs.influence_box.connect(influence_box)

    @staticmethod
    def _spec():
        spec = Specification(description="""Generate a workflow that can map results from a support to another one.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "input_support", type_names=["field","abstract_meshed_region"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "output_support", type_names=["field","abstract_meshed_region"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "filter_radius", type_names=["double"], optional=False, document="""Radius size for the RBF filter"""), 
                                 3 : PinSpecification(name = "influence_box", type_names=["double"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mapping_workflow", type_names=["workflow"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "prepare_mapping_workflow")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPrepareMappingWorkflow 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPrepareMappingWorkflow 
        """
        return super().outputs


#internal name: prepare_mapping_workflow
#scripting name: prepare_mapping_workflow
class InputsPrepareMappingWorkflow(_Inputs):
    """Intermediate class used to connect user inputs to prepare_mapping_workflow operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.prepare_mapping_workflow()
      >>> my_input_support = dpf.Field()
      >>> op.inputs.input_support.connect(my_input_support)
      >>> my_output_support = dpf.Field()
      >>> op.inputs.output_support.connect(my_output_support)
      >>> my_filter_radius = float()
      >>> op.inputs.filter_radius.connect(my_filter_radius)
      >>> my_influence_box = float()
      >>> op.inputs.influence_box.connect(my_influence_box)
    """
    def __init__(self, op: Operator):
        super().__init__(prepare_mapping_workflow._spec().inputs, op)
        self._input_support = Input(prepare_mapping_workflow._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._input_support)
        self._output_support = Input(prepare_mapping_workflow._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._output_support)
        self._filter_radius = Input(prepare_mapping_workflow._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._filter_radius)
        self._influence_box = Input(prepare_mapping_workflow._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._influence_box)

    @property
    def input_support(self):
        """Allows to connect input_support input to the operator

        Parameters
        ----------
        my_input_support : Field, MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.prepare_mapping_workflow()
        >>> op.inputs.input_support.connect(my_input_support)
        >>> #or
        >>> op.inputs.input_support(my_input_support)

        """
        return self._input_support

    @property
    def output_support(self):
        """Allows to connect output_support input to the operator

        Parameters
        ----------
        my_output_support : Field, MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.prepare_mapping_workflow()
        >>> op.inputs.output_support.connect(my_output_support)
        >>> #or
        >>> op.inputs.output_support(my_output_support)

        """
        return self._output_support

    @property
    def filter_radius(self):
        """Allows to connect filter_radius input to the operator

        - pindoc: Radius size for the RBF filter

        Parameters
        ----------
        my_filter_radius : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.prepare_mapping_workflow()
        >>> op.inputs.filter_radius.connect(my_filter_radius)
        >>> #or
        >>> op.inputs.filter_radius(my_filter_radius)

        """
        return self._filter_radius

    @property
    def influence_box(self):
        """Allows to connect influence_box input to the operator

        Parameters
        ----------
        my_influence_box : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.prepare_mapping_workflow()
        >>> op.inputs.influence_box.connect(my_influence_box)
        >>> #or
        >>> op.inputs.influence_box(my_influence_box)

        """
        return self._influence_box

class OutputsPrepareMappingWorkflow(_Outputs):
    """Intermediate class used to get outputs from prepare_mapping_workflow operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.prepare_mapping_workflow()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mapping_workflow = op.outputs.mapping_workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(prepare_mapping_workflow._spec().outputs, op)
        self._mapping_workflow = Output(prepare_mapping_workflow._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mapping_workflow)

    @property
    def mapping_workflow(self):
        """Allows to get mapping_workflow output of the operator


        Returns
        ----------
        my_mapping_workflow : Workflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.prepare_mapping_workflow()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mapping_workflow = op.outputs.mapping_workflow() 
        """
        return self._mapping_workflow

