from fetcher import basefetcher
import requests
from requests.exceptions import Timeout

class GinkgoFetcher(basefetcher.BaseFetcher):
    """
    中国银杏网页面下载器
    """

    def fetch(self, url):
        return self.send_requests_get(url)

    def send_requests_get(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response.encoding = 'gbk'
                print('页面读取成功')
                return response
            else:
                return None
        except Exception as e:
            print(e)

if __name__ == '__main__':
    s = GinkgoFetcher()
    s.send_requests_get('http://www.cnyxs.com/news_type.asp?id=34946')