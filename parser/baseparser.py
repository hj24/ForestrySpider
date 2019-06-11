from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import re

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
    """
    PARSER_TYPE = 'lxml'
    TITLE = 'h1'

    def __init__(self, content):
        self.content = content

    @property
    def soup(self):
        return BeautifulSoup(self.content, self.PARSER_TYPE)

    @property
    def link_pattern(self):
        return re.compile('.*?本文地址:<a.*?href="(.*?)">.*?</a>')

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