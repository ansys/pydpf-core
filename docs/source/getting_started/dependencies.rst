.. _ref_dependencies:

============
Dependencies
============

Package dependencies
--------------------

Dependencies for the ``ansys-dpf-core`` package are automatically checked when the
package is installed. Package dependencies are:

- `google-api-python-client <https://pypi.org/project/google-api-python-client/>`_
- `grpcio <https://pypi.org/project/grpcio/>`_
- `importlib-metadata <https://pypi.org/project/importlib-metadata/>`_
- `numpy <https://pypi.org/project/numpy/>`_
- `packaging <https://pypi.org/project/packaging/>`_
- `protobuf <https://pypi.org/project/protobuf/>`_
- `psutil <https://pypi.org/project/psutil/>`_
- `setuptools <https://pypi.org/project/setuptools/>`_
- `tqdm <https://pypi.org/project/tqdm/>`_

For ``ansys-dpf-core<0.10.0``, the :py:mod:`ansys.dpf.gate`, :py:mod:`ansys.dpf.gatebin` and
:py:mod:`ansys.grpc.dpf` modules are not included and are dependencies:

- `ansys.dpf.gate <https://pypi.org/project/ansys-dpf-gate/>`_, which is the gate
  to the DPF C API or Python gRPC API. The gate depends on the server configuration:
- `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ is the gRPC code
  generated from protobuf files and is a dependency of ``ansys-dpf-gate``.
- `ansys.dpf.gatebin <https://pypi.org/project/ansys-dpf-gatebin/>`_ is the
  operating system-specific binaries with DPF C APIs and is a dependency of ``ansys-dpf-gate``.


Optional dependencies
~~~~~~~~~~~~~~~~~~~~~

For plotting, you can install these optional Python packages:

- `matplotlib <https://pypi.org/project/matplotlib/>`_ package for chart plotting
- `pyvista <https://pypi.org/project/pyvista/>`_ package for 3D plotting
