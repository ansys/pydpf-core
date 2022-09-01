"""Build static source operators from DPF server."""
import copy
import os
from datetime import datetime
from textwrap import wrap

import black
import chevron
from ansys.dpf import core as dpf
from ansys.dpf.core import common
from ansys.dpf.core.dpf_operator import available_operator_names
from ansys.dpf.core.outputs import _make_printable_type
from ansys.dpf.core.mapping_types import map_types_to_python


dpf.start_local_server(config=dpf.AvailableServerConfigs.LegacyGrpcServer)

def build_docstring(specification):
    """Used to generate class docstrings."""
    docstring = ""
    if specification.description:
        docstring += "\n".join(
            wrap(specification.description, subsequent_indent="    ")
        )
        docstring += "\n\n"
    docstring = docstring.rstrip()
    return docstring.replace('"', "'")


def map_types(cpp_types):
    """Map C++ object types to Python types."""
    types = []
    # These types don't get mapped to Python types
    types_to_ignore = ["vector", "umap", "enum"]
    for cpp_type in cpp_types:
        if any(type_name in cpp_type for type_name in types_to_ignore):
            continue
        else:
            types.append(map_types_to_python[cpp_type])
    return types


def update_type_names_for_ellipsis(type_names):
    # Remove vector and umap types from the Python type
    new_types = []
    for name in type_names:
        if name == "vector<double>" or name == "vector<int32>":
            new_types.append(name)
        elif "vector" not in name and "umap" not in name:
            new_types.append(name)
    return new_types


def build_pin_data(pins, output=False):
    """Build pin data for use within template."""
    pin_ids = [pin for pin in pins]
    pin_ids.sort()

    data = []
    for id in pin_ids:
        specification = pins[id]

        type_names = specification.type_names
        if specification.ellipsis:
            type_names = update_type_names_for_ellipsis(type_names)
        docstring_types = map_types(type_names)
        parameter_types = " or ".join(docstring_types)
        parameter_types = "\n".join(
            wrap(parameter_types, subsequent_indent="        ", width=60)
        )

        pin_name = specification.name
        pin_name = pin_name.replace("<", "_")
        pin_name = pin_name.replace(">", "_")

        main_type = docstring_types[0] if len(docstring_types) >= 1 else ""
        built_in_types = ("int", "double", "string", "bool", "float", "str")

        # Case where output pin has multiple types.
        multiple_types = len(type_names) >= 2
        printable_type_names = type_names
        if multiple_types and output:
            printable_type_names = [_make_printable_type(name) for name in type_names]

        pin_data = {
            "id": id,
            "name": pin_name,
            "pin_name": pin_name, # Base pin name, without numbers for when pin is ellipsis
            "has_types": len(type_names) >= 1,
            "multiple_types": multiple_types,
            "printable_type_names": printable_type_names,
            "types": type_names,
            "types_for_docstring": parameter_types,
            "main_type": main_type,
            "built_in_main_type": main_type in built_in_types,
            "optional": specification.optional,
            "document": "\n".join(
                wrap(
                    specification.document.capitalize().lstrip(' '),
                    subsequent_indent="        ",
                    width=45,
                )
            ),
            "ellipsis": 0 if specification.ellipsis else -1,
        }

        if specification.ellipsis:
            # Create two pins for ellipsis field with exactly the same
            # properties, just different names, ids, and ellipsis values
            pin_data["name"] = pin_name + "1"
            data.append(pin_data)

            second_pin_data = copy.deepcopy(pin_data)
            second_pin_data["name"] = pin_name + "2"
            second_pin_data["id"] = id + 1
            second_pin_data["ellipsis"] = 1
            data.append(second_pin_data)
        else:
            data.append(pin_data)

    return data


def build_operator(
    specification, operator_name, class_name, capital_class_name, category
):

    input_pins = []
    if specification.inputs:
        input_pins = build_pin_data(specification.inputs)

    output_pins = []
    if specification.outputs:
        output_pins = build_pin_data(specification.outputs, output=True)
    multiple_output_types = any(pin["multiple_types"] for pin in output_pins)

    docstring = build_docstring(specification)

    specification_description = "\n".join(
        wrap(specification.description, subsequent_indent="            ")
    )

    date_and_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    data = {
        "operator_name": operator_name,
        "class_name": class_name,
        "class_name_underlining": len(class_name)*"=",
        "capital_class_name": capital_class_name,
        "docstring": docstring,
        "specification_description": specification_description,
        "input_pins": input_pins,
        "output_pins": output_pins,
        "outputs": len(output_pins) >= 1,
        "multiple_output_types": multiple_output_types,
        "category": category,
        "date_and_time": date_and_time,
    }

    this_path = os.path.dirname(os.path.abspath(__file__))
    mustache_file = os.path.join(this_path, "operator.mustache")
    with open(mustache_file, "r") as f:
        cls = chevron.render(f, data)

    return black.format_str(cls, mode=black.FileMode())


if __name__ == "__main__":
    this_path = os.path.dirname(os.path.abspath(__file__))

    available_operators = available_operator_names()

    succeeded = 0
    for operator_name in available_operators:
        specification = dpf.Operator.operator_specification(operator_name)

        category = specification.properties.get("category", "")
        if not category:
            raise (f"Category not defined for operator {operator_name}.")
        scripting_name = specification.properties.get("scripting_name", "")

        # Make directory for new category
        category_path = os.path.join(this_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        # Clean up scripting name
        if scripting_name == "":
            scripting_name = operator_name
        if "::" in scripting_name:
            scripting_name = scripting_name.split("::")[-1]
        if "." in scripting_name:
            scripting_name = scripting_name.split(".")[-1]

        # Get python class name from scripting name
        capital_class_name = common._snake_to_camel_case(scripting_name)

        # Write to operator file
        operator_file = os.path.join(category_path, scripting_name + ".py")
        with open(operator_file, "w") as f:
            try:
                operator_str = build_operator(
                    specification,
                    operator_name,
                    scripting_name,
                    capital_class_name,
                    category,
                )
                exec(operator_str)
                f.write(operator_str)
                succeeded += 1
            except SyntaxError as e:
                error_message = (
                    f"Unable to generate {operator_name}, {scripting_name}, {capital_class_name}.\n"
                    f"Error message: {e}\n"
                )
                with open(os.path.join(this_path, "failures.txt"), "w") as error_file:
                    error_file.write(error_message)
                    error_file.write(f"Class: {operator_str}")
                print(error_message)

    print(f"Generated {succeeded} out of {len(available_operators)}")
    dpf.SERVER.shutdown()
