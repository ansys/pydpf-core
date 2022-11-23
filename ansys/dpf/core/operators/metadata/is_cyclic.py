"""
is_cyclic
=========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "metadata" category
"""

class is_cyclic(Operator):
    """Read if the model is cyclic form the result file.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - file_path (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.is_cyclic()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.is_cyclic(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_file_path = op.outputs.file_path()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="is_cyclic", config = config, server = server)
        self._inputs = InputsIsCyclic(self)
        self._outputs = OutputsIsCyclic(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read if the model is cyclic form the result file.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""streams (result file container) (optional)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""if the stream is null then we need to get the file path from the data sources""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "is_cyclic")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIsCyclic 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIsCyclic 
        """
        return super().outputs


#internal name: is_cyclic
#scripting name: is_cyclic
class InputsIsCyclic(_Inputs):
    """Intermediate class used to connect user inputs to is_cyclic operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.is_cyclic()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(is_cyclic._spec().inputs, op)
        self._streams_container = Input(is_cyclic._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(is_cyclic._spec().input_pin(4), 4, op, -1) 
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

        >>> op = dpf.operators.metadata.is_cyclic()
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

        >>> op = dpf.operators.metadata.is_cyclic()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsIsCyclic(_Outputs):
    """Intermediate class used to get outputs from is_cyclic operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.is_cyclic()
      >>> # Connect inputs : op.inputs. ...
      >>> result_file_path = op.outputs.file_path()
    """
    def __init__(self, op: Operator):
        super().__init__(is_cyclic._spec().outputs, op)
        self._file_path = Output(is_cyclic._spec().output_pin(0), 0, op) 
        self._outputs.append(self._file_path)

    @property
    def file_path(self):
        """Allows to get file_path output of the operator


        - pindoc: returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model

        Returns
        ----------
        my_file_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.is_cyclic()
        >>> # Connect inputs : op.inputs. ...
        >>> result_file_path = op.outputs.file_path() 
        """
        return self._file_path

