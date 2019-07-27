from abc import ABC, abstractmethod
import logging.config

from config.log.settings import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('fetcher')

PROXY = True
proxy_server = None
try:
    from config.proxy.settings import (proxy_host, proxy_port, proxy_user, proxy_pass, proxy_headers)
    if proxy_host is None or proxy_port is None or proxy_user is None or proxy_pass is None:
        raise ImportError
except ImportError:
    logger.error('请检查代理配置')
    PROXY = False
else:
    proxy_server = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"


class BaseFetcher(ABC):
    """
    爬虫的核心，获取页面信息

    方法:
        send_requests_get - 发送get请求
        fetch - 获取内容的主函数
    """

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get(self, *args, **kwargs):
        pass

    @abstractmethod
    async def fetch(self, *args, **kwargs):
        """
        处理fetch的主函数

        参数:
            url - 目标网页的url
        返回值:
            经过处理整合分类的网页的内容
        """
        pass

    @abstractmethod
    async def send_requests_get(self, *args, **kwargs):
        """
        发送get请求，主要在fetch函数中调用

        参数:
            url - 目标网页的url
        返回值:
            目标网页的内容
        """
        pass