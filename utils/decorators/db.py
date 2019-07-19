import functools

from config.db.settings import DATABASE


db = DATABASE['mysqldb']

def auto_connect(*, db):

    def decorate(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            db.connect()
            res = func(*args, **kwargs)
            db.close()
            return res
        return inner

    return decorate