import json
import re


class ZgzwParser:
    """
    中国知网api解析器
    """


    def __init__(self, content):
        """
        参数:
        content -  json数据
        cells   -  json中的所有文章信息
        """

        self.content = content

        if type(content) == str:
            self.json_content = eval(content)
        elif type(content) == dict:
            self.json_content = content

    def __parse_cells(self):
        return self.json_content["cells"]

    def parse_factory(self):
        cells = self.__parse_cells()
        for cell in cells:
            cell['type'] = 2
            # cell = json.dumps(cell)
        return cells

class ZgzwMainDataParser:
    """
    - 解析总json数
    - 生成所有api url
    """


    TOTAL_NUMS = None
    ROOT_URL = None
    CUT = 10

    def __init__(self, content, root):
        """
        参数:
        content -  知网接口返回的json字符串，由于比较复杂，需要先json.dumps处理成合法字符串
        """
        json_str = content
        json_content = eval(json_str)

        self.TOTAL_NUMS = int(json_content["count"])
        self.ROOT_URL = root

    def generate_all_links(self):
        """
        变量:
            pattern -  可复用的正则对象，用于替换生成url
        匿名函数:
            replace_pattern -  生成替换的正则的匿名函数
            pages           -  计算总页数的匿名函数
        返回:
            return_urls -  返回生成的url
        """

        parttern = re.compile('&start=(.*?)&')

        replace_parttern = lambda x: r'&start=' + str(x) + '&'
        pages = lambda x: x // self.CUT

        return_urls = [re.sub(parttern, replace_parttern(i * self.CUT), self.ROOT_URL)
                       for i in range(pages(self.TOTAL_NUMS))]

        return return_urls


if __name__ == '__main__':
    from utils.zgzw_test_utils import json_obj, url

    zgzw = ZgzwParser(json_obj)
    print(zgzw.parse_factory())

    res = ZgzwMainDataParser(json_obj, url).generate_all_links()
    print(len(res))