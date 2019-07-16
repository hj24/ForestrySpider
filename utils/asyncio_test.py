import time
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


def get_title(url, cnt):
    response = requests.get(url)  # 提交请求,获取响应内容
    html = response.content  # 获取网页内容(content返回的是bytes型数据,text()获取的是Unicode型数据)
    title = etree.HTML(html).xpath('//*[@id="title"]/text()')  # 由xpath解析HTML
    print('第%d个title:%s' % (cnt, ''.join(title)))


if __name__ == '__main__':
    start1 = time.time()
    i = 0
    for url in urls:
        i = i + 1
        start = time.time()
        get_title(url, i)
        print('第%d个title爬取耗时:%.5f秒' % (i, float(time.time() - start)))
    print('爬取总耗时:%.5f秒' % float(time.time() - start1))