# encoding=utf-8
import re

from parser import baseparser
from parser.baseparser import logger


class MenuParser(baseparser.MenuBaseParser):
    """
    主页解析器

    - 对应中国银杏网每一个专题的第一页
    - 解析它们的页数并生成每一页的url连接
    """


    def __init__(self, content, url=None):
        super().__init__(content, url)

    @property
    def page_num_pattern(self):
        return re.compile('<a.*?class=Black.*?href=.*?&pageno=.*?&gjz=>尾页</a>&nbsp;&nbsp;第1页/共(.*?)页&nbsp;&nbsp;共.*?条文章</p>')
        #return re.compile('</a>&nbsp;&nbsp;.*?第.*?页/共(.*?)页&nbsp;&nbsp;共.*?条.*?</td>')

    def parse_page_nums(self, *args, **kwargs):
        """
        解析中国银杏网一个专题有多少页
        """
        # logger.info(re.findall(self.page_num_pattern, self.content))
        nums = re.findall(self.page_num_pattern, self.content)[0]
        return int(nums)


    def generate_links(self, nums):
        """
        根据 parse_page_nums 方法产生每一页的 url

        参数:
            nums -  parse_page_nums的返回值，表示页数
        """

        base = self.root_url
        return [base + '&pageno=' + str(i) for i in range(1, nums + 1)]


class UrlListParser(baseparser.UrlListBaseParser):
    """
    文章url解析器

    - 解析每一页的所有文章的url
    """

    def __init__(self, content, url=None):
        super().__init__(content, url)

    def parse_all_links(self, *args, **kwargs):
        tags = self.soup.find_all(name='a', attrs={'class': 'news_name'})
        return ['http://m.cnyxs.com/' + str(t.get('href')) for t in tags]

if __name__ == '__main__':
    pass