# coding=utf-8
import re
import json

from parser import baseparser


class GinkgoParser(baseparser.ArticleBaseParser):

    TITLE = 'h1'

    def __init__(self, content):
        super().__init__(content)

    @property
    def info(self):
        """
        根据字体颜色，提取标题下一栏信息内容，供各个解析器使用
        只需前 4 个

        返回:
            infos - 标题下一栏信息的列表
        """
        fonts = self.soup.find_all('font')
        infos = []
        for i, f in enumerate(fonts):
            if f['color'] == '#990000' and i < 4:
                infos.append(f)
        return infos

    @property
    def link_pattern(self):
        return re.compile('.*?本文地址:<a.*?href="(.*?)">.*?</a>')

    def parse_title(self):
        return self.soup.find(self.TITLE).string

    def parse_author(self, *args, **kwargs):
        return self.info[0].string

    def parse_source(self, *args, **kwargs):
        return self.info[1].string

    def parse_date(self, *args, **kwargs):
        return self.info[2].string

    def parse_body(self, *args, **kwargs):
        """
        解析文章内容

        返回:
            body - 文章的内容，列表中每一项代表一段
        """
        body = []
        for p in self.soup.find_all('p'):
            body.append(p.text.strip())
        return body

    def parse_link(self, *args, **kwargs):
        # 返回值是一个只含一个元素的列表，arr[0]取出
        return re.findall(self.link_pattern, self.content)[0]

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
            link    -   原文地址
        匿名函数:
            summary -   截取做摘要的部分，默认取原文的1/20
        返回:
            json对象
        """

        content = {}

        content['type'] = 1
        content['title'] = self.parse_title()

        detail = self.parse_body()
        detail_length = len(detail)
        summary = lambda x: x - 19 * x // 20

        content['summary'] = detail[:summary(detail_length)]
        content['detail'] = detail
        content['author'] = self.parse_author()
        content['source'] = self.parse_source()
        content['date'] = self.parse_date()
        content['link'] = self.parse_link()

        return json.dumps(content, ensure_ascii=False)


if __name__ == '__main__':
    from utils.test import content
    parser = GinkgoParser(content)
    print(parser.parse_factory())