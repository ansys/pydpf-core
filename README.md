# DPF - Ansys Data Processing Framework

[![PyPI version](https://badge.fury.io/py/ansys-dpf-core.svg)](https://badge.fury.io/py/ansys-dpf-core)

[![Build Status](https://dev.azure.com/pyansys/pyansys/_apis/build/status/pyansys.DPF-Core?branchName=master)](https://dev.azure.com/pyansys/pyansys/_build/latest?definitionId=2&branchName=master)


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

## Documentation

Visit the [DPF-Core Documentation](https://dpfdocs.pyansys.com) for a
detailed description of the library, or see the [Examples
Gallery](https://dpfdocs.pyansys.com/examples/index.html) for more
detailed examples.


Visit the [DPF-Core Documentation](https://dpfdocs.pyansys.com) for a
detailed description of the library, or see the [Examples
Gallery](https://dpfdocs.pyansys.com/examples/index.html) for more
detailed examples.

## Installation

Install this repository with:

```
pip install ansys-dpf-core 
```

You can also clone and install this repository with:

```
git clone https://github.com/pyansys/pydpf-core
cd pydpf-core
pip install . --user
```


## Running DPF

See the example scripts in the examples folder for some basic example.  More will be added later.

### Brief Demo

Provided you have ANSYS 2021R1 or higher installed, a DPF server will start
automatically once you start using DPF.

To open a result file and explore what's inside, do:

```py
>>> from ansys.dpf import core as dpf
>>> from ansys.dpf.core import examples
>>> model = dpf.Model(examples.simple_bar)
>>> print(model)

    DPF Model
    ------------------------------
    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mecanic
    Available results:
         -  displacement: Nodal Displacement
         -  element_nodal_forces: ElementalNodal Element nodal Forces
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region: 
      3751 nodes 
      3000 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 1 
    Cumulative     Time (s)       LoadStep       Substep         
    1              1.000000       1              1               


```

Read a result with:

```py
>>> result = model.results.displacement.eval()
```

Then start connecting operators with:

```py
>>> from ansys.dpf.core import operators as ops
>>> norm = ops.math.norm(model.results.displacement())
```

### Starting the Service

The `ansys.dpf.core` automatically starts a local instance of the DPF service in the
background and connects to it.  If you need to connect to an existing
remote or local DPF instance, use the ``connect_to_server`` function:

```py
>>> from ansys.dpf import core as dpf
>>> dpf.connect_to_server(ip='10.0.0.22', port=50054)
```

Once connected, this connection will remain for the duration of the
module until you exit python or connect to a different server.

     
