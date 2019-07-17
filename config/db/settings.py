import os
from peewee import *

from config.db.configer import DBConfiger, read_db_config_file

# 根目录文件位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 配置文件位置
CONFIG_PATH = os.path.join(PARENT_PATH, 'conf')
# 数据库配置文件
DB_CONFIG_FILE = os.path.join(CONFIG_PATH, 'info.ini')
# 数据库配置引擎
DB = DBConfiger(DB_CONFIG_FILE)


# 在此添加数据库
mysql_db = read_db_config_file(DB, 'mysqldb')

# 在此添加数据库连接配置
DATABASE = {
    'mysqldb': MySQLDatabase(mysql_db.name, user=mysql_db.user, password=mysql_db.passw,
                            host=mysql_db.host, port=mysql_db.port),
}