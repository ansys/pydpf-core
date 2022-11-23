"""
poynting_vector
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class poynting_vector(Operator):
    """Compute the Poynting Vector

      available inputs:
        - fields_containerA (FieldsContainer)
        - fields_containerB (FieldsContainer)
        - fields_containerC (FieldsContainer)
        - fields_containerD (FieldsContainer)
        - meshed_region (MeshedRegion) (optional)
        - int32 (int) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.poynting_vector()

      >>> # Make input connections
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_fields_containerC = dpf.FieldsContainer()
      >>> op.inputs.fields_containerC.connect(my_fields_containerC)
      >>> my_fields_containerD = dpf.FieldsContainer()
      >>> op.inputs.fields_containerD.connect(my_fields_containerD)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_int32 = int()
      >>> op.inputs.int32.connect(my_int32)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.poynting_vector(fields_containerA=my_fields_containerA,fields_containerB=my_fields_containerB,fields_containerC=my_fields_containerC,fields_containerD=my_fields_containerD,meshed_region=my_meshed_region,int32=my_int32)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_containerA=None, fields_containerB=None, fields_containerC=None, fields_containerD=None, meshed_region=None, int32=None, config=None, server=None):
        super().__init__(name="PoyntingVector", config = config, server = server)
        self._inputs = InputsPoyntingVector(self)
        self._outputs = OutputsPoyntingVector(self)
        if fields_containerA !=None:
            self.inputs.fields_containerA.connect(fields_containerA)
        if fields_containerB !=None:
            self.inputs.fields_containerB.connect(fields_containerB)
        if fields_containerC !=None:
            self.inputs.fields_containerC.connect(fields_containerC)
        if fields_containerD !=None:
            self.inputs.fields_containerD.connect(fields_containerD)
        if meshed_region !=None:
            self.inputs.meshed_region.connect(meshed_region)
        if int32 !=None:
            self.inputs.int32.connect(int32)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the Poynting Vector""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_containerA", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fields_containerB", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "fields_containerC", type_names=["fields_container"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "fields_containerD", type_names=["fields_container"], optional=False, document=""""""), 
                                 4 : PinSpecification(name = "meshed_region", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin have to be boundary or skin mesh"""), 
                                 5 : PinSpecification(name = "int32", type_names=["int32"], optional=True, document="""load step number, if it's specified, the Poynting Vector is computed only on the substeps of this step""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "PoyntingVector")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsPoyntingVector 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsPoyntingVector 
        """
        return super().outputs


#internal name: PoyntingVector
#scripting name: poynting_vector
class InputsPoyntingVector(_Inputs):
    """Intermediate class used to connect user inputs to poynting_vector operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.poynting_vector()
      >>> my_fields_containerA = dpf.FieldsContainer()
      >>> op.inputs.fields_containerA.connect(my_fields_containerA)
      >>> my_fields_containerB = dpf.FieldsContainer()
      >>> op.inputs.fields_containerB.connect(my_fields_containerB)
      >>> my_fields_containerC = dpf.FieldsContainer()
      >>> op.inputs.fields_containerC.connect(my_fields_containerC)
      >>> my_fields_containerD = dpf.FieldsContainer()
      >>> op.inputs.fields_containerD.connect(my_fields_containerD)
      >>> my_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.meshed_region.connect(my_meshed_region)
      >>> my_int32 = int()
      >>> op.inputs.int32.connect(my_int32)
    """
    def __init__(self, op: Operator):
        super().__init__(poynting_vector._spec().inputs, op)
        self._fields_containerA = Input(poynting_vector._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_containerA)
        self._fields_containerB = Input(poynting_vector._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fields_containerB)
        self._fields_containerC = Input(poynting_vector._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fields_containerC)
        self._fields_containerD = Input(poynting_vector._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._fields_containerD)
        self._meshed_region = Input(poynting_vector._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._meshed_region)
        self._int32 = Input(poynting_vector._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._int32)

    @property
    def fields_containerA(self):
        """Allows to connect fields_containerA input to the operator

        Parameters
        ----------
        my_fields_containerA : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.fields_containerA.connect(my_fields_containerA)
        >>> #or
        >>> op.inputs.fields_containerA(my_fields_containerA)

        """
        return self._fields_containerA

    @property
    def fields_containerB(self):
        """Allows to connect fields_containerB input to the operator

        Parameters
        ----------
        my_fields_containerB : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.fields_containerB.connect(my_fields_containerB)
        >>> #or
        >>> op.inputs.fields_containerB(my_fields_containerB)

        """
        return self._fields_containerB

    @property
    def fields_containerC(self):
        """Allows to connect fields_containerC input to the operator

        Parameters
        ----------
        my_fields_containerC : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.fields_containerC.connect(my_fields_containerC)
        >>> #or
        >>> op.inputs.fields_containerC(my_fields_containerC)

        """
        return self._fields_containerC

    @property
    def fields_containerD(self):
        """Allows to connect fields_containerD input to the operator

        Parameters
        ----------
        my_fields_containerD : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.fields_containerD.connect(my_fields_containerD)
        >>> #or
        >>> op.inputs.fields_containerD(my_fields_containerD)

        """
        return self._fields_containerD

    @property
    def meshed_region(self):
        """Allows to connect meshed_region input to the operator

        - pindoc: the mesh region in this pin have to be boundary or skin mesh

        Parameters
        ----------
        my_meshed_region : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.meshed_region.connect(my_meshed_region)
        >>> #or
        >>> op.inputs.meshed_region(my_meshed_region)

        """
        return self._meshed_region

    @property
    def int32(self):
        """Allows to connect int32 input to the operator

        - pindoc: load step number, if it's specified, the Poynting Vector is computed only on the substeps of this step

        Parameters
        ----------
        my_int32 : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.poynting_vector()
        >>> op.inputs.int32.connect(my_int32)
        >>> #or
        >>> op.inputs.int32(my_int32)

        """
        return self._int32

class OutputsPoyntingVector(_Outputs):
    """Intermediate class used to get outputs from poynting_vector operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.poynting_vector()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(poynting_vector._spec().outputs, op)
        self._fields_container = Output(poynting_vector._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.poynting_vector()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

