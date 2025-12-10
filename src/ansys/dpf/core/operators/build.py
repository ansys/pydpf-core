"""Build static source operators from DPF server."""

import copy
from datetime import datetime
import importlib
import inspect
import os
import pkgutil
from textwrap import wrap
import time
from typing import Optional

import black
import chevron

from ansys.dpf import core as dpf
from ansys.dpf.core import common
from ansys.dpf.core.dpf_operator import available_operator_names
from ansys.dpf.core.mapping_types import map_types_to_python
from ansys.dpf.core.operators.translator import Markdown2RstTranslator
from ansys.dpf.core.outputs import _make_printable_type

# Operator internal names to call if first name is not available
# Allows deprecating internal names associated to public Python operator modules
OPERATOR_ALIASES = {
    "support_provider_cyclic": "mapdl::rst::support_provider_cyclic",
    "NMISC": "mapdl::nmisc",
    "SMISC": "mapdl::smisc",
    "result_provider": "custom",
    "CS": "mapdl::rst::CS",
    "MCF": "U",
}

BUILT_IN_TYPES = ("int", "double", "string", "bool", "float", "str", "dict")

TYPES_WITHOUT_PYTHON_IMPLEMENTATION = (
    "Materials",
    "AnsDispatchHolder",
    "Stream",
    "AbstractFieldSupport",
    "AnyCollection",
    "CustomTypeFieldsContainer",
    "MeshSelectionManager",
    "Class Dataprocessing::Dpftypecollection<Class Dataprocessing::Cpropertyfield>",
    "Struct Iansdispatch",
    "PropertyFieldsContainer",
    "Class Dataprocessing::Crstfilewrapper",
    "Char",
)


def find_class_origin(class_name: str, package_name: str = "ansys.dpf.core") -> Optional[str]:
    """Find the fully qualified import path where a class is originally defined."""
    try:
        pkg = importlib.import_module(package_name)
    except ModuleNotFoundError:
        raise ValueError(f"Package '{package_name}' not found")

    # ensure we’re working with a real package, not a module
    if not hasattr(pkg, "__path__"):
        raise ValueError(f"'{package_name}' is not a package")

    # include the top-level package itself
    modules_to_check = [package_name]

    # add all submodules of the package
    for modinfo in pkgutil.walk_packages(pkg.__path__, prefix=f"{package_name}."):
        modules_to_check.append(modinfo.name)

    # search through all modules
    for mod_name in modules_to_check:
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            # skip broken or unimportable modules
            continue

        cls = getattr(mod, class_name, None)
        if cls is None or not inspect.isclass(cls):
            continue

        # get the module where the class is actually defined
        defining_module = inspect.getmodule(cls)
        if defining_module and defining_module.__name__ == mod_name:
            return f"{defining_module.__name__}"

    return None


def build_docstring(specification_description):
    """Used to generate class docstrings."""
    docstring = ""
    if specification_description:
        docstring += specification_description.replace("\n", "\n    ")
    return docstring


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
        # Process type_names for property_fields_container --> property_fields_collection
        type_names = [
            name.replace("property_fields_container", "property_fields_collection")
            for name in type_names
        ]

        derived_class_type_name = specification.name_derived_class

        if specification.ellipsis:
            type_names = update_type_names_for_ellipsis(type_names)
        docstring_types = map_types(type_names)
        parameter_types = " or ".join(docstring_types)
        parameter_types = "\n".join(wrap(parameter_types, subsequent_indent="      ", width=60))

        type_list_for_annotation = " | ".join(
            docstring_type
            for docstring_type in docstring_types
            if docstring_type
            not in TYPES_WITHOUT_PYTHON_IMPLEMENTATION  # Types without python implementations can't be typechecked
        )

        pin_name = specification.name
        pin_name = pin_name.replace("<", "_")
        pin_name = pin_name.replace(">", "_")
        # Process pin name for property_fields_container --> property_fields_collection
        pin_name = pin_name.replace("property_fields_container", "property_fields_collection")

        main_type = docstring_types[0] if len(docstring_types) >= 1 else ""

        # Case where output pin has multiple types.
        multiple_types = len(type_names) >= 2
        printable_type_names = type_names
        if multiple_types and output:
            printable_type_names = [_make_printable_type(name) for name in type_names]

        document = specification.document
        document_pin_docstring = document.replace("\n", "\n        ")

        pin_data = {
            "id": id,
            "name": pin_name,
            "pin_name": pin_name,  # Base pin name, without numbers for when pin is ellipsis
            "has_types": len(type_names) >= 1,
            "has_derived_class": len(derived_class_type_name) >= 1,
            "multiple_types": multiple_types,
            "printable_type_names": printable_type_names,
            "types": type_names,
            "derived_type_name": derived_class_type_name,
            "docstring_types": docstring_types,
            "type_list_for_annotation": type_list_for_annotation,
            "types_for_docstring": parameter_types,
            "main_type": main_type,
            "built_in_main_type": main_type in BUILT_IN_TYPES,
            "optional": specification.optional,
            "document": document,
            "document_pin_docstring": document_pin_docstring,
            "ellipsis": 0 if specification.ellipsis else -1,
            "has_aliases": len(specification.aliases) > 0,
            "aliases_list": [dict([("alias", alias)]) for alias in specification.aliases],
            "aliases": str(specification.aliases),
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
    specification,
    operator_name,
    class_name,
    capital_class_name,
    category,
    specification_description,
):
    input_pins = []
    if specification.inputs:
        input_pins = build_pin_data(specification.inputs)
    has_input_aliases = any(len(pin["aliases_list"]) > 0 for pin in input_pins)

    output_pins = []
    if specification.outputs:
        output_pins = build_pin_data(specification.outputs, output=True)
    multiple_output_types = any(pin["multiple_types"] for pin in output_pins)
    has_output_aliases = any(len(pin["aliases_list"]) > 0 for pin in output_pins)

    # Process specification description for property_fields_container --> property_fields_collection
    specification_description = specification_description.replace("property_fields_container", "property_fields_collection")
    specification_description = specification_description.replace("PropertyFieldsContainer", "PropertyFieldsCollection")

    docstring = build_docstring(specification_description)

    date_and_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    annotation_import_types = set()
    for input_pin in input_pins:
        annotation_import_types.update(input_pin["docstring_types"])
    for output_pin in output_pins:
        # Output pins with multiple types can't be annotated with current operators design
        if output_pin["multiple_types"]:
            continue
        annotation_import_types.update(output_pin["docstring_types"])
    annotation_import_list = []
    for annotation_type in annotation_import_types:
        if annotation_type in BUILT_IN_TYPES + TYPES_WITHOUT_PYTHON_IMPLEMENTATION:
            continue
        definition_location = find_class_origin(annotation_type)
        annotation_import_list.append(
            {
                "class_name": annotation_type,
                "definition_location": definition_location,
            }
        )
    annotation_import_list.sort(key= lambda x: x["class_name"].split("ansys.dpf.core.")[-1])
    non_empty_annotation_import_list = bool(annotation_import_list)

    data = {
        "operator_name": operator_name,
        "class_name": class_name,
        "class_name_underlining": len(class_name) * "=",
        "capital_class_name": capital_class_name,
        "docstring": docstring,
        "specification_description": specification_description,
        "annotation_import_list": annotation_import_list,
        "non_empty_annotation_import_list": non_empty_annotation_import_list,
        "input_pins": input_pins,
        "output_pins": output_pins,
        "outputs": len(output_pins) >= 1,
        "multiple_output_types": multiple_output_types,
        "category": category,
        "date_and_time": date_and_time,
        "has_input_aliases": has_input_aliases,
        "has_output_aliases": has_output_aliases,
        "has_internal_name_alias": operator_name in OPERATOR_ALIASES.keys(),
        "internal_name_alias": OPERATOR_ALIASES.get(operator_name),
    }

    this_path = os.path.dirname(os.path.abspath(__file__))
    mustache_file = os.path.join(this_path, "operator.mustache")
    with open(mustache_file, "r") as f:
        cls = chevron.render(f, data)
    try:
        return black.format_str(cls, mode=black.FileMode())
    except Exception as e:
        print(f"{operator_name=}")
        raise e


def build_operators():
    print(f"Generating operators for server {dpf.SERVER.version} ({dpf.SERVER.ansys_path})")
    time_0 = time.time()

    this_path = os.path.dirname(os.path.abspath(__file__))

    available_operators = available_operator_names()

    print(f"{len(available_operators)} operators found to generate.")

    succeeded = 0
    done = 0
    hidden = 0
    # List of hidden operators to still expose for retro-compatibility
    # until they are fully deprecated
    hidden_to_expose = [  # Use internal names
        "change_fc",
        "dot",
        "dot_tensor",
        "scale_by_field",
        "scale_by_field_fc",
        "invert",
        "invert_fc",
    ]
    categories = set()

    translator = Markdown2RstTranslator()

    for operator_name in available_operators:
        if succeeded == done + 100:
            done += 100
            print(f"{done} operators done...")
        specification = dpf.Operator.operator_specification(operator_name)

        if (
            specification.properties["exposure"] in ["hidden", "private"]
            and operator_name not in hidden_to_expose
        ):
            hidden += 1
            continue

        category = specification.properties.get("category", "")
        categories.add(category)
        if not category:
            raise ValueError(f"Category not defined for operator {operator_name}.")
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

        # Convert Markdown descriptions to RST
        specification_description = translator.convert(specification.description)

        # Write to operator file
        operator_file = os.path.join(category_path, scripting_name + ".py")
        with open(operator_file, "w", encoding="utf-8", newline="\u000a") as f:
            operator_str = scripting_name
            try:
                operator_str = build_operator(
                    specification,
                    operator_name,
                    scripting_name,
                    capital_class_name,
                    category,
                    specification_description,
                )
                exec(operator_str, globals())
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

    print(f"Generated {succeeded} out of {len(available_operators)} ({hidden} hidden)")

    # Create __init__.py files
    print(f"Generating __init__.py files...")
    with open(
        os.path.join(this_path, "__init__.py"), "w", encoding="utf-8", newline="\u000a"
    ) as main_init:
        for category in sorted(categories):
            # Add category to main init file imports
            main_init.write(f"from . import {category}\n")
            # Create category init file
            category_operators = os.listdir(os.path.join(this_path, category.split(".")[0]))
            with open(
                os.path.join(this_path, category, "__init__.py"),
                "w",
                encoding="utf-8",
                newline="\u000a",
            ) as category_init:
                for category_operator in sorted(category_operators):
                    operator_name = category_operator.split(".")[0]
                    category_init.write(f"from .{operator_name} import {operator_name}\n")

    if succeeded == len(available_operators) - hidden:
        print("Success")
        print(f"Took {time.time() - time_0}")
        exit(0)
    else:
        print("Terminated with errors")
        exit(1)


if __name__ == "__main__":
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    dpf.start_local_server(config=dpf.AvailableServerConfigs.LegacyGrpcServer)
    build_operators()
    dpf.SERVER.shutdown()
