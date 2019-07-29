# encoding=utf-8
import logging.config

from config.log.settings import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('utils')

if __name__ == '__main__':
    logger.info('fake test')