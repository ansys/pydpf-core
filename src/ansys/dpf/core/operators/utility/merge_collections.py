"""
merge_collections
=================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class merge_collections(Operator):
    """Merges a set of collections into a unique one.

    Parameters
    ----------
    collections1 : AnyCollection
        A vector of collections to merge or
        collections from pin 0 to ...
    collections2 : AnyCollection
        A vector of collections to merge or
        collections from pin 0 to ...


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.merge_collections()

    >>> # Make input connections
    >>> my_collections1 = dpf.AnyCollection()
    >>> op.inputs.collections1.connect(my_collections1)
    >>> my_collections2 = dpf.AnyCollection()
    >>> op.inputs.collections2.connect(my_collections2)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.merge_collections(
    ...     collections1=my_collections1,
    ...     collections2=my_collections2,
    ... )

    >>> # Get output data
    >>> result_merged_collections = op.outputs.merged_collections()
    """

    def __init__(self, collections1=None, collections2=None, config=None, server=None):
        super().__init__(name="merge::any_collection", config=config, server=server)
        self._inputs = InputsMergeCollections(self)
        self._outputs = OutputsMergeCollections(self)
        if collections1 is not None:
            self.inputs.collections1.connect(collections1)
        if collections2 is not None:
            self.inputs.collections2.connect(collections2)

    @staticmethod
    def _spec():
        description = """Merges a set of collections into a unique one."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="collections",
                    type_names=["any_collection"],
                    optional=False,
                    document="""A vector of collections to merge or
        collections from pin 0 to ...""",
                ),
                1: PinSpecification(
                    name="collections",
                    type_names=["any_collection"],
                    optional=False,
                    document="""A vector of collections to merge or
        collections from pin 0 to ...""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="merged_collections",
                    type_names=["any_collection"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="merge::any_collection", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeCollections
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMergeCollections
        """
        return super().outputs


class InputsMergeCollections(_Inputs):
    """Intermediate class used to connect user inputs to
    merge_collections operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_collections()
    >>> my_collections1 = dpf.AnyCollection()
    >>> op.inputs.collections1.connect(my_collections1)
    >>> my_collections2 = dpf.AnyCollection()
    >>> op.inputs.collections2.connect(my_collections2)
    """

    def __init__(self, op: Operator):
        super().__init__(merge_collections._spec().inputs, op)
        self._collections1 = Input(merge_collections._spec().input_pin(0), 0, op, 0)
        self._inputs.append(self._collections1)
        self._collections2 = Input(merge_collections._spec().input_pin(1), 1, op, 1)
        self._inputs.append(self._collections2)

    @property
    def collections1(self):
        """Allows to connect collections1 input to the operator.

        A vector of collections to merge or
        collections from pin 0 to ...

        Parameters
        ----------
        my_collections1 : AnyCollection

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_collections()
        >>> op.inputs.collections1.connect(my_collections1)
        >>> # or
        >>> op.inputs.collections1(my_collections1)
        """
        return self._collections1

    @property
    def collections2(self):
        """Allows to connect collections2 input to the operator.

        A vector of collections to merge or
        collections from pin 0 to ...

        Parameters
        ----------
        my_collections2 : AnyCollection

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_collections()
        >>> op.inputs.collections2.connect(my_collections2)
        >>> # or
        >>> op.inputs.collections2(my_collections2)
        """
        return self._collections2


class OutputsMergeCollections(_Outputs):
    """Intermediate class used to get outputs from
    merge_collections operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.merge_collections()
    >>> # Connect inputs : op.inputs. ...
    >>> result_merged_collections = op.outputs.merged_collections()
    """

    def __init__(self, op: Operator):
        super().__init__(merge_collections._spec().outputs, op)
        self._merged_collections = Output(
            merge_collections._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._merged_collections)

    @property
    def merged_collections(self):
        """Allows to get merged_collections output of the operator

        Returns
        ----------
        my_merged_collections : AnyCollection

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.merge_collections()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_collections = op.outputs.merged_collections()
        """  # noqa: E501
        return self._merged_collections