"""
svd
===
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class svd(Operator):
    """
Computes the [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition)
$A = U \Sigma V^{*T}$ for each matrix field in the input fields container.
Both real and complex matrices are supported.
The decomposition satisfies $A = U S V^T$ (real) or $A = U S V^{*T}$ (complex),
where $S$ contains the singular values, $U$ is left-unitary, and $V^T$ (or $V^{*T}$) is right-unitary.


      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - s_svd (FieldsContainer)
        - u_svd (FieldsContainer)
        - vt_svd (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.svd()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.svd(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_s_svd = op.outputs.s_svd()
      >>> result_u_svd = op.outputs.u_svd()
      >>> result_vt_svd = op.outputs.vt_svd()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="svdOp", config = config, server = server)
        self._inputs = InputsSvd(self)
        self._outputs = OutputsSvd(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes the [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition)
$A = U \Sigma V^{*T}$ for each matrix field in the input fields container.
Both real and complex matrices are supported.
The decomposition satisfies $A = U S V^T$ (real) or $A = U S V^{*T}$ (complex),
where $S$ contains the singular values, $U$ is left-unitary, and $V^T$ (or $V^{*T}$) is right-unitary.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""Fields container of matrix fields to decompose. May be real or complex (complex label required for complex inputs). Each field must represent a matrix.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "s_svd", type_names=["fields_container"], optional=False, document="""Singular values $S$ of the decomposition $A = U S V^{*T}$. Same label structure as the input."""), 
                                 1 : PinSpecification(name = "u_svd", type_names=["fields_container"], optional=False, document="""Left unitary matrix $U$ of the decomposition $A = U S V^{*T}$. Same label structure as the input."""), 
                                 2 : PinSpecification(name = "vt_svd", type_names=["fields_container"], optional=False, document="""Conjugate transpose of the right unitary matrix $V^{*T}$ of the decomposition $A = U S V^{*T}$. Same label structure as the input.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "svdOp")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsSvd 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsSvd 
        """
        return super().outputs


#internal name: svdOp
#scripting name: svd
class InputsSvd(_Inputs):
    """Intermediate class used to connect user inputs to svd operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.svd()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(svd._spec().inputs, op)
        self._fields_container = Input(svd._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        - pindoc: Fields container of matrix fields to decompose. May be real or complex (complex label required for complex inputs). Each field must represent a matrix.

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.svd()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsSvd(_Outputs):
    """Intermediate class used to get outputs from svd operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.svd()
      >>> # Connect inputs : op.inputs. ...
      >>> result_s_svd = op.outputs.s_svd()
      >>> result_u_svd = op.outputs.u_svd()
      >>> result_vt_svd = op.outputs.vt_svd()
    """
    def __init__(self, op: Operator):
        super().__init__(svd._spec().outputs, op)
        self._s_svd = Output(svd._spec().output_pin(0), 0, op) 
        self._outputs.append(self._s_svd)
        self._u_svd = Output(svd._spec().output_pin(1), 1, op) 
        self._outputs.append(self._u_svd)
        self._vt_svd = Output(svd._spec().output_pin(2), 2, op) 
        self._outputs.append(self._vt_svd)

    @property
    def s_svd(self):
        """Allows to get s_svd output of the operator


        - pindoc: Singular values $S$ of the decomposition $A = U S V^{*T}$. Same label structure as the input.

        Returns
        ----------
        my_s_svd : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.svd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_s_svd = op.outputs.s_svd() 
        """
        return self._s_svd

    @property
    def u_svd(self):
        """Allows to get u_svd output of the operator


        - pindoc: Left unitary matrix $U$ of the decomposition $A = U S V^{*T}$. Same label structure as the input.

        Returns
        ----------
        my_u_svd : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.svd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_u_svd = op.outputs.u_svd() 
        """
        return self._u_svd

    @property
    def vt_svd(self):
        """Allows to get vt_svd output of the operator


        - pindoc: Conjugate transpose of the right unitary matrix $V^{*T}$ of the decomposition $A = U S V^{*T}$. Same label structure as the input.

        Returns
        ----------
        my_vt_svd : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.svd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_vt_svd = op.outputs.vt_svd() 
        """
        return self._vt_svd

