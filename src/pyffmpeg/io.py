from typing import Sequence, Any

from pyffmpeg.node import (
    FilterMultiOutput,
    FilterNode,
    InputNode,
    RunnableNode,
    OutputNode,
    Stream,
    MergedOutputNode,
    GraphSorter,
    CommandBuilder,
)


def input(
    filename: str,
    format: str | None = None,
    ss: str | float | None = None,
    t: str | float | None = None,
    to: str | float | None = None,
    r: str | int | float | None = None,
    video_size: str | tuple[int, int] | None = None,
    pix_fmt: str | None = None,
    hwaccel: str | None = None,
    loop: bool | int | None = None,
    re: bool = False,
    **kwargs,
) -> Stream:
    """Creates an input stream from a filename with optional input-specific flags.

    This function serves as the entry point for creating a processing graph.
    It accepts common FFmpeg input options as explicit arguments.
    Less common options can be passed via kwargs.

    Args:
        filename (str): Path to the input file, URL, or device.
        format (str | None): Force input format (ffmpeg flag: ``-f``).
            Example: ``'image2'``, ``'alsa'``, ``'v4l2'``, ``'rawvideo'``.
        ss (str | float | None): Seeks in this input file to position.
            Note: When used as an input option, this seeks BEFORE decoding
            (fast but less accurate).
        t (str | float | None): Limit the duration of data read from the input file.
        to (str | float | None): Stop reading the input after a specific time position.
        r (str | int | float | None): Set frame rate (Hz value, fraction or abbreviation).
            Crucial for raw video or image sequences.
        video_size (str | tuple[int, int] | None): Set frame size.
            Can be a string (e.g., ``'1920x1080'``) or a tuple ``(1920, 1080)``.
            Required for raw video.
        pix_fmt (str | None): Set input pixel format. Required for raw video (e.g., ``'yuv420p'``).
        hwaccel (str | None): Use hardware acceleration to decode the matching stream(s).
            Example: ``'cuda'``, ``'videotoolbox'``, ``'vaapi'``.
        loop (bool | int | None): Loop over the input stream. Useful for images.
            Set to ``True`` or ``1`` to enable looping.
        re (bool): Read input at native frame rate (ffmpeg flag: ``-re``).
            Mainly used for simulating a grab device or live input stream.
            Defaults to ``False``.
        **kwargs: Additional input options specific to the demuxer or decoder.
            Example: ``input("file.mp4", log_level="debug")``.

    Returns:
        Stream: Output stream of the created InputNode.
    """
    options: dict[str, Any] = kwargs.copy()

    if re:
        options["re"] = None

    if format is not None:
        options["format"] = format
    if ss is not None:
        options["ss"] = ss
    if t is not None:
        options["t"] = t
    if to is not None:
        options["to"] = to
    if r is not None:
        options["r"] = r
    if video_size is not None:
        options["video_size"] = video_size
    if pix_fmt is not None:
        options["pix_fmt"] = pix_fmt
    if hwaccel is not None:
        options["hwaccel"] = hwaccel
    if loop is not None:
        options["loop"] = loop

    return InputNode(filename, options).output_streams[0]


def merge_outputs(*nodes: "RunnableNode") -> "MergedOutputNode":
    """
    Groups multiple runnable nodes (outputs or sinks) into a single execution unit.

    Args:
        *nodes (RunnableNode): Variable list of graph endpoints. Accepts both standard OutputNode
            and SinkNode objects.

    Returns:
        MergedOutputNode: An aggregate object that can be run as a single process.
    """
    return MergedOutputNode(nodes)


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
        positional_arguments=args,
        named_arguments=kwargs,
        inputs=inputs,
        num_output_streams=0,
    )
    return FilterMultiOutput(node)
