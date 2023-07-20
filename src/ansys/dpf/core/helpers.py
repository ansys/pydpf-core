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
    field: Field
    **kwargs : optional
        Additional keyword arguments for the streamline
        computation. More information is available at
        :func:`pyvista.DataSetFilters.streamlines`.

    Returns
    -------
    streamlines: FieldsContainer

    """
    pass
