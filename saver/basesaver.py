from abc import abstractmethod, ABC
import logging.config

from config.log.settings import LOGGING
from model.articlemodel import Article
from utils.decorators.db import auto_connect
from config.db.settings import DATABASE

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('saver')

try:
    from utils.webutils.savers import ext_saver
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
    def ext_save(self, *args, **kwargs):
        pass

class Saver(BaseSaver):

    def __init__(self, content):
        super().__init__(content)

    @auto_connect(db=db)
    def save(self, *args, **kwargs):

        title = self.content['title']

        with db.atomic():
            Article.get_or_create(title=title, defaults={'content': self.content})

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