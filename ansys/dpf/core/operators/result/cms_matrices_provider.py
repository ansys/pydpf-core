"""
cms_matrices_provider
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "result" category
"""

class cms_matrices_provider(Operator):
    """Read reduced matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.

      available inputs:
        - data_sources (DataSources)
        - matrix_form (bool)

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
      >>> my_matrix_form = bool()
      >>> op.inputs.matrix_form.connect(my_matrix_form)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.cms_matrices_provider(data_sources=my_data_sources,matrix_form=my_matrix_form)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, data_sources=None, matrix_form=None, config=None, server=None):
        super().__init__(name="cms_matrices_provider", config = config, server = server)
        self._inputs = InputsCmsMatricesProvider(self)
        self._outputs = OutputsCmsMatricesProvider(self)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if matrix_form !=None:
            self.inputs.matrix_form.connect(matrix_form)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read reduced matrices for cms elements. Extract stiffness, damping, mass matrices and load vector from a subfile.""",
                             map_input_pin_spec={
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Data_sources (must contain at list one subfile)."""), 
                                 200 : PinSpecification(name = "matrix_form", type_names=["bool"], optional=False, document="""If this pin i set to true, data are return as matrix form.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container containing in this order : stiffness, damping, mass matrices, and then load vector. But if pin 200 is set to true, it's in matrix form.""")})
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
      >>> my_matrix_form = bool()
      >>> op.inputs.matrix_form.connect(my_matrix_form)
    """
    def __init__(self, op: Operator):
        super().__init__(cms_matrices_provider._spec().inputs, op)
        self._data_sources = Input(cms_matrices_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._matrix_form = Input(cms_matrices_provider._spec().input_pin(200), 200, op, -1) 
        self._inputs.append(self._matrix_form)

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

    @property
    def matrix_form(self):
        """Allows to connect matrix_form input to the operator

        - pindoc: If this pin i set to true, data are return as matrix form.

        Parameters
        ----------
        my_matrix_form : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.cms_matrices_provider()
        >>> op.inputs.matrix_form.connect(my_matrix_form)
        >>> #or
        >>> op.inputs.matrix_form(my_matrix_form)

        """
        return self._matrix_form

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


        - pindoc: Fields container containing in this order : stiffness, damping, mass matrices, and then load vector. But if pin 200 is set to true, it's in matrix form.

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

