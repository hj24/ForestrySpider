import gc
import functools


def disable_gc(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        gc.disable()
        res = func(*args, **kwargs)
        gc.enable()
        return res
    return inner