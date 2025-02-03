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

"""
CustomContainerBase.

This module contains the `CustomContainerBase` class, which serves as a base
for creating wrappers around `GenericDataContainer` objects.

These wrappers provide an interface for accessing and managing data in
generic containers, enabling more intuitive usage and the addition of custom
behaviors tailored to specific use cases.
"""

from ansys.dpf.core.generic_data_container import GenericDataContainer


class CustomContainerBase:
    """
    Base class for custom container wrappers.

    This class provides a common interface for managing an underlying
    `GenericDataContainer` object.
    """

    def __init__(self, container: GenericDataContainer) -> None:
        """
        Initialize the base container with a `GenericDataContainer`.

        Parameters
        ----------
        container : GenericDataContainer
            The underlying data container to be wrapped by this class.
        """
        self._container = container
