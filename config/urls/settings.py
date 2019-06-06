import os

# 根目录文件位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 配置文件位置
CONFIG_PATH = os.path.join(PARENT_PATH, 'conf')

# 中国银杏网接口文件
GINKGO_CONFIG_FILE = os.path.join(CONFIG_PATH, 'ginkgo.json')
# 中国知网接口文件
ZGZW_CONFIG_FILE = os.path.join(CONFIG_PATH, 'zgzw.json')