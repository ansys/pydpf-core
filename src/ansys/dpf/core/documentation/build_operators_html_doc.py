# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Generation of the legacy static HTML documentation page for operators of a given DPF installation."""

from __future__ import annotations

import argparse

from ansys.dpf import core as dpf
from ansys.dpf.core.server_context import SERVER_CONTEXT


def generate_operators_html_doc(
    output_path: str = "doc/source/_static/dpf_operators.html",
    ansys_path: str = None,
    verbose: bool = True,
) -> None:
    """Generate the legacy static HTML documentation page listing operators of a DPF installation.

    Parameters
    ----------
    output_path:
        Path to write the generated HTML documentation file at.
    ansys_path:
        Path to the DPF installation to use to start a server.
    verbose:
        Whether to print progress information.

    """
    server = dpf.start_local_server(ansys_path=ansys_path)
    if verbose:  # pragma: nocover
        print(f"Server version: {server.version}")
        print("Generating operator documentation")
        print(f"Current context: {SERVER_CONTEXT}")
    dpf.operators.utility.html_doc(str(output_path)).eval()
    if verbose:  # pragma: nocover
        print("Done.")


def run_with_args():  # pragma: nocover
    """Run generate_operators_html_doc from the command line with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate the legacy static HTML operator documentation page "
        "for a given DPF installation."
    )
    parser.add_argument(
        "--ansys_path", default=None, help="Path to Ansys DPF Server installation directory"
    )
    parser.add_argument(
        "--output_path",
        default="doc/source/_static/dpf_operators.html",
        help="Path to write the generated HTML documentation file at",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=True,
        help="Print script progress information.",
    )
    args = parser.parse_args()

    generate_operators_html_doc(
        output_path=args.output_path,
        ansys_path=args.ansys_path,
        verbose=args.verbose,
    )


if __name__ == "__main__":  # pragma: nocover
    run_with_args()
