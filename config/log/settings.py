import os


# 根目录名
PARENT_PATH = os.path.abspath(os.path.dirname(__file__))

# 日志模块名, 不存在就创建
LOGGER_PATH = os.path.abspath(os.path.join(PARENT_PATH, 'logs'))
if not os.path.exists(LOGGER_PATH):
    os.makedirs(LOGGER_PATH)
# 日志文件
DEBUG_FILE = os.path.join(LOGGER_PATH, 'debug.log')
ERROR_FILE = os.path.join(LOGGER_PATH, 'error.log')

# 配置
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
        'parser': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
        'saver': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
        'engine': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
        'config': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        },
        'model': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
        'utils': {
            'level': 'INFO',
            'handlers': ['console']
        },
        'single': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error']
        },
    },
}