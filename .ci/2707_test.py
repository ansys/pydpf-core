from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.helpers.streamlines import compute_streamlines
from ansys.dpf.core import animation
from ansys.dpf.core.plotter import DpfPlotter

ds_fluent = dpf.DataSources()
fluent_files = examples.download_fluent_mixing_elbow_transient()
ds_fluent.set_result_file_path(fluent_files["flprj"], "flprj")

m_fluent = dpf.Model(ds_fluent)
meshed_region = m_fluent.metadata.meshed_region
tfq = m_fluent.metadata.time_freq_support

time_scop = dpf.Scoping()
time_scop.location = dpf.locations.time_freq
time_scop.ids = range(1, 6)

velocity_op = m_fluent.results.velocity()
velocity_op.inputs.time_scoping.connect(time_scop)
fc = velocity_op.outputs.fields_container()

streamlines_fc = dpf.FieldsContainer()
streamlines_fc.labels = ["time"]

for ind, field in enumerate(fc):
    field = dpf.operators.averaging.to_nodal(field=field).outputs.field()

    streamline_obj, src_obj = compute_streamlines(
        meshed_region=meshed_region,
        field=field,
        return_source=True,
        source_center=(0.56, 0.48, 0.0),
        n_points=10,
        source_radius=0.075,
        max_time=10.0,
    )

    streamlines_fc.add_field({"time": ind + 1}, streamline_obj.as_field())

streamlines_fc.time_freq_support = fc.time_freq_support

# for f in streamlines_fc:
#     pl2 = DpfPlotter()
#     pl2.add_mesh(meshed_region, opacity=0.2)
#     streamline_instance = dpf.helpers.streamlines.Streamlines(data=f)
#     pl2.add_streamlines(
#         streamlines=streamline_instance,
#         radius=0.001,
#     )
#     # pl2.add_field(field=f, meshed_region=f.meshed_region)
#     pl2.show_figure(show_axes=True)

streamlines_fc.animate(scale_factor=3.0, save_as="d:/temp/tmp.gif", streamlines_mesh_base=meshed_region)

