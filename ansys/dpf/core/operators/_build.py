"""Build static source operators from DPF server."""
import os
from datetime import datetime
from textwrap import wrap

import black
import chevron
from ansys.dpf import core as dpf
from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.operators._operators_list import operators

map_types_to_python = dict(map_types_to_python)
map_types_to_python["b"] = "bool"

def build_docstring(op):
    """Used to generate class docstrings."""
    txt = ""
    if op._description:
        txt += "\n".join(wrap(op._description, subsequent_indent="    "))
        txt += "\n\n"
    if op.inputs:
        line = [" ", str(op.inputs)]
        txt += "{:^3} {:^21}".format(*line)
        txt += "\n"
    if op.outputs:
        txt += "\n"
        line = [" ", str(op.outputs)]
        txt += "{:^3} {:^21}".format(*line)
    txt = txt.rstrip()
    return txt.replace('"', "'")

def map_types(cpp_types):
    """Map C++ object types to Python types."""
    types = []
    for cpp_type in cpp_types:
        if cpp_type in map_types_to_python:
            types.append(map_types_to_python[cpp_type])
        else:
            types.append(cpp_type)
    return types

def build_pin_data(pins):
    """Build pin data for use within template."""
    pin_ids = [pin for pin in pins]
    pin_ids.sort()

    data = []
    optional = []
    required = []
    for id in pin_ids:
        specification = pins[id]
        docstring_types = map_types(specification.type_names)
        parameter_types = " or ".join(docstring_types)
        parameter_types = "\n".join(wrap(parameter_types, subsequent_indent="        ", width=60))
        data.append(
            {
                "id": id,
                "name": specification.name,
                "types": specification.type_names,
                "types_for_docstring": parameter_types,
                "main_type": docstring_types[0] if len(docstring_types) >= 1 else "",
                "optional": specification.optional,
                "document": "\n".join(
                    wrap(
                        specification.document.capitalize(),
                        subsequent_indent="        ",
                        width=45
                    )
                ),
                "ellipsis": 0 if specification.ellipsis else -1,
            }
        )
        if specification.optional:
            optional.append(specification.name)
        else:
            required.append(specification.name)
    return data, required, optional

def build_operator(name, class_name, snake_case_class_name, category):
    operator = dpf.Operator(name)

    input_pins = []
    required = []
    optional = []
    if operator.inputs:
        input_pins, required, optional = build_pin_data(operator.inputs._dict_inputs)

    output_pins = []
    if operator.outputs:
        output_pins = build_pin_data(operator.outputs._dict_outputs)[0]

    docstring = build_docstring(operator)

    # Init parameters
    init_parameters = []
    if required:
        init_parameters.extend(required)
    if optional:
        init_parameters.extend([f"{param}=None" for param in optional])
    init_parameters = ", ".join(init_parameters)

    specification_description = "\n".join(
        wrap(operator._description, subsequent_indent="            ")
    )

    date_and_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    data = {
        "class_name": class_name,
        "snake_case_class_name": snake_case_class_name,
        "docstring": docstring,
        "init_parameters": init_parameters,
        "specification_description": specification_description,
        "input_pins": input_pins,
        "output_pins": output_pins,
        "category": category,
        "date_and_time": date_and_time,
    }

    this_path = os.path.dirname(os.path.abspath(__file__))
    mustache_file = os.path.join(this_path, "operator_template.mustache")
    with open(mustache_file, "r") as f:
        cls = chevron.render(f, data)

    return black.format_str(cls, mode=black.FileMode())
    # return cls

if __name__ == "__main__":
    this_path = os.path.dirname(os.path.abspath(__file__))

    # Create file per operator and organize into directories
    # per category
    succeeded = 0
    for operator_name, operator_data in operators.items():
        # Make directory for new category
        category = operator_data["category"]
        category_path = os.path.join(this_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        # Clean up short name
        short_name = operator_data["short_name"]
        if short_name == "":
            short_name = operator_name
        if "::" in short_name:
            short_name = short_name.split("::")[-1]
        if "." in short_name:
            short_name = short_name.split(".")[-1]

        # Get python class name fron short name
        split_name = short_name.split("_")
        class_name = "".join([part.capitalize() for part in split_name])

        # Write to operator file
        operator_file = os.path.join(category_path, short_name + ".py")
        with open(operator_file, "w") as f:
            try:
                operator_str = build_operator(operator_name, class_name, short_name, category)
                exec(operator_str)
                f.write(operator_str)
                succeeded += 1
            except SyntaxError as e:
                error_message = (
                    f"Unable to generate {operator_name}, {short_name}, {class_name}.\n"
                    f"Error message: {e}\n"
                )
                with open(os.path.join(this_path, "failures.txt"), "w") as error_file:
                    error_file.write(error_message)
                    error_file.write(f"Class: {operator_str}")
                print(error_message)

    print(f"Generated {succeeded} out of {len(operators)}")
    dpf.SERVER.shutdown()
