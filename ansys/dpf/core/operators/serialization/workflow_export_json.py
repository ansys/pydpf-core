"""
workflow_export_json
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "serialization" category
"""

class workflow_export_json(Operator):
    """Export a workflow in json format.

      available inputs:
        - workflow (Workflow)
        - file_path (str) (optional)

      available outputs:
        - json_workflow (DataSources ,str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.workflow_export_json()

      >>> # Make input connections
      >>> my_workflow = dpf.Workflow()
      >>> op.inputs.workflow.connect(my_workflow)
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.workflow_export_json(workflow=my_workflow,file_path=my_file_path)

      >>> # Get output data
      >>> result_json_workflow = op.outputs.json_workflow()"""
    def __init__(self, workflow=None, file_path=None, config=None, server=None):
        super().__init__(name="serialization::workflow_export_json", config = config, server = server)
        self._inputs = InputsWorkflowExportJson(self)
        self._outputs = OutputsWorkflowExportJson(self)
        if workflow !=None:
            self.inputs.workflow.connect(workflow)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Export a workflow in json format.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "workflow", type_names=["workflow"], optional=False, document="""Workflow to serialize."""), 
                                 1 : PinSpecification(name = "file_path", type_names=["string"], optional=True, document="""File path to write results to. When given the operator will return a data source to the path, otherwise a json string will be output.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "json_workflow", type_names=["data_sources","string"], optional=False, document="""Depending on the input of pin 1 the output will either be a data source to a json file or a json string.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "serialization::workflow_export_json")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsWorkflowExportJson 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsWorkflowExportJson 
        """
        return super().outputs


#internal name: serialization::workflow_export_json
#scripting name: workflow_export_json
class InputsWorkflowExportJson(_Inputs):
    """Intermediate class used to connect user inputs to workflow_export_json operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.workflow_export_json()
      >>> my_workflow = dpf.Workflow()
      >>> op.inputs.workflow.connect(my_workflow)
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
    """
    def __init__(self, op: Operator):
        super().__init__(workflow_export_json._spec().inputs, op)
        self._workflow = Input(workflow_export_json._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._workflow)
        self._file_path = Input(workflow_export_json._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._file_path)

    @property
    def workflow(self):
        """Allows to connect workflow input to the operator

        - pindoc: Workflow to serialize.

        Parameters
        ----------
        my_workflow : Workflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.workflow_export_json()
        >>> op.inputs.workflow.connect(my_workflow)
        >>> #or
        >>> op.inputs.workflow(my_workflow)

        """
        return self._workflow

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator

        - pindoc: File path to write results to. When given the operator will return a data source to the path, otherwise a json string will be output.

        Parameters
        ----------
        my_file_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.workflow_export_json()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> #or
        >>> op.inputs.file_path(my_file_path)

        """
        return self._file_path

class OutputsWorkflowExportJson(_Outputs):
    """Intermediate class used to get outputs from workflow_export_json operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.workflow_export_json()
      >>> # Connect inputs : op.inputs. ...
      >>> result_json_workflow = op.outputs.json_workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(workflow_export_json._spec().outputs, op)
        self.json_workflow_as_data_sources = Output( _modify_output_spec_with_one_type(workflow_export_json._spec().output_pin(0), "data_sources"), 0, op) 
        self._outputs.append(self.json_workflow_as_data_sources)
        self.json_workflow_as_string = Output( _modify_output_spec_with_one_type(workflow_export_json._spec().output_pin(0), "string"), 0, op) 
        self._outputs.append(self.json_workflow_as_string)

