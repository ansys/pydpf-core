# DPF - Ansys Data Processing Framework
[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![Python](https://img.shields.io/badge/Python-3.8-blue)](https://pypi.org/project/ansys-dpf-core/)
[![pypi](https://img.shields.io/pypi/v/ansys-dpf-core.svg?logo=python&logoColor=white)](https://pypi.org/project/ansys-dpf-core)
[![freq-PyDPF-Core](https://img.shields.io/github/commit-activity/m/pyansys/pydpf-core)](https://github.com/pyansys/pydpf-core)
[![GH-CI](https://github.com/pyansys/pydpf-core/actions/workflows/ci.yml/badge.svg)](https://github.com/pyansys/pydpf-core/actions/workflows/ci.yml)
[![docs](https://img.shields.io/website?down_color=lightgrey&down_message=invalid&label=documentation&up_color=brightgreen&up_message=up&url=https%3A%2F%2Fdpfdocs.pyansys.com%2F)](https://dpfdocs.pyansys.com)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pypidl](https://img.shields.io/pypi/dm/ansys-dpf-core.svg?label=PyPI%20downloads)](https://pypi.org/project/ansys-dpf-core/)
[![cov](https://codecov.io/gh/pyansys/pydpf-core/branch/master/graph/badge.svg)](https://codecov.io/gh/pyansys/pydpf-core)
[![codacy](https://app.codacy.com/project/badge/Grade/61b6a519aea64715ad1726b3955fcf98)](https://www.codacy.com/gh/pyansys/pydpf-core/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pyansys/pydpf-core&amp;utm_campaign=Badge_Grade)

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

## Installation

DPF requires an Ansys installation and must be compatible with it.
Compatibility between PyDPF-Core and Ansys is documented 
[here](https://dpfdocs.pyansys.com/getting_started/index.html#compatibility).

Starting with Ansys 2021R2, install this package with:

```
pip install ansys-dpf-core 
```

For use with Ansys 2021R1, install this package with:

```
pip install ansys-dpf-core==0.2.1
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

     
