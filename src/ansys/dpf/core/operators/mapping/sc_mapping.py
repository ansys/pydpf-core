"""
sc_mapping
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mapping" category
"""

class sc_mapping(Operator):
    """Apply System Coupling to map data from an input mesh to a target mesh.

      available inputs:
        - source_mesh (MeshedRegion)
        - target_mesh (MeshedRegion)
        - is_conservative (bool)
        - location (str)
        - dimensionality (int)
        - target_scoping (Scoping, ScopingsContainer) (optional)
        - source_data (Field, FieldsContainer)

      available outputs:
        - target_data (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mapping.sc_mapping()

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
      >>> my_target_scoping = dpf.Scoping()
      >>> op.inputs.target_scoping.connect(my_target_scoping)
      >>> my_source_data = dpf.Field()
      >>> op.inputs.source_data.connect(my_source_data)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mapping.sc_mapping(source_mesh=my_source_mesh,target_mesh=my_target_mesh,is_conservative=my_is_conservative,location=my_location,dimensionality=my_dimensionality,target_scoping=my_target_scoping,source_data=my_source_data)

      >>> # Get output data
      >>> result_target_data = op.outputs.target_data()"""
    def __init__(self, source_mesh=None, target_mesh=None, is_conservative=None, location=None, dimensionality=None, target_scoping=None, source_data=None, config=None, server=None):
        super().__init__(name="sc_mapping", config = config, server = server)
        self._inputs = InputsScMapping(self)
        self._outputs = OutputsScMapping(self)
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
        if target_scoping !=None:
            self.inputs.target_scoping.connect(target_scoping)
        if source_data !=None:
            self.inputs.source_data.connect(source_data)

    @staticmethod
    def _spec():
        spec = Specification(description="""Apply System Coupling to map data from an input mesh to a target mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "source_mesh", type_names=["abstract_meshed_region"], optional=False, document="""Mesh where the source data is defined.interpolations only support meshed_region."""), 
                                 1 : PinSpecification(name = "target_mesh", type_names=["abstract_meshed_region"], optional=False, document="""Mesh where the target data is defined. interpolations only support meshed_region."""), 
                                 2 : PinSpecification(name = "is_conservative", type_names=["bool"], optional=False, document="""Boolean that indicates if the mapped variable is conservative (e.g. force) or not (e.g. pressure)."""), 
                                 3 : PinSpecification(name = "location", type_names=["string"], optional=False, document="""Mesh support of the mapped variable. Supported options: Nodal and Elemental."""), 
                                 4 : PinSpecification(name = "dimensionality", type_names=["int32"], optional=False, document="""Dimensionality of the mapped variable. Supported options: 1 and 3 (scalars or vectors)."""), 
                                 5 : PinSpecification(name = "target_scoping", type_names=["scoping","scopings_container"], optional=True, document="""Scoping that restricts the interpolation to a given set of nodes/elements in the target mesh. """), 
                                 6 : PinSpecification(name = "source_data", type_names=["field","fields_container"], optional=False, document="""data to be mapped.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "target_data", type_names=["fields_container"], optional=False, document="""data mapped on the target mesh""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sc_mapping")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsScMapping 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsScMapping 
        """
        return super().outputs


#internal name: sc_mapping
#scripting name: sc_mapping
class InputsScMapping(_Inputs):
    """Intermediate class used to connect user inputs to sc_mapping operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.sc_mapping()
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
      >>> my_target_scoping = dpf.Scoping()
      >>> op.inputs.target_scoping.connect(my_target_scoping)
      >>> my_source_data = dpf.Field()
      >>> op.inputs.source_data.connect(my_source_data)
    """
    def __init__(self, op: Operator):
        super().__init__(sc_mapping._spec().inputs, op)
        self._source_mesh = Input(sc_mapping._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._source_mesh)
        self._target_mesh = Input(sc_mapping._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._target_mesh)
        self._is_conservative = Input(sc_mapping._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._is_conservative)
        self._location = Input(sc_mapping._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._location)
        self._dimensionality = Input(sc_mapping._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._dimensionality)
        self._target_scoping = Input(sc_mapping._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._target_scoping)
        self._source_data = Input(sc_mapping._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._source_data)

    @property
    def source_mesh(self):
        """Allows to connect source_mesh input to the operator

        - pindoc: Mesh where the source data is defined.interpolations only support meshed_region.

        Parameters
        ----------
        my_source_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.source_mesh.connect(my_source_mesh)
        >>> #or
        >>> op.inputs.source_mesh(my_source_mesh)

        """
        return self._source_mesh

    @property
    def target_mesh(self):
        """Allows to connect target_mesh input to the operator

        - pindoc: Mesh where the target data is defined. interpolations only support meshed_region.

        Parameters
        ----------
        my_target_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.target_mesh.connect(my_target_mesh)
        >>> #or
        >>> op.inputs.target_mesh(my_target_mesh)

        """
        return self._target_mesh

    @property
    def is_conservative(self):
        """Allows to connect is_conservative input to the operator

        - pindoc: Boolean that indicates if the mapped variable is conservative (e.g. force) or not (e.g. pressure).

        Parameters
        ----------
        my_is_conservative : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.is_conservative.connect(my_is_conservative)
        >>> #or
        >>> op.inputs.is_conservative(my_is_conservative)

        """
        return self._is_conservative

    @property
    def location(self):
        """Allows to connect location input to the operator

        - pindoc: Mesh support of the mapped variable. Supported options: Nodal and Elemental.

        Parameters
        ----------
        my_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.location.connect(my_location)
        >>> #or
        >>> op.inputs.location(my_location)

        """
        return self._location

    @property
    def dimensionality(self):
        """Allows to connect dimensionality input to the operator

        - pindoc: Dimensionality of the mapped variable. Supported options: 1 and 3 (scalars or vectors).

        Parameters
        ----------
        my_dimensionality : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.dimensionality.connect(my_dimensionality)
        >>> #or
        >>> op.inputs.dimensionality(my_dimensionality)

        """
        return self._dimensionality

    @property
    def target_scoping(self):
        """Allows to connect target_scoping input to the operator

        - pindoc: Scoping that restricts the interpolation to a given set of nodes/elements in the target mesh. 

        Parameters
        ----------
        my_target_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.target_scoping.connect(my_target_scoping)
        >>> #or
        >>> op.inputs.target_scoping(my_target_scoping)

        """
        return self._target_scoping

    @property
    def source_data(self):
        """Allows to connect source_data input to the operator

        - pindoc: data to be mapped.

        Parameters
        ----------
        my_source_data : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> op.inputs.source_data.connect(my_source_data)
        >>> #or
        >>> op.inputs.source_data(my_source_data)

        """
        return self._source_data

class OutputsScMapping(_Outputs):
    """Intermediate class used to get outputs from sc_mapping operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mapping.sc_mapping()
      >>> # Connect inputs : op.inputs. ...
      >>> result_target_data = op.outputs.target_data()
    """
    def __init__(self, op: Operator):
        super().__init__(sc_mapping._spec().outputs, op)
        self._target_data = Output(sc_mapping._spec().output_pin(0), 0, op) 
        self._outputs.append(self._target_data)

    @property
    def target_data(self):
        """Allows to get target_data output of the operator


        - pindoc: data mapped on the target mesh

        Returns
        ----------
        my_target_data : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mapping.sc_mapping()
        >>> # Connect inputs : op.inputs. ...
        >>> result_target_data = op.outputs.target_data() 
        """
        return self._target_data

