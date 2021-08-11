"""
elemental_difference
====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from the "averaging" category."""

class elemental_difference(Operator):
    """Transform an ``ElementalNodal`` or ``Nodal`` field into an ``Elemental`` field. 
    
    Each elemental value is the maximum difference between the computed result for all 
    nodes in this element. The result is computed on a given element scoping.

    Parameters
    ----------
    field : str, optional
        Name of the field or fields container. The default is ``None``.
    mesh_scoping : optional
        Name of the mesh scoping. The default is ``None``.
    mesh : optional
        Name of the meshed region. The default is ``None``.
    through_layers : bool, optional
    
    config : optional
        The default is ``None``.
    server : optional
        The default is ``None``.
        
    Returns
    -------
    :class:`ansys.dpf.core.fields_container`
        Fields container object.    
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.averaging.elemental_difference()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_through_layers = bool()
    >>> op.inputs.through_layers.connect(my_through_layers)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.averaging.elemental_difference(field=my_field,mesh_scoping=my_mesh_scoping,mesh=my_mesh,through_layers=my_through_layers)

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """
    
    def __init__(self, field=None, mesh_scoping=None, mesh=None, through_layers=None, config=None, server=None):
        super().__init__(name="elemental_difference", config = config, server = server)
        self._inputs = InputsElementalDifference(self)
        self._outputs = OutputsElementalDifference(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if through_layers !=None:
            self.inputs.through_layers.connect(through_layers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform an ``ElementalNodal`` or ``Nodal`` field into an ``Elemental`` field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""Field or fields container with only one field is expected."""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document="""Average only on these entities."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 10 : PinSpecification(name = "through_layers", type_names=["bool"], optional=True, document="""The maximum elemental difference is taken through the different shell layers if ``True``. The default is ``False``.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_difference")

    @property
    def inputs(self):
        """Inputs to connect to the operator.

        Returns
        --------
        inputs : InputsElementalDifference 
        """
        return super().inputs


    @property
    def outputs(self):
        """Outputs of the operator that are obtained by evaluating it.

        Returns
        --------
        outputs : OutputsElementalDifference 
        """
        return super().outputs


#internal name: elemental_difference
#scripting name: elemental_difference
class InputsElementalDifference(_Inputs):
    """Connects user inputs to the elemental difference operator.
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> op = dpf.operators.averaging.elemental_difference()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_through_layers = bool()
    >>> op.inputs.through_layers.connect(my_through_layers)
    """
    
    def __init__(self, op: Operator):
        super().__init__(elemental_difference._spec().inputs, op)
        self._field = Input(elemental_difference._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh_scoping = Input(elemental_difference._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._mesh = Input(elemental_difference._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)
        self._through_layers = Input(elemental_difference._spec().input_pin(10), 10, op, -1) 
        self._inputs.append(self._through_layers)

    @property
    def field(self):
        """Field inputs to connect to the operator.

        - pindoc: A field or fields container with only one field is expected.

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_difference()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def mesh_scoping(self):
        """Mesh scoping input to connect to the operator.

        - pindoc: Average only on these entities.

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_difference()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def mesh(self):
        """Mesh input to connect to the operator.

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_difference()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def through_layers(self):
        """Through layers input to connect to the operator.

        - pindoc: The maximum elemental difference is taken through the different shell layers if ``True``. The default is ``False``.

        Parameters
        ----------
        my_through_layers : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_difference()
        >>> op.inputs.through_layers.connect(my_through_layers)
        >>> #or
        >>> op.inputs.through_layers(my_through_layers)

        """
        return self._through_layers

class OutputsElementalDifference(_Outputs):
    """Retrieves outputs from the elemental difference operator.
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> op = dpf.operators.averaging.elemental_difference()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_difference._spec().outputs, op)
        self._fields_container = Output(elemental_difference._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Fields container output of the operator.

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_difference()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        
        """
        return self._fields_container

