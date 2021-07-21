"""
remote_data_provider
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "metadata" category
"""

class remote_data_provider(Operator):
    """Returns the data of a remote locally for a given protocol registered in the streams.

      available inputs:
        - remote_workflow_output_name (str)
        - remote_workflow (RemoteWorkflow) (optional)

      available outputs:
        - local_data ()

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.remote_data_provider()

      >>> # Make input connections
      >>> my_remote_workflow_output_name = str()
      >>> op.inputs.remote_workflow_output_name.connect(my_remote_workflow_output_name)
      >>> my_remote_workflow = dpf.RemoteWorkflow()
      >>> op.inputs.remote_workflow.connect(my_remote_workflow)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.remote_data_provider(remote_workflow_output_name=my_remote_workflow_output_name,remote_workflow=my_remote_workflow)

      >>> # Get output data
      >>> result_local_data = op.outputs.local_data()"""
    def __init__(self, remote_workflow_output_name=None, remote_workflow=None, config=None, server=None):
        super().__init__(name="remote_data_provider", config = config, server = server)
        self._inputs = InputsRemoteDataProvider(self)
        self._outputs = OutputsRemoteDataProvider(self)
        if remote_workflow_output_name !=None:
            self.inputs.remote_workflow_output_name.connect(remote_workflow_output_name)
        if remote_workflow !=None:
            self.inputs.remote_workflow.connect(remote_workflow)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns the data of a remote locally for a given protocol registered in the streams.""",
                             map_input_pin_spec={
                                 2 : PinSpecification(name = "remote_workflow_output_name", type_names=["string"], optional=False, document="""name of the remote workflow output to chain to the local workflow"""), 
                                 3 : PinSpecification(name = "remote_workflow", type_names=["remote_workflow"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "local_data", type_names=[], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "remote_data_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoteDataProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoteDataProvider 
        """
        return super().outputs


#internal name: remote_data_provider
#scripting name: remote_data_provider
class InputsRemoteDataProvider(_Inputs):
    """Intermediate class used to connect user inputs to remote_data_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.remote_data_provider()
      >>> my_remote_workflow_output_name = str()
      >>> op.inputs.remote_workflow_output_name.connect(my_remote_workflow_output_name)
      >>> my_remote_workflow = dpf.RemoteWorkflow()
      >>> op.inputs.remote_workflow.connect(my_remote_workflow)
    """
    def __init__(self, op: Operator):
        super().__init__(remote_data_provider._spec().inputs, op)
        self._remote_workflow_output_name = Input(remote_data_provider._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._remote_workflow_output_name)
        self._remote_workflow = Input(remote_data_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._remote_workflow)

    @property
    def remote_workflow_output_name(self):
        """Allows to connect remote_workflow_output_name input to the operator

        - pindoc: name of the remote workflow output to chain to the local workflow

        Parameters
        ----------
        my_remote_workflow_output_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.remote_data_provider()
        >>> op.inputs.remote_workflow_output_name.connect(my_remote_workflow_output_name)
        >>> #or
        >>> op.inputs.remote_workflow_output_name(my_remote_workflow_output_name)

        """
        return self._remote_workflow_output_name

    @property
    def remote_workflow(self):
        """Allows to connect remote_workflow input to the operator

        Parameters
        ----------
        my_remote_workflow : RemoteWorkflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.remote_data_provider()
        >>> op.inputs.remote_workflow.connect(my_remote_workflow)
        >>> #or
        >>> op.inputs.remote_workflow(my_remote_workflow)

        """
        return self._remote_workflow

class OutputsRemoteDataProvider(_Outputs):
    """Intermediate class used to get outputs from remote_data_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.remote_data_provider()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(remote_data_provider._spec().outputs, op)
        pass 

