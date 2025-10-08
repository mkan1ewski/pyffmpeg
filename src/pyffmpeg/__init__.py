from pyffmpeg.utils import input


def __getattr__(name):
    def wrapper(obj, *args, **kwargs):
        return getattr(obj, name)(*args, **kwargs)

    return wrapper
