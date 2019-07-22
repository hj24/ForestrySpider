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
        return re.compile('</a>&nbsp;&nbsp;.*?第.*?页/共(.*?)页&nbsp;&nbsp;共.*?条.*?</td>')

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

    @property
    def url_link_pattern(self):
        return re.compile('<td.*?width="99%".*?height="26">\[.*?\]&nbsp;<a.*?href="(.*?)".*?target="_blank">.*?</a>.*?</td>')

    def parse_all_links(self, *args, **kwargs):
        # logger.info(re.findall(self.url_link_pattern, self.content))
        return re.findall(self.url_link_pattern, self.content)

if __name__ == '__main__':
    from utils.test import main_page
    from fetcher.ginkgofetcher import MainPageFetcher
    import asyncio

    root_url = 'http://www.cnyxs.com/news.asp?lb=%D2%F8%D0%D3%D0%C2%CE%C5&pageno=22'

    loop = asyncio.get_event_loop()

    sem = asyncio.Semaphore(10)

    task = asyncio.ensure_future(MainPageFetcher(root_url).fetch(sem))

    res = loop.run_until_complete(task)

    loop.close()

    print(res)




    # m = MenuParser(main_page, root_url)
    # print(m.generate_links(m.parse_page_nums()))

    u = UrlListParser(main_page, root_url)
    print(u.parse_all_links())