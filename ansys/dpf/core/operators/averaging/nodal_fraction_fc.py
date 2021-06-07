"""
nodal_fraction_fc
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class nodal_fraction_fc(Operator):
    """Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion) (optional)
        - scoping (Scoping) (optional)
        - denominator (FieldsContainer) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.nodal_fraction_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_denominator = dpf.FieldsContainer()
      >>> op.inputs.denominator.connect(my_denominator)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.nodal_fraction_fc(fields_container=my_fields_container,mesh=my_mesh,scoping=my_scoping,denominator=my_denominator)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, scoping=None, denominator=None, config=None, server=None):
        super().__init__(name="nodal_fraction_fc", config = config, server = server)
        self._inputs = InputsNodalFractionFc(self)
        self._outputs = OutputsNodalFractionFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if denominator !=None:
            self.inputs.denominator.connect(denominator)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document="""average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container"""), 
                                 6 : PinSpecification(name = "denominator", type_names=["fields_container"], optional=True, document="""if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "nodal_fraction_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalFractionFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalFractionFc 
        """
        return super().outputs


#internal name: nodal_fraction_fc
#scripting name: nodal_fraction_fc
class InputsNodalFractionFc(_Inputs):
    """Intermediate class used to connect user inputs to nodal_fraction_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_fraction_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_denominator = dpf.FieldsContainer()
      >>> op.inputs.denominator.connect(my_denominator)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_fraction_fc._spec().inputs, op)
        self._fields_container = Input(nodal_fraction_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(nodal_fraction_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._scoping = Input(nodal_fraction_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._scoping)
        self._denominator = Input(nodal_fraction_fc._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._denominator)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_fraction_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: the mesh region in this pin is used to perform the averaging, if there is no field's support it is used

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_fraction_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_fraction_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def denominator(self):
        """Allows to connect denominator input to the operator

        - pindoc: if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc

        Parameters
        ----------
        my_denominator : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.nodal_fraction_fc()
        >>> op.inputs.denominator.connect(my_denominator)
        >>> #or
        >>> op.inputs.denominator(my_denominator)

        """
        return self._denominator

class OutputsNodalFractionFc(_Outputs):
    """Intermediate class used to get outputs from nodal_fraction_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.nodal_fraction_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_fraction_fc._spec().outputs, op)
        self._fields_container = Output(nodal_fraction_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.nodal_fraction_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

