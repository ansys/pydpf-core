"""Helpers for using specific capabilities.

For example, provide helpers to compute and manipulate
streamlines.
"""

def compute_streamlines(meshed_region, field, **kwargs):
    """Compute the streamlines for a given mesh and velocity
    field.

    Parameters
    ----------
    meshed_region: MeshedRegion
        MeshedRegion the streamline will be computed on.
    field: Field
        Field containing raw vector data the streamline is
        computed from. The data location must be nodal, velocity
        values must be defined at nodes.
    **kwargs : optional
        Additional keyword arguments for the streamline
        computation. More information is available at
        :func:`pyvista.DataSetFilters.streamlines`.

    Returns
    -------
    streamlines: FieldsContainer

    """
    pass
