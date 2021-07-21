"""
remote_workflow_provider
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "metadata" category
"""

class remote_workflow_provider(Operator):
    """Sends a workflow to a remote process for a given protocol registered in the streams.

      available inputs:
        - local_workflow ()
        - streams_to_remote (StreamsContainer)

      available outputs:
        - remote_workflow (RemoteWorkflow)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.remote_workflow_provider()

      >>> # Make input connections
      >>> my_streams_to_remote = dpf.StreamsContainer()
      >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.remote_workflow_provider(streams_to_remote=my_streams_to_remote)

      >>> # Get output data
      >>> result_remote_workflow = op.outputs.remote_workflow()"""
    def __init__(self, streams_to_remote=None, config=None, server=None):
        super().__init__(name="remote_workflow_provider", config = config, server = server)
        self._inputs = InputsRemoteWorkflowProvider(self)
        self._outputs = OutputsRemoteWorkflowProvider(self)
        if streams_to_remote !=None:
            self.inputs.streams_to_remote.connect(streams_to_remote)

    @staticmethod
    def _spec():
        spec = Specification(description="""Sends a workflow to a remote process for a given protocol registered in the streams.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "local_workflow", type_names=[], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "streams_to_remote", type_names=["streams_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "remote_workflow", type_names=["remote_workflow"], optional=False, document="""remote workflow containing an image of the remote workflow and the protocols streams""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "remote_workflow_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRemoteWorkflowProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRemoteWorkflowProvider 
        """
        return super().outputs


#internal name: remote_workflow_provider
#scripting name: remote_workflow_provider
class InputsRemoteWorkflowProvider(_Inputs):
    """Intermediate class used to connect user inputs to remote_workflow_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.remote_workflow_provider()
      >>> my_streams_to_remote = dpf.StreamsContainer()
      >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
    """
    def __init__(self, op: Operator):
        super().__init__(remote_workflow_provider._spec().inputs, op)
        self._streams_to_remote = Input(remote_workflow_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_to_remote)

    @property
    def streams_to_remote(self):
        """Allows to connect streams_to_remote input to the operator

        Parameters
        ----------
        my_streams_to_remote : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.remote_workflow_provider()
        >>> op.inputs.streams_to_remote.connect(my_streams_to_remote)
        >>> #or
        >>> op.inputs.streams_to_remote(my_streams_to_remote)

        """
        return self._streams_to_remote

class OutputsRemoteWorkflowProvider(_Outputs):
    """Intermediate class used to get outputs from remote_workflow_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.remote_workflow_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_remote_workflow = op.outputs.remote_workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(remote_workflow_provider._spec().outputs, op)
        self._remote_workflow = Output(remote_workflow_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._remote_workflow)

    @property
    def remote_workflow(self):
        """Allows to get remote_workflow output of the operator


        - pindoc: remote workflow containing an image of the remote workflow and the protocols streams

        Returns
        ----------
        my_remote_workflow : RemoteWorkflow, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.remote_workflow_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_remote_workflow = op.outputs.remote_workflow() 
        """
        return self._remote_workflow

