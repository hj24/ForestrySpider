from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import logging.config

from config.log.settings import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('parser')


class ArticleBaseParser(ABC):
    """
    文章解析器基类，定义了一些解析器通用的方法

    方法:
        parse_author - 从网页中解析出作者
        parse_date   - 解析日期信息
        parse_source - 解析文章来源
        parse_body   - 解析文章内容
        parse_link   - 解析文章链接
    属性:
        PARSER_TYPE  - 文档解析器类型
        soup         - lxml解析器，可通过设置PARSER_TYPE改变
        content      - 页面内容
        url          - 可选参数，当前页面的url
    """


    PARSER_TYPE = 'lxml'

    def __init__(self, content, url=None):
        self.content = content
        self.root_url = url

    @property
    def soup(self):
        return BeautifulSoup(self.content, self.PARSER_TYPE)

    @abstractmethod
    def parse_title(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_author(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_date(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_source(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_body(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_link(self, *args, **kwargs):
        pass

    @abstractmethod
    def parse_tag(self, *args, **kwargs):
        pass

class UrlListBaseParser(ABC):
    """
    url解析器

    方法:
        parse_page_nums    - 解析主页面下要爬的子页面一共有多少页
        parse_detail_links - 解析每一页的文章链接
    属性:
        content - 页面内容
        url     - 可选参数，当前页面的url
    """


    PARSER_TYPE = 'lxml'

    def __init__(self, content, url=None):
        self.content = content
        self.root_url = url

    @abstractmethod
    def parse_all_links(self, *args, **kwargs):
        pass

class MenuBaseParser(ABC):

    def __init__(self, content, url=None):
        self.content = content
        self.root_url = url

    @abstractmethod
    def parse_page_nums(self, *args, **kwargs):
        pass