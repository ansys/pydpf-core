# DPF - ANSYS Data Processing Framework


## Installation

Clone and install this repository with:

```
git clone https://github.com/pyansys/DPF-Core
cd DPF-Core
pip install . --user
```

Install any missing libraries from Artifactory with:

```
pip install --extra-index-url=http://canartifactory.ansys.com:8080/artifactory/api/pypi/pypi/simple --trusted-host canartifactory.ansys.com ansys-grpc-dpf
```

This step will be eliminated once DPF is live on PyPi.


## Running DPF

Provided you have ANSYS 2021R1 installed, a DPF server will start
automatically once you start using DPF:


```py
from ansys.dpf import core

norm = core.Operator('norm_fc')

# or open up a model
model = core.Model('file.rst')

```

The `ansys.dpf.core` module takes care of starting your local server
for you so you don't have to.  If you need to connect to a remote DPF
instance, use the ``connect_to_server`` function:

```py
from ansys.dpf import core
connect_to_server('10.0.0.22, 50054)
```

Once connected, this connection will remain for the duration of the
module until you exit python or connect to a different server.


## Unit Testing

Unit tests can be run by first installing the testing requirements with `pip install -r requirements_test.txt` and then running pytest with:

```
pytest
```

If you have ANSYS v2021R1 installed locally, the unit tests will
automatically start up the DPF server and run the tests.  If you need
to disable this and have the unit tests run against a remote server,
setup the following environment variables:

```
set DPF_START_SERVER=False
set DPF_IP=<IP of Remote Computer>
set DPF_PORT=<Port of Remote DPF Server>
```


## Examples
See the example scripts in the examples folder for some basic examples.
