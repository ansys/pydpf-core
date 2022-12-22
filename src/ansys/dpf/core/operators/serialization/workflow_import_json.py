"""
workflow_import_json
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "serialization" category
"""

class workflow_import_json(Operator):
    """Import a workflow in json format.

      available inputs:
        - json_workflow (str, DataSources)

      available outputs:
        - workflow (Workflow)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.workflow_import_json()

      >>> # Make input connections
      >>> my_json_workflow = str()
      >>> op.inputs.json_workflow.connect(my_json_workflow)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.workflow_import_json(json_workflow=my_json_workflow)

      >>> # Get output data
      >>> result_workflow = op.outputs.workflow()"""
    def __init__(self, json_workflow=None, config=None, server=None):
        super().__init__(name="serialization::workflow_import_json", config = config, server = server)
        self._inputs = InputsWorkflowImportJson(self)
        self._outputs = OutputsWorkflowImportJson(self)
        if json_workflow !=None:
            self.inputs.json_workflow.connect(json_workflow)

    @staticmethod
    def _spec():
        spec = Specification(description="""Import a workflow in json format.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "json_workflow", type_names=["string","data_sources"], optional=False, document="""Input json data as either a data source or a string""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "workflow", type_names=["workflow"], optional=False, document="""Instantiate workflow.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "serialization::workflow_import_json")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsWorkflowImportJson 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsWorkflowImportJson 
        """
        return super().outputs


#internal name: serialization::workflow_import_json
#scripting name: workflow_import_json
class InputsWorkflowImportJson(_Inputs):
    """Intermediate class used to connect user inputs to workflow_import_json operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.workflow_import_json()
      >>> my_json_workflow = str()
      >>> op.inputs.json_workflow.connect(my_json_workflow)
    """
    def __init__(self, op: Operator):
        super().__init__(workflow_import_json._spec().inputs, op)
        self._json_workflow = Input(workflow_import_json._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._json_workflow)

    @property
    def json_workflow(self):
        """Allows to connect json_workflow input to the operator

        - pindoc: Input json data as either a data source or a string

        Parameters
        ----------
        my_json_workflow : str, DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.workflow_import_json()
        >>> op.inputs.json_workflow.connect(my_json_workflow)
        >>> #or
        >>> op.inputs.json_workflow(my_json_workflow)

        """
        return self._json_workflow

class OutputsWorkflowImportJson(_Outputs):
    """Intermediate class used to get outputs from workflow_import_json operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.workflow_import_json()
      >>> # Connect inputs : op.inputs. ...
      >>> result_workflow = op.outputs.workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(workflow_import_json._spec().outputs, op)
        self._workflow = Output(workflow_import_json._spec().output_pin(0), 0, op) 
        self._outputs.append(self._workflow)

    @property
    def workflow(self):
        """Allows to get workflow output of the operator


        - pindoc: Instantiate workflow.

        Returns
        ----------
        my_workflow : Workflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.workflow_import_json()
        >>> # Connect inputs : op.inputs. ...
        >>> result_workflow = op.outputs.workflow() 
        """
        return self._workflow

