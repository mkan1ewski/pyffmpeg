import inspect
import functools
from typing import Any
from collections.abc import Callable, Sequence
from pyffmpeg._run import run, compile
from pyffmpeg import _run
from pyffmpeg._utils import escape_text_content
from pyffmpeg.io import input, merge_outputs, get_args
from pyffmpeg.probe import probe
from pyffmpeg.errors import Error
from pyffmpeg.node import (
    Node,
    OutputNode,
    Stream,
    TypedStream,
    IndexedStream,
    FilterNode,
    FilterMultiOutput,
)


def __getattr__(name: str) -> Callable[..., Any]:
    """
    Lets call methods of StreamCompatWrapper or Node as a standalone functions.
    First argument should be of type StreamCompatWrapper, Node or list list of StreamCompatWrapper.
    """

    def wrapper(
        obj: StreamCompatWrapper | Node | list[StreamCompatWrapper], *args, **kwargs
    ) -> Any:
        target_obj = obj
        if isinstance(obj, (list, tuple)) and obj:
            target_obj = obj[0]
            inputs_list = obj[1:]
        if not isinstance(target_obj, (StreamCompatWrapper, Node)):
            raise TypeError(
                f"Cannot call '{name}'. First argument "
                f"is '{type(obj)}', but must be StreamCompatWrapper, Node or a list of StreamCompatWrapper."
            )
        try:
            method = getattr(target_obj, name)
        except AttributeError:
            raise AttributeError(
                f"Module 'pyffmpeg._compat' does not have a function '{name}' "
                f"and an object of type '{type(target_obj)}' does not have a method with that name."
            )
        sig = inspect.signature(method)
        if "inputs" in sig.parameters:
            args = (inputs_list, *args)
            return method(*args, **kwargs)
        else:
            return method(*args, **kwargs)

    return wrapper


def wrap_stream_output(func):
    """Wraps output of func which is expected to be a stream or a sequence of streams in a StreamCompatWrapper"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_object = func(*args, **kwargs)
        if isinstance(return_object, Stream):
            return StreamCompatWrapper(return_object)
        if isinstance(return_object, Sequence) and all(
            isinstance(stream, (Stream | TypedStream | IndexedStream))
            for stream in return_object
        ):
            return [StreamCompatWrapper(stream) for stream in return_object]
        return return_object

    return wrapper


def wrap_stream_input(func):
    """Converts any argument of type StreamCompatWrapper to stream it contains and calls func"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = [
            arg.stream if isinstance(arg, StreamCompatWrapper) else arg for arg in args
        ]
        return func(*args, **kwargs)

    return wrapper


input = wrap_stream_output(input)


class StreamCompatWrapper:
    """Encapsulates the stream to invoke its methods underneath while providing backward compatible API."""

    def __init__(self, stream: Stream | TypedStream | IndexedStream):
        self.stream: Stream | TypedStream | IndexedStream = stream

    def __getattr__(self, name):
        """Returns wrapped stream method or wrapped stream attribute."""
        if hasattr(self.stream, name):
            attr = getattr(self.stream, name)

            if callable(attr):
                return wrap_stream_input(wrap_stream_output(attr))
            if isinstance(attr, (TypedStream, IndexedStream)):
                return StreamCompatWrapper(attr)
            if isinstance(attr, Sequence) and all(isinstance(x, Stream) for x in attr):
                return [StreamCompatWrapper(stream) for stream in attr]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StreamCompatWrapper):
            return NotImplemented
        return self.stream == other.stream

    def __hash__(self) -> int:
        return hash(self.stream)

    def __getitem__(self, key: str) -> "StreamCompatWrapper":
        return StreamCompatWrapper(self.stream[key])

    @wrap_stream_input
    def output(self, *args, **kwargs) -> "OutputNode":
        streams = []
        filename = None
        streams.append(self)

        for arg in args:
            if isinstance(arg, Stream):
                streams.append(arg)
            elif isinstance(arg, str):
                filename = arg
            else:
                raise TypeError(f"Unexpected argument type: {type(arg)}")

        if not filename:
            raise ValueError("No output filename provided to output()")

        return OutputNode(filename, streams, output_options=kwargs)

    def filter(self, filter_name: str, *args, **kwargs) -> "StreamCompatWrapper":
        """Custom filter with a single input and a single output"""
        return StreamCompatWrapper(
            self.stream._apply_filter(filter_name, args, kwargs)[0]
        )

    @wrap_stream_output
    @wrap_stream_input
    def scale(self, height: int, width: int) -> "Stream":
        """Scales to width and height."""
        return self._apply_filter(
            "scale", named_arguments={"height": str(height), "width": str(width)}
        )[0]

    @wrap_stream_output
    @wrap_stream_input
    def split(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical streams."""
        return self._apply_filter(
            "split", postional_arguments=(num_outputs,), num_output_streams=num_outputs
        )

    @wrap_stream_output
    @wrap_stream_input
    def asplit(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical audio streams."""
        return self._apply_filter(
            "asplit", postional_arguments=(num_outputs,), num_output_streams=num_outputs
        )

    @wrap_stream_output
    @wrap_stream_input
    def overlay(
        self,
        overlay_stream: "Stream",
        x: int | None = None,
        y: int | None = None,
        eof_action: str = "repeat",
    ) -> "Stream":
        """Overlay another video stream on top of this one."""
        named_arguments = {"eof_action": eof_action}
        if x:
            named_arguments["x"] = str(x)
        if y:
            named_arguments["y"] = str(y)

        return self._apply_filter(
            "overlay",
            named_arguments=named_arguments,
            inputs=[self, overlay_stream],
        )[0]

    @wrap_stream_output
    @wrap_stream_input
    def trim(self, **kwargs) -> "Stream":
        return self._apply_filter("trim", named_arguments=kwargs)[0]

    @wrap_stream_output
    @wrap_stream_input
    def vflip(self) -> "Stream":
        """Flip the input video vertically"""
        return self._apply_filter(filter_name="vflip")[0]

    @wrap_stream_output
    @wrap_stream_input
    def hflip(self) -> "Stream":
        """Flip the input video horizontally"""
        return self._apply_filter(filter_name="hflip")[0]

    @wrap_stream_output
    @wrap_stream_input
    def crop(self, x: int, y: int, width: int, height: int) -> "Stream":
        """Crop the input video to given dimensions"""
        return self._apply_filter("crop", postional_arguments=(width, height, x, y))[0]

    @wrap_stream_output
    @wrap_stream_input
    def concat(self, *streams: "Stream", **kwargs) -> "Stream":
        """Concatenate audio and video streams, joining them together one after the other"""
        video_stream_count = kwargs.get("v", 1)
        audio_stream_count = kwargs.get("a", 0)
        output_stream_count = video_stream_count + audio_stream_count
        input_stream_count = int(len([self, *streams]))
        if (input_stream_count % output_stream_count) != 0:
            raise ValueError(
                f"Expected concat input streams to have length multiple of {output_stream_count} (v={video_stream_count}, a={audio_stream_count}); got {input_stream_count}"
            )
        kwargs["n"] = int(input_stream_count / output_stream_count)
        return self._apply_filter(
            "concat",
            named_arguments=kwargs,
            inputs=[self, *streams],
            num_output_streams=output_stream_count,
        )[0]

    @wrap_stream_output
    @wrap_stream_input
    def drawbox(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: str,
        thickness: int | None = None,
    ) -> "Stream":
        """Draw a colored box on the input image"""
        return self._apply_filter(
            "drawbox",
            postional_arguments=(x, y, width, height, color),
            named_arguments={"t": str(thickness)},
        )[0]

    @wrap_stream_output
    @wrap_stream_input
    def drawtext(self, text: str, **kwargs) -> "Stream":
        kwargs["text"] = escape_text_content(text)
        return self._apply_filter("drawtext", named_arguments=kwargs)[0]


def filter(
    stream_spec: list[StreamCompatWrapper] | StreamCompatWrapper,
    filter_name: str,
    *args,
    **kwargs,
) -> StreamCompatWrapper:
    if isinstance(stream_spec, StreamCompatWrapper):
        stream_spec = [stream_spec.stream]
    if all(isinstance(s, StreamCompatWrapper) for s in stream_spec):
        stream_spec = [s.stream for s in stream_spec]
    return StreamCompatWrapper(
        stream_spec[0]._apply_filter(filter_name, args, kwargs, inputs=stream_spec)[0]
    )


def filter_multi_output(
    stream_spec: list[StreamCompatWrapper] | StreamCompatWrapper,
    filter_name: str,
    *args,
    **kwargs,
) -> StreamCompatWrapper:
    if isinstance(stream_spec, StreamCompatWrapper):
        stream_spec = [stream_spec.stream]
    if all(isinstance(s, StreamCompatWrapper) for s in stream_spec):
        stream_spec = [s.stream for s in stream_spec]
    node = FilterNode(
        filter_name=filter_name,
        positional_arguments=args,
        named_arguments=kwargs,
        inputs=stream_spec,
        num_output_streams=0,
    )
    return FilterMultiOutput(node)
