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
"""Provides functions for argument filtering and text indenting."""

import inspect
import sys
from typing import Any, Optional


def _sort_supported_kwargs(bound_method, **kwargs):
    """Filter the kwargs for a given method."""
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


def indent(text: Any, subsequent_indent: str = "", initial_indent: Optional[str] = None) -> str:
    r"""Indent each line of a given text.

    Parameters
    ----------
    text : Any
        The input text to be indented. If it is not already a string, it will be converted to one.
    subsequent_indent : str, optional
        The string to prefix all lines of the text after the first line. Default is an empty string.
    initial_indent : Optional[str], optional
        The string to prefix the first line of the text. If not provided, `subsequent_indent` will be used.

    Returns
    -------
    str
        The indented text with specified prefixes applied to each line.

    Examples
    --------
    >>> text = "Hello\\nWorld"
    >>> print(indent(text, subsequent_indent="    ", initial_indent="--> "))
    --> Hello
        World
    """
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
