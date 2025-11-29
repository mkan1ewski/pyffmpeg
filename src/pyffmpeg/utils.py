from typing import Sequence

from pyffmpeg.node import (
    FilterMultiOutput,
    FilterNode,
    InputNode,
    OutputNode,
    Stream,
    MergedOutputNode,
    GraphSorter,
    CommandBuilder,
)


def input(path: str, **kwargs) -> Stream:
    """Creates input stream from a filename"""
    """Accepts input options through kwargs"""
    return InputNode(path, kwargs).output_streams[0]


def merge_outputs(*outputs: OutputNode) -> MergedOutputNode:
    """Creates multioutput object from many outputs"""
    return MergedOutputNode(outputs)


def get_args(
    output: OutputNode | Sequence[OutputNode] | MergedOutputNode, **global_options
) -> list[str]:
    """Creates command arguments for the output or a list of outputs"""
    if isinstance(output, Sequence):
        # output is reversed to satisfy tests order requirements
        output = MergedOutputNode(outputs=tuple(reversed(output)))
    sorter = GraphSorter(output)
    command_builder = CommandBuilder(
        sorter.sort(),
        output.global_options + output._compile_global_kwargs(global_options),
    )
    return command_builder.build_args()


def filter(
    stream_or_streams_list: Stream | list[Stream], filter_name: str, *args, **kwargs
) -> "Stream":
    """Custom filter with single or many inputs and a single output"""
    if isinstance(stream_or_streams_list, (list, tuple)):
        if stream_or_streams_list and isinstance(stream_or_streams_list[0], Stream):
            return stream_or_streams_list[0]._apply_filter(
                filter_name, args, kwargs, stream_or_streams_list
            )
    if isinstance(stream_or_streams_list, Stream):
        return stream_or_streams_list.filter(filter_name, *args, **kwargs)


def filter_multi_output(
    stream_or_streams_list: Stream | list[Stream], filter_name: str, *args, **kwargs
) -> "FilterMultiOutput":
    """Creates a custom filter allowing dynamic creation of output streams, accepts many inputs"""
    if isinstance(stream_or_streams_list, (list, tuple)):
        inputs = stream_or_streams_list
    elif isinstance(stream_or_streams_list, Stream):
        inputs = [stream_or_streams_list]
    node = FilterNode(
        filter_name=filter_name,
        postional_arguments=args,
        named_arguments=kwargs,
        inputs=inputs,
        num_output_streams=0,
    )
    return FilterMultiOutput(node)
