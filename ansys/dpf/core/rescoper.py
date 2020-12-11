import numpy as np
from ansys.dpf.core.common import locations


class Rescoper:
    """Rescope a field relative to a mesh and its location.

    Its aim is to help while plotting results.

    Parameters
    ----------
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
            raise ValueError(f"Location {location} not supported.")

        self.location = location
        self.mesh_scoping = mesh_scoping
        self._num_comp = num_comp    

    @property
    def nan_field(self):
        """Array of NAN sized to match the mesh scoping"""
        nan_field = np.empty((len(self.mesh_scoping), self._num_comp))
        nan_field[:] = np.nan
        return nan_field

    def rescope(self, field_to_rescope):
        """Return a rescoped field (function of the mesh contained 
        by the rescoper object).
    
        Parameters
        ----------
        field_to_rescope: dpf.core.Field
            Field to rescope to.

        Returns
        -------
        output : np.ndarray
            Rescoped data from the field.

        """
        location = field_to_rescope.location
        if location != self.location:
            raise ValueError('Given field has not the same location as the rescoper '
                             f'({location} is different from {self.location}).  '
                             'Create another rescoper with different location to'
                             'rescope the field.')
        output = self.nan_field

        # looping is only faster when requesting just a few values
        mesh_ids = np.asarray(self.mesh_scoping.ids)
        field_scoping = field_to_rescope.scoping.ids
        if len(mesh_ids) < 25 or self.location == 'Elemental':
            for i, data_id in enumerate(mesh_ids):
                try:
                    # output[i] = field_to_rescope.get_entity_data_by_id(data_id)
                    index = field_scoping.index(data_id)
                    output[i] = field_to_rescope.data[index]
                except:
                    pass
            if len(output[0]) == 1:
                output = np.reshape(output, len(output))

        else:  # simply request all the data and rescope it client-side

            # since the mesh nodal scoping is always sorted, sort the
            # rescoped ids as well
            rescope_ids = np.asarray(field_to_rescope.scoping.ids)
            sidx = np.argsort(rescope_ids)
            sorted_ids = rescope_ids[sidx]

            # field ids in common with mesh
            mask_a = np.in1d(mesh_ids, rescope_ids, assume_unique=True)

            # mesh ids in common with the field
            mask_b = np.in1d(sorted_ids, mesh_ids, assume_unique=True)

            # indes of the data must be sorted to match the mesh
            idx = sidx[mask_b]
            output[mask_a] = field_to_rescope.data[idx]

        return output
