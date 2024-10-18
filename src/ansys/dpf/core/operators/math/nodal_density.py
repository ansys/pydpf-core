"""
nodal_density
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class nodal_density(Operator):
    """Extract Nodal Topology Density result from topo solver output. Default behavior is to use graphical density.

      available inputs:
        - time_scoping (Scoping) (optional)
        - mesh_scoping (Scoping) (optional)
        - streams (StreamsContainer) (optional)
        - data_sources (DataSources) (optional)
        - custom_ponderation_name (str)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.nodal_density()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_custom_ponderation_name = str()
      >>> op.inputs.custom_ponderation_name.connect(my_custom_ponderation_name)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.nodal_density(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,streams=my_streams,data_sources=my_data_sources,custom_ponderation_name=my_custom_ponderation_name)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, streams=None, data_sources=None, custom_ponderation_name=None, config=None, server=None):
        super().__init__(name="hdf5::topo::nodal_density", config = config, server = server)
        self._inputs = InputsNodalDensity(self)
        self._outputs = OutputsNodalDensity(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if streams !=None:
            self.inputs.streams.connect(streams)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if custom_ponderation_name !=None:
            self.inputs.custom_ponderation_name.connect(custom_ponderation_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extract Nodal Topology Density result from topo solver output. Default behavior is to use graphical density.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams", type_names=["streams_container"], optional=True, document="""topo file stream."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=True, document="""topo file data source."""), 
                                 200 : PinSpecification(name = "custom_ponderation_name", type_names=["string"], optional=False, document="""take custom ponderation_field from the topo file by name""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "hdf5::topo::nodal_density")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsNodalDensity 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsNodalDensity 
        """
        return super().outputs


#internal name: hdf5::topo::nodal_density
#scripting name: nodal_density
class InputsNodalDensity(_Inputs):
    """Intermediate class used to connect user inputs to nodal_density operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.nodal_density()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_custom_ponderation_name = str()
      >>> op.inputs.custom_ponderation_name.connect(my_custom_ponderation_name)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_density._spec().inputs, op)
        self._time_scoping = Input(nodal_density._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(nodal_density._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._streams = Input(nodal_density._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams)
        self._data_sources = Input(nodal_density._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._custom_ponderation_name = Input(nodal_density._spec().input_pin(200), 200, op, -1) 
        self._inputs.append(self._custom_ponderation_name)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        Parameters
        ----------
        my_time_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def streams(self):
        """Allows to connect streams input to the operator

        - pindoc: topo file stream.

        Parameters
        ----------
        my_streams : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> op.inputs.streams.connect(my_streams)
        >>> #or
        >>> op.inputs.streams(my_streams)

        """
        return self._streams

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: topo file data source.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def custom_ponderation_name(self):
        """Allows to connect custom_ponderation_name input to the operator

        - pindoc: take custom ponderation_field from the topo file by name

        Parameters
        ----------
        my_custom_ponderation_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> op.inputs.custom_ponderation_name.connect(my_custom_ponderation_name)
        >>> #or
        >>> op.inputs.custom_ponderation_name(my_custom_ponderation_name)

        """
        return self._custom_ponderation_name

class OutputsNodalDensity(_Outputs):
    """Intermediate class used to get outputs from nodal_density operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.nodal_density()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_density._spec().outputs, op)
        self._field = Output(nodal_density._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.nodal_density()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

