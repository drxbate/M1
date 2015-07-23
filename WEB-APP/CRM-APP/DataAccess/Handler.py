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
        Redis.__init__(self,host="140.206.217.95",port=6379,password="Enter4Me")

RedisCli=RedisHandler()

class MongoHandler(object):
    def __init__(self):
        self.client=MongoClient("mongodb://root:root@140.206.217.95/user")

    def opendb(self,name):
        db = self.client.get_database(name)
        #db.authenticate("root","root")
        return db
    def getUser(self):
        return self.opendb("user")
     

MongoCli=MongoHandler()