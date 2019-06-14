# encoding=utf-8
from parser import baseparser
import re

class MenuParser(baseparser.MenuBaseParser):

    def __init__(self, content, url=None):
        super().__init__(content, url)

    @property
    def page_num_pattern(self):
        return re.compile('</a>&nbsp;&nbsp;下一页&nbsp;&nbsp;尾页&nbsp;&nbsp;第.*?页/共(.*?)页&nbsp;&nbsp;共.*?条银杏网动态</td>')

    def parse_page_nums(self, *args, **kwargs):
        nums = re.findall(self.page_num_pattern, self.content)[0]
        return int(nums)

    def generate_links(self, nums):
        base = self.root_url
        return [base + '&pageno=' + str(i) for i in range(1, nums)]


class UrlListParser(baseparser.UrlListBaseParser):

    def __init__(self, content, url=None):
        super().__init__(content, url)

    @property
    def url_link_pattern(self):
        return re.compile('<td.*?width="99%".*?height="26">\[.*?\]&nbsp;<a.*?href="(.*?)".*?target="_blank">.*?</a>.*?</td>')

    def parse_all_links(self, *args, **kwargs):
        return re.findall(self.url_link_pattern, self.content)

if __name__ == '__main__':
    from utils.test import main_page
    root_url = 'http://www.cnyxs.com/news.asp?lb=%D2%F8%D0%D3%CD%F8%B6%AF%CC%AC'
    m = MenuParser(main_page, root_url)
    print(m.generate_links(m.parse_page_nums()))

    u = UrlListParser(main_page, root_url)
    print(u.parse_all_links())