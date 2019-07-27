import logging.config
import asyncio
import random

from config.log.settings import LOGGING
from config.urls.ginkgoconfig import GinkgoConfig
from config.urls.zgzwconfig import ZgzwConfig
from parser import listparser
from parser import zgzwparser
from parser import ginkgoparser
from fetcher import ginkgofetcher
from fetcher import zgzwfetcher
from saver.basesaver import Saver
from utils.decorators.memory import disable_gc


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('engine')

# url池队列
URL_POOL = asyncio.Queue()

# 用于判断网址来源
GINKGO_TYPE = 1
ZGZW_TYPE = 2

def load_url_config():
    """
    - 从配置中加载初始数据的函数
    """

    init_list = GinkgoConfig().parser()
    # init_list = []
    # zgzw_result = None
    zgzw_result = ZgzwConfig().parser()

    if type(zgzw_result) == dict:
        init_list.append(zgzw_result)
    elif type(zgzw_result) == list:
        init_list.extend(zgzw_result)
    return init_list

class App:

    def __init__(self, init_urls):
        """
        参数:
            init_urls - 初始化的urls
            semaphore - 协程信号量，用于控制爬虫频率
            lock      - 协程锁，存数据到列表时，要对协程进行同步
        """

        self.init_url_list = init_urls
        self.semaphore = asyncio.Semaphore(2)
        self.lock = asyncio.Lock()

    async def produce_url(self):
        """
        生产者模块

        - 用于产生待爬取的url，放入队列，任务结束发送一个信号None给消费者

        关键变量:
            url_dict: type 为 1 时代表中国银杏网，为 2 时代表中国知网
            中国银杏网：
                - main_page_fetcher: 获取中国银杏网每一个tag下的首页
                - main_page_parser: 解析每一个tag的首页，以获取该tag下的所有页面，结果为all_pages
                - UrlListParser: 解析每一个页面下的所有文章的链接，放入队列中
            中国知网:
                - ZgzwFetcher: 获取中国知网论文摘要，结果是一个XHR对象（json格式）
                - ZgzwMainDataParser: 根据首页的url信息，解析总结果数，生成所有连接存入all_links
        """

        for url_dict in self.init_url_list:
            if url_dict['type'] == 1:
                main_page_fetcher = ginkgofetcher.MainPageFetcher(url_dict['url'])
                main_page = await main_page_fetcher.fetch(self.semaphore)
                try:
                    main_page_parser = listparser.MenuParser(main_page, url=url_dict['url'])
                    all_pages = main_page_parser.generate_links(main_page_parser.parse_page_nums())
                except IndexError:
                    logger.error('error on:', url_dict['url'])
                except Exception as e:
                    logger.error(e)
                else:
                    for page in all_pages:
                        try:
                            detail_links_page = await ginkgofetcher.MainPageFetcher(page).fetch(self.semaphore)
                            [(await URL_POOL.put(l))
                             for l in listparser.UrlListParser(detail_links_page).parse_all_links()]
                        except TypeError:
                            logger.error('error on:', page)
                        except Exception as e:
                            logger.error(e)
            elif url_dict['type'] == 2:
                main_data = await zgzwfetcher.ZgzwFetcher(url_dict['url']).fetch(self.semaphore)
                all_links = zgzwparser.ZgzwMainDataParser(main_data, url_dict['url']).generate_all_links()
                [(await URL_POOL.put(link)) for link in all_links]

        await URL_POOL.put(None)

    def __judge_url(self, url):
        """
        - 根据url不同，判断是那个网址的链接

        ToDo: 其实此处设计有一点不合理，但是没有影响
        """

        if url.startswith('http://m.cnyxs') or url.startswith('https://m.cnyxs'):
            return GINKGO_TYPE
        if url.startswith('http://m.cnki') or url.startswith('https://m.cnki'):
            return ZGZW_TYPE

    @disable_gc
    async def __pre_process_data(self, data_to_store, response, type):
        """
        - 将所有结果存入data_to_store列表中
        - 为了防止列表的append操作效率过低，因此采用装饰器暂时关闭python的垃圾回收机制
        """

        with await self.lock:
            if type == GINKGO_TYPE:
                data_to_store.append(response)
            elif type == ZGZW_TYPE and response is not None:
                data_to_store.extend(response)

    async def consume_url(self, data_to_store):
        """
        消费者模块

        - 用于消费生产者生产的url，进行爬取、解析和存储, 收到None时结束循环

        关键变量:
             - response: 获取爬取网页的结果
             - choice: 判断网页来源，是中国银杏网还是中国知网
             - json_response: 用解析器解析response, 并生产相应的符合数据库模型的字典存入data_to_store
        """

        sleep_count = 1

        while True:
            url = await URL_POOL.get()
            logger.info('times: %s - url: %s', sleep_count, url)

            await asyncio.sleep(random.uniform(0, 1.0))

            sleep_count += 1

            if url is None:
                break

            try:
                response = None
                choice = None
                if self.__judge_url(url) == GINKGO_TYPE:
                    response = await ginkgofetcher.GinkgoFetcher(url).fetch(self.semaphore)
                    choice = GINKGO_TYPE
                elif self.__judge_url(url) == ZGZW_TYPE:
                    response = await zgzwfetcher.ZgzwFetcher(url).fetch(self.semaphore)
                    choice = ZGZW_TYPE
                if response is None:
                    raise IOError
            except IOError:
                logger.error('url: %s 内容获取失败', url)
            else:
                json_response = None

                if choice == GINKGO_TYPE:
                    json_response = ginkgoparser.GinkgoParser(response, url=url).parse_factory()
                    await self.__pre_process_data(data_to_store, json_response, GINKGO_TYPE)
                elif choice == ZGZW_TYPE:
                    json_response = zgzwparser.ZgzwParser(response).parse_factory()
                    await self.__pre_process_data(data_to_store, json_response, ZGZW_TYPE)

                logger.info(json_response)

                URL_POOL.task_done()

    def run(self):

        data_to_store = []

        loop = asyncio.get_event_loop()

        producers = asyncio.ensure_future(self.produce_url())
        consumers = asyncio.ensure_future(self.consume_url(data_to_store))
        tasks = [producers] + [consumers]

        loop.run_until_complete(asyncio.gather(*tasks))

        logger.info('队列任务执行完毕')

        # Saver(data_to_store).save_many(batch=1000)
        for data in data_to_store:
            logger.info('***: %s', data)

        loop.close()

def run():
    init_urls = load_url_config()
    app = App(init_urls)
    app.run()

if __name__ == '__main__':
    run()