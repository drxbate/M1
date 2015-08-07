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
        Redis.__init__(self,host="119.37.1.44",port=6379,password="Enter4Me")

RedisCli=RedisHandler()

class MongoHandler(object):
    def __init__(self):
        self.client=MongoClient("mongodb://root:access4Me@119.37.1.44:27017")
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