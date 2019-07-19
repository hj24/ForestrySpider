from config.db.settings import DATABASE
from peewee import *
from playhouse.mysql_ext import JSONField
from utils.decorators.db import auto_connect

db = DATABASE['mysqldb']

class Test3(Model):

    name = CharField(max_length=10, unique=True)
    content = JSONField()

    class Meta:
        database = db

# def create_table():
#     with db:
#         db.create_tables([Test2])

auto_connect(db=db)
def save():
    Test3.create_table()
    person, created = Test3.get_or_create(name='hj', defaults={'content': json_obj})
    person1, created1 = Test3.get_or_create(name='爸爸', defaults={'content': json_obj})
    print(person, created)

if __name__ == '__main__':

    from config.urls.zgzwconfig import ZgzwConfig

    zg = ZgzwConfig()

    json_obj = zg.parser()

    # db.connect()
    # Test3.create_table()
    # # create_table()
    # Test3.create(name='hj', content=json_obj)
    # Test3.create(name='ynm', content=json_obj)
    # db.close()
    save()