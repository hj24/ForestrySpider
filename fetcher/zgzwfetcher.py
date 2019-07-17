import aiohttp
from aiohttp import web
import asyncio

from fetcher.ginkgofetcher import GinkgoFetcher


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
    中国知网银杏主题论文下载器
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
    z = ZgzwConfig()
    test_url = z.parser()['url']


    sem = asyncio.Semaphore(20)
    t = TotalUrlNumberFetcher(test_url)
    zz = ZgzwFetcher(test_url)

    import time
    st = time.time()

    loop = asyncio.get_event_loop()
    tasks = [zz.fetch(sem) for _ in range(20)]
    res, _ = loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    e = time.time()
    print(e - st)