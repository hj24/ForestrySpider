import aiohttp
from aiohttp import web
import asyncio

from fetcher.ginkgofetcher import GinkgoFetcher
from fetcher.basefetcher import logger


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
        # 获取响应结果，按状态码不同进行相应处理
        async with session.get(url) as response:
            if response.status == 200:
                res = await response.text()
                return eval(res)
            elif response.status == 404:
                raise web.HTTPNotFound()
            else:
                raise aiohttp.http.HttpProcessingError(
                    code=response.status,
                    message=response.reason,
                    headers=response.headers
                )

    async def fetch(self, semaphore):
        response = await self.send_requests_get(self.url, semaphore)
        return response

if __name__ == '__main__':
    from config.urls.zgzwconfig import ZgzwConfig
    from parser.zgzwparser import ZgzwParser
    z = ZgzwConfig()
    test_url = z.parser()['url']


    sem = asyncio.Semaphore(20)
    t = TotalUrlNumberFetcher(test_url)
    zz = ZgzwFetcher(test_url)

    import time
    st = time.time()

    def callback(res):
        from copy import deepcopy

        res = ZgzwParser(res.result()).parse_factory()

        #
        print(res)

        return res


    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(zz.fetch(sem)) for _ in range(10)]

    for t in tasks:
        t.add_done_callback(callback)

    res = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    for i in res:
        print(i)

    e = time.time()
    print(e - st)