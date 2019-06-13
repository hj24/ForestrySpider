# coding=utf-8
from bs4 import BeautifulSoup
from parser import baseparser
import re

class GinkgoParser(baseparser.ArticleBaseParser):

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

if __name__ == '__main__':
    content = """
    <P>本网英文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
    href="http://www.cnyxs.com/">www.cnyxs.com</A></STRONG> 中文域名:<STRONG style="color: rgb(255, 0, 0);"> <A 
    href="http://www.cnyxs.com/">中国银杏网</A></STRONG>.com－中国最专业的<A style="padding: 0px;" 
    href="http://www.cnyxs.com/">银杏</A><a href="http://www.cnyxs.com/baiguo/" target="_blank">白果</a>行业门户网站</P>
    """
    parser = GinkgoParser(content)