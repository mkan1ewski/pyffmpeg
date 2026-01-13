from pyffmpeg import _utils
from pyffmpeg.io import input, merge_outputs, get_args, filter, filter_multi_output
from pyffmpeg._run import run, compile
from pyffmpeg.errors import Error
from pyffmpeg.node import Stream, Node
from pyffmpeg.probe import probe
from collections.abc import Callable
from typing import Any


def __getattr__(name: str) -> Callable[..., Any]:
    def wrapper(obj: Stream | Node | list[Stream], *args, **kwargs) -> Any:
        target_obj = obj
        inputs_list = []

        if isinstance(obj, (list, tuple)) and obj:
            target_obj = obj[0]
            inputs_list = obj[1:]

        if not isinstance(target_obj, (Stream, Node)):
            raise TypeError(
                f"Cannot call '{name}'. First argument is '{type(obj)}', "
                f"but must be Stream, Node or a list of Streams."
            )

        try:
            method = getattr(target_obj, name)
        except AttributeError:
            raise AttributeError(
                f"Module 'pyffmpeg' does not have a function '{name}' "
                f"and an object of type '{type(target_obj)}' does not have a method with that name."
            )

        return method(*inputs_list, *args, **kwargs)

    return wrapper
