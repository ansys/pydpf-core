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

import sys
import traceback
import warnings

from ansys.dpf.gate.generated import capi as _gate_capi


def _is_local_capi_deleter(deleter):
    """Return whether a deleter calls the generated in-process C API."""
    return getattr(deleter, "__module__", "").startswith("ansys.dpf.gate.generated.")


def release_dpf_object(obj):
    """Release a DPF object through its configured native deleter."""
    if sys is None or sys.is_finalizing():
        return
    try:
        deleter = getattr(obj, "_deleter_func", None)
        if deleter is None:
            return
        if getattr(obj, "_internal_obj", None) is None:
            return
        native_obj = deleter[1](obj)
        if native_obj is not None:
            if getattr(_gate_capi, "_api_loading", False) and not _is_local_capi_deleter(
                deleter[0]
            ):
                deleter[0](native_obj)
            else:
                _gate_capi._call_or_defer(deleter[0], native_obj)
    except Exception:
        warn = getattr(warnings, "warn", None)
        format_exc = getattr(traceback, "format_exc", None)
        if warn is not None and format_exc is not None:
            warn(format_exc())
