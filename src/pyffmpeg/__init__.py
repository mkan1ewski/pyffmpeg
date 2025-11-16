from pyffmpeg import _utils
from pyffmpeg.utils import input, merge_outputs, get_args
from pyffmpeg._run import run, run_async, compile
from pyffmpeg.errors import Error
from pyffmpeg.node import Stream, Node
from collections.abc import Callable
from typing import Any
import inspect


def __getattr__(name: str) -> Callable[..., Any]:
    def wrapper(obj: Stream | Node | list[Stream], *args, **kwargs) -> Any:
        target_obj = obj
        if isinstance(obj, (list, tuple)) and obj:
            target_obj = obj[0]
            inputs_list = obj[1:]
        if not isinstance(target_obj, (Stream, Node)):
            raise TypeError(
                f"Cannot call '{name}'. First argument "
                f"is '{type(obj)}', but must be Stream, Node or a list of Streams."
            )
        try:
            method = getattr(target_obj, name)
        except AttributeError:
            raise AttributeError(
                f"Module 'pyffmpeg' does not have a function '{name}' "
                f"and an object of type '{type(target_obj)}' does not have a method with that name."
            )
        sig = inspect.signature(method)
        if "inputs" in sig.parameters:
            args = (inputs_list, *args)
            return method(*args, **kwargs)
        else:
            return method(*args, **kwargs)

    return wrapper
