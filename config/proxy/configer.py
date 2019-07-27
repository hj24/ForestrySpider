import configparser
import os


# 父目录位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 代理配置文件位置
PROXY_DIR = os.path.join(PARENT_PATH, 'conf')
PROXY_FILE = os.path.join(PROXY_DIR, 'proxy.ini')
# 解析器
configer = configparser.ConfigParser()
configer.read(PROXY_FILE)