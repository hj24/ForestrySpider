from peewee import *
import os


# 根目录文件位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 配置文件位置
CONFIG_PATH = os.path.join(PARENT_PATH, 'conf')

# 数据库配置文件
DB_CONFIG_FILE = os.path.join(CONFIG_PATH, 'info.ini')




# MYSQL_DB = MySQLDatabase()