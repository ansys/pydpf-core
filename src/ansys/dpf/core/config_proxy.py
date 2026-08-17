# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT.
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

"""
Provide server-synchronized operator configuration access.

`_ConfigProxy` delegates configuration reads to `Config` and synchronizes
configuration updates with the remote operator. Each write is applied to a
temporary configuration and then sent back to the operator.
"""

from ansys.dpf.core.config import Config


class _ConfigProxy:
    """Proxy config class that syncs Config modifications back to operator.

    Ensures that all Config writes happen on server.
    Reads are delegated to Config class objects.
    """

    def __init__(self, operator):
        self._operator = operator

    def set_config_option(self, config_name, config_value):
        """Create a temp config, modify and write back to server."""
        cfg = self._get_temp_config()
        cfg.set_config_option(config_name, config_value)
        self._operator.config = cfg

    def _get_temp_config(self):
        """Get current config from server."""
        config = self._operator._api.operator_get_config(self._operator)
        return Config(config=config, server=self._operator._server, spec=self._operator._spec)

    def __getattr__(self, name):
        """Delegate reads, but intercept set_*_option for auto-sync."""
        if name.startswith("set_") and name.endswith("_option"):

            def wrapped_setter(value):
                cfg = self._get_temp_config()
                getattr(cfg, name)(value)
                self._operator.config = cfg

            return wrapped_setter
        return getattr(self._get_temp_config(), name)
