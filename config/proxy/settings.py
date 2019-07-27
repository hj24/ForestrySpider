import logging.config

from config.proxy.configer import configer
from config.log.settings import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('config')

proxy_host = None
proxy_port = None
proxy_user = None
proxy_pass = None

try:
    # 读取section
    proxy_section = configer.sections()[0]
    if proxy_section is None:
        raise KeyError
except KeyError:
    logger.error('请检查配置文件')
except Exception as e:
    logger.error(e)
else:
    # 读取端口密码等
    proxy_host = configer.get(proxy_section, 'host')
    proxy_port = configer.get(proxy_section, 'port')
    proxy_user = configer.get(proxy_section, 'user')
    proxy_pass = configer.get(proxy_section, 'pass')

proxy_headers = {'User-Agent': 'curl/7.x/line'}