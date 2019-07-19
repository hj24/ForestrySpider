import threading

from lxml import etree
import requests


urls = [
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
    'http://www.cnyxs.com/news_type.asp?id=34946',
]

'''
提交请求获取AAAI网页,并解析HTML获取title
'''

import time
from concurrent.futures import ThreadPoolExecutor

def get_title(url, cnt):
    response = requests.get(url)  # 提交请求,获取响应内容
    html = response.content  # 获取网页内容(content返回的是bytes型数据,text()获取的是Unicode型数据)
    title = etree.HTML(html).xpath('//*[@id="title"]/text()')  # 由xpath解析HTML
    print('第%d个title:%s' % (cnt, ''.join(title)))



start1 = time.time()

pool = ThreadPoolExecutor(max_workers=20)

pool_list = []

for c, url in enumerate(urls):
    p = pool.submit(get_title, url, c)

pool.shutdown()

for p in pool_list:
    print('***', p.result())

print('主程序')

print('爬取总耗时:%.5f秒' % float(time.time() - start1))

