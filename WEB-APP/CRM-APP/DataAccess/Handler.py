#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from redis import Redis
from pymongo import MongoClient

class RedisHandler(Redis):
    def __init__(self):
        Redis.__init__(self,host="10.8.0.1",port=6379,password="Enter4Me")

RedisCli=RedisHandler()

class MongoHandler(object):
    def __init__(self):
        if not hasattr(MongoHandler, "DATABASE"):
            #"mongodb://root:access4Me@10.8.0.1:27017"
            setattr(MongoHandler, "DATABASE", MongoClient("mongodb://10.8.0.1:27017"))
        self.client=getattr(MongoHandler,"DATABASE")
    def opendb(self,name):
        db = self.client.get_database(name)
        #db.authenticate("root","root")
        return db
    @property
    def User(self):
        return self.opendb("user")
    @property
    def Customer(self):
        return self.opendb("customerdb")

MongoCli=MongoHandler()