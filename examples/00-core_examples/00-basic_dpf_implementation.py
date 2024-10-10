# # ~~~~~~~ DPF PRESENTATION ~~~~~~~ # #

# Ansys Data Processing Framework (DPF) provides a modular and easy to use toolbox for accessing and transforming
# simulation data using the DPF operators.
# DPF is a workflow-based framework which allows simple and/or complex evaluations by chaining operators.

# DPF is developed around two core components:
# - Data represented as a *field* (Component based on vectors quantities where the data is defined)
# - An *operator* to act upon this data
# Operators are like verbs, acting on the data, while fields are like nouns, objects that hold data.

######################################################################################################################
# # ~~~~~~~ DPF CODE ORGANISATION ~~~~~~~ # #

# DPF package is named : 'ansys.dpf.core package'. This package contains (based in the 2024 doc version):
# a) Three subpackages:
#       - 'ansys.dpf.core.examples' package
#       - 'ansys.dpf.core.helpers' namespace
#       - 'ansys.dpf.core.operators' package
# b) Sixty three submodules
#       - 'animation', 'animator', 'any', 'available_result', 'collection', 'collection_base', 'common',
#       'Operator config', 'core', 'custom_fields_container', 'custom_operator_base', 'custom_type_field',
#       'cyclic_support', 'data_sources', 'data_tree', 'dimensionality', 'dpf_array', 'dpf_operator', 'elements',
#       'element_descriptor', 'errors', 'faces', 'field','fields_definition', 'fields_container',
#       'fields_container_factory', 'fields_factory', 'generic_data_container', 'generic_support','normalize_vector',
#       'create_point', 'incremental', 'inputs', 'meshed_region', 'meshes_container', 'mesh_info',
#       'mesh_scoping_factory', 'model', 'nodes', 'operator_specification', 'outputs', 'path_utilities', 'plotter',
#       'plugins', 'property_field', 'results', 'result_info', 'runtime_config', 'scoping', 'scopings_container',
#       'server', 'server_context', 'server_factory', 'server_types', 'session', 'settings', 'streams_container',
#       'string_field', 'support', 'time_freq_scoping_factory', 'time_freq_support', 'unit_system', 'workflow'

######################################################################################################################
# # ~~~~~~~ USING DPF ~~~~~~~ # #

# An operator is the main object here. You use them to load, operate on, and output data.

# Each operator contains input and output pins, like those in an integrated circuit in electronics, that
# submit data to the operator and output the computed result from the operator, with respect to its description.
# Each pin has a number and a name

# The basic steps for using the operators are:
# ---------------------------------------------------------------------------------------------------------------------
# 1) Instance the operator. There are two ways for doing this:
#
#     1.1) By instantiating any of the derived classes available in the 'ansys.dpf.core.operators' package.
#     This package also have its subpackages:
#             - 'ansys.dpf.core.operators.averaging' package
#             - 'ansys.dpf.core.operators.compression' namespace
#             - 'ansys.dpf.core.operators.filter' package
#             - 'ansys.dpf.core.operators.geo' package
#             - 'aansys.dpf.core.operators.invariant package' package
#             - 'ansys.dpf.core.operators.logic' package
#             - 'ansys.dpf.core.operators.mapping' package
#             - 'ansys.dpf.core.operators.math' package
#             - 'ansys.dpf.core.operators.mesh' package
#             - 'ansys.dpf.core.operators.metadata' package
#             - 'ansys.dpf.core.operators.min_max' package
#             - 'ansys.dpf.core.operators.result' package
#             - 'ansys.dpf.core.operators.scoping' package
#             - 'ansys.dpf.core.operators.serialization' package
#             - 'ansys.dpf.core.operators.server' package
#             - 'ansys.dpf.core.operators.utility' package

#      If you believe you'll be using multiple modules available in the same package, its better to import it all
#      at the beginning
        from ansys.dpf.core import operators as ops # Import of the dpf core subpackage 'ansys.dpf.core.operators'
        my_operator = ops.subpackageAttribute.operatorAttribute() # I use the word attribute for any name following a dot
#      or
        from ansys.dpf import core as dpf
        my_operator = dpf.operators.subpackageAttribute.operatorAttribute()
#      or
        my_operator = ansys.dpf.core.operators.subpackageAttribute.operatorAttribute()

#      An example on how to create a displacement operator:
        from ansys.dpf.core import operators as ops
        my_displacement_operator = ops.result.displacement()

#     1.2) By instantiating  directly with the Operator submodule using the internal name string that indicates the operator
#     type. As this submodule is a class this can be done like :

        my_operator = ansys.dpf.core.Operator("internal_name_string")

#       An example on how to create a displacement operator:
        my_displacement_operator = ansys.dpf.core.Operator("U")

# As a guideline for better comprehension and clarity of the code, we recommend the use of the first method (1.1)

# You can check the available input (and outputs pints) pins by printing  the instantiated operator:
print(my_operator)

# ---------------------------------------------------------------------------------------------------------------------
# 2) Connect the operator input pin, this allows the user to pass on his data to the operator.
# Every operator have at least one imperative input pin. There are two ways for doing this:

#      2.1) By using the class property 'inputs':

#       We will use the operator instantiated above "my_operator"
        my_operator.inputs.pinName(expectedDataType)

#       An example with the "my_displacement_operator":
#       The displacement operator is a class that requires at least the pin named 'data_sources'.
#       (The explanation on how to create an object o type 'data_sources' is in the following example). Here this
#       object will hypothetically be instantiated with the name "my_displacement_ds"
        my_displacement_operator.inputs.data_sources(my_displacement_ds)

#      2.2) By using the class parameters when instantiating the operator:

#       We will use the 1.1 method
        from ansys.dpf.core import operators as ops
        my_operator = ops.subpackageAttribute.operatorAttribute(parameterName=expectedDataType)

#       An example with the displacement operator
#       The displacement operator is a class that requires at least the pin named 'data_sources'.
#       (The explanation on how to create an object o type 'data_sources' is in the following example). Here this
#       object will hypothetically be instantiated with the name "my_displacement_ds"
        from ansys.dpf.core import operators as ops
        my_displacement_operator=ops.result.displacement(data_sources=my_displacement_ds)

# ---------------------------------------------------------------------------------------------------------------------
# 3) Get the computed result from the output pin. There are two ways for doing this:

#      3.1) By using the class property 'outputs':

#       We will use the operator instantiated above "my_operator"
        my_operator.outputs.pinName()

#       An example with the "my_displacement_operator":
#       The displacement operator is a class that has one output pin named 'fields_container'
        my_displacement_operator.outputs.fields_container()

#      3.2) By evaluating the operator when instantiating it with the 'eval()' method

#       We will use the 1.1 method
        from ansys.dpf.core import operators as ops
        my_operator = ops.subpackageAttribute.operatorAttribute(parameterName=expectedDataType).eval()
#       or
        from ansys.dpf.core import operators as ops
        my_operator = ops.subpackageAttribute.operatorAttribute(parameterName=expectedDataType)
        my_operator.eval()

#       An example with the "my_displacement_operator":
#       The displacement operator is a class that has one output pin named 'fields_container'
#       (The explanation on how to create an object o type 'data_sources' is in the following example). Here this
#       object will hypothetically be instantiated with the name "my_displacement_ds"
        from ansys.dpf.core import operators as ops
        my_displacement_operator=ops.result.displacement(data_sources=my_displacement_ds).eval()
#       or
        from ansys.dpf.core import operators as ops
        my_displacement_operator=ops.result.displacement(data_sources=my_displacement_ds)
        my_displacement_operator.eval()

# ---------------------------------------------------------------------------------------------------------------------
# 4) Chain operators. You can attach one operator’s outputs to another operator’s inputs to chain operators together.
# This allows you to create a workflow to create more complex operations and customizable results.DPF evaluates each
# operator only when the final operator is evaluated and the data is requested. So the order that you connect the
# operators is important. There are three ways for doing this:

#      4.1) By using the 'connect()' method derived from the 'Inputs' class, that the outputs pin of one operator to the inputs
#      pin of another operator

#       We will use the operator instantiated above "my_operator" and a new "my_other_operator"
        my_other_operator.inputs.connect(my_operator.outputs) # Here the output of "my_operator" is connected
#                                                               to the "my_other_operator" input
#       or
        my_other_operator.inputs.inputPinName.connect(my_operator.outputs.outputPinName)
#  While this last approach is more verbose, it can be useful for operators having several matching inputs or outputs.

#       An example with the "my_displacement_operator":
#       We will use the case where we want to find the maximum value of the displacement field. So we instantiate an
#       operator named "my_min_max_operator"
        my_min_max_operator.inputs.connect(my_displacement_operator.outputs)
#       or
        my_min_max_operator.inputs.field.connect(my_displacement_operator.outputs.fields_container)

#      4.2) By using the 'connect()' method from the own operator class. The difference here is that the input
#      pin number needs to be specified

#       We will use the operator instantiated above "my_operator" and a new "my_other_operator"
        my_other_ooperator.connect(pin=inputPinNumber,inpt=my_operator,pin_out=outputPinNumber)
#       Here the output of the "my_operator" is being connected to the "my_other_operator" input. So the inputPinNumber
#       is the number o the "my_other_operator" pin where you tuo connect the output pin identified with "outputPinNumber"
#       from "my_operator"

#       An example with the "my_displacement_operator":
#       We will use the case where we want to find the maximum value of the displacement field. So we instantiate an
#       operator named "my_min_max_operator"
        my_min_max_operator.connect(pin=0, input=my_displacement_operator, pin_out=0)

#      4.3) By directly instantiating the new operator with the other operator as a parameter:

#       We will use the 1.1 method
        from ansys.dpf.core import operators as ops
        my_other_operator = ops.subpackageAttribute.operatorAttribute(parameterName=my_operator)

#       An example with the "my_displacement_operator":
#       We will use the case where we want to find the maximum value of the displacement field.
        from ansys.dpf.core import operators as ops
        my_min_max_operator = ops.min_max.min_max(my_displacement_operator)

######################################################################################################################
# # ~~~~~~~ THE OPERATORS ~~~~~~~ # #

# DPF provides three main types of operators:
# 1- Operators for importing or reading data
# 2- Operators for transforming data
# 3- Operators for exporting data
#
# Those operators are defined in the subpackages and submodules of DPF. Each operator is of type Operator.

# When post-processing a simulation with DPF the typical basic steps are:
# 1- Load the result File
# 2- Acces the data
# 3- Transform the data
# 4- Display the new results
# 5- Export the new results

# The following examples will describe in details how to use each groupe of operator