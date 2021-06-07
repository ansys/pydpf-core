"""
result_info_provider
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "metadata" category
"""

class result_info_provider(Operator):
    """Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - result_info (ResultInfo)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.result_info_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.result_info_provider(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_result_info = op.outputs.result_info()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="ResultInfoProvider", config = config, server = server)
        self._inputs = InputsResultInfoProvider(self)
        self._outputs = OutputsResultInfoProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the result info with information sucha as available results or unit system from the results files contained in the streams or data sources.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "result_info", type_names=["result_info"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ResultInfoProvider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsResultInfoProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsResultInfoProvider 
        """
        return super().outputs


#internal name: ResultInfoProvider
#scripting name: result_info_provider
class InputsResultInfoProvider(_Inputs):
    """Intermediate class used to connect user inputs to result_info_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.result_info_provider()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().inputs, op)
        self._streams_container = Input(result_info_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(result_info_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: streams (result file container) (optional)

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.result_info_provider()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: if the stream is null then we need to get the file path from the data sources

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.result_info_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsResultInfoProvider(_Outputs):
    """Intermediate class used to get outputs from result_info_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.result_info_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_result_info = op.outputs.result_info()
    """
    def __init__(self, op: Operator):
        super().__init__(result_info_provider._spec().outputs, op)
        self._result_info = Output(result_info_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._result_info)

    @property
    def result_info(self):
        """Allows to get result_info output of the operator


        Returns
        ----------
        my_result_info : ResultInfo, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.result_info_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_result_info = op.outputs.result_info() 
        """
        return self._result_info

