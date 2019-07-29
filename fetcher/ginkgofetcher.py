import aiohttp
from aiohttp import web
import asyncio

from fetcher import basefetcher
from fetcher.basefetcher import logger
from config.urls.settings import GINKGO_HEADERS
from fetcher.basefetcher import (PROXY, proxy_server, proxy_headers)


class GinkgoFetcher(basefetcher.BaseFetcher):
    """
    中国银杏网页面下载器
    """

    def __init__(self, url):
        super().__init__()
        self.url = url

    async def __process_response(self, response):
        if response.status == 200:
            res = await response.text(encoding='gb18030')
            return res
        elif response.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.http.HttpProcessingError(
                code=response.status,
                message=response.reason,
            )

    async def get(self, session, url):
        """
        如果有代理就用代理，没有就用本机IP爬
        """

        try:
            if not PROXY:
                raise ModuleNotFoundError
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession(headers=proxy_headers, connector=conn) as sess:
                async with sess.get(url, timeout=60, proxy=proxy_server) as resp:
                    await resp.read()

                    return await self.__process_response(resp)
        except (ModuleNotFoundError, aiohttp.http.HttpProcessingError, Exception) as e:
            logger.error('%s - 转为本机爬取', e)
            async with session.get(url, timeout=60, headers=GINKGO_HEADERS) as resp:
                await resp.read()
                try:
                    return await self.__process_response(resp)
                except Exception as e:
                    logger.error(e)

    async def fetch(self, semaphore):
        response =  await self.send_requests_get(self.url, semaphore)
        return response

    async def send_requests_get(self, url, semaphore):
        try:
            with (await semaphore):
                async with aiohttp.ClientSession() as session:
                    html = await self.get(session, url)
        except web.HTTPNotFound as notfound:
            logger.debug(notfound)
        except Exception as e:
            logger.info('fetcher:', e)
        else:
            return html

class MainPageFetcher(GinkgoFetcher):
    """
    主页面下载器，获取当前母url下的主页面
    继承 GinkgoFetcher 所有内容
    """
    pass


if __name__ == '__main__':
    pass