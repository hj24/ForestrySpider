from abc import abstractmethod, ABC

from model.articlemodel import Article
from utils.decorators.db import auto_connect
from config.db.settings import DATABASE


db = DATABASE['mysqldb']

class BaseSaver(ABC):

    def __init__(self, content):
        self.content = content

    @abstractmethod
    def save(self, *args, **kwargs):
        pass

class Saver(BaseSaver):

    def __init__(self, content):
        super().__init__(content)

    @auto_connect(db=db)
    def save(self, *args, **kwargs):

        title = self.content['title']

        with db.atomic():
            Article.get_or_create(title=title, defaults={'content': self.content})