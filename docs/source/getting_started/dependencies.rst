.. _ref_dependencies:

============
Dependencies
============

Package dependencies
--------------------

PyDPF-Core dependencies are automatically checked when packages are
installed. Package dependencies follow:

- `ansys.dpf.gate <https://pypi.org/project/ansys-dpf-gate/>`_, which is the gate
  to the DPF C API or Python gRPC API. The gate depends on the server configuration:

    - `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ is the gRPC code
      generated from protobuf files.
    - `ansys.dpf.gatebin <https://pypi.org/project/ansys-dpf-gatebin/>`_ is the
      operating system-specific binaries with DPF C APIs.

- `psutil <https://pypi.org/project/psutil/>`_
- `tqdm <https://pypi.org/project/tqdm/>`_
- `packaging <https://pypi.org/project/packaging/>`_
- `numpy <https://pypi.org/project/numpy/>`_

Optional dependencies
~~~~~~~~~~~~~~~~~~~~~

For plotting, you can install these optional Python packages:

- `matplotlib <https://pypi.org/project/matplotlib/>`_ for chart plotting
- `pyvista <https://pypi.org/project/pyvista/>`_ for 3D plotting
