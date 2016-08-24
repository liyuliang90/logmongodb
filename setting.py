#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import ConfigParser

class config():
    def __init__(self):
        config_path = os.path.abspath(os.path.dirname(__file__))
        config_file = os.path.join(config_path, 'config.conf')
        self.body = ConfigParser.ConfigParser()
        self.body.read(config_file)

    def get(self,block,key):
        return self.body.get(block,key)

