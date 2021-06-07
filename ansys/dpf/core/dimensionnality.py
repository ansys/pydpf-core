"""
Dimensionnality
===============
"""

from ansys.grpc.dpf import field_definition_pb2
from ansys.dpf.core.common import natures

class Dimensionnality:
    """Class representing the dimensionnality of the field
        Read list of dim (1D vector for scalar and vector and 2D vector for matrix)
        and create a field_definition_pb2.Dimensionality message
        
    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    dim_vec : list of int
        [1]: scalar
        [3]: 3d vector
        [3,3]: matrix 3 3
        
    nature : Nature
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
        """Dimensionnality instance corresponding to a scalar field

        Returns
        -------
        dimensionnality : Dimensionnality
        """
        return Dimensionnality([1], natures.scalar)
    
    @staticmethod
    def vector_dim(size):
        """Dimensionnality instance corresponding to a vector field of size "size"

        Parameters
        ----------
        size : int
            number of components by entity
        
        Returns
        -------
        dimensionnality : Dimensionnality
        """
        return Dimensionnality([size], natures.vector)
    
    @staticmethod
    def vector_3d_dim():
        """Dimensionnality instance corresponding to a 3 dimensions vector field

        Returns
        -------
        dimensionnality : Dimensionnality
        """
        return Dimensionnality([3], natures.vector)
    
    @staticmethod
    def tensor_dim():
        """Dimensionnality instance corresponding to a symmetrical 3 3 tensor field

        Returns
        -------
        dimensionnality : Dimensionnality
        """
        return Dimensionnality([3,3], natures.symmatrix)
