from abc import ABC, abstractmethod
import asyncio

class BaseFetcher(ABC):
    """
    爬虫的核心，获取页面信息

    方法:
        send_requests_get - 发送get请求
        fetch - 获取内容的主函数
    """

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