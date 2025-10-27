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
import os
from pathlib import Path
import re

from ansys.dpf import core as dpf
from ansys.dpf.core.changelog import Changelog
from ansys.dpf.core.core import load_library
from ansys.dpf.core.dpf_operator import available_operator_names


class Jinja2ImportError(ModuleNotFoundError):  # pragma: nocover
    """Error raised when Jinja2 could not be imported during operator documentation generation."""

    def __init__(
        self,
        msg="To generate Markdown documentation of operators, please install jinja2 with:\n"
        "pip install jinja2",
    ):
        ModuleNotFoundError.__init__(self, msg)


try:
    import jinja2
except ModuleNotFoundError:  # pragma: nocover
    raise Jinja2ImportError


def initialize_server(
    ansys_path: str | os.PathLike = None,
    include_composites: bool = False,
    include_sound: bool = False,
    verbose: bool = False,
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
    verbose:
        Whether to print progress information.

    Returns
    -------
    server:
        A running DPF server to generate operator documentation for.

    """
    server = dpf.start_local_server(ansys_path=ansys_path)
    if verbose:  # pragma: nocover
        print(f"Ansys Path: {server.ansys_path}")
        print(f"Server Info: {server.info}")
        print(f"Server Context: {server.context}")
        print(f"Server Config: {server.config}")
        print(f"Server version: {dpf.global_server().version}")
    if include_composites:  # pragma: nocover
        if verbose:
            print("Loading Composites Plugin")
        if server.os == "nt":
            binary_name = "composite_operators.dll"
        else:
            binary_name = "libcomposite_operators.so"
        load_library(
            filename=Path(server.ansys_path) / "dpf" / "plugins" / "dpf_composites" / binary_name,
            name="composites",
        )
    if include_sound and server.os == "nt":  # pragma: nocover
        if verbose:
            print("Loading Acoustics Plugin")
        load_library(
            filename=Path(server.ansys_path) / "Acoustics" / "SAS" / "ads" / "dpf_sound.dll",
            name="sound",
        )
    if verbose:  # pragma: nocover
        print(f"Loaded plugins: {list(server.plugins.keys())}")
    return server


def extract_operator_description_update(content: str) -> str:
    """Extract the updated description to use for an operator.

    Parameters
    ----------
    content:
        The contents of the '*_upd.md' file.

    Returns
    -------
        description_update:
            The updated description to use for the operator.
    """
    match = re.search(r"## Description\s*(.*?)\s*(?=## |\Z)", content, re.DOTALL)
    description = match.group(0) + os.linesep if match else None
    # Handle unicode characters
    return description.encode("unicode-escape").decode()


def replace_operator_description(original_documentation: str, new_description: str):
    """Replace the original operator description with a new one in the operator documentation file.

    Parameters
    ----------
    original_documentation:
        Original operator documentation.
    new_description:
        New operator description

    Returns
    -------
    updated_documentation:
        The updated operator documentation content

    """
    return re.sub(
        r"## Description\s*.*?(?=## |\Z)", new_description, original_documentation, flags=re.DOTALL
    )


def update_operator_descriptions(
    docs_path: Path,
    verbose: bool = False,
):
    """Update operator descriptions based on '*_upd.md' files in DPF documentation sources.

    Parameters
    ----------
    docs_path:
        Root path of the DPF documentation to update operator descriptions for.
    verbose:
        Whether to print progress information.

    """
    all_md_files = {}
    specs_path = docs_path / Path("operator-specifications")
    # Walk through the target directory and all subdirectories
    for root, _, files in os.walk(specs_path):
        for file in files:
            if file.endswith(".md"):
                full_path = Path(root) / Path(file)
                all_md_files[str(full_path)] = file  # Store full path and just filename

    for base_path, file_name in all_md_files.items():
        if file_name.endswith("_upd.md"):
            continue  # Skip update files

        # Construct the expected update file name and path
        upd_file_name = f"{file_name[:-3]}_upd.md"

        # Look for the update file in the same folder
        upd_path = Path(base_path).parent / Path(upd_file_name)
        if not upd_path.exists():
            continue

        # Load contents
        with Path(base_path).open(mode="r", encoding="utf-8") as bf:
            base_content = bf.read()
        with Path(upd_path).open(mode="r", encoding="utf-8") as uf:
            upd_content = uf.read()

        # Extract and replace description
        new_description = extract_operator_description_update(upd_content)
        if new_description:
            updated_content = replace_operator_description(base_content, new_description)
            with Path(base_path).open(mode="w", encoding="utf-8") as bf:
                bf.write(updated_content)
            if verbose:
                print(f"Updated description for: {file_name}")
        else:
            if verbose:
                print(f"No operator description found in: {upd_path}")


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

    op_description = latex_to_dollars(spec.description)

    return {
        "operator_name": op_friendly_name,
        "operator_description": op_description,
        "inputs": input_info,
        "outputs": output_info,
        "configurations": configurations_info,
        "scripting_info": scripting_info,
        "exposure": exposure,
    }


def latex_to_dollars(text: str) -> str:
    r"""Convert LaTeX math delimiters from \\[.\\] to $$.$$ and from \\(.\\) to $.$ in a given text.

    Parameters
    ----------
    text:
        The input text containing LaTeX math delimiters.
    """
    return (
        text.replace(r"\\[", "$$").replace(r"\\]", "$$").replace(r"\\(", "$").replace(r"\\)", "$")
    )


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
    server: dpf.AnyServerType,
    operator_name: str,
    include_private: bool,
    output_path: Path,
    router_info: dict = None,
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
    router_info:
        Information about router operators.

    """
    operator_info = fetch_doc_info(server, operator_name)
    supported_file_types = {}
    if router_info is not None:
        operator_info["is_router"] = operator_name in router_info["router_map"].keys()
        if operator_info["is_router"]:
            supported_keys = router_info["router_map"].get(operator_name, []).split(";")
            for key in supported_keys:
                if key in router_info["namespace_ext_map"]:
                    namespace = router_info["namespace_ext_map"][key]
                    if namespace not in supported_file_types:
                        supported_file_types[namespace] = [key]
                    else:
                        supported_file_types[namespace].append(key)
        for namespace, supported_keys in supported_file_types.items():
            supported_file_types[namespace] = ", ".join(sorted(supported_keys))
    else:
        operator_info["is_router"] = False
    operator_info["supported_file_types"] = supported_file_types
    scripting_name = operator_info["scripting_info"]["scripting_name"]
    category: str = operator_info["scripting_info"]["category"]
    if scripting_name:
        file_name = scripting_name
    else:
        file_name = operator_name
    if "::" in file_name:
        file_name = file_name.replace("::", "_")
    if not include_private and operator_info["exposure"] == "private":
        return
    template_path = Path(__file__).parent / "operator_doc_template.j2"
    spec_folder = output_path / Path("operator-specifications")
    category_dir = spec_folder / category
    spec_folder.mkdir(parents=True, exist_ok=True)
    if category is not None:
        category_dir.mkdir(parents=True, exist_ok=True)  # Ensure all parent directories are created
        file_dir = category_dir
    else:
        file_dir = spec_folder
    with Path.open(template_path, "r") as file:
        template = jinja2.Template(file.read())

    output = template.render(operator_info)
    with Path.open(Path(file_dir) / f"{file_name}.md", "w") as file:
        file.write(output)


def update_toc_tree(docs_path: Path):
    """Update the global toc.yml file for the DPF documentation based on the operators found.

    Parameters
    ----------
    docs_path:
        Path to the root of the DPF documentation sources.

    """
    data = []
    specs_path = docs_path / Path("operator-specifications")
    for folder in specs_path.iterdir():
        if folder.is_dir():  # Ensure 'folder' is a directory
            category = folder.name
            operators = []  # Reset operators for each category
            for file in folder.iterdir():
                if (
                    file.is_file()
                    and file.suffix == ".md"
                    and not file.name.endswith("_upd.md")
                    and not file.name.endswith("_category.md")
                ):  # Ensure 'file' is a file with .md extension
                    file_name = file.name
                    file_path = f"{category}/{file_name}"
                    operator_name = file_name.replace("_", " ").replace(".md", "")
                    operators.append({"operator_name": operator_name, "file_path": file_path})
            data.append({"category": category, "operators": operators})

    # Render the Jinja2 template
    template_path = Path(__file__).parent / "toc_template.j2"
    with template_path.open(mode="r") as template_file:
        template = jinja2.Template(template_file.read())
    output = template.render(data=data)  # Pass 'data' as a named argument

    # Update the original toc.yml file with the rendered output for operator_specifications
    toc_path = docs_path / Path("toc.yml")
    with toc_path.open(mode="r") as file:
        original_toc = file.read()
    new_toc = re.sub(
        pattern=r"- name: Operator specifications\s*.*?(?=- name: Changelog|\Z)",
        repl=output,
        string=original_toc,
        flags=re.DOTALL,
    )
    with toc_path.open(mode="w") as file:
        file.write(new_toc)


def update_categories(docs_path: Path):
    """Update the category index files for the operator specifications.

    Parameters
    ----------
    docs_path:
        Path to the root of the DPF documentation sources.

    """
    specs_path = docs_path / Path("operator-specifications")
    for folder in specs_path.iterdir():
        if folder.is_dir():  # Ensure 'folder' is a directory
            category = folder.name
            operators = []  # Reset operators for each category
            for file in folder.iterdir():
                if (
                    file.is_file()
                    and file.suffix == ".md"
                    and not file.name.endswith("_upd.md")
                    and not file.name.endswith("_category.md")
                ):  # Ensure 'file' is a file with .md extension
                    file_name = file.name
                    operator_name = file_name.replace("_", " ").replace(".md", "")
                    operators.append({"operator_name": operator_name, "file_path": file_name})
            # Update category index file
            category_file_path = folder / f"{category}_category.md"
            with category_file_path.open(mode="w") as cat_file:
                cat_file.write(f"# {category.capitalize()} operators\n\n")
                for operator in operators:
                    cat_file.write(f"- [{operator['operator_name']}]({operator['file_path']})\n")


def update_operator_index(docs_path: Path):
    """Update the main index file for all operator specifications.

    Parameters
    ----------
    docs_path:
        Path to the root of the DPF documentation sources.

    """
    specs_path = docs_path / Path("operator-specifications")
    index_file_path = specs_path / "operator-specifications.md"
    with index_file_path.open(mode="w") as index_file:
        index_file.write("# Operator Specifications\n\n")
        for folder in specs_path.iterdir():
            if folder.is_dir():  # Ensure 'folder' is a directory
                category = folder.name
                index_file.write(
                    f"- [{category.capitalize()} operators]({category}/{category}_category.md)\n\n"
                )
                index_file.write("\n")


def get_operator_routing_info(server: dpf.AnyServerType) -> dict:
    """Get information about router operators.

    Parameters
    ----------
    server:
        DPF server to query for the operator routing map.

    Returns
    -------
    routing_map:
        A dictionary with three main keys: "aliases", "namespace_ext_map", and "router_map".
        "aliases" is a dictionary of operator aliases.
        "namespace_ext_map" is a dictionary mapping keys to namespaces.
        "router_map" is a dictionary mapping operator names to lists of supported keys.
    """
    dt_root: dpf.DataTree = dpf.dpf_operator.Operator(
        name="info::router_discovery",
        server=server,
    ).eval()
    router_info: dict = dt_root.to_dict()
    return router_info


def generate_operators_doc(
    output_path: Path,
    ansys_path: Path = None,
    include_composites: bool = False,
    include_sound: bool = False,
    include_private: bool = False,
    desired_plugin: str = None,
    verbose: bool = True,
):
    """Generate the Markdown source files for the DPF operator documentation.

    This function generates a Markdown file for each operator found in a given DPF installation,
    categorized in folders per operator category, as well as a `toc.yml` file.
    These are used to generate the DPF html documentation website as seen on the Developer Portal.

    Parameters
    ----------
    output_path:
        Path to write the output files at.
    ansys_path:
        Path to an Ansys/DPF installation.
    include_composites:
        Whether to include operators of the Composites plugin.
    include_sound:
        Whether to include operators of the Sound plugin.
    include_private:
        Whether to include private operators.
    desired_plugin:
        Restrict documentation generation to the operators of this specific plugin.
    verbose:
        Whether to print progress information.

    """
    server = initialize_server(ansys_path, include_composites, include_sound, verbose)
    if desired_plugin is None:
        operators = available_operator_names(server)
    else:
        operators = get_plugin_operators(server, desired_plugin)
    if server.meet_version(required_version="11.0"):
        router_info = get_operator_routing_info(server)
    else:
        router_info = None
    for operator_name in operators:
        generate_operator_doc(server, operator_name, include_private, output_path, router_info)
    # Generate the toc tree
    update_toc_tree(output_path)
    # Generate the category index files
    update_categories(output_path)
    # Generate the main index file for all categories
    update_operator_index(output_path)
    # Use update files in output_path
    update_operator_descriptions(output_path)


def run_with_args():  # pragma: nocover
    """Run generate_operators_doc from the command line with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate the operator documentation sources for operators of a given DPF installation."
    )
    parser.add_argument(
        "--ansys_path", default=None, help="Path to Ansys DPF Server installation directory"
    )
    parser.add_argument("--output_path", default=".", help="Path to output directory")
    parser.add_argument("--include_private", action="store_true", help="Include private operators")
    parser.add_argument(
        "--include_composites", action="store_true", help="Include Composites operators"
    )
    parser.add_argument(
        "--include_sound", action="store_true", help="Include Sound operators (Windows only)"
    )
    parser.add_argument("--plugin", help="Restrict to the given plugin.")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=True,
        help="Print script progress information.",
    )
    args = parser.parse_args()

    generate_operators_doc(
        output_path=args.output_path,
        ansys_path=args.ansys_path,
        include_composites=args.include_composites,
        include_sound=args.include_sound,
        include_private=args.include_private,
        desired_plugin=args.plugin,
    )


if __name__ == "__main__":  # pragma: nocover
    run_with_args()
