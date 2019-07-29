import functools
from peewee import *

from config.db.settings import DATABASE


db = DATABASE['mysqldb']

def auto_connect(*, db):

    def decorate(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                db.connect()
            except (OperationalError, Exception):
                pass
            res = func(*args, **kwargs)
            try:
                db.close()
            except (OperationalError, Exception):
                pass
            return res
        return inner

    return decorate