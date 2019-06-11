# coding=gbk
from bs4 import BeautifulSoup
from parser import baseparser
import re

class GinkgoParser(baseparser.ArticleBaseParser):

    def __init__(self, content):
        super().__init__(content)

    @property
    def info(self):
        fonts = self.soup.find_all('font')
        infos = []
        for i, f in enumerate(fonts):
            if f['color'] == '#990000' and i < 4:
                infos.append(f)
        return infos

    def parse_title(self):
        return self.soup.find(self.TITLE).string

    def parse_author(self, *args, **kwargs):
        return self.info[0].string

    def parse_source(self, *args, **kwargs):
        return self.info[1].string

    def parse_date(self, *args, **kwargs):
        return self.info[2].string

    def parse_body(self, *args, **kwargs):
        pass

    def parse_link(self, *args, **kwargs):
        # 返回值是一个只含一个元素的列表，arr[0]取出
        return re.findall(self.link_pattern, self.content)[0]

if __name__ == '__main__':
    pass