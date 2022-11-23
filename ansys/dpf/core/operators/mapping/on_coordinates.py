"""
on_coordinates
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mapping" category
"""

class on_coordinates(Operator):
    """Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).

      available inputs:
        - fields_container (FieldsContainer)
        - coordinates (Field, FieldsContainer, MeshedRegion, MeshesContainer)
        - create_support (bool) (optional)
        - mapping_on_scoping (bool) (optional)
        - mesh (MeshedRegion, MeshesContainer) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.on_coordinates()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_coordinates = dpf.Field()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_create_support = bool()
      >>> op.inputs.create_support.connect(my_create_support)
      >>> my_mapping_on_scoping = bool()
      >>> op.inputs.mapping_on_scoping.connect(my_mapping_on_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.on_coordinates(fields_container=my_fields_container,coordinates=my_coordinates,create_support=my_create_support,mapping_on_scoping=my_mapping_on_scoping,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, coordinates=None, create_support=None, mapping_on_scoping=None, mesh=None, config=None, server=None):
        super().__init__(name="mapping", config = config, server = server)
        self._inputs = InputsOnCoordinates(self)
        self._outputs = OutputsOnCoordinates(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if coordinates !=None:
            self.inputs.coordinates.connect(coordinates)
        if create_support !=None:
            self.inputs.create_support.connect(create_support)
        if mapping_on_scoping !=None:
            self.inputs.mapping_on_scoping.connect(mapping_on_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "coordinates", type_names=["field","fields_container","abstract_meshed_region","meshes_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "create_support", type_names=["bool"], optional=True, document="""if this pin is set to true, then, a support associated to the fields consisting of points is created"""), 
                                 3 : PinSpecification(name = "mapping_on_scoping", type_names=["bool"], optional=True, document="""if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false), if a meshes container with several meshes is set, it should be on the same label spaces as the coordinates fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapping")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOnCoordinates 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOnCoordinates 
        """
        return super().outputs


#internal name: mapping
#scripting name: on_coordinates
class InputsOnCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to on_coordinates operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.on_coordinates()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_coordinates = dpf.Field()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_create_support = bool()
      >>> op.inputs.create_support.connect(my_create_support)
      >>> my_mapping_on_scoping = bool()
      >>> op.inputs.mapping_on_scoping.connect(my_mapping_on_scoping)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(on_coordinates._spec().inputs, op)
        self._fields_container = Input(on_coordinates._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._coordinates = Input(on_coordinates._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._coordinates)
        self._create_support = Input(on_coordinates._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._create_support)
        self._mapping_on_scoping = Input(on_coordinates._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._mapping_on_scoping)
        self._mesh = Input(on_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def coordinates(self):
        """Allows to connect coordinates input to the operator

        Parameters
        ----------
        my_coordinates : Field, FieldsContainer, MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> op.inputs.coordinates.connect(my_coordinates)
        >>> #or
        >>> op.inputs.coordinates(my_coordinates)

        """
        return self._coordinates

    @property
    def create_support(self):
        """Allows to connect create_support input to the operator

        - pindoc: if this pin is set to true, then, a support associated to the fields consisting of points is created

        Parameters
        ----------
        my_create_support : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> op.inputs.create_support.connect(my_create_support)
        >>> #or
        >>> op.inputs.create_support(my_create_support)

        """
        return self._create_support

    @property
    def mapping_on_scoping(self):
        """Allows to connect mapping_on_scoping input to the operator

        - pindoc: if this pin is set to true, then the mapping between the coordinates and the fields is created only on the first field scoping

        Parameters
        ----------
        my_mapping_on_scoping : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> op.inputs.mapping_on_scoping.connect(my_mapping_on_scoping)
        >>> #or
        >>> op.inputs.mapping_on_scoping(my_mapping_on_scoping)

        """
        return self._mapping_on_scoping

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: if the first field in input has no mesh in support, then the mesh in this pin is expected (default is false), if a meshes container with several meshes is set, it should be on the same label spaces as the coordinates fields container

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsOnCoordinates(_Outputs):
    """Intermediate class used to get outputs from on_coordinates operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.on_coordinates()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(on_coordinates._spec().outputs, op)
        self._fields_container = Output(on_coordinates._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.mapping.on_coordinates()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

