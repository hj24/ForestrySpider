import time
import functools

def counter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()

        res = func(*args, **kwargs)

        end_time = time.time()
        return res

    return inner