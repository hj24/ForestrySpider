# coding=utf-8
import json

from parser import baseparser
from parser.baseparser import logger


class GinkgoParser(baseparser.ArticleBaseParser):

    TITLE = {'class': 'news_detailtitle'}
    DATE = {'class': 'news_time01'}
    CONTENT = {'class': 'news_detailinfo'}
    AUTHOR = {'class': 'news_author'}

    def __init__(self, content, *, url=None):
        super().__init__(content)
        self.url = 'N/A' if url is None else url

    def parse_title(self):
        title = None
        try:
            title = str(self.soup.find(name='div', attrs=self.TITLE).string)
        except Exception as e:
            logger.info(e)
            title = 'N/A'
        finally:
            return title

    def parse_author(self, *args, **kwargs):
        try:
            return str(self.soup.find(name='span', attrs=self.AUTHOR).string)
        except Exception as e:
            logger.error(e)
            return 'N/A'

    def parse_date(self, *args, **kwargs):
        try:
            return str(self.soup.find(name='span', attrs=self.DATE).string)
        except Exception as e:
            logger.error(e)
            return 'N/A'

    def parse_tag(self, *args, **kwargs):
        try:
            return self.parse_author()[5:]
        except Exception as e:
            logger.error(e)
            return '佚名'

    def parse_body(self, *args, **kwargs):
        """
        解析文章内容

        返回:
            body - 文章的内容，字符串形式，保留html标签
        """
        try:
            content = self.soup.find(name='div', attrs=self.CONTENT).contents
        except Exception as e:
            logger.error(e)
            return '文章为空'
        else:
            return ''.join([str(c) for c in content])

    def parse_link(self, *args, **kwargs):
        return self.url

    def parse_factory(self, *args, **kwargs):
        """
        将解析结果封装成json

        参数:
            type    -   文章类型，区分是知网还是银杏网的内容
            title   -   标题
            summary -   摘要，取正文的四分之一
            detail  -   详细全文
            author  -   作者
            source  -   出处
            date    -   日期
            tag     -   文章标签
            link    -   原文地址
        匿名函数:
            summary -   截取做摘要的部分，默认取原文的1/20
        返回:
            response - 数据库的title和content字段组成的json对象
        """

        content = {}

        detail = self.parse_body()
        detail_length = len(detail)
        summary = lambda x: x - 19 * x // 20

        content['title'], content['summary'], content['detail'] = self.parse_title(), detail[:summary(detail_length)], detail
        content['creator'], content['date'], content['link'] = self.parse_author(), self.parse_date(), self.parse_link()

        return {'title': content['title'],
                'type': 1,
                'tag': self.parse_tag(),
                'content': json.dumps(content, ensure_ascii=False)}

if __name__ == '__main__':
    from utils.test import content
    url = ' http://www.cnyxs.com/news_type.asp?id=12070'
    parser = GinkgoParser(content, url=url)
    logger.info(parser.parse_factory())