import aiohttp
from aiohttp import web
import asyncio

from fetcher import basefetcher
from fetcher.basefetcher import logger


class GinkgoFetcher(basefetcher.BaseFetcher):
    """
    中国银杏网页面下载器
    """

    def __init__(self, url):
        super().__init__()
        self.url = url

    async def get(self, session, url):
        # 获取网页内容，按状态码不同进行相应处理
        async with session.get(url, timeout=60) as response:
            # res = await response.text()
            # return res
            if response.status == 200:
                res = await response.text(encoding='gb18030')
                return res
            elif response.status == 404:
                raise web.HTTPNotFound()
            else:
                raise aiohttp.http.HttpProcessingError(
                    code=response.status,
                    message=response.reason,
                    headers=response.headers
                )

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
    test_url = 'http://www.cnyxs.com/news_type.asp?id=34946'
    sem = asyncio.Semaphore(20)
    s = GinkgoFetcher(test_url)
    import time
    st = time.time()

    loop = asyncio.get_event_loop()

    def callback():
        pass

    tasks = [asyncio.ensure_future(s.fetch(sem)) for _ in range(1)]

    res, _ = loop.run_until_complete(asyncio.wait(tasks))

    loop.close()

    e = time.time()
    logger.info(e - st)