# -*- coding: UTF-8 -*-
import logging.config
config_dir = '/data/logs'
config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'verbose': {  # 详细
            'format': '%(levelname)s %(asctime)s - [line:%(lineno)d] - %(module)s %(process)d %(thread)d %(message)s'
        },
        # 其他的 formatter
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'verbose'
        },
        'info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config_dir + '/info.log',
            'level': 'WARN',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config_dir + '/error.log',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        # 其他的 handler
        'datahub': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config_dir + '/datahub.log',
            'level': 'WARN',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'kafka': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config_dir + '/kafka.log',
            'level': 'WARN',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'schedular': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config_dir + '/schedular.log',
            'level': 'WARN',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'verbose'
        },
    },
    'loggers':{
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'PhasrLog': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'info', 'error'],
            'level': 'DEBUG',
        },
        'DataHub': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'datahub', 'error'],
            'level': 'DEBUG',
        },
        'KafkaTask': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'kafka', 'error'],
            'level': 'INFO',
        },
        'SchedularTask': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'schedular', 'error'],
            'level': 'INFO',
        }
    }
}

logging.config.dictConfig(config)
