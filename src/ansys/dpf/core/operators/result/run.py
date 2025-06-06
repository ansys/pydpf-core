"""
run

Autogenerated DPF operator classes.
"""

from __future__ import annotations

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification
from ansys.dpf.core.config import Config
from ansys.dpf.core.server_types import AnyServerType


class run(Operator):
    r"""Solve in mapdl a dat/inp file and returns a datasources with the rst
    file.


    Parameters
    ----------
    mapdl_exe_path: str, optional
    working_dir: str, optional
    number_of_processes: int, optional
        Set the number of MPI processes used for resolution (default is 2)
    number_of_threads: int, optional
        Set the number of threads used for resolution (default is 1)
    data_sources: DataSources
        data sources containing the input file.
    server_mode: bool, optional
        used when a user includes commands in the input file allowing to launch DPF server inside MAPDL to interact with MAPDL using DPF client API

    Returns
    -------
    data_sources: DataSources
        returns the data source if the server_mode pin is not set to yes
    ip: str
        returns the Ip if the server_mode pin is set to yes
    port: str
        returns a port when the server mode pin is set to yes

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.run()

    >>> # Make input connections
    >>> my_mapdl_exe_path = str()
    >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
    >>> my_working_dir = str()
    >>> op.inputs.working_dir.connect(my_working_dir)
    >>> my_number_of_processes = int()
    >>> op.inputs.number_of_processes.connect(my_number_of_processes)
    >>> my_number_of_threads = int()
    >>> op.inputs.number_of_threads.connect(my_number_of_threads)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_server_mode = bool()
    >>> op.inputs.server_mode.connect(my_server_mode)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.run(
    ...     mapdl_exe_path=my_mapdl_exe_path,
    ...     working_dir=my_working_dir,
    ...     number_of_processes=my_number_of_processes,
    ...     number_of_threads=my_number_of_threads,
    ...     data_sources=my_data_sources,
    ...     server_mode=my_server_mode,
    ... )

    >>> # Get output data
    >>> result_data_sources = op.outputs.data_sources()
    >>> result_ip = op.outputs.ip()
    >>> result_port = op.outputs.port()
    """

    def __init__(
        self,
        mapdl_exe_path=None,
        working_dir=None,
        number_of_processes=None,
        number_of_threads=None,
        data_sources=None,
        server_mode=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mapdl::run", config=config, server=server)
        self._inputs = InputsRun(self)
        self._outputs = OutputsRun(self)
        if mapdl_exe_path is not None:
            self.inputs.mapdl_exe_path.connect(mapdl_exe_path)
        if working_dir is not None:
            self.inputs.working_dir.connect(working_dir)
        if number_of_processes is not None:
            self.inputs.number_of_processes.connect(number_of_processes)
        if number_of_threads is not None:
            self.inputs.number_of_threads.connect(number_of_threads)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if server_mode is not None:
            self.inputs.server_mode.connect(server_mode)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Solve in mapdl a dat/inp file and returns a datasources with the rst
file.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mapdl_exe_path",
                    type_names=["string"],
                    optional=True,
                    document=r"""""",
                ),
                1: PinSpecification(
                    name="working_dir",
                    type_names=["string"],
                    optional=True,
                    document=r"""""",
                ),
                2: PinSpecification(
                    name="number_of_processes",
                    type_names=["int32"],
                    optional=True,
                    document=r"""Set the number of MPI processes used for resolution (default is 2)""",
                ),
                3: PinSpecification(
                    name="number_of_threads",
                    type_names=["int32"],
                    optional=True,
                    document=r"""Set the number of threads used for resolution (default is 1)""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""data sources containing the input file.""",
                ),
                5: PinSpecification(
                    name="server_mode",
                    type_names=["bool"],
                    optional=True,
                    document=r"""used when a user includes commands in the input file allowing to launch DPF server inside MAPDL to interact with MAPDL using DPF client API""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""returns the data source if the server_mode pin is not set to yes""",
                ),
                1: PinSpecification(
                    name="ip",
                    type_names=["string"],
                    optional=False,
                    document=r"""returns the Ip if the server_mode pin is set to yes""",
                ),
                2: PinSpecification(
                    name="port",
                    type_names=["string"],
                    optional=False,
                    document=r"""returns a port when the server mode pin is set to yes""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server: AnyServerType = None) -> Config:
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server:
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.

        Returns
        -------
        config:
            A new Config instance equivalent to the default config for this operator.
        """
        return Operator.default_config(name="mapdl::run", server=server)

    @property
    def inputs(self) -> InputsRun:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsRun.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsRun:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsRun.
        """
        return super().outputs


class InputsRun(_Inputs):
    """Intermediate class used to connect user inputs to
    run operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.run()
    >>> my_mapdl_exe_path = str()
    >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
    >>> my_working_dir = str()
    >>> op.inputs.working_dir.connect(my_working_dir)
    >>> my_number_of_processes = int()
    >>> op.inputs.number_of_processes.connect(my_number_of_processes)
    >>> my_number_of_threads = int()
    >>> op.inputs.number_of_threads.connect(my_number_of_threads)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_server_mode = bool()
    >>> op.inputs.server_mode.connect(my_server_mode)
    """

    def __init__(self, op: Operator):
        super().__init__(run._spec().inputs, op)
        self._mapdl_exe_path = Input(run._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mapdl_exe_path)
        self._working_dir = Input(run._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._working_dir)
        self._number_of_processes = Input(run._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._number_of_processes)
        self._number_of_threads = Input(run._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._number_of_threads)
        self._data_sources = Input(run._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)
        self._server_mode = Input(run._spec().input_pin(5), 5, op, -1)
        self._inputs.append(self._server_mode)

    @property
    def mapdl_exe_path(self) -> Input:
        r"""Allows to connect mapdl_exe_path input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
        >>> # or
        >>> op.inputs.mapdl_exe_path(my_mapdl_exe_path)
        """
        return self._mapdl_exe_path

    @property
    def working_dir(self) -> Input:
        r"""Allows to connect working_dir input to the operator.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.working_dir.connect(my_working_dir)
        >>> # or
        >>> op.inputs.working_dir(my_working_dir)
        """
        return self._working_dir

    @property
    def number_of_processes(self) -> Input:
        r"""Allows to connect number_of_processes input to the operator.

        Set the number of MPI processes used for resolution (default is 2)

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.number_of_processes.connect(my_number_of_processes)
        >>> # or
        >>> op.inputs.number_of_processes(my_number_of_processes)
        """
        return self._number_of_processes

    @property
    def number_of_threads(self) -> Input:
        r"""Allows to connect number_of_threads input to the operator.

        Set the number of threads used for resolution (default is 1)

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.number_of_threads.connect(my_number_of_threads)
        >>> # or
        >>> op.inputs.number_of_threads(my_number_of_threads)
        """
        return self._number_of_threads

    @property
    def data_sources(self) -> Input:
        r"""Allows to connect data_sources input to the operator.

        data sources containing the input file.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def server_mode(self) -> Input:
        r"""Allows to connect server_mode input to the operator.

        used when a user includes commands in the input file allowing to launch DPF server inside MAPDL to interact with MAPDL using DPF client API

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> op.inputs.server_mode.connect(my_server_mode)
        >>> # or
        >>> op.inputs.server_mode(my_server_mode)
        """
        return self._server_mode


class OutputsRun(_Outputs):
    """Intermediate class used to get outputs from
    run operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.run()
    >>> # Connect inputs : op.inputs. ...
    >>> result_data_sources = op.outputs.data_sources()
    >>> result_ip = op.outputs.ip()
    >>> result_port = op.outputs.port()
    """

    def __init__(self, op: Operator):
        super().__init__(run._spec().outputs, op)
        self._data_sources = Output(run._spec().output_pin(0), 0, op)
        self._outputs.append(self._data_sources)
        self._ip = Output(run._spec().output_pin(1), 1, op)
        self._outputs.append(self._ip)
        self._port = Output(run._spec().output_pin(2), 2, op)
        self._outputs.append(self._port)

    @property
    def data_sources(self) -> Output:
        r"""Allows to get data_sources output of the operator

        returns the data source if the server_mode pin is not set to yes

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> # Get the output from op.outputs. ...
        >>> result_data_sources = op.outputs.data_sources()
        """
        return self._data_sources

    @property
    def ip(self) -> Output:
        r"""Allows to get ip output of the operator

        returns the Ip if the server_mode pin is set to yes

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> # Get the output from op.outputs. ...
        >>> result_ip = op.outputs.ip()
        """
        return self._ip

    @property
    def port(self) -> Output:
        r"""Allows to get port output of the operator

        returns a port when the server mode pin is set to yes

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.run()
        >>> # Get the output from op.outputs. ...
        >>> result_port = op.outputs.port()
        """
        return self._port
