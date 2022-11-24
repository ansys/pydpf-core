"""
contact_sliding_distance
========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class contact_sliding_distance(Operator):
    """Read/compute element contact sliding distance by calling the readers defined by the datasources.

      available inputs:
        - time_scoping (Scoping, int, listfloat, Field, list) (optional)
        - mesh_scoping (ScopingsContainer, Scoping) (optional)
        - fields_container (FieldsContainer) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - bool_rotate_to_global (bool) (optional)
        - mesh (MeshedRegion, MeshesContainer) (optional)
        - read_cyclic (int) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.contact_sliding_distance()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_bool_rotate_to_global = bool()
      >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_read_cyclic = int()
      >>> op.inputs.read_cyclic.connect(my_read_cyclic)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.contact_sliding_distance(time_scoping=my_time_scoping,mesh_scoping=my_mesh_scoping,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, time_scoping=None, mesh_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="ECT_SLIDE", config = config, server = server)
        self._inputs = InputsContactSlidingDistance(self)
        self._outputs = OutputsContactSlidingDistance(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read/compute element contact sliding distance by calling the readers defined by the datasources.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","int32","vector<int32>","double","field","vector<double>"], optional=True, document="""time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output"""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scopings_container","scoping"], optional=True, document="""nodes or elements scoping required in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains"""), 
                                 2 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=True, document="""Fields container already allocated modified inplace"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 5 : PinSpecification(name = "bool_rotate_to_global", type_names=["bool"], optional=True, document="""if true the field is rotated to global coordinate system (default true)"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""prevents from reading the mesh in the result files"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "ECT_SLIDE")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsContactSlidingDistance 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsContactSlidingDistance 
        """
        return super().outputs


#internal name: ECT_SLIDE
#scripting name: contact_sliding_distance
class InputsContactSlidingDistance(_Inputs):
    """Intermediate class used to connect user inputs to contact_sliding_distance operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.contact_sliding_distance()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_mesh_scoping = dpf.ScopingsContainer()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_bool_rotate_to_global = bool()
      >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_read_cyclic = int()
      >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    """
    def __init__(self, op: Operator):
        super().__init__(contact_sliding_distance._spec().inputs, op)
        self._time_scoping = Input(contact_sliding_distance._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._mesh_scoping = Input(contact_sliding_distance._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._fields_container = Input(contact_sliding_distance._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_container)
        self._streams_container = Input(contact_sliding_distance._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(contact_sliding_distance._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._bool_rotate_to_global = Input(contact_sliding_distance._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._bool_rotate_to_global)
        self._mesh = Input(contact_sliding_distance._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)
        self._read_cyclic = Input(contact_sliding_distance._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self._read_cyclic)

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

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        - pindoc: nodes or elements scoping required in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains

        Parameters
        ----------
        my_mesh_scoping : ScopingsContainer, Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Fields container already allocated modified inplace

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

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

        >>> op = dpf.operators.result.contact_sliding_distance()
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

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def bool_rotate_to_global(self):
        """Allows to connect bool_rotate_to_global input to the operator

        - pindoc: if true the field is rotated to global coordinate system (default true)

        Parameters
        ----------
        my_bool_rotate_to_global : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.bool_rotate_to_global.connect(my_bool_rotate_to_global)
        >>> #or
        >>> op.inputs.bool_rotate_to_global(my_bool_rotate_to_global)

        """
        return self._bool_rotate_to_global

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: prevents from reading the mesh in the result files

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def read_cyclic(self):
        """Allows to connect read_cyclic input to the operator

        - pindoc: if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1)

        Parameters
        ----------
        my_read_cyclic : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> op.inputs.read_cyclic.connect(my_read_cyclic)
        >>> #or
        >>> op.inputs.read_cyclic(my_read_cyclic)

        """
        return self._read_cyclic

class OutputsContactSlidingDistance(_Outputs):
    """Intermediate class used to get outputs from contact_sliding_distance operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.contact_sliding_distance()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(contact_sliding_distance._spec().outputs, op)
        self._fields_container = Output(contact_sliding_distance._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.contact_sliding_distance()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

