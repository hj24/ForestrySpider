import os

# 根目录文件位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 配置文件位置
CONFIG_PATH = os.path.join(PARENT_PATH, 'conf')

# 中国银杏网接口文件
GINKGO_CONFIG_FILE = os.path.join(CONFIG_PATH, 'mginkgo.json')
# 中国知网接口文件
ZGZW_CONFIG_FILE = os.path.join(CONFIG_PATH, 'zgzw.json')

# 请求头配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'ASPSESSIONIDCQDSCQRA=HFAAMGGBFNGHNNPFPGDHKICC',
    'Cache-Control': 'max-age=0',
}