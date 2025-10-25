from pyffmpeg.utils import input, merge_outputs, get_args


def __getattr__(name):
    def wrapper(obj, *args, **kwargs):
        return getattr(obj, name)(*args, **kwargs)

    return wrapper
