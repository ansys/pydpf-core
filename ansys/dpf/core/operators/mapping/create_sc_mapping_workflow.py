"""
create_sc_mapping_workflow
==========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mapping" category
"""


class create_sc_mapping_workflow(Operator):
    """Prepares a workflow able to map data from an input mesh to a target mesh.

      available inputs:
        - source_mesh (MeshedRegion, MeshesContainer, Field, FieldsContainer) (optional)
        - target_mesh (MeshedRegion, MeshesContainer, Field, FieldsContainer) (optional)
        - is_conservative (bool) (optional)
        - location (str) (optional)
        - dimensionality (int) (optional)
        - is_pointcloud (bool) (optional)
        - target_scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
        - mapping_workflow (Workflow)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.create_sc_mapping_workflow()

      >>> # Make input connections
      >>> my_source_mesh = dpf.MeshedRegion()
      >>> op.inputs.source_mesh.connect(my_source_mesh)
      >>> my_target_mesh = dpf.MeshedRegion()
      >>> op.inputs.target_mesh.connect(my_target_mesh)
      >>> my_is_conservative = bool()
      >>> op.inputs.is_conservative.connect(my_is_conservative)
      >>> my_location = str()
      >>> op.inputs.location.connect(my_location)
      >>> my_dimensionality = int()
      >>> op.inputs.dimensionality.connect(my_dimensionality)
      >>> my_is_pointcloud = bool()
      >>> op.inputs.is_pointcloud.connect(my_is_pointcloud)
      >>> my_target_scoping = dpf.Scoping()
      >>> op.inputs.target_scoping.connect(my_target_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.create_sc_mapping_workflow(source_mesh=my_source_mesh,target_mesh=my_target_mesh,is_conservative=my_is_conservative,location=my_location,dimensionality=my_dimensionality,is_pointcloud=my_is_pointcloud,target_scoping=my_target_scoping)

      >>> # Get output data
      >>> result_mapping_workflow = op.outputs.mapping_workflow()"""
    def __init__(self, source_mesh=None, target_mesh=None, is_conservative=None, location=None, dimensionality=None, is_pointcloud=None, target_scoping=None, config=None, server=None):
        super().__init__(name="create_sc_mapping_workflow", config = config, server = server)
        self._inputs = InputsCreateScMappingWorkflow(self)
        self._outputs = OutputsCreateScMappingWorkflow(self)
        if source_mesh !=None:
            self.inputs.source_mesh.connect(source_mesh)
        if target_mesh !=None:
            self.inputs.target_mesh.connect(target_mesh)
        if is_conservative !=None:
            self.inputs.is_conservative.connect(is_conservative)
        if location !=None:
            self.inputs.location.connect(location)
        if dimensionality !=None:
            self.inputs.dimensionality.connect(dimensionality)
        if is_pointcloud !=None:
            self.inputs.is_pointcloud.connect(is_pointcloud)
        if target_scoping !=None:
            self.inputs.target_scoping.connect(target_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Prepares a workflow able to map data from an input mesh to a target mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "source_mesh", type_names=["abstract_meshed_region","meshes_container","field","fields_container"], optional=True, document="""Mesh where the source data is defined. PointCloud interpolations support both mesh/meshes_container and field/fields_container, whereas mesh-based interpolations only support mesh/meshes_container. If not set, an input pin named "source_mesh/source_coords" is exposed."""),
                                 1 : PinSpecification(name = "target_mesh", type_names=["abstract_meshed_region","meshes_container","field","fields_container"], optional=True, document="""Mesh where the target data is defined. PointCloud interpolations support both mesh/meshes_container and field/fields_container, whereas mesh-based interpolations only support mesh/meshes_container. If not set, an input pin named "source_mesh/source_coords" is exposed."""),
                                 2 : PinSpecification(name = "is_conservative", type_names=["bool"], optional=True, document="""Boolean that indicates if the mapped variable is conservative (e.g. force) or not (e.g. pressure). If not set, an input pin named "is_conservative" is exposed."""),
                                 3 : PinSpecification(name = "location", type_names=["string"], optional=True, document="""Mesh support of the mapped variable. Supported options: Nodal and Elemental. If not set, an input pin named "location" is exposed."""),
                                 4 : PinSpecification(name = "dimensionality", type_names=["int32"], optional=True, document="""Dimensionality of the mapped variable. Supported options: 1 and 3 (scalars or vectors). If not set, an input pin named "dimensionality" is exposed."""),
                                 5 : PinSpecification(name = "is_pointcloud", type_names=["bool"], optional=True, document="""Boolean that indicates if the PointCloud interpolation is preferred over the FEM interpolation. Default: false."""),
                                 6 : PinSpecification(name = "target_scoping", type_names=["scoping","scopings_container"], optional=True, document="""Scoping that restricts the interpolation to a given set of nodes/elements in the target mesh. If not set, an input pin named "target_scoping" is exposed.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mapping_workflow", type_names=["workflow"], optional=False, document="""Workflow with input pin "source_data"; optionally "source_mesh/source_coords", "target_mesh/target_coords", "is_conservative", "location", "dimensionality" and "target_scoping"; and output pin "target_data".""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "create_sc_mapping_workflow")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCreateScMappingWorkflow
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCreateScMappingWorkflow
        """
        return super().outputs


#internal name: create_sc_mapping_workflow
#scripting name: create_sc_mapping_workflow
class InputsCreateScMappingWorkflow(_Inputs):
    """Intermediate class used to connect user inputs to create_sc_mapping_workflow operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
      >>> my_source_mesh = dpf.MeshedRegion()
      >>> op.inputs.source_mesh.connect(my_source_mesh)
      >>> my_target_mesh = dpf.MeshedRegion()
      >>> op.inputs.target_mesh.connect(my_target_mesh)
      >>> my_is_conservative = bool()
      >>> op.inputs.is_conservative.connect(my_is_conservative)
      >>> my_location = str()
      >>> op.inputs.location.connect(my_location)
      >>> my_dimensionality = int()
      >>> op.inputs.dimensionality.connect(my_dimensionality)
      >>> my_is_pointcloud = bool()
      >>> op.inputs.is_pointcloud.connect(my_is_pointcloud)
      >>> my_target_scoping = dpf.Scoping()
      >>> op.inputs.target_scoping.connect(my_target_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(create_sc_mapping_workflow._spec().inputs, op)
        self._source_mesh = Input(create_sc_mapping_workflow._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._source_mesh)
        self._target_mesh = Input(create_sc_mapping_workflow._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._target_mesh)
        self._is_conservative = Input(create_sc_mapping_workflow._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._is_conservative)
        self._location = Input(create_sc_mapping_workflow._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._location)
        self._dimensionality = Input(create_sc_mapping_workflow._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._dimensionality)
        self._is_pointcloud = Input(create_sc_mapping_workflow._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._is_pointcloud)
        self._target_scoping = Input(create_sc_mapping_workflow._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._target_scoping)

    @property
    def source_mesh(self):
        """Allows to connect source_mesh input to the operator

        - pindoc: Mesh where the source data is defined. PointCloud interpolations support both mesh/meshes_container and field/fields_container, whereas mesh-based interpolations only support mesh/meshes_container. If not set, an input pin named "source_mesh/source_coords" is exposed.

        Parameters
        ----------
        my_source_mesh : MeshedRegion, MeshesContainer, Field, FieldsContainer,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.source_mesh.connect(my_source_mesh)
        >>> #or
        >>> op.inputs.source_mesh(my_source_mesh)

        """
        return self._source_mesh

    @property
    def target_mesh(self):
        """Allows to connect target_mesh input to the operator

        - pindoc: Mesh where the target data is defined. PointCloud interpolations support both mesh/meshes_container and field/fields_container, whereas mesh-based interpolations only support mesh/meshes_container. If not set, an input pin named "source_mesh/source_coords" is exposed.

        Parameters
        ----------
        my_target_mesh : MeshedRegion, MeshesContainer, Field, FieldsContainer,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.target_mesh.connect(my_target_mesh)
        >>> #or
        >>> op.inputs.target_mesh(my_target_mesh)

        """
        return self._target_mesh

    @property
    def is_conservative(self):
        """Allows to connect is_conservative input to the operator

        - pindoc: Boolean that indicates if the mapped variable is conservative (e.g. force) or not (e.g. pressure). If not set, an input pin named "is_conservative" is exposed.

        Parameters
        ----------
        my_is_conservative : bool,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.is_conservative.connect(my_is_conservative)
        >>> #or
        >>> op.inputs.is_conservative(my_is_conservative)

        """
        return self._is_conservative

    @property
    def location(self):
        """Allows to connect location input to the operator

        - pindoc: Mesh support of the mapped variable. Supported options: Nodal and Elemental. If not set, an input pin named "location" is exposed.

        Parameters
        ----------
        my_location : str,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.location.connect(my_location)
        >>> #or
        >>> op.inputs.location(my_location)

        """
        return self._location

    @property
    def dimensionality(self):
        """Allows to connect dimensionality input to the operator

        - pindoc: Dimensionality of the mapped variable. Supported options: 1 and 3 (scalars or vectors). If not set, an input pin named "dimensionality" is exposed.

        Parameters
        ----------
        my_dimensionality : int,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.dimensionality.connect(my_dimensionality)
        >>> #or
        >>> op.inputs.dimensionality(my_dimensionality)

        """
        return self._dimensionality

    @property
    def is_pointcloud(self):
        """Allows to connect is_pointcloud input to the operator

        - pindoc: Boolean that indicates if the PointCloud interpolation is preferred over the FEM interpolation. Default: false.

        Parameters
        ----------
        my_is_pointcloud : bool,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.is_pointcloud.connect(my_is_pointcloud)
        >>> #or
        >>> op.inputs.is_pointcloud(my_is_pointcloud)

        """
        return self._is_pointcloud

    @property
    def target_scoping(self):
        """Allows to connect target_scoping input to the operator

        - pindoc: Scoping that restricts the interpolation to a given set of nodes/elements in the target mesh. If not set, an input pin named "target_scoping" is exposed.

        Parameters
        ----------
        my_target_scoping : Scoping, ScopingsContainer,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> op.inputs.target_scoping.connect(my_target_scoping)
        >>> #or
        >>> op.inputs.target_scoping(my_target_scoping)

        """
        return self._target_scoping

class OutputsCreateScMappingWorkflow(_Outputs):
    """Intermediate class used to get outputs from create_sc_mapping_workflow operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mapping_workflow = op.outputs.mapping_workflow()
    """
    def __init__(self, op: Operator):
        super().__init__(create_sc_mapping_workflow._spec().outputs, op)
        self._mapping_workflow = Output(create_sc_mapping_workflow._spec().output_pin(0), 0, op)
        self._outputs.append(self._mapping_workflow)

    @property
    def mapping_workflow(self):
        """Allows to get mapping_workflow output of the operator


        - pindoc: Workflow with input pin "source_data"; optionally "source_mesh/source_coords", "target_mesh/target_coords", "is_conservative", "location", "dimensionality" and "target_scoping"; and output pin "target_data".

        Returns
        ----------
        my_mapping_workflow : Workflow,

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.create_sc_mapping_workflow()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mapping_workflow = op.outputs.mapping_workflow()
        """
        return self._mapping_workflow
