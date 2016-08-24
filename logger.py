#!/usr/bin/python
#-*- coding:utf-8 -*-

import logging
import logging.handlers
from setting import config

class Logging_Router(object):
    def __init__(self):
        cf = config()
        level_config = cf.get('log', 'level')
        log_file = cf.get('log', 'file_path')
        level = level_config.upper()
        level_dict = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      'CRITICAL': logging.CRITICAL,
                      'NOTSET': logging.NOTSET
                     }
        log_level = level_dict.get(level, '')
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        handler = logging.handlers.TimedRotatingFileHandler(log_file, when='M', interval=1, backupCount=10)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

class Logging_file(object):
    def __init__(self):
        cf = config()
        level_config = cf.get('log', 'level')
        log_file = cf.get('log', 'file_path')
        level = level_config.upper()
        level_dict = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      'CRITICAL': logging.CRITICAL,
                      'NOTSET': logging.NOTSET
                     }
        log_level = level_dict.get(level, '')
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
