#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''
from DataAccess.Handler import RedisCli

def getProfile(uid,name,*args):
    tag = "profile:%s:%s"%(uid,name)
    return RedisCli.get(tag)
def putProfile(uid,name,value):
    tag = "profile:%s:%s"%(uid,name)
    RedisCli.set(tag, value)
def appendToArray(uid,name,*value):
    tag = "profile:%s:%s"%(uid,name)
    RedisCli.lpush(tag,*value)
def getArray(uid,name):
    tag = "profile:%s:%s"%(uid,name)
    c = RedisCli.llen(tag)
    ll = RedisCli.lrange(tag, 0, -1)
    return ll
def removeFromArray(uid,name,value):
    tag = "profile:%s:%s"%(uid,name)
    RedisCli.lrem(tag,value)
def getHashTable(uid,name):
    tag = "profile:%s:%s"%(uid,name)
    return RedisCli.hgetall(tag)
def updateHashTable(uid,name,key="",value="",**dict):
    tag = "profile:%s:%s"%(uid,name)
    if dict!=None and len(dict)>0:
        RedisCli.hmset(tag, dict)
    if name!=None:
        RedisCli.hset(tag,key,value)
def removeHashTable(uid,name,*keys):
    tag = "profile:%s:%s"%(uid,name)
    if keys!=None and len(keys)>0:
        RedisCli.hdel(tag,*keys)
    else:
        RedisCli.hdel(tag)
