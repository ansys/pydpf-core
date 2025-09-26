# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Generation of Markdown documentation source files for operators of a given DPF installation."""

from __future__ import annotations

import argparse
from os import PathLike
from pathlib import Path

from ansys.dpf import core as dpf
from ansys.dpf.core.changelog import Changelog
from ansys.dpf.core.core import load_library
from ansys.dpf.core.dpf_operator import available_operator_names


class Jinja2ImportError(ModuleNotFoundError):
    """Error raised when Jinja2 could not be imported during operator documentation generation."""

    def __init__(
        self,
        msg="To generate Markdown documentation of operators, please install jinja2 with:\n"
        "pip install jinja2",
    ):
        ModuleNotFoundError.__init__(self, msg)


try:
    import jinja2
except ModuleNotFoundError:
    raise Jinja2ImportError


def initialize_server(
    ansys_path: str | PathLike = None, include_composites: bool = False, include_sound: bool = False
) -> dpf.AnyServerType:
    """Initialize a DPF server for a given installation folder by loading required plugins.

    Parameters
    ----------
    ansys_path:
        Path to the DPF installation to use to start a server.
    include_composites:
        Whether to generate documentation for operators of the Composites plugin.
    include_sound:
        Whether to generate documentation for operators of the Sound DPF plugin.

    Returns
    -------
    server:
        A running DPF server to generate operator documentation for.

    """
    server = dpf.start_local_server(ansys_path=ansys_path)
    print(server.plugins)
    print(f"Ansys Path: {server.ansys_path}")
    print(f"Server Info: {server.info}")
    print(f"Server Context: {server.context}")
    print(f"Server Config: {server.config}")
    print(f"Server version: {dpf.global_server().version}")
    if include_composites:
        print("Loading Composites Plugin")
        load_library(
            filename=Path(server.ansys_path)
            / "dpf"
            / "plugins"
            / "dpf_composites"
            / "composite_operators.dll",
            name="composites",
        )
    if include_sound:
        print("Loading Acoustics Plugin")
        load_library(
            filename=Path(server.ansys_path) / "Acoustics" / "SAS" / "ads" / "dpf_sound.dll",
            name="sound",
        )
    print(f"Loaded plugins: {list(server.plugins.keys())}")
    return server


def fetch_doc_info(server: dpf.AnyServerType, operator_name: str) -> dict:
    """Fetch information about the specifications of a given operator.

    Parameters
    ----------
    server:
        A DPF server to query the specifications of the operator.
    operator_name:
        The name of the operator of interest.

    Returns
    -------
    doc_info:
        Information about the operator structured for use with the documentation template.

    """
    spec = dpf.Operator.operator_specification(op_name=operator_name, server=server)
    input_info = []
    output_info = []
    configurations_info = []
    for input_pin in spec.inputs:
        input_pin_info = spec.inputs[input_pin]
        input_info.append(
            {
                "pin_number": input_pin,
                "name": input_pin_info.name,
                "types": [str(t) for t in input_pin_info._type_names],
                "document": input_pin_info.document,
                "optional": input_pin_info.optional,
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

    license_type = properties.pop("license", "None")

    exposure = properties.pop("exposure", "private")
    scripting_info = {
        "category": category,
        "plugin": plugin,
        "scripting_name": scripting_name,
        "full_name": full_name,
        "internal_name": operator_name,
        "license": license_type,
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


def get_plugin_operators(server: dpf.AnyServerType, plugin_name: str) -> list[str]:
    """Get the list of operators for a given plugin.

    Parameters
    ----------
    server:
        DPF server to query for the list of operators.
    plugin_name:
        Name of the plugin of interest.

    Returns
    -------
    operator_list:
        List of names of operators available on the server for the given plugin.

    """
    operators = available_operator_names(server)
    plugin_operators = []
    for operator_name in operators:
        spec = dpf.Operator.operator_specification(op_name=operator_name, server=server)
        if "plugin" in spec.properties and spec.properties["plugin"] == plugin_name:
            plugin_operators.append(operator_name)
    return plugin_operators


def generate_operator_doc(
    server: dpf.AnyServerType, operator_name: str, include_private: bool, output_path: Path
):
    """Write the Markdown documentation page for a given operator on a given DPF server.

    Parameters
    ----------
    server:
        DPF server of interest.
    operator_name:
        Name of the operator of interest.
    include_private:
        Whether to generate the documentation if the operator is private.
    output_path:
        Path to write the operator documentation at.

    """
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
    template_path = Path(__file__).parent / "operator_doc_template.md"
    spec_folder = output_path / "operator-specifications"
    category_dir = spec_folder / category
    spec_folder.mkdir(parents=True, exist_ok=True)
    if category is not None:
        category_dir.mkdir(parents=True, exist_ok=True)  # Ensure all parent directories are created
        file_dir = category_dir
    else:
        file_dir = output_path / "operator-specifications"
    with Path.open(template_path, "r") as file:
        template = jinja2.Template(file.read())

    output = template.render(operator_info)
    with Path.open(Path(file_dir) / f"{file_name}.md", "w") as file:
        file.write(output)


def generate_toc_tree(docs_path: Path):
    """Write the global toc.yml file for the DPF documentation based on the operators found.

    Parameters
    ----------
    docs_path:
        Path to the root of the DPF documentation sources.

    """
    data = []
    specs_path = docs_path / "operator-specifications"
    for folder in specs_path.iterdir():
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
    template_path = Path(__file__).parent / "toc_template.j2"
    with Path.open(template_path, "r") as template_file:
        template = jinja2.Template(template_file.read())
    output = template.render(data=data)  # Pass 'data' as a named argument

    # Write the rendered output to toc.yml at the operators_doc level
    with Path.open(docs_path / "toc.yml", "w") as file:
        file.write(output)


def generate_operators_doc(
    ansys_path: Path,
    output_path: Path,
    include_composites: bool = False,
    include_sound: bool = False,
    include_private: bool = False,
    desired_plugin: str = None,
):
    """Generate the Markdown source files for the DPF operator documentation.

    This function generates a Markdown file for each operator found in a given DPF installation,
    categorized in folders per operator category, as well as a `toc.yml` file.
    These are used to generate the DPF html documentation website as seen on the Developer Portal.

    Parameters
    ----------
    ansys_path:
        Path to an Ansys/DPF installation.
    output_path:
        Path to write the output files at.
    include_composites:
        Whether to include operators of the Composites plugin.
    include_sound:
        Whether to include operators of the Sound plugin.
    include_private:
        Whether to include private operators.
    desired_plugin:
        Restrict documentation generation to the operators of this specific plugin.

    """
    server = initialize_server(ansys_path, include_composites, include_sound)
    if desired_plugin is None:
        operators = available_operator_names(server)
    else:
        operators = get_plugin_operators(server, desired_plugin)
    for operator_name in operators:
        generate_operator_doc(server, operator_name, include_private, output_path)
    generate_toc_tree(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch available operators")
    parser.add_argument("--plugin", help="Filter operators by plugin")
    parser.add_argument(
        "--ansys_path", default=None, help="Path to Ansys DPF Server installation directory"
    )
    parser.add_argument(
        "--output_path", default=None, help="Path to output directory", required=True
    )
    parser.add_argument("--include_private", action="store_true", help="Include private operators")
    parser.add_argument(
        "--include_composites", action="store_true", help="Include composites operators"
    )
    parser.add_argument("--include_sound", action="store_true", help="Include sound operators")
    args = parser.parse_args()

    generate_operators_doc(
        ansys_path=args.ansys_path,
        output_path=args.output_path,
        include_composites=args.include_composites,
        include_sound=args.include_sound,
        include_private=args.include_private,
    )
