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

"""Dimensionality."""

from ansys.dpf.core.common import natures


class Dimensionality:
    """Represents the dimensionality of a field.

        This class reads a list of dimension vectors and creates a dimensionality message.

    Parameters
    ----------
    dim_vec : list
        List of integers for the dimension vectors. There is a 1D vector for a
        scalar or 3D vector. There is a 2D vector for a matrix. For example:

        * ``[1]``: scalar
        * ``[3]``: 3d vector
        * ``[3, 3]``: ``3 x 3`` matrix
    nature : :class:`ansys.dpf.core.common.natures`

    """

    def __init__(self, dim_vec=None, nature: natures = natures.vector):
        self.dim = dim_vec
        self.nature = nature
        # set nature
        if not isinstance(nature, natures):
            if isinstance(nature, str):
                self.nature = natures[nature]
            elif isinstance(nature, int):
                self.nature = natures(nature)
            else:
                raise TypeError("Nature is expected to be cast into ansys.dpf.core.natures enum")

        if self.dim is not None and 0 in self.dim:
            self.dim = [x for x in self.dim if x != 0]
            if len(self.dim) == 0:
                self.dim = None

        if self.dim is None:
            if self.nature == natures.vector:
                self.dim = [3]
            elif self.nature == natures.symmatrix:
                self.dim = [3, 3]
            elif self.nature == natures.scalar:
                self.dim = [1]

    def is_1d_dim(self):
        """Check if dimensionality is 1."""
        return len(self.dim) == 1

    def is_2d_dim(self):
        """Check if dimensionality is 2."""
        return len(self.dim) == 2

    def __str__(self):
        """Customize the string representation of the dimensionality."""
        return str(self.dim) + " " + self.nature.name

    @property
    def component_count(self):
        """Retrieve the number of components based on the dimensionality.

        Returns
        -------
        float
            Number of components.
        """
        count = 1
        for comp in self.dim:
            count *= comp
        return count

    @staticmethod
    def scalar_dim():
        """Retrieve the dimensionality of a scalar field.

        Returns
        -------
        :class:`ansys.dpf.core.dimensionnality.Dimensionality`
            Dimensionality of the scalar field.
        """
        return Dimensionality([1], natures.scalar)

    @staticmethod
    def vector_dim(size):
        """Retrieve the dimensionality of a vector field of a given size.

        Parameters
        ----------
        size : int
            Number of components by entity.

        Returns
        -------
        :class:`ansys.dpf.core.dimensionnality.Dimensionality`
            Dimensionality of the vector field.
        """
        return Dimensionality([size], natures.vector)

    @staticmethod
    def vector_3d_dim():
        """Retrieve the dimensionality of a three-dimension vector field.

        Returns
        -------
        :class:`ansys.dpf.core.dimensionnality.Dimensionality`
            Dimensionality of the three-dimension vector field.
        """
        return Dimensionality([3], natures.vector)

    @staticmethod
    def tensor_dim():
        """Retrieve the dimensionality of a symmetrical ``3 x 3`` tensor field.

        Returns
        -------
        :class:`ansys.dpf.core.dimensionnality.Dimensionality`
            Dimensionality of the symmetrical ``3 x 3`` tensor field.
        """
        return Dimensionality([3, 3], natures.symmatrix)

    def __eq__(self, other):
        """Check if this Dimensionality object is equal to another.

        Two Dimensionality objects are considered equal if their dimensionality
        vectors (`dim`) and natures (`nature`) are the same.

        Parameters
        ----------
        other : Dimensionality
            The other Dimensionality object to compare with.

        Returns
        -------
        bool
            `True` if the two objects are equal, `False` otherwise.
        """
        return self.dim == other.dim and self.nature == other.nature

    def __ne__(self, other):
        """Check if this Dimensionality object is not equal to another.

        Two Dimensionality objects are considered not equal if their dimensionality
        vectors (`dim`) or natures (`nature`) differ.

        Parameters
        ----------
        other : Dimensionality
            The other Dimensionality object to compare with.

        Returns
        -------
        bool
            `True` if the two objects are not equal, `False` otherwise.
        """
        return not self.__eq__(other)
