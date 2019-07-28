import aiohttp
from aiohttp import web
from aiohttp.http_exceptions import HttpProcessingError

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

    async def __procrss_response(self, response):
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

    async def get(self, session, url):
        try:
            if not PROXY:
                raise ModuleNotFoundError
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession(headers=proxy_headers, connector=conn) as sess:
                async with sess.get(url, timeout=60, proxy=proxy_server) as resp:
                    await resp.read()
                    return await self.__procrss_response(resp)
        except (ModuleNotFoundError, HttpProcessingError, Exception) as e:
            logger.error('%s - 转为本机爬取', e)
            async with session.get(url, timeout=60, headers=ZGZW_HEADERS) as resp:
                await resp.read()
                try:
                    return await self.__procrss_response(resp)
                except Exception as e:
                    logger.error(e)

    async def fetch(self, semaphore):
        response = await self.send_requests_get(self.url, semaphore)
        return response

if __name__ == '__main__':
    pass