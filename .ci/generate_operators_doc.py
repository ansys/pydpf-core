import argparse
from pathlib import Path

from jinja2 import Template

from ansys.dpf import core as dpf
from ansys.dpf.core.changelog import Changelog
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

    # Retrieve version and changelog using the Changelog class
    if hasattr(spec, "changelog") and isinstance(spec.changelog, dpf.GenericDataContainer):
        changelog_gdc = spec.changelog
        changelog = Changelog(gdc=changelog_gdc, server=server)
        last_version = changelog.last_version
        changelog_entries = [
            f"Version {str(version)}: {changelog[version]}" for version in changelog.versions
        ]
    else:
        last_version = "0.0.0"
        changelog_entries = [f"Version {last_version}: Initial release."]

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
        "version": str(last_version),  # Include last version in scripting_info
        "changelog": changelog_entries,  # Include all changelog entries
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
    scripting_name = operator_info["scripting_info"]["scripting_name"]
    category = operator_info["scripting_info"]["category"]
    if scripting_name:
        file_name = scripting_name
    else:
        file_name = operator_name
    if "::" in file_name:
        file_name = file_name.replace("::", "_")
    if not include_private and operator_info["exposure"] == "private":
        return
    script_path = Path(__file__)
    root_dir = script_path.parent.parent
    template_dir = Path(root_dir) / "doc" / "source" / "operators_doc" / "operator-specifications"
    category_dir = Path(template_dir) / category
    if not category_dir.exists() and category is not None:
        category_dir.mkdir()
    if category is not None:
        file_dir = category_dir
    else:
        file_dir = template_dir
    with Path.open(Path(template_dir) / "operator_doc_template.md", "r") as file:
        template = Template(file.read())

    output = template.render(operator_info)
    with Path.open(Path(file_dir) / f"{file_name}.md", "w") as file:
        file.write(output)


def generate_toc_tree(docs_path):
    # Target the operator-specifications folder for iteration
    # operator_specs_path = docs_path / "operator-specifications"
    data = []
    for folder in docs_path.iterdir():
        if folder.is_dir():  # Ensure 'folder' is a directory
            category = folder.name
            operators = []  # Reset operators for each category
            for file in folder.iterdir():
                if (
                    file.is_file() and file.suffix == ".md"
                ):  # Ensure 'file' is a file with .md extension
                    file_name = file.name
                    file_path = f"{category}/{file_name}"
                    operator_name = file_name.replace("_", " ").replace(".md", "")
                    operators.append({"operator_name": operator_name, "file_path": file_path})
            data.append({"category": category, "operators": operators})

    # Render the Jinja2 template
    template_path = docs_path / "toc_template.j2"
    with Path.open(template_path, "r") as template_file:
        template = Template(template_file.read())
    output = template.render(data=data)  # Pass 'data' as a named argument

    # Write the rendered output to toc.yml at the operators_doc level
    # toc_path = docs_path / "toc.yml"
    with Path.open(docs_path / "toc.yml", "w") as file:
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

    docs_path = (
        Path(__file__).parent.parent
        / "doc"
        / "source"
        / "operators_doc"
        / "operator-specifications"
    )
    print(docs_path)
    generate_toc_tree(docs_path)


if __name__ == "__main__":
    main()
