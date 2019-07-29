from abc import abstractmethod, ABC
import logging.config
from peewee import chunked

from config.log.settings import LOGGING
from model.articlemodel import Article
from config.db.settings import DATABASE
from utils.decorators.db import auto_connect


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('saver')

try:
    from utils.extension.savers import ext_saver
except ImportError as ie:
    ext_saver = None


db = DATABASE['mysqldb']

class BaseSaver(ABC):

    def __init__(self, content):
        self.content = content

    @abstractmethod
    def save(self, *args, **kwargs):
        pass

    @abstractmethod
    def save_many(self, *args, **kwargs):
        pass

    @abstractmethod
    def ext_save(self, *args, **kwargs):
        pass

class Saver(BaseSaver):

    def __init__(self, content=None):
        super().__init__(content)

    @auto_connect(db=db)
    @db.atomic()
    def save(self, data):
        try:
            title, type, tag, content = data['title'], data['type'], data['tag'], data['content']
            info, flag = Article.get_or_create(title=title, defaults={'type': type, 'tag': tag, 'content': content})
        except Exception as e:
            logger.error(e)
        else:
            return flag

    @db.atomic()
    def __save_many_without_batch(self):
        Article.insert_many(self.content).on_conflict_ignore().execute()

    @db.atomic()
    def __save_many_with_batch(self, batch):
        for bat in chunked(self.content, batch):
            Article.insert_many(bat).on_conflict_ignore().execute()

    def save_many(self, *, batch=None):
        if self.content is None:
            logger.error('data not found!')
            return
        try:
            if batch is None:
                self.__save_many_without_batch()
            else:
                self.__save_many_with_batch(batch=batch)
        except Exception as e:
            logger.error(e)
            db.rollback()
        else:
            logger.info('save: %s records success!', len(self.content))

    def ext_save(self, *args, **kwargs):
        """
        扩展存储器

        - 用于继承到django等web框架中自定义的orm操作
        - 一般在utils中的utils.webutils写，或者import
        - 如果为None则抛出异常
        - 此功能待具体优化
        """

        if ext_saver:
            ext_saver.save(self.content, *args, **kwargs)
        else:
            raise ImportError