from ansys.dpf.core.dpf_operator import Operator as _Operator
from ansys.dpf.core.inputs import Input
from ansys.dpf.core.outputs import Output
from ansys.dpf.core.inputs import _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.database_tools import PinSpecification as _PinSpecification

"""Operators from Ans.Dpf.FEMUtils.dll plugin, from "averaging" category
"""

#internal name: nodal_fraction_fc
#scripting name: nodal_fraction_fc
def _get_input_spec_nodal_fraction_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin6 = _PinSpecification(name = "denominator", type_names = ["fields_container"], optional = True, document = """if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc""")
    inputs_dict_nodal_fraction_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        6 : inpin6
    }
    if pin is None:
        return inputs_dict_nodal_fraction_fc
    else:
        return inputs_dict_nodal_fraction_fc[pin]

def _get_output_spec_nodal_fraction_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_fraction_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_fraction_fc
    else:
        return outputs_dict_nodal_fraction_fc[pin]

class _InputSpecNodalFractionFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_fraction_fc(), op)
        self.fields_container = Input(_get_input_spec_nodal_fraction_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_nodal_fraction_fc(), op)
        self.mesh = Input(_get_input_spec_nodal_fraction_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_nodal_fraction_fc(), op)
        self.scoping = Input(_get_input_spec_nodal_fraction_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_nodal_fraction_fc(), op)
        self.denominator = Input(_get_input_spec_nodal_fraction_fc(6), 6, op, -1) 

class _OutputSpecNodalFractionFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_fraction_fc(), op)
        self.fields_container = Output(_get_output_spec_nodal_fraction_fc(0), 0, op) 

class _NodalFractionFc(_Operator):
    """Operator's description:
    Internal name is "nodal_fraction_fc"
    Scripting name is "nodal_fraction_fc"

    Description: Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)
       6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_fraction_fc")
    >>> op_way2 = core.operators.averaging.nodal_fraction_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("nodal_fraction_fc")
        self.inputs = _InputSpecNodalFractionFc(self)
        self.outputs = _OutputSpecNodalFractionFc(self)

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

def nodal_fraction_fc():
    """Operator's description:
    Internal name is "nodal_fraction_fc"
    Scripting name is "nodal_fraction_fc"

    Description: Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)
       6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of elemental_nodal_To_nodal_fc)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_fraction_fc")
    >>> op_way2 = core.operators.averaging.nodal_fraction_fc()
    """
    return _NodalFractionFc()

#internal name: ElementalNodal_To_NodalElemental_fc
#scripting name: elemental_nodal_to_nodal_elemental_fc
def _get_input_spec_elemental_nodal_to_nodal_elemental_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_elemental_nodal_to_nodal_elemental_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_elemental_nodal_to_nodal_elemental_fc
    else:
        return inputs_dict_elemental_nodal_to_nodal_elemental_fc[pin]

def _get_output_spec_elemental_nodal_to_nodal_elemental_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_elemental_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_nodal_to_nodal_elemental_fc
    else:
        return outputs_dict_elemental_nodal_to_nodal_elemental_fc[pin]

class _InputSpecElementalNodalToNodalElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_nodal_to_nodal_elemental_fc(1), 1, op, -1) 

class _OutputSpecElementalNodalToNodalElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_nodal_to_nodal_elemental_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_nodal_to_nodal_elemental_fc(0), 0, op) 

class _ElementalNodalToNodalElementalFc(_Operator):
    """Operator's description:
    Internal name is "ElementalNodal_To_NodalElemental_fc"
    Scripting name is "elemental_nodal_to_nodal_elemental_fc"

    Description: Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh_scoping 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalNodal_To_NodalElemental_fc")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ElementalNodal_To_NodalElemental_fc")
        self.inputs = _InputSpecElementalNodalToNodalElementalFc(self)
        self.outputs = _OutputSpecElementalNodalToNodalElementalFc(self)

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

def elemental_nodal_to_nodal_elemental_fc():
    """Operator's description:
    Internal name is "ElementalNodal_To_NodalElemental_fc"
    Scripting name is "elemental_nodal_to_nodal_elemental_fc"

    Description: Transform ElementalNodal fields to NodalElemental fields, compute result on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh_scoping 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalNodal_To_NodalElemental_fc")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_elemental_fc()
    """
    return _ElementalNodalToNodalElementalFc()

#internal name: elemental_difference
#scripting name: elemental_difference
def _get_input_spec_elemental_difference(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_difference = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_elemental_difference
    else:
        return inputs_dict_elemental_difference[pin]

def _get_output_spec_elemental_difference(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_difference = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_difference
    else:
        return outputs_dict_elemental_difference[pin]

class _InputSpecElementalDifference(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_difference(), op)
        self.field = Input(_get_input_spec_elemental_difference(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_difference(), op)
        self.mesh = Input(_get_input_spec_elemental_difference(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_difference(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_difference(3), 3, op, -1) 
        super().__init__(_get_input_spec_elemental_difference(), op)
        self.through_layers = Input(_get_input_spec_elemental_difference(10), 10, op, -1) 

class _OutputSpecElementalDifference(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_difference(), op)
        self.fields_container = Output(_get_output_spec_elemental_difference(0), 0, op) 

class _ElementalDifference(_Operator):
    """Operator's description:
    Internal name is "elemental_difference"
    Scripting name is "elemental_difference"

    Description: Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_difference")
    >>> op_way2 = core.operators.averaging.elemental_difference()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_difference")
        self.inputs = _InputSpecElementalDifference(self)
        self.outputs = _OutputSpecElementalDifference(self)

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

def elemental_difference():
    """Operator's description:
    Internal name is "elemental_difference"
    Scripting name is "elemental_difference"

    Description: Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_difference")
    >>> op_way2 = core.operators.averaging.elemental_difference()
    """
    return _ElementalDifference()

#internal name: elemental_nodal_To_nodal
#scripting name: elemental_nodal_to_nodal
def _get_input_spec_elemental_nodal_to_nodal(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_nodal_to_nodal = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_elemental_nodal_to_nodal
    else:
        return inputs_dict_elemental_nodal_to_nodal[pin]

def _get_output_spec_elemental_nodal_to_nodal(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_nodal_to_nodal
    else:
        return outputs_dict_elemental_nodal_to_nodal[pin]

class _InputSpecElementalNodalToNodal(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_nodal_to_nodal(), op)
        self.field = Input(_get_input_spec_elemental_nodal_to_nodal(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal(), op)
        self.mesh = Input(_get_input_spec_elemental_nodal_to_nodal(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal(), op)
        self.should_average = Input(_get_input_spec_elemental_nodal_to_nodal(2), 2, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_nodal_to_nodal(3), 3, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal(), op)
        self.through_layers = Input(_get_input_spec_elemental_nodal_to_nodal(10), 10, op, -1) 

class _OutputSpecElementalNodalToNodal(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_nodal_to_nodal(), op)
        self.fields_container = Output(_get_output_spec_elemental_nodal_to_nodal(0), 0, op) 

class _ElementalNodalToNodal(_Operator):
    """Operator's description:
    Internal name is "elemental_nodal_To_nodal"
    Scripting name is "elemental_nodal_to_nodal"

    Description: Transform ElementalNodal field into Nodal field using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_nodal_To_nodal")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_nodal_To_nodal")
        self.inputs = _InputSpecElementalNodalToNodal(self)
        self.outputs = _OutputSpecElementalNodalToNodal(self)

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

def elemental_nodal_to_nodal():
    """Operator's description:
    Internal name is "elemental_nodal_To_nodal"
    Scripting name is "elemental_nodal_to_nodal"

    Description: Transform ElementalNodal field into Nodal field using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_nodal_To_nodal")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal()
    """
    return _ElementalNodalToNodal()

#internal name: elemental_difference_fc
#scripting name: elemental_difference_fc
def _get_input_spec_elemental_difference_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_difference_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_elemental_difference_fc
    else:
        return inputs_dict_elemental_difference_fc[pin]

def _get_output_spec_elemental_difference_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_difference_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_difference_fc
    else:
        return outputs_dict_elemental_difference_fc[pin]

class _InputSpecElementalDifferenceFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_difference_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_difference_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_difference_fc(), op)
        self.mesh = Input(_get_input_spec_elemental_difference_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_difference_fc(), op)
        self.scoping = Input(_get_input_spec_elemental_difference_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_elemental_difference_fc(), op)
        self.collapse_shell_layers = Input(_get_input_spec_elemental_difference_fc(10), 10, op, -1) 

class _OutputSpecElementalDifferenceFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_difference_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_difference_fc(0), 0, op) 

class _ElementalDifferenceFc(_Operator):
    """Operator's description:
    Internal name is "elemental_difference_fc"
    Scripting name is "elemental_difference_fc"

    Description: Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the unaveraged or averaged (depending on the input fields) computed result for all nodes in this element. Result is computed on a given element scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       10: collapse_shell_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_difference_fc")
    >>> op_way2 = core.operators.averaging.elemental_difference_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_difference_fc")
        self.inputs = _InputSpecElementalDifferenceFc(self)
        self.outputs = _OutputSpecElementalDifferenceFc(self)

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

def elemental_difference_fc():
    """Operator's description:
    Internal name is "elemental_difference_fc"
    Scripting name is "elemental_difference_fc"

    Description: Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the unaveraged or averaged (depending on the input fields) computed result for all nodes in this element. Result is computed on a given element scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       10: collapse_shell_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_difference_fc")
    >>> op_way2 = core.operators.averaging.elemental_difference_fc()
    """
    return _ElementalDifferenceFc()

#internal name: elemental_nodal_To_nodal_fc
#scripting name: elemental_nodal_to_nodal_fc
def _get_input_spec_elemental_nodal_to_nodal_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_elemental_nodal_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_elemental_nodal_to_nodal_fc
    else:
        return inputs_dict_elemental_nodal_to_nodal_fc[pin]

def _get_output_spec_elemental_nodal_to_nodal_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_nodal_to_nodal_fc
    else:
        return outputs_dict_elemental_nodal_to_nodal_fc[pin]

class _InputSpecElementalNodalToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_nodal_to_nodal_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_fc(), op)
        self.mesh = Input(_get_input_spec_elemental_nodal_to_nodal_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_fc(), op)
        self.should_average = Input(_get_input_spec_elemental_nodal_to_nodal_fc(2), 2, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_fc(), op)
        self.scoping = Input(_get_input_spec_elemental_nodal_to_nodal_fc(3), 3, op, -1) 

class _OutputSpecElementalNodalToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_nodal_to_nodal_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_nodal_to_nodal_fc(0), 0, op) 

class _ElementalNodalToNodalFc(_Operator):
    """Operator's description:
    Internal name is "elemental_nodal_To_nodal_fc"
    Scripting name is "elemental_nodal_to_nodal_fc"

    Description: Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_nodal_To_nodal_fc")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_nodal_To_nodal_fc")
        self.inputs = _InputSpecElementalNodalToNodalFc(self)
        self.outputs = _OutputSpecElementalNodalToNodalFc(self)

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

def elemental_nodal_to_nodal_fc():
    """Operator's description:
    Internal name is "elemental_nodal_To_nodal_fc"
    Scripting name is "elemental_nodal_to_nodal_fc"

    Description: Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_nodal_To_nodal_fc")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_fc()
    """
    return _ElementalNodalToNodalFc()

#internal name: elemental_to_nodal
#scripting name: elemental_to_nodal
def _get_input_spec_elemental_to_nodal(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["int32"], optional = True, document = """averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones)""")
    inputs_dict_elemental_to_nodal = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_elemental_to_nodal
    else:
        return inputs_dict_elemental_to_nodal[pin]

def _get_output_spec_elemental_to_nodal(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_to_nodal = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_to_nodal
    else:
        return outputs_dict_elemental_to_nodal[pin]

class _InputSpecElementalToNodal(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_to_nodal(), op)
        self.field = Input(_get_input_spec_elemental_to_nodal(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_to_nodal(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_to_nodal(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_to_nodal(), op)
        self.force_averaging = Input(_get_input_spec_elemental_to_nodal(2), 2, op, -1) 

class _OutputSpecElementalToNodal(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_to_nodal(), op)
        self.field = Output(_get_output_spec_elemental_to_nodal(0), 0, op) 

class _ElementalToNodal(_Operator):
    """Operator's description:
    Internal name is "elemental_to_nodal"
    Scripting name is "elemental_to_nodal"

    Description: Transform ElementalNodal field to Nodal field, compute result on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 
       2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_to_nodal")
    >>> op_way2 = core.operators.averaging.elemental_to_nodal()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_to_nodal")
        self.inputs = _InputSpecElementalToNodal(self)
        self.outputs = _OutputSpecElementalToNodal(self)

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

def elemental_to_nodal():
    """Operator's description:
    Internal name is "elemental_to_nodal"
    Scripting name is "elemental_to_nodal"

    Description: Transform ElementalNodal field to Nodal field, compute result on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 
       2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is 1 for integrated results and 0 for dicrete ones))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_to_nodal")
    >>> op_way2 = core.operators.averaging.elemental_to_nodal()
    """
    return _ElementalToNodal()

#internal name: elemental_to_nodal_fc
#scripting name: elemental_to_nodal_fc
def _get_input_spec_elemental_to_nodal_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["int32"], optional = True, document = """averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones)""")
    inputs_dict_elemental_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2
    }
    if pin is None:
        return inputs_dict_elemental_to_nodal_fc
    else:
        return inputs_dict_elemental_to_nodal_fc[pin]

def _get_output_spec_elemental_to_nodal_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_to_nodal_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_to_nodal_fc
    else:
        return outputs_dict_elemental_to_nodal_fc[pin]

class _InputSpecElementalToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_to_nodal_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_to_nodal_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_to_nodal_fc(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_to_nodal_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_to_nodal_fc(), op)
        self.force_averaging = Input(_get_input_spec_elemental_to_nodal_fc(2), 2, op, -1) 

class _OutputSpecElementalToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_to_nodal_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_to_nodal_fc(0), 0, op) 

class _ElementalToNodalFc(_Operator):
    """Operator's description:
    Internal name is "elemental_to_nodal_fc"
    Scripting name is "elemental_to_nodal_fc"

    Description: Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh_scoping 
       2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_to_nodal_fc")
    >>> op_way2 = core.operators.averaging.elemental_to_nodal_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_to_nodal_fc")
        self.inputs = _InputSpecElementalToNodalFc(self)
        self.outputs = _OutputSpecElementalToNodalFc(self)

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

def elemental_to_nodal_fc():
    """Operator's description:
    Internal name is "elemental_to_nodal_fc"
    Scripting name is "elemental_to_nodal_fc"

    Description: Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh_scoping 
       2: force_averaging (averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_to_nodal_fc")
    >>> op_way2 = core.operators.averaging.elemental_to_nodal_fc()
    """
    return _ElementalToNodalFc()

#internal name: nodal_difference
#scripting name: nodal_difference
def _get_input_spec_nodal_difference(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = False, document = """""")
    inpin2 = _PinSpecification(name = "should_average", type_names = ["bool"], optional = True, document = """each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = False, document = """average only on these entities""")
    inpin10 = _PinSpecification(name = "through_layers", type_names = ["bool"], optional = True, document = """the max elemental difference is taken through the different shell layers if true (default is false)""")
    inputs_dict_nodal_difference = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_nodal_difference
    else:
        return inputs_dict_nodal_difference[pin]

def _get_output_spec_nodal_difference(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_difference = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_difference
    else:
        return outputs_dict_nodal_difference[pin]

class _InputSpecNodalDifference(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_difference(), op)
        self.field = Input(_get_input_spec_nodal_difference(0), 0, op, -1) 
        super().__init__(_get_input_spec_nodal_difference(), op)
        self.mesh = Input(_get_input_spec_nodal_difference(1), 1, op, -1) 
        super().__init__(_get_input_spec_nodal_difference(), op)
        self.should_average = Input(_get_input_spec_nodal_difference(2), 2, op, -1) 
        super().__init__(_get_input_spec_nodal_difference(), op)
        self.mesh_scoping = Input(_get_input_spec_nodal_difference(3), 3, op, -1) 
        super().__init__(_get_input_spec_nodal_difference(), op)
        self.through_layers = Input(_get_input_spec_nodal_difference(10), 10, op, -1) 

class _OutputSpecNodalDifference(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_difference(), op)
        self.fields_container = Output(_get_output_spec_nodal_difference(0), 0, op) 

class _NodalDifference(_Operator):
    """Operator's description:
    Internal name is "nodal_difference"
    Scripting name is "nodal_difference"

    Description: Transform ElementalNodal field into Nodal field. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_difference")
    >>> op_way2 = core.operators.averaging.nodal_difference()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("nodal_difference")
        self.inputs = _InputSpecNodalDifference(self)
        self.outputs = _OutputSpecNodalDifference(self)

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

def nodal_difference():
    """Operator's description:
    Internal name is "nodal_difference"
    Scripting name is "nodal_difference"

    Description: Transform ElementalNodal field into Nodal field. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh 
       2: should_average (each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities))
       3: mesh_scoping (average only on these entities)
       10: through_layers (the max elemental difference is taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_difference")
    >>> op_way2 = core.operators.averaging.nodal_difference()
    """
    return _NodalDifference()

#internal name: nodal_difference_fc
#scripting name: nodal_difference_fc
def _get_input_spec_nodal_difference_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_nodal_difference_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_nodal_difference_fc
    else:
        return inputs_dict_nodal_difference_fc[pin]

def _get_output_spec_nodal_difference_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_difference_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_difference_fc
    else:
        return outputs_dict_nodal_difference_fc[pin]

class _InputSpecNodalDifferenceFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_difference_fc(), op)
        self.fields_container = Input(_get_input_spec_nodal_difference_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_nodal_difference_fc(), op)
        self.mesh = Input(_get_input_spec_nodal_difference_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_nodal_difference_fc(), op)
        self.scoping = Input(_get_input_spec_nodal_difference_fc(3), 3, op, -1) 

class _OutputSpecNodalDifferenceFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_difference_fc(), op)
        self.fields_container = Output(_get_output_spec_nodal_difference_fc(0), 0, op) 

class _NodalDifferenceFc(_Operator):
    """Operator's description:
    Internal name is "nodal_difference_fc"
    Scripting name is "nodal_difference_fc"

    Description: Transform ElementalNodal fields into Nodal fields. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_difference_fc")
    >>> op_way2 = core.operators.averaging.nodal_difference_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("nodal_difference_fc")
        self.inputs = _InputSpecNodalDifferenceFc(self)
        self.outputs = _OutputSpecNodalDifferenceFc(self)

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

def nodal_difference_fc():
    """Operator's description:
    Internal name is "nodal_difference_fc"
    Scripting name is "nodal_difference_fc"

    Description: Transform ElementalNodal fields into Nodal fields. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_difference_fc")
    >>> op_way2 = core.operators.averaging.nodal_difference_fc()
    """
    return _NodalDifferenceFc()

#internal name: elemental_fraction_fc
#scripting name: elemental_fraction_fc
def _get_input_spec_elemental_fraction_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin6 = _PinSpecification(name = "denominator", type_names = ["fields_container"], optional = True, document = """if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """the elemental difference and the entity average are taken through the different shell layers if true (default is false)""")
    inputs_dict_elemental_fraction_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        6 : inpin6,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_elemental_fraction_fc
    else:
        return inputs_dict_elemental_fraction_fc[pin]

def _get_output_spec_elemental_fraction_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_fraction_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_fraction_fc
    else:
        return outputs_dict_elemental_fraction_fc[pin]

class _InputSpecElementalFractionFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_fraction_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_fraction_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_fraction_fc(), op)
        self.mesh = Input(_get_input_spec_elemental_fraction_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_fraction_fc(), op)
        self.scoping = Input(_get_input_spec_elemental_fraction_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_elemental_fraction_fc(), op)
        self.denominator = Input(_get_input_spec_elemental_fraction_fc(6), 6, op, -1) 
        super().__init__(_get_input_spec_elemental_fraction_fc(), op)
        self.collapse_shell_layers = Input(_get_input_spec_elemental_fraction_fc(10), 10, op, -1) 

class _OutputSpecElementalFractionFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_fraction_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_fraction_fc(0), 0, op) 

class _ElementalFractionFc(_Operator):
    """Operator's description:
    Internal name is "elemental_fraction_fc"
    Scripting name is "elemental_fraction_fc"

    Description: Transform ElementalNodal fields into Elemental fields. Each elemental value is the fraction between the elemental difference and the entity average. Result is computed on a given elements scoping.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc)
       10: collapse_shell_layers (the elemental difference and the entity average are taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_fraction_fc")
    >>> op_way2 = core.operators.averaging.elemental_fraction_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("elemental_fraction_fc")
        self.inputs = _InputSpecElementalFractionFc(self)
        self.outputs = _OutputSpecElementalFractionFc(self)

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

def elemental_fraction_fc():
    """Operator's description:
    Internal name is "elemental_fraction_fc"
    Scripting name is "elemental_fraction_fc"

    Description: Transform ElementalNodal fields into Elemental fields. Each elemental value is the fraction between the elemental difference and the entity average. Result is computed on a given elements scoping.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       6: denominator (if a fields container is set in this pin, it is used as the denominator of the fraction instead of entity_average_fc)
       10: collapse_shell_layers (the elemental difference and the entity average are taken through the different shell layers if true (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("elemental_fraction_fc")
    >>> op_way2 = core.operators.averaging.elemental_fraction_fc()
    """
    return _ElementalFractionFc()

#internal name: to_nodal
#scripting name: to_nodal
def _get_input_spec_to_nodal(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_to_nodal = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_to_nodal
    else:
        return inputs_dict_to_nodal[pin]

def _get_output_spec_to_nodal(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_to_nodal = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_to_nodal
    else:
        return outputs_dict_to_nodal[pin]

class _InputSpecToNodal(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_to_nodal(), op)
        self.field = Input(_get_input_spec_to_nodal(0), 0, op, -1) 
        super().__init__(_get_input_spec_to_nodal(), op)
        self.mesh_scoping = Input(_get_input_spec_to_nodal(1), 1, op, -1) 

class _OutputSpecToNodal(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_to_nodal(), op)
        self.field = Output(_get_output_spec_to_nodal(0), 0, op) 

class _ToNodal(_Operator):
    """Operator's description:
    Internal name is "to_nodal"
    Scripting name is "to_nodal"

    Description: Transform input field into Nodal field using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_nodal")
    >>> op_way2 = core.operators.averaging.to_nodal()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("to_nodal")
        self.inputs = _InputSpecToNodal(self)
        self.outputs = _OutputSpecToNodal(self)

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

def to_nodal():
    """Operator's description:
    Internal name is "to_nodal"
    Scripting name is "to_nodal"

    Description: Transform input field into Nodal field using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_nodal")
    >>> op_way2 = core.operators.averaging.to_nodal()
    """
    return _ToNodal()

#internal name: to_nodal_fc
#scripting name: to_nodal_fc
def _get_input_spec_to_nodal_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_to_nodal_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_to_nodal_fc
    else:
        return inputs_dict_to_nodal_fc[pin]

def _get_output_spec_to_nodal_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_nodal_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_to_nodal_fc
    else:
        return outputs_dict_to_nodal_fc[pin]

class _InputSpecToNodalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_to_nodal_fc(), op)
        self.fields_container = Input(_get_input_spec_to_nodal_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_to_nodal_fc(), op)
        self.mesh = Input(_get_input_spec_to_nodal_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_to_nodal_fc(), op)
        self.mesh_scoping = Input(_get_input_spec_to_nodal_fc(3), 3, op, -1) 

class _OutputSpecToNodalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_to_nodal_fc(), op)
        self.fields_container = Output(_get_output_spec_to_nodal_fc(0), 0, op) 

class _ToNodalFc(_Operator):
    """Operator's description:
    Internal name is "to_nodal_fc"
    Scripting name is "to_nodal_fc"

    Description: Transform input fields into Nodal fields using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh 
       3: mesh_scoping 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_nodal_fc")
    >>> op_way2 = core.operators.averaging.to_nodal_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("to_nodal_fc")
        self.inputs = _InputSpecToNodalFc(self)
        self.outputs = _OutputSpecToNodalFc(self)

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

def to_nodal_fc():
    """Operator's description:
    Internal name is "to_nodal_fc"
    Scripting name is "to_nodal_fc"

    Description: Transform input fields into Nodal fields using an averaging process, result is computed on a given node scoping.

    Input list: 
       0: fields_container 
       1: mesh 
       3: mesh_scoping 

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_nodal_fc")
    >>> op_way2 = core.operators.averaging.to_nodal_fc()
    """
    return _ToNodalFc()

#internal name: ElementalNodal_To_NodalElemental
#scripting name: elemental_nodal_to_nodal_elemental
def _get_input_spec_elemental_nodal_to_nodal_elemental(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inputs_dict_elemental_nodal_to_nodal_elemental = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_elemental_nodal_to_nodal_elemental
    else:
        return inputs_dict_elemental_nodal_to_nodal_elemental[pin]

def _get_output_spec_elemental_nodal_to_nodal_elemental(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_nodal_to_nodal_elemental = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_nodal_to_nodal_elemental
    else:
        return outputs_dict_elemental_nodal_to_nodal_elemental[pin]

class _InputSpecElementalNodalToNodalElemental(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_elemental(), op)
        self.field = Input(_get_input_spec_elemental_nodal_to_nodal_elemental(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_nodal_to_nodal_elemental(), op)
        self.mesh_scoping = Input(_get_input_spec_elemental_nodal_to_nodal_elemental(1), 1, op, -1) 

class _OutputSpecElementalNodalToNodalElemental(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_nodal_to_nodal_elemental(), op)
        self.field = Output(_get_output_spec_elemental_nodal_to_nodal_elemental(0), 0, op) 

class _ElementalNodalToNodalElemental(_Operator):
    """Operator's description:
    Internal name is "ElementalNodal_To_NodalElemental"
    Scripting name is "elemental_nodal_to_nodal_elemental"

    Description: Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalNodal_To_NodalElemental")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_elemental()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("ElementalNodal_To_NodalElemental")
        self.inputs = _InputSpecElementalNodalToNodalElemental(self)
        self.outputs = _OutputSpecElementalNodalToNodalElemental(self)

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

def elemental_nodal_to_nodal_elemental():
    """Operator's description:
    Internal name is "ElementalNodal_To_NodalElemental"
    Scripting name is "elemental_nodal_to_nodal_elemental"

    Description: Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("ElementalNodal_To_NodalElemental")
    >>> op_way2 = core.operators.averaging.elemental_nodal_to_nodal_elemental()
    """
    return _ElementalNodalToNodalElemental()

#internal name: extend_to_mid_nodes
#scripting name: extend_to_mid_nodes
def _get_input_spec_extend_to_mid_nodes(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inputs_dict_extend_to_mid_nodes = { 
        0 : inpin0
    }
    if pin is None:
        return inputs_dict_extend_to_mid_nodes
    else:
        return inputs_dict_extend_to_mid_nodes[pin]

def _get_output_spec_extend_to_mid_nodes(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_extend_to_mid_nodes = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_extend_to_mid_nodes
    else:
        return outputs_dict_extend_to_mid_nodes[pin]

class _InputSpecExtendToMidNodes(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_extend_to_mid_nodes(), op)
        self.field = Input(_get_input_spec_extend_to_mid_nodes(0), 0, op, -1) 

class _OutputSpecExtendToMidNodes(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_extend_to_mid_nodes(), op)
        self.field = Output(_get_output_spec_extend_to_mid_nodes(0), 0, op) 

class _ExtendToMidNodes(_Operator):
    """Operator's description:
    Internal name is "extend_to_mid_nodes"
    Scripting name is "extend_to_mid_nodes"

    Description: Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("extend_to_mid_nodes")
    >>> op_way2 = core.operators.averaging.extend_to_mid_nodes()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("extend_to_mid_nodes")
        self.inputs = _InputSpecExtendToMidNodes(self)
        self.outputs = _OutputSpecExtendToMidNodes(self)

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

def extend_to_mid_nodes():
    """Operator's description:
    Internal name is "extend_to_mid_nodes"
    Scripting name is "extend_to_mid_nodes"

    Description: Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.

    Input list: 
       0: field (field or fields container with only one field is expected)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("extend_to_mid_nodes")
    >>> op_way2 = core.operators.averaging.extend_to_mid_nodes()
    """
    return _ExtendToMidNodes()

#internal name: extend_to_mid_nodes_fc
#scripting name: extend_to_mid_nodes_fc
def _get_input_spec_extend_to_mid_nodes_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inputs_dict_extend_to_mid_nodes_fc = { 
        0 : inpin0,
        1 : inpin1
    }
    if pin is None:
        return inputs_dict_extend_to_mid_nodes_fc
    else:
        return inputs_dict_extend_to_mid_nodes_fc[pin]

def _get_output_spec_extend_to_mid_nodes_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_extend_to_mid_nodes_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_extend_to_mid_nodes_fc
    else:
        return outputs_dict_extend_to_mid_nodes_fc[pin]

class _InputSpecExtendToMidNodesFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_extend_to_mid_nodes_fc(), op)
        self.fields_container = Input(_get_input_spec_extend_to_mid_nodes_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_extend_to_mid_nodes_fc(), op)
        self.mesh = Input(_get_input_spec_extend_to_mid_nodes_fc(1), 1, op, -1) 

class _OutputSpecExtendToMidNodesFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_extend_to_mid_nodes_fc(), op)
        self.fields_container = Output(_get_output_spec_extend_to_mid_nodes_fc(0), 0, op) 

class _ExtendToMidNodesFc(_Operator):
    """Operator's description:
    Internal name is "extend_to_mid_nodes_fc"
    Scripting name is "extend_to_mid_nodes_fc"

    Description: Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("extend_to_mid_nodes_fc")
    >>> op_way2 = core.operators.averaging.extend_to_mid_nodes_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("extend_to_mid_nodes_fc")
        self.inputs = _InputSpecExtendToMidNodesFc(self)
        self.outputs = _OutputSpecExtendToMidNodesFc(self)

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

def extend_to_mid_nodes_fc():
    """Operator's description:
    Internal name is "extend_to_mid_nodes_fc"
    Scripting name is "extend_to_mid_nodes_fc"

    Description: Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("extend_to_mid_nodes_fc")
    >>> op_way2 = core.operators.averaging.extend_to_mid_nodes_fc()
    """
    return _ExtendToMidNodesFc()

#internal name: entity_average
#scripting name: elemental_mean
def _get_input_spec_elemental_mean(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["bool"], optional = True, document = """if true you average, if false you just sum""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inputs_dict_elemental_mean = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3
    }
    if pin is None:
        return inputs_dict_elemental_mean
    else:
        return inputs_dict_elemental_mean[pin]

def _get_output_spec_elemental_mean(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_elemental_mean = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_mean
    else:
        return outputs_dict_elemental_mean[pin]

class _InputSpecElementalMean(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_mean(), op)
        self.field = Input(_get_input_spec_elemental_mean(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_mean(), op)
        self.collapse_shell_layers = Input(_get_input_spec_elemental_mean(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_mean(), op)
        self.force_averaging = Input(_get_input_spec_elemental_mean(2), 2, op, -1) 
        super().__init__(_get_input_spec_elemental_mean(), op)
        self.scoping = Input(_get_input_spec_elemental_mean(3), 3, op, -1) 

class _OutputSpecElementalMean(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_mean(), op)
        self.field = Output(_get_output_spec_elemental_mean(0), 0, op) 

class _ElementalMean(_Operator):
    """Operator's description:
    Internal name is "entity_average"
    Scripting name is "elemental_mean"

    Description: Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).

    Input list: 
       0: field 
       1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
       2: force_averaging (if true you average, if false you just sum)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("entity_average")
    >>> op_way2 = core.operators.averaging.elemental_mean()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("entity_average")
        self.inputs = _InputSpecElementalMean(self)
        self.outputs = _OutputSpecElementalMean(self)

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

def elemental_mean():
    """Operator's description:
    Internal name is "entity_average"
    Scripting name is "elemental_mean"

    Description: Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).

    Input list: 
       0: field 
       1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
       2: force_averaging (if true you average, if false you just sum)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("entity_average")
    >>> op_way2 = core.operators.averaging.elemental_mean()
    """
    return _ElementalMean()

#internal name: entity_average_fc
#scripting name: elemental_mean_fc
def _get_input_spec_elemental_mean_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inpin2 = _PinSpecification(name = "force_averaging", type_names = ["bool"], optional = True, document = """if true you average, if false you just sum""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin4 = _PinSpecification(name = "meshed_region", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inputs_dict_elemental_mean_fc = { 
        0 : inpin0,
        1 : inpin1,
        2 : inpin2,
        3 : inpin3,
        4 : inpin4
    }
    if pin is None:
        return inputs_dict_elemental_mean_fc
    else:
        return inputs_dict_elemental_mean_fc[pin]

def _get_output_spec_elemental_mean_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_elemental_mean_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_elemental_mean_fc
    else:
        return outputs_dict_elemental_mean_fc[pin]

class _InputSpecElementalMeanFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_elemental_mean_fc(), op)
        self.fields_container = Input(_get_input_spec_elemental_mean_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_elemental_mean_fc(), op)
        self.collapse_shell_layers = Input(_get_input_spec_elemental_mean_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_elemental_mean_fc(), op)
        self.force_averaging = Input(_get_input_spec_elemental_mean_fc(2), 2, op, -1) 
        super().__init__(_get_input_spec_elemental_mean_fc(), op)
        self.scoping = Input(_get_input_spec_elemental_mean_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_elemental_mean_fc(), op)
        self.meshed_region = Input(_get_input_spec_elemental_mean_fc(4), 4, op, -1) 

class _OutputSpecElementalMeanFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_elemental_mean_fc(), op)
        self.fields_container = Output(_get_output_spec_elemental_mean_fc(0), 0, op) 

class _ElementalMeanFc(_Operator):
    """Operator's description:
    Internal name is "entity_average_fc"
    Scripting name is "elemental_mean_fc"

    Description: Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
       2: force_averaging (if true you average, if false you just sum)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       4: meshed_region (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("entity_average_fc")
    >>> op_way2 = core.operators.averaging.elemental_mean_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("entity_average_fc")
        self.inputs = _InputSpecElementalMeanFc(self)
        self.outputs = _OutputSpecElementalMeanFc(self)

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

def elemental_mean_fc():
    """Operator's description:
    Internal name is "entity_average_fc"
    Scripting name is "elemental_mean_fc"

    Description: Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal). If the input fields are mixed shell/solid and collapseShellLayers is not asked, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: collapse_shell_layers (if true shell layers are averaged as well (default is false))
       2: force_averaging (if true you average, if false you just sum)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       4: meshed_region (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("entity_average_fc")
    >>> op_way2 = core.operators.averaging.elemental_mean_fc()
    """
    return _ElementalMeanFc()

#internal name: to_elemental_fc
#scripting name: to_elemental_fc
def _get_input_spec_to_elemental_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """""")
    inpin3 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin7 = _PinSpecification(name = "smoothen_values", type_names = ["bool"], optional = True, document = """if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false)""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_to_elemental_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        7 : inpin7,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_to_elemental_fc
    else:
        return inputs_dict_to_elemental_fc[pin]

def _get_output_spec_to_elemental_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_to_elemental_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_to_elemental_fc
    else:
        return outputs_dict_to_elemental_fc[pin]

class _InputSpecToElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_to_elemental_fc(), op)
        self.fields_container = Input(_get_input_spec_to_elemental_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_to_elemental_fc(), op)
        self.mesh = Input(_get_input_spec_to_elemental_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_to_elemental_fc(), op)
        self.mesh_scoping = Input(_get_input_spec_to_elemental_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_to_elemental_fc(), op)
        self.smoothen_values = Input(_get_input_spec_to_elemental_fc(7), 7, op, -1) 
        super().__init__(_get_input_spec_to_elemental_fc(), op)
        self.collapse_shell_layers = Input(_get_input_spec_to_elemental_fc(10), 10, op, -1) 

class _OutputSpecToElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_to_elemental_fc(), op)
        self.fields_container = Output(_get_output_spec_to_elemental_fc(0), 0, op) 

class _ToElementalFc(_Operator):
    """Operator's description:
    Internal name is "to_elemental_fc"
    Scripting name is "to_elemental_fc"

    Description: Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.

    Input list: 
       0: fields_container 
       1: mesh 
       3: mesh_scoping 
       7: smoothen_values (if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false))
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_elemental_fc")
    >>> op_way2 = core.operators.averaging.to_elemental_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("to_elemental_fc")
        self.inputs = _InputSpecToElementalFc(self)
        self.outputs = _OutputSpecToElementalFc(self)

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

def to_elemental_fc():
    """Operator's description:
    Internal name is "to_elemental_fc"
    Scripting name is "to_elemental_fc"

    Description: Transform input fields into Elemental fields using an averaging process, result is computed on a given elements scoping.

    Input list: 
       0: fields_container 
       1: mesh 
       3: mesh_scoping 
       7: smoothen_values (if it is set to true, elemental nodal fields are first averaged on nodes and then averaged on elements (default is false))
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("to_elemental_fc")
    >>> op_way2 = core.operators.averaging.to_elemental_fc()
    """
    return _ToElementalFc()

#internal name: nodal_to_elemental
#scripting name: nodal_to_elemental
def _get_input_spec_nodal_to_elemental(pin = None):
    inpin0 = _PinSpecification(name = "field", type_names = ["field","fields_container"], optional = False, document = """field or fields container with only one field is expected""")
    inpin1 = _PinSpecification(name = "mesh_scoping", type_names = ["scoping"], optional = True, document = """""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_nodal_to_elemental = { 
        0 : inpin0,
        1 : inpin1,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_nodal_to_elemental
    else:
        return inputs_dict_nodal_to_elemental[pin]

def _get_output_spec_nodal_to_elemental(pin = None):
    outpin0 = _PinSpecification(name = "field", type_names = ["field"], document = """""")
    outputs_dict_nodal_to_elemental = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_to_elemental
    else:
        return outputs_dict_nodal_to_elemental[pin]

class _InputSpecNodalToElemental(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_to_elemental(), op)
        self.field = Input(_get_input_spec_nodal_to_elemental(0), 0, op, -1) 
        super().__init__(_get_input_spec_nodal_to_elemental(), op)
        self.mesh_scoping = Input(_get_input_spec_nodal_to_elemental(1), 1, op, -1) 
        super().__init__(_get_input_spec_nodal_to_elemental(), op)
        self.collapse_shell_layers = Input(_get_input_spec_nodal_to_elemental(10), 10, op, -1) 

class _OutputSpecNodalToElemental(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_to_elemental(), op)
        self.field = Output(_get_output_spec_nodal_to_elemental(0), 0, op) 

class _NodalToElemental(_Operator):
    """Operator's description:
    Internal name is "nodal_to_elemental"
    Scripting name is "nodal_to_elemental"

    Description: Transform Nodal field to Elemental field, compute result on a given element scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_to_elemental")
    >>> op_way2 = core.operators.averaging.nodal_to_elemental()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("nodal_to_elemental")
        self.inputs = _InputSpecNodalToElemental(self)
        self.outputs = _OutputSpecNodalToElemental(self)

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

def nodal_to_elemental():
    """Operator's description:
    Internal name is "nodal_to_elemental"
    Scripting name is "nodal_to_elemental"

    Description: Transform Nodal field to Elemental field, compute result on a given element scoping.

    Input list: 
       0: field (field or fields container with only one field is expected)
       1: mesh_scoping 
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: field 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_to_elemental")
    >>> op_way2 = core.operators.averaging.nodal_to_elemental()
    """
    return _NodalToElemental()

#internal name: nodal_to_elemental_fc
#scripting name: nodal_to_elemental_fc
def _get_input_spec_nodal_to_elemental_fc(pin = None):
    inpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], optional = False, document = """""")
    inpin1 = _PinSpecification(name = "mesh", type_names = ["meshed_region"], optional = True, document = """the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")
    inpin3 = _PinSpecification(name = "scoping", type_names = ["scoping"], optional = True, document = """average only on these elements, if it is scoping container, the label must correspond to the one of the fields container""")
    inpin10 = _PinSpecification(name = "collapse_shell_layers", type_names = ["bool"], optional = True, document = """if true shell layers are averaged as well (default is false)""")
    inputs_dict_nodal_to_elemental_fc = { 
        0 : inpin0,
        1 : inpin1,
        3 : inpin3,
        10 : inpin10
    }
    if pin is None:
        return inputs_dict_nodal_to_elemental_fc
    else:
        return inputs_dict_nodal_to_elemental_fc[pin]

def _get_output_spec_nodal_to_elemental_fc(pin = None):
    outpin0 = _PinSpecification(name = "fields_container", type_names = ["fields_container"], document = """""")
    outputs_dict_nodal_to_elemental_fc = { 
        0 : outpin0
    }
    if pin is None:
        return outputs_dict_nodal_to_elemental_fc
    else:
        return outputs_dict_nodal_to_elemental_fc[pin]

class _InputSpecNodalToElementalFc(_Inputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_input_spec_nodal_to_elemental_fc(), op)
        self.fields_container = Input(_get_input_spec_nodal_to_elemental_fc(0), 0, op, -1) 
        super().__init__(_get_input_spec_nodal_to_elemental_fc(), op)
        self.mesh = Input(_get_input_spec_nodal_to_elemental_fc(1), 1, op, -1) 
        super().__init__(_get_input_spec_nodal_to_elemental_fc(), op)
        self.scoping = Input(_get_input_spec_nodal_to_elemental_fc(3), 3, op, -1) 
        super().__init__(_get_input_spec_nodal_to_elemental_fc(), op)
        self.collapse_shell_layers = Input(_get_input_spec_nodal_to_elemental_fc(10), 10, op, -1) 

class _OutputSpecNodalToElementalFc(_Outputs):
    def __init__(self, op: _Operator):
        super().__init__(_get_output_spec_nodal_to_elemental_fc(), op)
        self.fields_container = Output(_get_output_spec_nodal_to_elemental_fc(0), 0, op) 

class _NodalToElementalFc(_Operator):
    """Operator's description:
    Internal name is "nodal_to_elemental_fc"
    Scripting name is "nodal_to_elemental_fc"

    Description: Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_to_elemental_fc")
    >>> op_way2 = core.operators.averaging.nodal_to_elemental_fc()
    """
    def __init__(self):
        """Specific operator class."""
        super().__init__("nodal_to_elemental_fc")
        self.inputs = _InputSpecNodalToElementalFc(self)
        self.outputs = _OutputSpecNodalToElementalFc(self)

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

def nodal_to_elemental_fc():
    """Operator's description:
    Internal name is "nodal_to_elemental_fc"
    Scripting name is "nodal_to_elemental_fc"

    Description: Transform Nodal fields into Elemental fields using an averaging process, result is computed on a given elements scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are splitted by element shape and the output fields container has elshape label.

    Input list: 
       0: fields_container 
       1: mesh (the mesh region in this pin is used to perform the averaging, if there is no field's support it is used)
       3: scoping (average only on these elements, if it is scoping container, the label must correspond to the one of the fields container)
       10: collapse_shell_layers (if true shell layers are averaged as well (default is false))

    Output list: 
       0: fields_container 

    Examples
    --------
    >>> from ansys.dpf import core
    >>> op_way1 = core.Operator("nodal_to_elemental_fc")
    >>> op_way2 = core.operators.averaging.nodal_to_elemental_fc()
    """
    return _NodalToElementalFc()

