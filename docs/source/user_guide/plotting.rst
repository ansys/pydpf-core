.. _user_guide_plotting:

========
Plotting
========
DPF-Core has a variety of plotting methods to generate 3D plots of
ANSYS models directly from Python.  These methods use VTK and leverage
the `pyvista <https://github.com/pyvista/pyvista>`_ Python library to
simplify plotting.  Please see the `pyvista Documentation
<https://docs.pyvista.org>`_ for additional details.


Plotting the Mesh from the Model Object
---------------------------------------
The :py:meth:`Model.plot() <ansys.dpf.core.model.Model.plot>` method can be used to
immediately plot the mesh of the model after loading it.  In the
following example, a simple pontoon mesh is downloaded from the
internet and loaded using the ``Model`` class.

.. code:: python

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> filename = examples.download_pontoon()
    >>> model = dpf.Model(filename)
    >>> model.plot()

.. image:: ../images/plotting/pontoon.png

The default plotter settings display the mesh with edges shown with
lighting enabled.  For a full listing of all the keyword arguments, please see `plot <https://docs.pyvista.org/plotting/plotting.html?highlight=plot#pyvista.plot>`_.


Plotting using the MeshedRegion
-------------------------------
The :py:meth:`MeshedRegion.plot() <ansys.dpf.core.meshed_region.MeshedRegion.plot>` method plots the meshed
region.  If the ``MeshedRegion`` is generated from the model's
metadata, it will generate an identical plot as in the
``Model.plot()``:

.. code:: python

    >>> mesh = model.metadata.meshed_region
    >>> mesh.plot()

.. image:: ../images/plotting/pontoon.png

However, when provided with a field as the first argument, it will
plot the mesh using those values.  In the following example, we will
extract the nodal strain in the X direction.

.. code:: python

    First, extract the X component strain

    >>> strain = model.results.strain()
    >>> fields = strain.outputs.fields_container()
    >>> field = fields.select_component(0)[0]
    >>> print(field)
    DPF elastic_strain_1.s Field
        Location:   ElementalNodal
        Unit:       
        Num. id(s): 8640
        Shape:      69120

    This ElementalNodal strain must be converted to nodal strain for
    it to be plotted.

    >>> nodal_field = field.to_nodal()
    >>> mesh.plot(nodal_field)

.. image:: ../images/plotting/pontoon_strain.png

.. note::

   At the moment, only fields with Elemental and Nodal locations are
   supported.  Use the :py:meth:`to_nodal
   <ansys.dpf.core.field.Field.to_nodal>` to convert to nodal or the
   ``'nodal_to_elemental'`` operator to convert to elemental.

