#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

"""
@Time    : 4/13/21 1:24 PM
@Author  : CQ
@Describe:
"""


import logging
import logging.config

logging.config.fileConfig('settings.ini')

# create logger
logger = logging.getLogger('file')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')