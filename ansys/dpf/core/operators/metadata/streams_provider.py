"""
streams_provider
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "metadata" category
"""

class streams_provider(Operator):
    """Creates streams (files with cache) from the data sources.

      available inputs:
        - data_sources (DataSources)

      available outputs:
        - streams_container (StreamsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.streams_provider()

      >>> # Make input connections
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.streams_provider(data_sources=my_data_sources)

      >>> # Get output data
      >>> result_streams_container = op.outputs.streams_container()"""
    def __init__(self, data_sources=None, config=None, server=None):
        super().__init__(name="stream_provider", config = config, server = server)
        self._inputs = InputsStreamsProvider(self)
        self._outputs = OutputsStreamsProvider(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Creates streams (files with cache) from the data sources.""",
                             map_input_pin_spec={
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "stream_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsStreamsProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsStreamsProvider 
        """
        return super().outputs


#internal name: stream_provider
#scripting name: streams_provider
class InputsStreamsProvider(_Inputs):
    """Intermediate class used to connect user inputs to streams_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.streams_provider()
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(streams_provider._spec().inputs, op)
        self._data_sources = Input(streams_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.streams_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsStreamsProvider(_Outputs):
    """Intermediate class used to get outputs from streams_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.streams_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_streams_container = op.outputs.streams_container()
    """
    def __init__(self, op: Operator):
        super().__init__(streams_provider._spec().outputs, op)
        self._streams_container = Output(streams_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._streams_container)

    @property
    def streams_container(self):
        """Allows to get streams_container output of the operator


        Returns
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.streams_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_streams_container = op.outputs.streams_container() 
        """
        return self._streams_container

