"""
hdf5dpf_generate_result_file

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


class hdf5dpf_generate_result_file(Operator):
    r"""Generate a dpf result file from provided information.


    Parameters
    ----------
    append_mode: bool, optional
        Experimental: Allow appending chunked data to the file. This disables fields container content deduplication.
    dataset_size_compression_threshold: int, optional
        Integer value that defines the minimum dataset size (in bytes) to use h5 native compression Applicable for arrays of floats, doubles and integers.
    h5_native_compression: int or DataTree, optional
        Integer value / DataTree that defines the h5 native compression used For Integer Input {0: No Compression (default); 1-9: GZIP Compression : 9 provides maximum compression but at the slowest speed.}For DataTree Input {type: None / GZIP / ZSTD; level: GZIP (1-9) / ZSTD (1-20); num_threads: ZSTD (>0)}
    export_floats: bool, optional
        converts double to float to reduce file size (default is true)
    filename: str
        name of the output file that will be generated (utf8).
    mesh_provider_out: MeshedRegion, optional
        defines the MeshedRegion that is exported and provided by MeshProvider.
    time_freq_support_out: TimeFreqSupport, optional
        defines the TimeFreqSupport that is exported and provided by TimeFreqSupportProvider.
    ansys_unit_system_id: int or ResultInfo, optional
        defines the unit system the results are exported with. A Result info can be input to also export Physics Type and Analysis Type.
    input_name1: str or Any, optional
        Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.
    input_name2: str or Any, optional
        Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.

    Returns
    -------
    data_sources: DataSources
        data_sources filled with the H5 generated file path.

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()

    >>> # Make input connections
    >>> my_append_mode = bool()
    >>> op.inputs.append_mode.connect(my_append_mode)
    >>> my_dataset_size_compression_threshold = int()
    >>> op.inputs.dataset_size_compression_threshold.connect(my_dataset_size_compression_threshold)
    >>> my_h5_native_compression = int()
    >>> op.inputs.h5_native_compression.connect(my_h5_native_compression)
    >>> my_export_floats = bool()
    >>> op.inputs.export_floats.connect(my_export_floats)
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_mesh_provider_out = dpf.MeshedRegion()
    >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)
    >>> my_time_freq_support_out = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support_out.connect(my_time_freq_support_out)
    >>> my_ansys_unit_system_id = int()
    >>> op.inputs.ansys_unit_system_id.connect(my_ansys_unit_system_id)
    >>> my_input_name1 = str()
    >>> op.inputs.input_name1.connect(my_input_name1)
    >>> my_input_name2 = str()
    >>> op.inputs.input_name2.connect(my_input_name2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file(
    ...     append_mode=my_append_mode,
    ...     dataset_size_compression_threshold=my_dataset_size_compression_threshold,
    ...     h5_native_compression=my_h5_native_compression,
    ...     export_floats=my_export_floats,
    ...     filename=my_filename,
    ...     mesh_provider_out=my_mesh_provider_out,
    ...     time_freq_support_out=my_time_freq_support_out,
    ...     ansys_unit_system_id=my_ansys_unit_system_id,
    ...     input_name1=my_input_name1,
    ...     input_name2=my_input_name2,
    ... )

    >>> # Get output data
    >>> result_data_sources = op.outputs.data_sources()
    """

    def __init__(
        self,
        append_mode=None,
        dataset_size_compression_threshold=None,
        h5_native_compression=None,
        export_floats=None,
        filename=None,
        mesh_provider_out=None,
        time_freq_support_out=None,
        ansys_unit_system_id=None,
        input_name1=None,
        input_name2=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="hdf5::h5dpf::make_result_file", config=config, server=server
        )
        self._inputs = InputsHdf5DpfGenerateResultFile(self)
        self._outputs = OutputsHdf5DpfGenerateResultFile(self)
        if append_mode is not None:
            self.inputs.append_mode.connect(append_mode)
        if dataset_size_compression_threshold is not None:
            self.inputs.dataset_size_compression_threshold.connect(
                dataset_size_compression_threshold
            )
        if h5_native_compression is not None:
            self.inputs.h5_native_compression.connect(h5_native_compression)
        if export_floats is not None:
            self.inputs.export_floats.connect(export_floats)
        if filename is not None:
            self.inputs.filename.connect(filename)
        if mesh_provider_out is not None:
            self.inputs.mesh_provider_out.connect(mesh_provider_out)
        if time_freq_support_out is not None:
            self.inputs.time_freq_support_out.connect(time_freq_support_out)
        if ansys_unit_system_id is not None:
            self.inputs.ansys_unit_system_id.connect(ansys_unit_system_id)
        if input_name1 is not None:
            self.inputs.input_name1.connect(input_name1)
        if input_name2 is not None:
            self.inputs.input_name2.connect(input_name2)

    @staticmethod
    def _spec() -> Specification:
        description = r"""Generate a dpf result file from provided information.
"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                -6: PinSpecification(
                    name="append_mode",
                    type_names=["bool"],
                    optional=True,
                    document=r"""Experimental: Allow appending chunked data to the file. This disables fields container content deduplication.""",
                ),
                -5: PinSpecification(
                    name="dataset_size_compression_threshold",
                    type_names=["int32"],
                    optional=True,
                    document=r"""Integer value that defines the minimum dataset size (in bytes) to use h5 native compression Applicable for arrays of floats, doubles and integers.""",
                ),
                -2: PinSpecification(
                    name="h5_native_compression",
                    type_names=["int32", "abstract_data_tree"],
                    optional=True,
                    document=r"""Integer value / DataTree that defines the h5 native compression used For Integer Input {0: No Compression (default); 1-9: GZIP Compression : 9 provides maximum compression but at the slowest speed.}For DataTree Input {type: None / GZIP / ZSTD; level: GZIP (1-9) / ZSTD (1-20); num_threads: ZSTD (>0)}""",
                ),
                -1: PinSpecification(
                    name="export_floats",
                    type_names=["bool"],
                    optional=True,
                    document=r"""converts double to float to reduce file size (default is true)""",
                ),
                0: PinSpecification(
                    name="filename",
                    type_names=["string"],
                    optional=False,
                    document=r"""name of the output file that will be generated (utf8).""",
                ),
                1: PinSpecification(
                    name="mesh_provider_out",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document=r"""defines the MeshedRegion that is exported and provided by MeshProvider.""",
                ),
                2: PinSpecification(
                    name="time_freq_support_out",
                    type_names=["time_freq_support"],
                    optional=True,
                    document=r"""defines the TimeFreqSupport that is exported and provided by TimeFreqSupportProvider.""",
                ),
                3: PinSpecification(
                    name="ansys_unit_system_id",
                    type_names=["int32", "result_info"],
                    optional=True,
                    document=r"""defines the unit system the results are exported with. A Result info can be input to also export Physics Type and Analysis Type.""",
                ),
                4: PinSpecification(
                    name="input_name",
                    type_names=["string", "any"],
                    optional=True,
                    document=r"""Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.""",
                ),
                5: PinSpecification(
                    name="input_name",
                    type_names=["string", "any"],
                    optional=True,
                    document=r"""Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document=r"""data_sources filled with the H5 generated file path.""",
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
        return Operator.default_config(
            name="hdf5::h5dpf::make_result_file", server=server
        )

    @property
    def inputs(self) -> InputsHdf5DpfGenerateResultFile:
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs:
            An instance of InputsHdf5DpfGenerateResultFile.
        """
        return super().inputs

    @property
    def outputs(self) -> OutputsHdf5DpfGenerateResultFile:
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs:
            An instance of OutputsHdf5DpfGenerateResultFile.
        """
        return super().outputs


class InputsHdf5DpfGenerateResultFile(_Inputs):
    """Intermediate class used to connect user inputs to
    hdf5dpf_generate_result_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
    >>> my_append_mode = bool()
    >>> op.inputs.append_mode.connect(my_append_mode)
    >>> my_dataset_size_compression_threshold = int()
    >>> op.inputs.dataset_size_compression_threshold.connect(my_dataset_size_compression_threshold)
    >>> my_h5_native_compression = int()
    >>> op.inputs.h5_native_compression.connect(my_h5_native_compression)
    >>> my_export_floats = bool()
    >>> op.inputs.export_floats.connect(my_export_floats)
    >>> my_filename = str()
    >>> op.inputs.filename.connect(my_filename)
    >>> my_mesh_provider_out = dpf.MeshedRegion()
    >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)
    >>> my_time_freq_support_out = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support_out.connect(my_time_freq_support_out)
    >>> my_ansys_unit_system_id = int()
    >>> op.inputs.ansys_unit_system_id.connect(my_ansys_unit_system_id)
    >>> my_input_name1 = str()
    >>> op.inputs.input_name1.connect(my_input_name1)
    >>> my_input_name2 = str()
    >>> op.inputs.input_name2.connect(my_input_name2)
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_generate_result_file._spec().inputs, op)
        self._append_mode = Input(
            hdf5dpf_generate_result_file._spec().input_pin(-6), -6, op, -1
        )
        self._inputs.append(self._append_mode)
        self._dataset_size_compression_threshold = Input(
            hdf5dpf_generate_result_file._spec().input_pin(-5), -5, op, -1
        )
        self._inputs.append(self._dataset_size_compression_threshold)
        self._h5_native_compression = Input(
            hdf5dpf_generate_result_file._spec().input_pin(-2), -2, op, -1
        )
        self._inputs.append(self._h5_native_compression)
        self._export_floats = Input(
            hdf5dpf_generate_result_file._spec().input_pin(-1), -1, op, -1
        )
        self._inputs.append(self._export_floats)
        self._filename = Input(
            hdf5dpf_generate_result_file._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._filename)
        self._mesh_provider_out = Input(
            hdf5dpf_generate_result_file._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mesh_provider_out)
        self._time_freq_support_out = Input(
            hdf5dpf_generate_result_file._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._time_freq_support_out)
        self._ansys_unit_system_id = Input(
            hdf5dpf_generate_result_file._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._ansys_unit_system_id)
        self._input_name1 = Input(
            hdf5dpf_generate_result_file._spec().input_pin(4), 4, op, 0
        )
        self._inputs.append(self._input_name1)
        self._input_name2 = Input(
            hdf5dpf_generate_result_file._spec().input_pin(5), 5, op, 1
        )
        self._inputs.append(self._input_name2)

    @property
    def append_mode(self) -> Input:
        r"""Allows to connect append_mode input to the operator.

        Experimental: Allow appending chunked data to the file. This disables fields container content deduplication.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.append_mode.connect(my_append_mode)
        >>> # or
        >>> op.inputs.append_mode(my_append_mode)
        """
        return self._append_mode

    @property
    def dataset_size_compression_threshold(self) -> Input:
        r"""Allows to connect dataset_size_compression_threshold input to the operator.

        Integer value that defines the minimum dataset size (in bytes) to use h5 native compression Applicable for arrays of floats, doubles and integers.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.dataset_size_compression_threshold.connect(my_dataset_size_compression_threshold)
        >>> # or
        >>> op.inputs.dataset_size_compression_threshold(my_dataset_size_compression_threshold)
        """
        return self._dataset_size_compression_threshold

    @property
    def h5_native_compression(self) -> Input:
        r"""Allows to connect h5_native_compression input to the operator.

        Integer value / DataTree that defines the h5 native compression used For Integer Input {0: No Compression (default); 1-9: GZIP Compression : 9 provides maximum compression but at the slowest speed.}For DataTree Input {type: None / GZIP / ZSTD; level: GZIP (1-9) / ZSTD (1-20); num_threads: ZSTD (>0)}

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.h5_native_compression.connect(my_h5_native_compression)
        >>> # or
        >>> op.inputs.h5_native_compression(my_h5_native_compression)
        """
        return self._h5_native_compression

    @property
    def export_floats(self) -> Input:
        r"""Allows to connect export_floats input to the operator.

        converts double to float to reduce file size (default is true)

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.export_floats.connect(my_export_floats)
        >>> # or
        >>> op.inputs.export_floats(my_export_floats)
        """
        return self._export_floats

    @property
    def filename(self) -> Input:
        r"""Allows to connect filename input to the operator.

        name of the output file that will be generated (utf8).

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.filename.connect(my_filename)
        >>> # or
        >>> op.inputs.filename(my_filename)
        """
        return self._filename

    @property
    def mesh_provider_out(self) -> Input:
        r"""Allows to connect mesh_provider_out input to the operator.

        defines the MeshedRegion that is exported and provided by MeshProvider.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.mesh_provider_out.connect(my_mesh_provider_out)
        >>> # or
        >>> op.inputs.mesh_provider_out(my_mesh_provider_out)
        """
        return self._mesh_provider_out

    @property
    def time_freq_support_out(self) -> Input:
        r"""Allows to connect time_freq_support_out input to the operator.

        defines the TimeFreqSupport that is exported and provided by TimeFreqSupportProvider.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.time_freq_support_out.connect(my_time_freq_support_out)
        >>> # or
        >>> op.inputs.time_freq_support_out(my_time_freq_support_out)
        """
        return self._time_freq_support_out

    @property
    def ansys_unit_system_id(self) -> Input:
        r"""Allows to connect ansys_unit_system_id input to the operator.

        defines the unit system the results are exported with. A Result info can be input to also export Physics Type and Analysis Type.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.ansys_unit_system_id.connect(my_ansys_unit_system_id)
        >>> # or
        >>> op.inputs.ansys_unit_system_id(my_ansys_unit_system_id)
        """
        return self._ansys_unit_system_id

    @property
    def input_name1(self) -> Input:
        r"""Allows to connect input_name1 input to the operator.

        Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.input_name1.connect(my_input_name1)
        >>> # or
        >>> op.inputs.input_name1(my_input_name1)
        """
        return self._input_name1

    @property
    def input_name2(self) -> Input:
        r"""Allows to connect input_name2 input to the operator.

        Set of even and odd pins to serialize results. Odd pins (4, 6, 8...) are strings, and they represent the names of the results to be serialized. Even pins (5, 7, 9...) are DPF types, and they represent the results to be serialized. They should go in pairs (for each result name, there should be a result) and connected sequentially.

        Returns
        -------
        input:
            An Input instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> op.inputs.input_name2.connect(my_input_name2)
        >>> # or
        >>> op.inputs.input_name2(my_input_name2)
        """
        return self._input_name2


class OutputsHdf5DpfGenerateResultFile(_Outputs):
    """Intermediate class used to get outputs from
    hdf5dpf_generate_result_file operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
    >>> # Connect inputs : op.inputs. ...
    >>> result_data_sources = op.outputs.data_sources()
    """

    def __init__(self, op: Operator):
        super().__init__(hdf5dpf_generate_result_file._spec().outputs, op)
        self._data_sources = Output(
            hdf5dpf_generate_result_file._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._data_sources)

    @property
    def data_sources(self) -> Output:
        r"""Allows to get data_sources output of the operator

        data_sources filled with the H5 generated file path.

        Returns
        -------
        output:
            An Output instance for this pin.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.hdf5dpf_generate_result_file()
        >>> # Get the output from op.outputs. ...
        >>> result_data_sources = op.outputs.data_sources()
        """
        return self._data_sources
