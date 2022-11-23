"""
beam_t_shear_force
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class beam_t_shear_force(Operator):
    """Read Beam T Shear Force (LSDyna) by calling the readers defined by the datasources.

      available inputs:
        - time_scoping (Scoping, int, listfloat, Field, list) (optional)
        - mesh_scoping (ScopingsContainer, Scoping) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.beam_t_shear_force()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.beam_t_shear_force(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="B_T2", config = config, server = server)
        self._inputs = InputsBeamTShearForce(self)
        self._outputs = OutputsBeamTShearForce(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read Beam T Shear Force (LSDyna) by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""elements scoping required in output."""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "B_T2")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsBeamTShearForce 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsBeamTShearForce 
        """
        return super().outputs


#internal name: B_T2
#scripting name: beam_t_shear_force
class InputsBeamTShearForce(_Inputs):
    """Intermediate class used to connect user inputs to beam_t_shear_force operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.beam_t_shear_force()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(beam_t_shear_force._spec().inputs, op)
        self._time_scoping = Input(beam_t_shear_force._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(beam_t_shear_force._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._streams_container = Input(beam_t_shear_force._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(beam_t_shear_force._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output

        Parameters
        ----------
        my_time_scoping : Scoping, int, list, float, Field, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.beam_t_shear_force()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: elements scoping required in output.

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer, Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.beam_t_shear_force()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: result file container allowed to be kept open to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.beam_t_shear_force()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: result file path container, used if no streams are set

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.beam_t_shear_force()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsBeamTShearForce(_Outputs):
    """Intermediate class used to get outputs from beam_t_shear_force operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.beam_t_shear_force()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(beam_t_shear_force._spec().outputs, op)
        self._fields_container = Output(beam_t_shear_force._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.beam_t_shear_force()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

