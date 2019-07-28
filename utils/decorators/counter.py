import time
import functools
import logging.config

from config.log.settings import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('utils')

def counter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        logger.info('%s 用时: %s', func.__name__, end_time - start_time)
        return res
    return inner