<!-- these nodes should be moved into contributing -->

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
