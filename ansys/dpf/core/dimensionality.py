"""
Dimensionality
==============
"""

from ansys.grpc.dpf import field_definition_pb2
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
    
    def __init__(self, dim_vec, nature : natures):
        self.dim = dim_vec
        self.nature = nature
        
    def _parse_dim_to_message(self):
        message = field_definition_pb2.Dimensionality()
        message.size.extend(self.dim)
        message.nature = self.nature.value
        return message
    
    def __str__(self):
        return str(self.dim) + " "+ self.nature.name
    
    
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
        return Dimensionality([3,3], natures.symmatrix)
