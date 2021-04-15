#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

"""
@Time    : 4/13/21 4:08 PM
@Author  : CQ
@Describe:
"""

import logging
import logging.config


def main():
    config_dict = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'console': {
                'class': 'logging.Formatter',
                'format': 'console %(asctime)s %(levelname)s %(message)s'
            },
            'file': {
                'class': 'logging.Formatter',
                'format': 'file %(asctime)s.%(msecs)05d %(levelname)s - %(filename)s - [line:%(lineno)d] - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
                'level': 'INFO'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'file.log',
                'mode': 'w',
                'formatter': 'file'
            },
        },
        'loggers': {
            'console': {
                'handlers': ['console']
            },
            'file': {
                'handlers': ['file']
            }
        },
        'root': {
            'handlers': ['file'],
            'level': 'DEBUG'
        }
    }
    # Log some initial events, just to show that logging in the parent works
    # normally.
    logging.config.dictConfig(config_dict)
    logger = logging.getLogger('console')
    logger.error('asdf')

    logger1 = logging.getLogger('file')
    logger1.error('a111sdf')


if __name__ == '__main__':
    main()