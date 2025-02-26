import argparse
from pathlib import Path

from jinja2 import Template

from ansys.dpf import core as dpf
from ansys.dpf.core.core import load_library
from ansys.dpf.core.dpf_operator import available_operator_names


def initialize_server(ansys_path=None, include_composites=False, include_sound=False):
    server = dpf.start_local_server(ansys_path=ansys_path)
    print(f"Ansys Path: {server.ansys_path}")
    print(f"Server Info: {server.info}")
    print(f"Server Context: {server.context}")
    print(f"Server Config: {server.config}")
    print(f"Server version: {dpf.global_server().version}")
    if include_composites:
        print("Loading Composites Plugin")
        load_library(
            Path(server.ansys_path)
            / "dpf"
            / "plugins"
            / "dpf_composites"
            / "composite_operators.dll"
        )
    if include_sound:
        print("Loading Acoustics Plugin")
        load_library(Path(server.ansys_path) / "Acoustics" / "SAS" / "ads" / "dpf_sound.dll")
    return server


def fetch_doc_info(server, operator_name):
    spec = dpf.Operator.operator_specification(op_name=operator_name, server=server)
    input_info = []
    output_info = []
    configurations_info = []
    for input_pin in spec.inputs:
        input = spec.inputs[input_pin]
        input_info.append(
            {
                "pin_number": input_pin,
                "name": input.name,
                "types": [str(t) for t in input._type_names],
                "document": input.document,
                "optional": input.optional,
            }
        )
    for output_pin in spec.outputs:
        output = spec.outputs[output_pin]
        output_info.append(
            {
                "pin_number": output_pin,
                "name": output.name,
                "types": [str(t) for t in output._type_names],
                "document": output.document,
                "optional": output.optional,
            }
        )
    for configuration_key in spec.config_specification:
        configuration = spec.config_specification[configuration_key]
        configurations_info.append(
            {
                "name": configuration.name,
                "types": [str(t) for t in configuration.type_names],
                "document": configuration.document,
                "default_value": configuration.default_value_str,
            }
        )
    properties = spec.properties
    plugin = properties.pop("plugin", "N/A")

    category = properties.pop("category", None)

    scripting_name = properties.pop("scripting_name", None)
    if category and scripting_name:
        full_name = category + "." + scripting_name
    else:
        full_name = None

    user_name = properties.pop("user_name", operator_name)

    op_friendly_name = user_name
    if category:
        op_friendly_name = category + ":" + op_friendly_name

    license = properties.pop("license", "None")

    exposure = properties.pop("exposure", "private")
    scripting_info = {
        "category": category,
        "plugin": plugin,
        "scripting_name": scripting_name,
        "full_name": full_name,
        "internal_name": operator_name,
        "license": license,
    }
    return {
        "operator_name": op_friendly_name,
        "operator_description": spec.description,
        "inputs": input_info,
        "outputs": output_info,
        "configurations": configurations_info,
        "scripting_info": scripting_info,
        "exposure": exposure,
    }


def get_plugin_operators(server, plugin_name):
    operators = available_operator_names(server)
    plugin_operators = []
    for operator_name in operators:
        spec = dpf.Operator.operator_specification(op_name=operator_name, server=server)
        if "plugin" in spec.properties and spec.properties["plugin"] == plugin_name:
            plugin_operators.append(operator_name)
    return plugin_operators


def generate_operator_doc(server, operator_name, include_private):
    operator_info = fetch_doc_info(server, operator_name)
    if not include_private and operator_info["exposure"] == "private":
        return
    script_path = Path(__file__)
    root_dir = script_path.parent.parent
    template_dir = Path(root_dir) / "doc" / "source" / "operators_doc"
    with Path.open(Path(template_dir) / "operator_doc_template.md", "r") as file:
        template = Template(file.read())

    output = template.render(operator_info)
    if "::" in operator_name:
        operator_name = operator_name.replace("::", "_")
    with Path.open(Path(template_dir) / f"{operator_name}.md", "w") as file:
        file.write(output)


def main():
    parser = argparse.ArgumentParser(description="Fetch available operators")
    parser.add_argument("--plugin", help="Filter operators by plugin")
    parser.add_argument(
        "--ansys_path", default=None, help="Path to Ansys DPF Server installation directory"
    )
    parser.add_argument("--include_private", action="store_true", help="Include private operators")
    parser.add_argument(
        "--include_composites", action="store_true", help="Include composites operators"
    )
    parser.add_argument("--include_sound", action="store_true", help="Include sound operators")
    args = parser.parse_args()
    desired_plugin = args.plugin

    server = initialize_server(args.ansys_path, args.include_composites, args.include_sound)
    if desired_plugin is None:
        operators = available_operator_names(server)
    else:
        operators = get_plugin_operators(server, desired_plugin)
    for operator_name in operators:
        generate_operator_doc(server, operator_name, args.include_private)


if __name__ == "__main__":
    main()
