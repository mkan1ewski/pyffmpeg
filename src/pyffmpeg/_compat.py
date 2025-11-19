from pyffmpeg import __getattr__ as __init__getattr
from collections.abc import Callable, Sequence
from typing import Any
from pyffmpeg._run import run, run_async, compile
from pyffmpeg.utils import input, merge_outputs, get_args
import functools
from pyffmpeg.node import Stream, TypedStream, IndexedStream


def __getattr__(name: str) -> Callable[..., Any]:
    return wrap_stream_output(wrap_stream_input(__init__getattr(name)))


def wrap_stream_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_object = func(*args, **kwargs)
        if isinstance(return_object, Stream):
            return StreamWrapper(return_object)
        if isinstance(return_object, Sequence) and all(
            isinstance(stream, (Stream | TypedStream | IndexedStream))
            for stream in return_object
        ):
            return [StreamWrapper(stream) for stream in return_object]
        return return_object

    return wrapper


def wrap_stream_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = [arg.stream if isinstance(arg, StreamWrapper) else arg for arg in args]
        return func(*args, **kwargs)

    return wrapper


input = wrap_stream_output(input)


class StreamWrapper:
    def __init__(self, stream: Stream | TypedStream | IndexedStream):
        self.stream: Stream | TypedStream | IndexedStream = stream

    def __getattr__(self, name):
        if hasattr(self.stream, name):
            attr = getattr(self.stream, name)

            if callable(attr):
                return wrap_stream_input(wrap_stream_output(attr))
            if isinstance(attr, (TypedStream, IndexedStream)):
                return StreamWrapper(attr)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StreamWrapper):
            return NotImplemented
        return self.stream == other.stream

    def __hash__(self) -> int:
        return hash(self.stream)

    def __getitem__(self, key: str) -> "StreamWrapper":
        return StreamWrapper(self.stream[key])
