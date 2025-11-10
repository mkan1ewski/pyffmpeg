from pyffmpeg import _utils
from pyffmpeg.utils import input, merge_outputs, get_args
from pyffmpeg._run import run, compile
from pyffmpeg.node import Stream, Node
from collections.abc import Callable
from typing import Any


def __getattr__(name: str) -> Callable[..., Any]:
    def wrapper(obj: Stream | Node, *args, **kwargs) -> Any:
        return getattr(obj, name)(*args, **kwargs)

    return wrapper
