from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "invariant" category
"""

#internal name: eig_values
#scripting name: eigen_values
def _get_input_spec_eigen_values(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_eigen_values = { 
        0 : inpin0
    }
    return inputs_dict_eigen_values[pin]

def _get_output_spec_eigen_values(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_eigen_values = { 
        0 : outpin0
    }
    return outputs_dict_eigen_values[pin]

class _InputSpecEigenValues(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_eigen_values(0), 0, op, -1) 

class _OutputSpecEigenValues(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_eigen_values(0), 0, op) 

class _EigenValues(_Operator):
    """Operator's description:
    Internal name is "eig_values"
    Scripting name is "eigen_values"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_values")
    >>> op_way2 = core.operators.invariant.eigen_values()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eig_values")
        self._name = "eig_values"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecEigenValues(self._op)
        self.outputs = _OutputSpecEigenValues(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def eigen_values():
    """Operator's description:
    Internal name is "eig_values"
    Scripting name is "eigen_values"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_values")
    >>> op_way2 = core.operators.invariant.eigen_values()
    """
    return _EigenValues()

#internal name: eqv
#scripting name: von_mises_eqv
def _get_input_spec_von_mises_eqv(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_von_mises_eqv = { 
        0 : inpin0
    }
    return inputs_dict_von_mises_eqv[pin]

def _get_output_spec_von_mises_eqv(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_von_mises_eqv = { 
        0 : outpin0
    }
    return outputs_dict_von_mises_eqv[pin]

class _InputSpecVonMisesEqv(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_von_mises_eqv(0), 0, op, -1) 

class _OutputSpecVonMisesEqv(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_von_mises_eqv(0), 0, op) 

class _VonMisesEqv(_Operator):
    """Operator's description:
    Internal name is "eqv"
    Scripting name is "von_mises_eqv"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eqv")
    >>> op_way2 = core.operators.invariant.von_mises_eqv()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eqv")
        self._name = "eqv"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecVonMisesEqv(self._op)
        self.outputs = _OutputSpecVonMisesEqv(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def von_mises_eqv():
    """Operator's description:
    Internal name is "eqv"
    Scripting name is "von_mises_eqv"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eqv")
    >>> op_way2 = core.operators.invariant.von_mises_eqv()
    """
    return _VonMisesEqv()

#internal name: eqv_fc
#scripting name: von_mises_eqv_fc
def _get_input_spec_von_mises_eqv_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_von_mises_eqv_fc = { 
        0 : inpin0
    }
    return inputs_dict_von_mises_eqv_fc[pin]

def _get_output_spec_von_mises_eqv_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_von_mises_eqv_fc = { 
        0 : outpin0
    }
    return outputs_dict_von_mises_eqv_fc[pin]

class _InputSpecVonMisesEqvFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_von_mises_eqv_fc(0), 0, op, -1) 

class _OutputSpecVonMisesEqvFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_von_mises_eqv_fc(0), 0, op) 

class _VonMisesEqvFc(_Operator):
    """Operator's description:
    Internal name is "eqv_fc"
    Scripting name is "von_mises_eqv_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eqv_fc")
    >>> op_way2 = core.operators.invariant.von_mises_eqv_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eqv_fc")
        self._name = "eqv_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecVonMisesEqvFc(self._op)
        self.outputs = _OutputSpecVonMisesEqvFc(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def von_mises_eqv_fc():
    """Operator's description:
    Internal name is "eqv_fc"
    Scripting name is "von_mises_eqv_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eqv_fc")
    >>> op_way2 = core.operators.invariant.von_mises_eqv_fc()
    """
    return _VonMisesEqvFc()

#internal name: invariants_deriv
#scripting name: invariants
def _get_input_spec_invariants(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inputs_dict_invariants = { 
        0 : inpin0
    }
    return inputs_dict_invariants[pin]

def _get_output_spec_invariants(pin):
    outpin0 = _PinSpecification(name = "field_int", type_names = ["field"], document = """stress intensity field""")
    outpin1 = _PinSpecification(name = "field_eqv", type_names = ["field"], document = """stress equivalent intensity""")
    outpin2 = _PinSpecification(name = "field_max_shear", type_names = ["field"], document = """max shear stress field""")
    outputs_dict_invariants = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2
    }
    return outputs_dict_invariants[pin]

class _InputSpecInvariants(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_invariants(0), 0, op, -1) 

class _OutputSpecInvariants(_Outputs):
    def __init__(self, op: _Operator):
        self.field_int = _Output(_get_output_spec_invariants(0), 0, op) 
        self.field_eqv = _Output(_get_output_spec_invariants(1), 1, op) 
        self.field_max_shear = _Output(_get_output_spec_invariants(2), 2, op) 

class _Invariants(_Operator):
    """Operator's description:
    Internal name is "invariants_deriv"
    Scripting name is "invariants"

    Input list: 
       0: field 

    Output list: 
       0: field_int (stress intensity field)
       1: field_eqv (stress equivalent intensity)
       2: field_max_shear (max shear stress field)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_deriv")
    >>> op_way2 = core.operators.invariant.invariants()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("invariants_deriv")
        self._name = "invariants_deriv"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecInvariants(self._op)
        self.outputs = _OutputSpecInvariants(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def invariants():
    """Operator's description:
    Internal name is "invariants_deriv"
    Scripting name is "invariants"

    Input list: 
       0: field 

    Output list: 
       0: field_int (stress intensity field)
       1: field_eqv (stress equivalent intensity)
       2: field_max_shear (max shear stress field)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_deriv")
    >>> op_way2 = core.operators.invariant.invariants()
    """
    return _Invariants()

#internal name: invariants_fc
#scripting name: principal_invariants_fc
def _get_input_spec_principal_invariants_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_principal_invariants_fc = { 
        0 : inpin0
    }
    return inputs_dict_principal_invariants_fc[pin]

def _get_output_spec_principal_invariants_fc(pin):
    outpin0 = _PinSpecification(name = "fields_eig_1", type_names = ["fields_container"], document = """first eigen value fields""")
    outpin1 = _PinSpecification(name = "fields_eig_2", type_names = ["fields_container"], document = """second eigen value fields""")
    outpin2 = _PinSpecification(name = "fields_eig_3", type_names = ["fields_container"], document = """third eigen value fields""")
    outputs_dict_principal_invariants_fc = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2
    }
    return outputs_dict_principal_invariants_fc[pin]

class _InputSpecPrincipalInvariantsFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_principal_invariants_fc(0), 0, op, -1) 

class _OutputSpecPrincipalInvariantsFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_eig_1 = _Output(_get_output_spec_principal_invariants_fc(0), 0, op) 
        self.fields_eig_2 = _Output(_get_output_spec_principal_invariants_fc(1), 1, op) 
        self.fields_eig_3 = _Output(_get_output_spec_principal_invariants_fc(2), 2, op) 

class _PrincipalInvariantsFc(_Operator):
    """Operator's description:
    Internal name is "invariants_fc"
    Scripting name is "principal_invariants_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_eig_1 (first eigen value fields)
       1: fields_eig_2 (second eigen value fields)
       2: fields_eig_3 (third eigen value fields)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_fc")
    >>> op_way2 = core.operators.invariant.principal_invariants_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("invariants_fc")
        self._name = "invariants_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecPrincipalInvariantsFc(self._op)
        self.outputs = _OutputSpecPrincipalInvariantsFc(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def principal_invariants_fc():
    """Operator's description:
    Internal name is "invariants_fc"
    Scripting name is "principal_invariants_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_eig_1 (first eigen value fields)
       1: fields_eig_2 (second eigen value fields)
       2: fields_eig_3 (third eigen value fields)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_fc")
    >>> op_way2 = core.operators.invariant.principal_invariants_fc()
    """
    return _PrincipalInvariantsFc()

#internal name: eig_values_fc
#scripting name: eigen_values_fc
def _get_input_spec_eigen_values_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_eigen_values_fc = { 
        0 : inpin0
    }
    return inputs_dict_eigen_values_fc[pin]

def _get_output_spec_eigen_values_fc(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_eigen_values_fc = { 
        0 : outpin0
    }
    return outputs_dict_eigen_values_fc[pin]

class _InputSpecEigenValuesFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_eigen_values_fc(0), 0, op, -1) 

class _OutputSpecEigenValuesFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_eigen_values_fc(0), 0, op) 

class _EigenValuesFc(_Operator):
    """Operator's description:
    Internal name is "eig_values_fc"
    Scripting name is "eigen_values_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_values_fc")
    >>> op_way2 = core.operators.invariant.eigen_values_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eig_values_fc")
        self._name = "eig_values_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecEigenValuesFc(self._op)
        self.outputs = _OutputSpecEigenValuesFc(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def eigen_values_fc():
    """Operator's description:
    Internal name is "eig_values_fc"
    Scripting name is "eigen_values_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_values_fc")
    >>> op_way2 = core.operators.invariant.eigen_values_fc()
    """
    return _EigenValuesFc()

#internal name: invariants_deriv_fc
#scripting name: invariants_fc
def _get_input_spec_invariants_fc(pin):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inputs_dict_invariants_fc = { 
        0 : inpin0
    }
    return inputs_dict_invariants_fc[pin]

def _get_output_spec_invariants_fc(pin):
    outpin0 = _PinSpecification(name = "fields_int", type_names = ["fields_container"], document = """stress intensity field""")
    outpin1 = _PinSpecification(name = "fields_eqv", type_names = ["fields_container"], document = """stress equivalent intensity""")
    outpin2 = _PinSpecification(name = "fields_max_shear", type_names = ["fields_container"], document = """max shear stress field""")
    outputs_dict_invariants_fc = { 
        0 : outpin0,
        1 : outpin1,
        2 : outpin2
    }
    return outputs_dict_invariants_fc[pin]

class _InputSpecInvariantsFc(_Inputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Input(_get_input_spec_invariants_fc(0), 0, op, -1) 

class _OutputSpecInvariantsFc(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_int = _Output(_get_output_spec_invariants_fc(0), 0, op) 
        self.fields_eqv = _Output(_get_output_spec_invariants_fc(1), 1, op) 
        self.fields_max_shear = _Output(_get_output_spec_invariants_fc(2), 2, op) 

class _InvariantsFc(_Operator):
    """Operator's description:
    Internal name is "invariants_deriv_fc"
    Scripting name is "invariants_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_int (stress intensity field)
       1: fields_eqv (stress equivalent intensity)
       2: fields_max_shear (max shear stress field)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_deriv_fc")
    >>> op_way2 = core.operators.invariant.invariants_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("invariants_deriv_fc")
        self._name = "invariants_deriv_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecInvariantsFc(self._op)
        self.outputs = _OutputSpecInvariantsFc(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def invariants_fc():
    """Operator's description:
    Internal name is "invariants_deriv_fc"
    Scripting name is "invariants_fc"

    Input list: 
       0: fields_container 

    Output list: 
       0: fields_int (stress intensity field)
       1: fields_eqv (stress equivalent intensity)
       2: fields_max_shear (max shear stress field)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("invariants_deriv_fc")
    >>> op_way2 = core.operators.invariant.invariants_fc()
    """
    return _InvariantsFc()

from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input as _Input
from ansys.dpf.core.outputs import Output as _Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from mapdlOperatorsCore.dll plugin, from "invariant" category
"""

#internal name: eig_vectors_fc
#scripting name: eigen_vectors_fc
def _get_input_spec_eigen_vectors_fc(pin):
    inpin0 = _PinSpecification(name = "field", type_names = ["fields_container","field"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_eigen_vectors_fc = { 
        0 : inpin0
    }
    return inputs_dict_eigen_vectors_fc[pin]

def _get_output_spec_eigen_vectors_fc(pin):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_eigen_vectors_fc = { 
        0 : outpin0
    }
    return outputs_dict_eigen_vectors_fc[pin]

class _InputSpecEigenVectorsFc(_Inputs):
    def __init__(self, op: _Operator):
        self.field = _Input(_get_input_spec_eigen_vectors_fc(0), 0, op, -1) 

class _OutputSpecEigenVectorsFc(_Outputs):
    def __init__(self, op: _Operator):
        self.field = _Output(_get_output_spec_eigen_vectors_fc(0), 0, op) 

class _EigenVectorsFc(_Operator):
    """Operator's description:
    Internal name is "eig_vectors_fc"
    Scripting name is "eigen_vectors_fc"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_vectors_fc")
    >>> op_way2 = core.operators.invariant.eigen_vectors_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eig_vectors_fc")
        self._name = "eig_vectors_fc"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecEigenVectorsFc(self._op)
        self.outputs = _OutputSpecEigenVectorsFc(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def eigen_vectors_fc():
    """Operator's description:
    Internal name is "eig_vectors_fc"
    Scripting name is "eigen_vectors_fc"

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_vectors_fc")
    >>> op_way2 = core.operators.invariant.eigen_vectors_fc()
    """
    return _EigenVectorsFc()

#internal name: eig_vectors
#scripting name: eigen_vectors
def _get_input_spec_eigen_vectors(pin):
    inpin0 = _PinSpecification(name = "fields", type_names = ["fields_container","field"], optional = False, document = """""")
    inputs_dict_eigen_vectors = { 
        0 : inpin0
    }
    return inputs_dict_eigen_vectors[pin]

def _get_output_spec_eigen_vectors(pin):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_eigen_vectors = { 
        0 : outpin0
    }
    return outputs_dict_eigen_vectors[pin]

class _InputSpecEigenVectors(_Inputs):
    def __init__(self, op: _Operator):
        self.fields = _Input(_get_input_spec_eigen_vectors(0), 0, op, -1) 

class _OutputSpecEigenVectors(_Outputs):
    def __init__(self, op: _Operator):
        self.fields_container = _Output(_get_output_spec_eigen_vectors(0), 0, op) 

class _EigenVectors(_Operator):
    """Operator's description:
    Internal name is "eig_vectors"
    Scripting name is "eigen_vectors"

    Input list: 
       0: fields 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_vectors")
    >>> op_way2 = core.operators.invariant.eigen_vectors()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("eig_vectors")
        self._name = "eig_vectors"
        self._op = _Operator(self._name)
        self.inputs = _InputSpecEigenVectors(self._op)
        self.outputs = _OutputSpecEigenVectors(self._op)

    def __str__(self):
        return """Specific operator object.

Input and outputs can be connected together.

Examples
--------
>>> from ansys.dpf import core)
>>> op1 = core.operators.result.stress()
>>> op1.inputs.data_sources.connect(core.DataSources('file.rst'))
>>> op2 = core.operators.averaging.to_elemental_fc()
>>> op2.inputs.fields_container.connect(op1.outputs.fields_container)
"""

def eigen_vectors():
    """Operator's description:
    Internal name is "eig_vectors"
    Scripting name is "eigen_vectors"

    Input list: 
       0: fields 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("eig_vectors")
    >>> op_way2 = core.operators.invariant.eigen_vectors()
    """
    return _EigenVectors()

