import os
import yaml


# 日志模块名
LOGGER = 'logger/logs'
# 配置文件名
NAME = 'log.yaml'
# 根目录文件位置
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
# 配置文件位置
CONFIG_PATH = os.path.join(PARENT_PATH, 'conf')
# 项目根目录
ROOT_FILE = os.path.abspath(os.path.dirname( os.path.dirname(os.getcwd())))
print(ROOT_FILE)
# 日志文件地址
LOG_FILE = os.path.join(ROOT_FILE, LOGGER)
# Debug日志
DEBUG_FILE = os.path.abspath(os.path.join(LOG_FILE, 'debug.log'))
# ERROR日志
ERROR_FILE = os.path.abspath(os.path.join(LOG_FILE, 'error.log'))
# log配置文件
LOGGING_CONFIG_FILE = os.path.join(CONFIG_PATH, NAME)

print(DEBUG_FILE)

# 导入配置
with open(LOGGING_CONFIG_FILE, 'r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# format
FORMATTER = config['formatters']
# handlers
handlers = config['handlers']
# 控制台handler
CONSOLE_HANDLER = handlers['console']
FILE_HANDLER = handlers['file']
ERROR_HANDLER = handlers['error']



LOGGING = {
    'version': 1,
    'formatters': {
        'brief': {'format': '%(asctime)s - %(message)s'},
        'simple': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'}},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
            'filename': DEBUG_FILE,
        },
        'error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'simple',
            'filename': ERROR_FILE,
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        }
    },
    'loggers': {
        'fetcher': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}
