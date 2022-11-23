"""
extract_sub_mc
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class extract_sub_mc(Operator):
    """Create a new MeshesContainer with all the MeshedRegions corresponding to the label space in input 1

      available inputs:
        - meshes (MeshesContainer)
        - label_space (LabelSpace)

      available outputs:
        - meshes_container (MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.extract_sub_mc()

      >>> # Make input connections
      >>> my_meshes = dpf.MeshesContainer()
      >>> op.inputs.meshes.connect(my_meshes)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.extract_sub_mc(meshes=my_meshes,label_space=my_label_space)

      >>> # Get output data
      >>> result_meshes_container = op.outputs.meshes_container()"""
    def __init__(self, meshes=None, label_space=None, config=None, server=None):
        super().__init__(name="extract_sub_mc", config = config, server = server)
        self._inputs = InputsExtractSubMc(self)
        self._outputs = OutputsExtractSubMc(self)
        if meshes !=None:
            self.inputs.meshes.connect(meshes)
        if label_space !=None:
            self.inputs.label_space.connect(label_space)

    @staticmethod
    def _spec():
        spec = Specification(description="""Create a new MeshesContainer with all the MeshedRegions corresponding to the label space in input 1""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "meshes", type_names=["meshes_container"], optional=False, document="""meshes"""), 
                                 1 : PinSpecification(name = "label_space", type_names=["label_space"], optional=False, document="""label_space""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "meshes_container", type_names=["meshes_container"], optional=False, document="""meshes""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extract_sub_mc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractSubMc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtractSubMc 
        """
        return super().outputs


#internal name: extract_sub_mc
#scripting name: extract_sub_mc
class InputsExtractSubMc(_Inputs):
    """Intermediate class used to connect user inputs to extract_sub_mc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_mc()
      >>> my_meshes = dpf.MeshesContainer()
      >>> op.inputs.meshes.connect(my_meshes)
      >>> my_label_space = dpf.LabelSpace()
      >>> op.inputs.label_space.connect(my_label_space)
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_mc._spec().inputs, op)
        self._meshes = Input(extract_sub_mc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._meshes)
        self._label_space = Input(extract_sub_mc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._label_space)

    @property
    def meshes(self):
        """Allows to connect meshes input to the operator

        - pindoc: meshes

        Parameters
        ----------
        my_meshes : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> op.inputs.meshes.connect(my_meshes)
        >>> #or
        >>> op.inputs.meshes(my_meshes)

        """
        return self._meshes

    @property
    def label_space(self):
        """Allows to connect label_space input to the operator

        - pindoc: label_space

        Parameters
        ----------
        my_label_space : LabelSpace, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> op.inputs.label_space.connect(my_label_space)
        >>> #or
        >>> op.inputs.label_space(my_label_space)

        """
        return self._label_space

class OutputsExtractSubMc(_Outputs):
    """Intermediate class used to get outputs from extract_sub_mc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.extract_sub_mc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_meshes_container = op.outputs.meshes_container()
    """
    def __init__(self, op: Operator):
        super().__init__(extract_sub_mc._spec().outputs, op)
        self._meshes_container = Output(extract_sub_mc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._meshes_container)

    @property
    def meshes_container(self):
        """Allows to get meshes_container output of the operator


        - pindoc: meshes

        Returns
        ----------
        my_meshes_container : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.extract_sub_mc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_meshes_container = op.outputs.meshes_container() 
        """
        return self._meshes_container

