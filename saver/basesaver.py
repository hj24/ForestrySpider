from abc import abstractmethod, ABC
import logging.config
from peewee import chunked

from config.log.settings import LOGGING
from model.articlemodel import Article
from config.db.settings import DATABASE


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('saver')

try:
    from utils.extension.savers import ext_saver
except ImportError as ie:
    ext_saver = None
    logger.error(ie)


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

    def __init__(self, content):
        super().__init__(content)

    @db.atomic()
    def save(self, *args, **kwargs):
        try:
            title = self.content['title']
            Article.get_or_create(title=title, defaults={'content': self.content})
        except Exception as e:
            logger.error(e)
        else:
            logger.info('save success!')

    @db.atomic()
    def save_many(self, *, batch=None):
        try:
            if batch is None:
                Article.insert_many(self.content).on_conflict_ignore().execute()
            else:
                for bat in chunked(self.content, batch):
                    Article.insert_many(bat).on_conflict_ignore().execute()
        except Exception as e:
            logger.info(e)
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