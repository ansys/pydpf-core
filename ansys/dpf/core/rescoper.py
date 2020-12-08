import numpy as np
from ansys.dpf.core.common import locations

class Rescoper:
    """Object which will help to rescope the results.
    Its aim is to help while plotting results.
    
    Parameters
    -----
        mesh: dpf.core.meshed_region
        location: str (location of the field or fields container to rescope)
        num_comp: int (number of component for an elementary data)
        """
    def __init__(self, mesh, location, num_comp):
        mesh_scoping = None
        if (location == locations.elemental):
            mesh_scoping = mesh.elements.scoping
        elif (location == locations.nodal):
            mesh_scoping = mesh.nodes.scoping
        else:
            raise Exception("Location "+location+" not supported.")
        
        self.location = location
        self.mesh_scoping = mesh_scoping
        self.nan_field = np.array(len(mesh_scoping) * [ num_comp * [float("nan")]])
    
    
    def get_nan_field(self):
        """Returns a NaN (not a number) field of the 
        mesh scoping length with only NaN values.
        
        Parameters
        -----
        None
        
        Return
        -----
        numpy.array (dpf.core.Field)
        """
        return self.nan_field
    
        
    def rescope(self, field_to_rescope):
        """Return a rescoped field (function of the mesh contained 
        by the rescoper object).
    
        Parameters
        -----
            field_to_rescope: dpf.core.Field
        
        
        Return
        -----
        np.array (dpf.core.Field)
        """
        location = field_to_rescope.location
        if location != self.location:
            raise Exception("Given field has not the same location as the rescoper ( "+ location + " is different from " + self.location + "). Create another rescoper with different location to rescope the field.")
        output = self.nan_field
        i = 0
        ids = self.mesh_scoping.ids
        field_scoping = field_to_rescope.scoping.ids
        for data_id in ids:
            try:
                # output[i] = field_to_rescope.get_entity_data_by_id(data_id)
                index = field_scoping.index(data_id)
                output[i] = field_to_rescope.data[index]
            except:
                pass
            i += 1
        if (len(output[0]) == 1):
            output = np.reshape(output, len(output))
        return output