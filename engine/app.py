import logging.config
import asyncio

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

URL_POOL = asyncio.Queue()

GINKGO_TYPE = 1
ZGZW_TYPE = 2

def load_url_config():
    #init_list = GinkgoConfig().parser()
    init_list = []
    zgzw_result = ZgzwConfig().parser()
    if type(zgzw_result) == dict:
        init_list.append(zgzw_result)
    elif type(zgzw_result) == list:
        init_list.extend(zgzw_result)
    return init_list

class App:

    def __init__(self, init_urls):
        self.init_url_list = init_urls
        self.semaphore = asyncio.Semaphore(20)
        self.lock = asyncio.Lock()

    async def produce_url(self):
        for url_dict in self.init_url_list:
            # type为1表示是中国银杏网
            if url_dict['type'] == 1:
                # 爬取每个专题的主页
                main_page_fetcher = ginkgofetcher.MainPageFetcher(url_dict['url'])
                main_page = await main_page_fetcher.fetch(self.semaphore)
                # 解析每个专题下有多少页以及每一页的文章url
                try:
                    main_page_parser = listparser.MenuParser(main_page, url=url_dict['url'])
                    all_pages = main_page_parser.generate_links(main_page_parser.parse_page_nums())
                except IndexError:
                    logger.error('error on:', url_dict['url'])
                except Exception as e:
                    logger.error(e)
                else:
                    # 放入url池
                    for page in all_pages:
                        try:
                            detail_links_page = await ginkgofetcher.MainPageFetcher(page).fetch(self.semaphore)
                            [(await URL_POOL.put(l))
                             for l in listparser.UrlListParser(detail_links_page).parse_all_links()]
                        except TypeError:
                            logger.error('error on:', page)
                        except Exception as e:
                            logger.error(e)

            # type为2表示中国知网
            elif url_dict['type'] == 2:
                # 解析主json对象，得到所有链接
                main_data = await zgzwfetcher.ZgzwFetcher(url_dict['url']).fetch(self.semaphore)
                all_links = zgzwparser.ZgzwMainDataParser(main_data, url_dict['url']).generate_all_links()
                # 放入url池
                [(await URL_POOL.put(link)) for link in all_links]

        await URL_POOL.put(None)

        logger.info('server: %s', '所有url产生完毕')

        #await URL_POOL.join()

    def __judge_url(self, url):
        if url.startswith('http://w') or url.startswith('https://w'):
            return GINKGO_TYPE
        if url.startswith('http://m') or url.startswith('https://m'):
            return ZGZW_TYPE

    @disable_gc
    async def __pre_process_data(self, data_to_store, response, type):
        with await self.lock:
            if type == GINKGO_TYPE:
                data_to_store.append(response)
            elif type == ZGZW_TYPE and response is not None:
                data_to_store.extend(response)

    async def consume_url(self, data_to_store):

        while True:
            url = await URL_POOL.get()
            logger.info(url)
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
                logger.error('url:' + url + '内容获取失败')
            else:
                json_response = None

                if choice == GINKGO_TYPE:
                    json_response = ginkgoparser.GinkgoParser(response).parse_factory()
                    await self.__pre_process_data(data_to_store, json_response, GINKGO_TYPE)
                elif choice == ZGZW_TYPE:
                    json_response = zgzwparser.ZgzwParser(response).parse_factory()
                    await self.__pre_process_data(data_to_store, json_response, ZGZW_TYPE)

                logger.info(json_response)

                URL_POOL.task_done()

        logger.info(URL_POOL.qsize())

    def run(self):

        data_to_store = []

        loop = asyncio.get_event_loop()

        producers = asyncio.ensure_future(self.produce_url())
        consumers = asyncio.ensure_future(self.consume_url(data_to_store))
        tasks = [producers] + [consumers]

        loop.run_until_complete(asyncio.gather(*tasks))

        logger.info('队列完毕？')

        Saver(data_to_store).save_many()

        loop.close()

def run():
    init_urls = load_url_config()
    app = App(init_urls)
    app.run()

if __name__ == '__main__':
    run()