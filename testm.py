#!/usr/bin/python
#-*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client.test_db
collection = db.test_collection

a={'hello':2}

#collection.insert(a)

d=MongoClient('localhost', 27017)['mongolog']['log']
#d.save(a)
c=d.find()
for i in c:
    print i


