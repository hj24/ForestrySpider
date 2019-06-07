from abc import ABC, abstractmethod

class BaseParser(ABC):
    """
    解析器基类，定义了一些解析器通用的方法

    方法:
        parse_author - 从网页中解析出作者
        parse_date   - 解析日期信息
        parse_source - 解析文章来源
        parse_body   - 解析文章内容
        parse_link   - 解析文章链接
    """

    @abstractmethod
    def parse_author(self, content):
        pass

    @abstractmethod
    def parse_date(self, content):
        pass

    @abstractmethod
    def parse_source(self, content):
        pass

    @abstractmethod
    def parse_body(self, content):
        pass

    @abstractmethod
    def parse_link(self, content):
        pass