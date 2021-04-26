"""
Invariant Operators
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils.dll plugin, from "invariant" category
"""

#internal name: eig_values
#scripting name: eigen_values
class _InputsEigenValues(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_values._spec().inputs, op)
        self.field = Input(eigen_values._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsEigenValues(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_values._spec().outputs, op)
        self.field = Output(eigen_values._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class eigen_values(Operator):
    """Computes the element-wise eigen values of a tensor field.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.invariant.eigen_values()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="eig_values", config = config, server = server)
        self.inputs = _InputsEigenValues(self)
        self.outputs = _OutputsEigenValues(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen values of a tensor field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eig_values")

#internal name: invariants
#scripting name: principal_invariants
class _InputsPrincipalInvariants(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(principal_invariants._spec().inputs, op)
        self.field = Input(principal_invariants._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsPrincipalInvariants(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(principal_invariants._spec().outputs, op)
        self.field_eig_1 = Output(principal_invariants._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_eig_1)
        self.field_eig_2 = Output(principal_invariants._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_eig_2)
        self.field_eig_3 = Output(principal_invariants._spec().output_pin(2), 2, op) 
        self._outputs.append(self.field_eig_3)

class principal_invariants(Operator):
    """Computes the element-wise eigen values of a tensor field

      available inputs:
         field (Field)

      available outputs:
         field_eig_1 (Field)
         field_eig_2 (Field)
         field_eig_3 (Field)

      Examples
      --------
      >>> op = operators.invariant.principal_invariants()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="invariants", config = config, server = server)
        self.inputs = _InputsPrincipalInvariants(self)
        self.outputs = _OutputsPrincipalInvariants(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen values of a tensor field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_eig_1", type_names=["field"], optional=False, document="""first eigen value field"""), 
                                 1 : PinSpecification(name = "field_eig_2", type_names=["field"], optional=False, document="""second eigen value field"""), 
                                 2 : PinSpecification(name = "field_eig_3", type_names=["field"], optional=False, document="""third eigen value field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants")

#internal name: eqv
#scripting name: von_mises_eqv
class _InputsVonMisesEqv(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv._spec().inputs, op)
        self.field = Input(von_mises_eqv._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsVonMisesEqv(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv._spec().outputs, op)
        self.field = Output(von_mises_eqv._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class von_mises_eqv(Operator):
    """Computes the element-wise Von-Mises criteria on a tensor field.

      available inputs:
         field (Field, FieldsContainer)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.invariant.von_mises_eqv()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="eqv", config = config, server = server)
        self.inputs = _InputsVonMisesEqv(self)
        self.outputs = _OutputsVonMisesEqv(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise Von-Mises criteria on a tensor field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eqv")

#internal name: eqv_fc
#scripting name: von_mises_eqv_fc
class _InputsVonMisesEqvFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv_fc._spec().inputs, op)
        self.fields_container = Input(von_mises_eqv_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsVonMisesEqvFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(von_mises_eqv_fc._spec().outputs, op)
        self.fields_container = Output(von_mises_eqv_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class von_mises_eqv_fc(Operator):
    """Computes the element-wise Von-Mises criteria on all the tensor fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.invariant.von_mises_eqv_fc()

    """
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="eqv_fc", config = config, server = server)
        self.inputs = _InputsVonMisesEqvFc(self)
        self.outputs = _OutputsVonMisesEqvFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise Von-Mises criteria on all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eqv_fc")

#internal name: invariants_deriv
#scripting name: invariants
class _InputsInvariants(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(invariants._spec().inputs, op)
        self.field = Input(invariants._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsInvariants(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(invariants._spec().outputs, op)
        self.field_int = Output(invariants._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field_int)
        self.field_eqv = Output(invariants._spec().output_pin(1), 1, op) 
        self._outputs.append(self.field_eqv)
        self.field_max_shear = Output(invariants._spec().output_pin(2), 2, op) 
        self._outputs.append(self.field_max_shear)

class invariants(Operator):
    """Computes the element-wise invariants of a tensor field.

      available inputs:
         field (Field)

      available outputs:
         field_int (Field)
         field_eqv (Field)
         field_max_shear (Field)

      Examples
      --------
      >>> op = operators.invariant.invariants()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="invariants_deriv", config = config, server = server)
        self.inputs = _InputsInvariants(self)
        self.outputs = _OutputsInvariants(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise invariants of a tensor field.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_int", type_names=["field"], optional=False, document="""stress intensity field"""), 
                                 1 : PinSpecification(name = "field_eqv", type_names=["field"], optional=False, document="""stress equivalent intensity"""), 
                                 2 : PinSpecification(name = "field_max_shear", type_names=["field"], optional=False, document="""max shear stress field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants_deriv")

#internal name: eig_values_fc
#scripting name: eigen_values_fc
class _InputsEigenValuesFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_values_fc._spec().inputs, op)
        self.fields_container = Input(eigen_values_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsEigenValuesFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_values_fc._spec().outputs, op)
        self.fields_container = Output(eigen_values_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class eigen_values_fc(Operator):
    """Computes the element-wise eigen values of all the tensor fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.invariant.eigen_values_fc()

    """
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="eig_values_fc", config = config, server = server)
        self.inputs = _InputsEigenValuesFc(self)
        self.outputs = _OutputsEigenValuesFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen values of all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eig_values_fc")

#internal name: invariants_deriv_fc
#scripting name: invariants_fc
class _InputsInvariantsFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(invariants_fc._spec().inputs, op)
        self.fields_container = Input(invariants_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsInvariantsFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(invariants_fc._spec().outputs, op)
        self.fields_int = Output(invariants_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_int)
        self.fields_eqv = Output(invariants_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.fields_eqv)
        self.fields_max_shear = Output(invariants_fc._spec().output_pin(2), 2, op) 
        self._outputs.append(self.fields_max_shear)

class invariants_fc(Operator):
    """Computes the element-wise invariants of all the tensor fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_int (FieldsContainer)
         fields_eqv (FieldsContainer)
         fields_max_shear (FieldsContainer)

      Examples
      --------
      >>> op = operators.invariant.invariants_fc()

    """
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="invariants_deriv_fc", config = config, server = server)
        self.inputs = _InputsInvariantsFc(self)
        self.outputs = _OutputsInvariantsFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise invariants of all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_int", type_names=["fields_container"], optional=False, document="""stress intensity field"""), 
                                 1 : PinSpecification(name = "fields_eqv", type_names=["fields_container"], optional=False, document="""stress equivalent intensity"""), 
                                 2 : PinSpecification(name = "fields_max_shear", type_names=["fields_container"], optional=False, document="""max shear stress field""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants_deriv_fc")

#internal name: invariants_fc
#scripting name: principal_invariants_fc
class _InputsPrincipalInvariantsFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(principal_invariants_fc._spec().inputs, op)
        self.fields_container = Input(principal_invariants_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields_container)

class _OutputsPrincipalInvariantsFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(principal_invariants_fc._spec().outputs, op)
        self.fields_eig_1 = Output(principal_invariants_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_eig_1)
        self.fields_eig_2 = Output(principal_invariants_fc._spec().output_pin(1), 1, op) 
        self._outputs.append(self.fields_eig_2)
        self.fields_eig_3 = Output(principal_invariants_fc._spec().output_pin(2), 2, op) 
        self._outputs.append(self.fields_eig_3)

class principal_invariants_fc(Operator):
    """Computes the element-wise eigen values of all the tensor fields of a fields container.

      available inputs:
         fields_container (FieldsContainer)

      available outputs:
         fields_eig_1 (FieldsContainer)
         fields_eig_2 (FieldsContainer)
         fields_eig_3 (FieldsContainer)

      Examples
      --------
      >>> op = operators.invariant.principal_invariants_fc()

    """
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="invariants_fc", config = config, server = server)
        self.inputs = _InputsPrincipalInvariantsFc(self)
        self.outputs = _OutputsPrincipalInvariantsFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen values of all the tensor fields of a fields container.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_eig_1", type_names=["fields_container"], optional=False, document="""first eigen value fields"""), 
                                 1 : PinSpecification(name = "fields_eig_2", type_names=["fields_container"], optional=False, document="""second eigen value fields"""), 
                                 2 : PinSpecification(name = "fields_eig_3", type_names=["fields_container"], optional=False, document="""third eigen value fields""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "invariants_fc")

"""
Invariant Operators
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore.dll plugin, from "invariant" category
"""

#internal name: eig_vectors_fc
#scripting name: eigen_vectors_fc
class _InputsEigenVectorsFc(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors_fc._spec().inputs, op)
        self.field = Input(eigen_vectors_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field)

class _OutputsEigenVectorsFc(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors_fc._spec().outputs, op)
        self.field = Output(eigen_vectors_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class eigen_vectors_fc(Operator):
    """Computes the element-wise eigen vectors for each tensor in the field

      available inputs:
         field (FieldsContainer, Field)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.invariant.eigen_vectors_fc()

    """
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="eig_vectors_fc", config = config, server = server)
        self.inputs = _InputsEigenVectorsFc(self)
        self.outputs = _OutputsEigenVectorsFc(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen vectors for each tensor in the field""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["fields_container","field"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eig_vectors_fc")

#internal name: eig_vectors
#scripting name: eigen_vectors
class _InputsEigenVectors(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().inputs, op)
        self.fields = Input(eigen_vectors._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.fields)

class _OutputsEigenVectors(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(eigen_vectors._spec().outputs, op)
        self.fields_container = Output(eigen_vectors._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class eigen_vectors(Operator):
    """Computes the element-wise eigen vectors for each tensor in the fields of the field container

      available inputs:
         fields (FieldsContainer, Field)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.invariant.eigen_vectors()

    """
    def __init__(self, fields=None, config=None, server=None):
        super().__init__(name="eig_vectors", config = config, server = server)
        self.inputs = _InputsEigenVectors(self)
        self.outputs = _OutputsEigenVectors(self)
        if fields !=None:
            self.inputs.fields.connect(fields)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the element-wise eigen vectors for each tensor in the fields of the field container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "eig_vectors")

