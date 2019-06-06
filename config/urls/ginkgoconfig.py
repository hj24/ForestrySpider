import json
from config.urls.settings import GINKGO_CONFIG_FILE
from config.urls import configer

class GinkgoConfig(configer.ParseConfig):
    """
    解析爬虫接口

    Parameters:
        PATH - 配置文件位置
    """

    PATH = GINKGO_CONFIG_FILE

if __name__ == '__main__':

    p = GinkgoConfig()
    print(p.parser())