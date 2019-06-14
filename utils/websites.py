import requests
from bs4 import BeautifulSoup

def get_main_page(url):
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

def count_page_nums(content):
    pass