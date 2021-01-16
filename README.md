# DPF - Ansys Data Processing Framework

[![PyPI version](https://badge.fury.io/py/ansys-dpf-core.svg)](https://badge.fury.io/py/ansys-dpf-core)

[![Build Status](https://dev.azure.com/pyansys/pyansys/_apis/build/status/pyansys.DPF-Core?branchName=docs%2Foperators)](https://dev.azure.com/pyansys/pyansys/_build/latest?definitionId=2&branchName=docs%2Foperators)

The Data Processing Framework (DPF) is designed to provide numerical
simulation users/engineers with a toolbox for accessing and
transforming simulation data. DPF can access data from solver result
files as well as several neutral formats (csv, hdf5, vtk,
etc.). Various operators are available allowing the manipulation and
the transformation of this data.

DPF is a workflow-based framework which allows simple and/or complex
evaluations by chaining operators. The data in DPF is defined based on
physics agnostic mathematical quantities described in a
self-sufficient entity called field. This allows DPF to be a modular
and easy to use tool with a large range of capabilities. It's a
product designed to handle large amount of data.

The Python ``ansys.dpf.core`` module provides a Python interface to
the powerful DPF framework enabling rapid post-processing of a variety
of Ansys file formats and physics solutions without ever leaving a
Python environment.


## Installation

Install this repository with:

```
pip install ansys-dpf-core
```

You can also clone and install this repository with:

```
git clone https://github.com/pyansys/DPF-Core
cd DPF-Core
pip install . --user
```


## Running DPF

### Brief Demo
Provided you have ANSYS 2021R1 installed, a DPF server will start
automatically once you start using DPF.

Opening a result file generated from Ansys workbench or MAPDL is as easy as:

```
>>> from ansys.dpf.core import Model
>>> model = Model('file.rst')
>>> print(model)
DPF Model
------------------------------
Static analysis
Unit system: Metric (m, kg, N, s, V, A)
Physics Type: Mecanic
Available results:
     -  displacement
     -  element_nodal_forces
     -  volume
     -  energy_stiffness_matrix
     -  hourglass_energy
     -  thermal_dissipation_energy
     -  kinetic_energy
     -  co_energy
     -  incremental_energy
     -  temperature
```

Open up an result with:

```py
>>> model.displacement
```

Then start linking operators with:

```py
>>> norm = core.Operator('norm_fc')
```

### Starting the Service

The `ansys.dpf.core` automatically starts the DPF service in the
background and connects to it.  If you need to connect to an existing
remote DPF instance, use the ``connect_to_server`` function:

```py
from ansys.dpf import core
connect_to_server('10.0.0.22, 50054)
```

Once connected, this connection will remain for the duration of the
module until you exit python or connect to a different server.

