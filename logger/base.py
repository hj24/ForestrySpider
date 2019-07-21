import logging
import logging.config
import os

from config.log import settings
from config.log.settings import LOGGING


logging.config.dictConfig(LOGGING)

# logger = logging.getLogger('fetcher')
#
# logger.info('xixi')
logging.info('xxxxxx')


