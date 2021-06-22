"""
cms_matrices_provider
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class cms_matrices_provider(Operator):
    """Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.

      available inputs:
        - data_sources (DataSources)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.cms_matrices_provider()

      >>> # Make input connections
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.cms_matrices_provider(data_sources=my_data_sources)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, data_sources=None, config=None, server=None):
        super().__init__(name="cms_matrices_provider", config = config, server = server)
        self._inputs = InputsCmsMatricesProvider(self)
        self._outputs = OutputsCmsMatricesProvider(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read reducted matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.""",
                             map_input_pin_spec={
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Data_sources (must contain at list one subfile).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "cms_matrices_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCmsMatricesProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCmsMatricesProvider 
        """
        return super().outputs


#internal name: cms_matrices_provider
#scripting name: cms_matrices_provider
class InputsCmsMatricesProvider(_Inputs):
    """Intermediate class used to connect user inputs to cms_matrices_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.cms_matrices_provider()
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(cms_matrices_provider._spec().inputs, op)
        self._data_sources = Input(cms_matrices_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: Data_sources (must contain at list one subfile).

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.cms_matrices_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsCmsMatricesProvider(_Outputs):
    """Intermediate class used to get outputs from cms_matrices_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.cms_matrices_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(cms_matrices_provider._spec().outputs, op)
        self._fields_container = Output(cms_matrices_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        - pindoc: Fields container containing in this order : stiffness, damping, mass matrices, and then load vector.

        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.cms_matrices_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

