import configparser
from collections import namedtuple


class DBConfiger:

    def __init__(self, DB_CONFIG_FILE):
        # 初始化文件解析实例
        self.config = configparser.ConfigParser()
        # 读取数据库配置文件
        self.db_config_file = DB_CONFIG_FILE
        self.database_sections = None

    def setup(self):
        self.config.read(self.db_config_file)
        self.database_sections = self.config.sections()

# 错误msg
keyerror_msg = '请检查数据库名称是否正确'

# 返回结果, 类型为命名元组
db = namedtuple('db', 'name user passw host port')

# 根据名称读取特定数据库
def which_db(sections, name):
    for id, db in enumerate(sections):
        if name == db:
            return sections[id]

def read_db_config_file(db_configer, name):
    # 初始化
    db_configer.setup()

    try:
        # 读取section
        db_section = which_db(db_configer.database_sections, name)
        if db_section is None:
            raise KeyError
    except KeyError:
        print(keyerror_msg)
    except Exception as e:
        print(e)
    else:
        # 读取端口密码等
        db_name = db_configer.config.get(db_section, 'name')
        db_user = db_configer.config.get(db_section, 'user')
        db_pass = db_configer.config.get(db_section, 'password')
        db_host = db_configer.config.get(db_section, 'host')
        db_port = db_configer.config.getint(db_section, 'port')
        return db(db_name, db_user, db_pass, db_host, db_port)