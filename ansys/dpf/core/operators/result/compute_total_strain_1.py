"""
compute_total_strain_1
======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class compute_total_strain_1(Operator):
    """Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the 1st principal component.

      available inputs:
        - time_scoping (Scoping, int, listfloat, Field, list) (optional)
        - scoping (Scoping) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources) (optional)
        - extrapolate (int) (optional)
        - nonlinear (int) (optional)
        - meshed_region (MeshedRegion) (optional)
        - requested_location (str) (optional)
        - displacement (FieldsContainer, Field) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.compute_total_strain_1()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_extrapolate = int()
      >>> op.inputs.extrapolate.connect(my_extrapolate)
      >>> my_nonlinear = int()
      >>> op.inputs.nonlinear.connect(my_nonlinear)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.compute_total_strain_1(time_scoping=my_time_scoping,scoping=my_scoping,streams_container=my_streams_container,data_sources=my_data_sources,extrapolate=my_extrapolate,nonlinear=my_nonlinear,meshed_region=my_meshed_region,requested_location=my_requested_location,displacement=my_displacement)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, time_scoping=None, scoping=None, streams_container=None, data_sources=None, extrapolate=None, nonlinear=None, meshed_region=None, requested_location=None, displacement=None, config=None, server=None):
        super().__init__(name="compute_total_strain_1", config = config, server = server)
        self._inputs = InputsComputeTotalStrain1(self)
        self._outputs = OutputsComputeTotalStrain1(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if extrapolate !=None:
            self.inputs.extrapolate.connect(extrapolate)
        if nonlinear !=None:
            self.inputs.nonlinear.connect(nonlinear)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if displacement !=None:
            self.inputs.displacement.connect(displacement)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the 1st principal component.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output. Will only be used if no displacement input is given (will be applied on displacement operator)."""), 
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""The element scoping on which the result is computed."""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""Optional if a mesh or a data_sources have been connected. Required if no displacement input have been connected."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=True, document="""Optional if a mesh or a streams_container have been connected, or if the displacement's field has a mesh support. Required if no displacement input have been connected."""), 
                                 5 : PinSpecification(name = "extrapolate", type_names=["int32"], optional=True, document="""Whether to extrapolate the data from the integration points to the nodes."""), 
                                 6 : PinSpecification(name = "nonlinear", type_names=["int32"], optional=True, document="""Whether to use nonlinear geometry or nonlinear material (1 = large strain, 2 = hyperelasticity)."""), 
                                 7 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""The underlying mesh. Optional if a data_sources or a streams_container have been connected, or if the displacement's field has a mesh support."""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string"], optional=True, document="""Average the Elemental Nodal result to the requested location."""), 
                                 10 : PinSpecification(name = "displacement", type_names=["fields_container","field"], optional=True, document="""Field/or fields container containing only the displacement field (nodal). If none specified, read displacements from result file using the data_sources.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""The computed result fields container (elemental nodal).""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "compute_total_strain_1")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeTotalStrain1 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsComputeTotalStrain1 
        """
        return super().outputs


#internal name: compute_total_strain_1
#scripting name: compute_total_strain_1
class InputsComputeTotalStrain1(_Inputs):
    """Intermediate class used to connect user inputs to compute_total_strain_1 operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.compute_total_strain_1()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_extrapolate = int()
      >>> op.inputs.extrapolate.connect(my_extrapolate)
      >>> my_nonlinear = int()
      >>> op.inputs.nonlinear.connect(my_nonlinear)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)
    """
    def __init__(self, op: Operator):
        super().__init__(compute_total_strain_1._spec().inputs, op)
        self._time_scoping = Input(compute_total_strain_1._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._scoping = Input(compute_total_strain_1._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scoping)
        self._streams_container = Input(compute_total_strain_1._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(compute_total_strain_1._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._extrapolate = Input(compute_total_strain_1._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._extrapolate)
        self._nonlinear = Input(compute_total_strain_1._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._nonlinear)
        self._meshed_region = Input(compute_total_strain_1._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._meshed_region)
        self._requested_location = Input(compute_total_strain_1._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self._requested_location)
        self._displacement = Input(compute_total_strain_1._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._displacement)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output. Will only be used if no displacement input is given (will be applied on displacement operator).

        Parameters
        ----------
        my_time_scoping : Scoping, int, list, float, Field, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: The element scoping on which the result is computed.

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: Optional if a mesh or a data_sources have been connected. Required if no displacement input have been connected.

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: Optional if a mesh or a streams_container have been connected, or if the displacement's field has a mesh support. Required if no displacement input have been connected.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def extrapolate(self):
        """Allows to connect extrapolate input to the operator

        - pindoc: Whether to extrapolate the data from the integration points to the nodes.

        Parameters
        ----------
        my_extrapolate : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.extrapolate.connect(my_extrapolate)
        >>> #or
        >>> op.inputs.extrapolate(my_extrapolate)

        """
        return self._extrapolate

    @property
    def nonlinear(self):
        """Allows to connect nonlinear input to the operator

        - pindoc: Whether to use nonlinear geometry or nonlinear material (1 = large strain, 2 = hyperelasticity).

        Parameters
        ----------
        my_nonlinear : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.nonlinear.connect(my_nonlinear)
        >>> #or
        >>> op.inputs.nonlinear(my_nonlinear)

        """
        return self._nonlinear

    @property
    def meshed_region(self):
        """Allows to connect meshed_region input to the operator

        - pindoc: The underlying mesh. Optional if a data_sources or a streams_container have been connected, or if the displacement's field has a mesh support.

        Parameters
        ----------
        my_meshed_region : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.meshed_region.connect(my_meshed_region)
        >>> #or
        >>> op.inputs.meshed_region(my_meshed_region)

        """
        return self._meshed_region

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        - pindoc: Average the Elemental Nodal result to the requested location.

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

    @property
    def displacement(self):
        """Allows to connect displacement input to the operator

        - pindoc: Field/or fields container containing only the displacement field (nodal). If none specified, read displacements from result file using the data_sources.

        Parameters
        ----------
        my_displacement : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> op.inputs.displacement.connect(my_displacement)
        >>> #or
        >>> op.inputs.displacement(my_displacement)

        """
        return self._displacement

class OutputsComputeTotalStrain1(_Outputs):
    """Intermediate class used to get outputs from compute_total_strain_1 operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.compute_total_strain_1()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(compute_total_strain_1._spec().outputs, op)
        self._fields_container = Output(compute_total_strain_1._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: The computed result fields container (elemental nodal).

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.compute_total_strain_1()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

