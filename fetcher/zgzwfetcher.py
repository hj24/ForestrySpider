import aiohttp
from aiohttp import web
from aiohttp import (ClientHttpProxyError, ClientProxyConnectionError)

from fetcher.ginkgofetcher import GinkgoFetcher
from fetcher.basefetcher import logger
from config.urls.settings import ZGZW_HEADERS
from fetcher.basefetcher import (PROXY, proxy_server, proxy_headers)


class TotalUrlNumberFetcher(GinkgoFetcher):
    """
    爬取总共有多少条XHR对象（总url数）的爬虫
    """

    def __init__(self, url):
        super().__init__(url)

    async def fetch(self, semaphore):
        # 知网的返回是个XHR对象，这里取它里面的总url数
        response =  await self.send_requests_get(self.url, semaphore)
        response = eval(response)
        return response['count']

class ZgzwFetcher(GinkgoFetcher):
    """
    中国知网 银杏主题论文下载器
    """

    def __init__(self, url):
        super().__init__(url)

    async def get(self, session, url):

        response = None

        try:
            if not PROXY:
                raise ModuleNotFoundError
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession(headers=proxy_headers, connector=conn) as sess:
                async with sess.get(url, timeout=60, proxy=proxy_server) as resp:
                    response = resp
                    await response.read()
        except (ModuleNotFoundError, ClientHttpProxyError, ClientProxyConnectionError, Exception):
            # 获取响应结果，按状态码不同进行相应处理
            async with session.get(url, timeout=60, headers=ZGZW_HEADERS) as resp:
                response = resp
                await response.read()
        finally:
            if response.status == 200:
                res = await response.text()
                return eval(res)
            elif response.status == 404:
                raise web.HTTPNotFound()
            else:
                raise aiohttp.http.HttpProcessingError(
                    code=response.status,
                    message=response.reason,
                )

    async def fetch(self, semaphore):
        response = await self.send_requests_get(self.url, semaphore)
        return response

if __name__ == '__main__':
    pass