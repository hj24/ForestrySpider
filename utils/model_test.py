from config.db.settings import DATABASE
from peewee import *
from peewee import chunked
from playhouse.mysql_ext import JSONField
from utils.decorators.db import auto_connect
from utils.decorators.counter import counter

db = DATABASE['mysqldb']

class Test3(Model):

    title = CharField(max_length=100, unique=True)
    type = IntegerField()
    tag = CharField(max_length=20)
    content = JSONField()

    class Meta:
        database = db

# def create_table():
#     with db:
#         db.create_tables([Test2])

@counter
def save(json_obj):
    # Test3.create_table()
    # person, created = Test3.get_or_create(name='嘿嘿', defaults={'content': json_obj})
    # person1, created1 = Test3.get_or_create(name='爸爸', defaults={'content': json_obj})
    data = [{'title': str(i), 'type': 1, 'tag': '媒体报道', 'content': '{"title": "银杏叶也能做枕头了？好处还不少 ", "summary": "\\n<p>\u3000\u3000银杏树，又叫白果树，是一种古老的植物", "detail": "\\n<p>\u3000\u3000银杏树，又叫白果树，是一种古老的植物，银杏树不仅是一种观赏价值很高的植物，而且它的果实和叶子都有很高的药用价值。但是你知道吗?银杏的叶子也可以用来制作枕头了，而且还有独到的好处，我们平时使用的枕头几乎没有听说过用银杏叶做枕头，是不是觉得很神奇?接下来我们就一起看看用银杏叶做的枕头都有哪些好处吧。</p><p>\u3000\u30001. \\r\\n银杏叶枕头有一股天然的清香，对于年轻人来说，银杏叶枕头最大的好处就在于能帮助人们提高睡眠质量。这对于压力山大而难以入眠的都市白领而言，无疑是一道福音。</p><p>\u3000\u30002.银杏叶枕头还能避免成年人因血管老化惹起的高血压、脑中风、糖尿病等，可使成年人特别在中老年时期维持正常的心脏输出量以及正常的神经系统功用的自然物质,使人尽可能坚持正常的细胞生命周期，坚持梦寐以求的青春生机。</p><p>\u3000\u3000值得注意的是，做银杏叶枕头时，又或是存放时，银杏叶需要保持干燥，不然容易发霉，枕在发霉的枕头上，自然对人身体是无益处的。知道银杏叶枕头的好处后大家可以尝试去做一个，给自己的生活增添不一样的景色。</p><p><br/></p>\\n", "creator": "新闻类型：媒体报道", "date": "2019年5月31日", "link": "http://m.cnyxs.com/news_type.asp?id=34948"}'}
            for i in range(20001)]


    with db.atomic():
        for bat in chunked(data, 1000):
            Test3.insert_many(bat).on_conflict_ignore().execute()
    #print(data)



if __name__ == '__main__':

    from config.urls.zgzwconfig import ZgzwConfig

    zg = ZgzwConfig()

    json_obj = zg.parser()
    # db.connect()
    Test3.create_table()
    # # create_table()
    # Test3.create(name='hj', content=json_obj)
    # Test3.create(name='ynm', content=json_obj)
    # db.close()
    save(json_obj)