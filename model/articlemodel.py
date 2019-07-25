from peewee import *
from playhouse.mysql_ext import JSONField

from config.db.settings import DATABASE


db = DATABASE['mysqldb']

class BaseModel(Model):

    class Meta:
        database = db

class Article(BaseModel):
    """
    文章模型

    字段:
        id      - 默认的自增型主键 id
        title   - 文章标题
        type    - 类别，区分知网和中国银杏网
        tag     - 标签，方便前端按页面查询
        content - json格式的内容，包含了文章内容来源等在内的所有信息
    """
    
    title = CharField(max_length=100, unique=True)
    type = IntegerField()
    tag = CharField(max_length=20)
    content = JSONField()

if not Article.table_exists():
    Article.create_table()