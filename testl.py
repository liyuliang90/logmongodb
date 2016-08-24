#!/usr/bin/python
#-*- coding:utf-8 -*-

import logging
import logging.handlers
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
a=logging.handlers.TimedRotatingFileHandler('/mnt/work/testmongodb_log/message', when='S', interval=10, backupCount=10)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
a.setFormatter(formatter)
logger.addHandler(a)
c=0
while 1:
    c+=1
    logger.debug('hello:%s' % c)
    time.sleep(1)
