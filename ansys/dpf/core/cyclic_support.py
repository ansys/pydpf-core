"""
Cyclic Support
==============
"""
import grpc

from ansys import dpf
from ansys.grpc.dpf import cyclic_support_pb2, cyclic_support_pb2_grpc
from ansys.grpc.dpf import base_pb2, support_pb2
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf import core
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.scoping import Scoping


class CyclicSupport:
    """Represents a cyclic support, which describes a model with cyclic symmetry.

    The model has the necessary data for cyclic (and multistage) expansion.

    Parameters
    ----------
    cyclic_support : ansys.grpc.dpf.cyclic_support_pb2.CyclicSupport message
        Cyclic support.
    server : DPFServer , optional
        Server with the channel connected to the remote or local instance. The default is
        ``None``, in which case an attempt is made to use the the global server.

    Examples
    --------
    Get a cyclic support from a model.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> multi_stage = examples.download_multi_stage_cyclic_result()
    >>> model = dpf.Model(multi_stage)
    >>> result_info = model.metadata.result_info
    >>> cyc_support = result_info.cyclic_support
    >>> cyc_support.num_sectors()
    6
    >>> cyc_support.num_stages
    2

    """

    def __init__(self, cyclic_support, server=None):
        """Initialize time frequency support with its `TimeFreqSupport` message (if possible)."""
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()
        self._message = cyclic_support

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

    @property
    def num_stages(self) -> int:
        """Number of cyclic stages in the model

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> cyc_support.num_stages
        2

        Returns
        -------
        int
            Number of cyclic stages in the model.
        """
        return self._stub.List(self._message).num_stages

    def num_sectors(self, stage_num=0) -> int:
        """Number of sectors to expand on 360 degrees.

        Parameters
        ----------
        stage_num : int , optional
            Number of the stages required (from 0 to num_stages).

        Returns
        -------
        int
            Number of sectors to expand on 360 degrees.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> cyc_support.num_sectors(0)
        6
        >>> cyc_support.num_sectors(1)
        12

        """
        return self._stub.List(self._message).stage_infos[stage_num].num_sectors

    def base_nodes_scoping(self, stage_num=0) -> int:
        """Retrieve a nodal scoping containing node IDs in the
        base sector of the given stage.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        base_nodes_scoping : Scoping
            Nodes IDs in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> base = cyc_support.base_nodes_scoping(0)

        """
        return Scoping(
            scoping=self._stub.List(self._message)
            .stage_infos[stage_num]
            .base_nodes_scoping,
            server=self._server,
        )

    def base_elements_scoping(self, stage_num=0) -> int:
        """Retrieve an elemental scoping containing elements IDs in the
        base sector of the given stage.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        base_elements_scoping : Scoping
            Elements ids in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> base = cyc_support.base_elements_scoping(stage_num=1)

        """
        return Scoping(
            scoping=self._stub.List(self._message)
            .stage_infos[stage_num]
            .base_elements_scoping,
            server=self._server,
        )

    def sectors_set_for_expansion(self, stage_num=0) -> int:
        """Retrieve a sector's scoping of the already expanded results and mesh or the list of sectors that will
        be expanded by default.

        A sector's scoping starts from 0, with the maximum equal to num_sectors-1.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to max = num_sectors-1).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> print(cyc_support.sectors_set_for_expansion(stage_num=1).ids)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        """
        return Scoping(
            scoping=self._stub.List(self._message)
            .stage_infos[stage_num]
            .sectors_for_expansion,
            server=self._server,
        )

    def expand_node_id(self, node_id, sectors=None, stage_num=0):
        """Retrieve the node IDs corresponding to the base sector node ID given in the input
        after expansion.

        Parameters
        ----------
        node_id : int
            Base sector's node ID to expand.
        sectors : Scoping , list of int, optional
            List of sectors to expand (from 0 to ``num_sectors - 1``).
            The default is ``None``, in which case all sectors are expanded.
        stage_num : int, optional
            Number of the stage required (from 0 to ``num_stages``).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to ``num_sectors - 1``).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> print(cyc_support.expand_node_id(1,stage_num=0).ids)
        [1, 3596, 5816, 8036, 10256, 12476]

        """
        if isinstance(sectors, list):
            sectors = Scoping(ids=sectors, location="sectors", server=self._server)

        request = cyclic_support_pb2.GetExpandedIdsRequest()
        request.support.CopyFrom(self._message)
        request.node_id = node_id
        request.stage_num = stage_num
        if sectors:
            request.sectors_to_expand.CopyFrom(sectors._message)
        return Scoping(
            scoping=self._stub.GetExpandedIds(request).expanded_ids, server=self._server
        )

    def expand_element_id(self, element_id, sectors=None, stage_num=0):
        """Retrieves the element IDs corresponding to the base sector element ID given in the input
        after expansion.

        Parameters
        ----------
        element_id : int
            Base sector's element ID to expand.
        sectors : Scoping or list of int, optional
            List of sectors to expand (from 0 to ``num_sectors - 1``).
            The default is ``None``, in which case all sectors are expanded.
        stage_num : int, optional
            Number of the stage required (from 0 to ``num_stages``).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to ``num_sectors - 1``).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> print(cyc_support.expand_element_id(1,stage_num=0).ids)
        [1, 1558, 2533, 3508, 4483, 5458]

        """
        if isinstance(sectors, list):
            sectors = Scoping(ids=sectors, location="sectors", server=self._server)

        request = cyclic_support_pb2.GetExpandedIdsRequest()
        request.support.CopyFrom(self._message)
        request.element_id = element_id
        request.stage_num = stage_num
        if sectors:
            request.sectors_to_expand.CopyFrom(sectors._message)
        return Scoping(
            scoping=self._stub.GetExpandedIds(request).expanded_ids, server=self._server
        )

    def _connect(self):
        """Connect to the grpc service"""
        return cyclic_support_pb2_grpc.CyclicSupportServiceStub(self._server.channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass
