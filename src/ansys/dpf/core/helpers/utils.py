# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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

import inspect
import sys


def _sort_supported_kwargs(bound_method, **kwargs):
    """Filters the kwargs for a given method."""
    # Ignore warnings unless specified
    if not sys.warnoptions:
        import warnings

        warnings.simplefilter("ignore")
    # Get supported arguments
    supported_args = inspect.getfullargspec(bound_method).args
    kwargs_in = {}
    kwargs_not_avail = {}
    # Filter the given arguments
    for key, item in kwargs.items():
        if key in supported_args:
            kwargs_in[key] = item
        else:
            kwargs_not_avail[key] = item
    # Prompt a warning for arguments filtered out
    if len(kwargs_not_avail) > 0:
        txt = f"The following arguments are not supported by {bound_method}: "
        txt += str(kwargs_not_avail)
        warnings.warn(txt)
    # Return the accepted arguments
    return kwargs_in


def indent(text, subsequent_indent="", initial_indent=None):
    if initial_indent is None:
        initial_indent = subsequent_indent

    if not isinstance(text, str):
        text = str(text)

    lines = text.rstrip().splitlines()
    indented_lines = [
        f"{initial_indent if index == 0 else subsequent_indent}{line}"
        for (index, line) in enumerate(lines)
    ]

    return "\n".join(indented_lines)
