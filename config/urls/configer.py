import json

class ParseConfig:
    """
    解析爬虫接口

    属性:
        PATH - 配置文件位置
        init_url_list - 用于保存爬虫接口的url列表

    方法:
        parser - 解析配置文件的函数
    """

    PATH = None

    def __init__(self):
        self.init_url_list = None

    def parser(self):
        """
        解析函数

        参数:
            None

        返回值:
            返回url列表，用于初始化爬虫的任务队列
        """

        with open(self.PATH, 'r') as fo:
            self.init_url_list = json.load(fo)
        return self.init_url_list