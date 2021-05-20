# DPF
ANSYS Data Processing Framework.

## Disclaimer

This API is currently a work in progress - things will break and change!


## Get Started as a public API consummer

It is possible either to use:

```
pip install ansys-dpf-core 
```

or clone or copy this directory at https://github.com/pyansys/DPF-Core and then install using:

```
pip install . --user 
```

See the example scripts in the examples folder for some basic example.  More will be added later.

## Get started as python developer

Clone the internal repository at https://tfs.ansys.com:8443/tfs/ANSYS_Development/DPF/_git/dpf-python-core and run:

```
pip install . --extra-index-url http://canartifactory.ansys.com:8080/artifactory/api/pypi/pypi/simple --trusted-host canartifactory.ansys.com
```

## Get started as Ansys internal consumer

To install all dpf python modules and requirements from the internal pypi, run: 

```
pip install ansys-dpf-core --extra-index-url http://canartifactory.ansys.com:8080/artifactory/api/pypi/pypi/simple --trusted-host canartifactory.ansys.com
```