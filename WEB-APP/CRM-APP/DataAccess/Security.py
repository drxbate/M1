#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月25日

@author: ruixidong
'''
from Handler import RedisCli,MongoCli
from bson import ObjectId
import json

def bindCode(code,info={},expire=30):
    RedisCli.set("Security:bindCode:%s"%code, json.dumps(info),ex=expire*60)


def loadCode(code,keepAlive=False):
    if keepAlive:
        js=RedisCli.get("Security:bindCode:%s"%code)
    else:
        js = RedisCli.getset("Security:bindCode:%s"%code, "")
    return None if js=="" else json.loads(js)

def exists(code):
    return RedisCli.exists("Security:bindCode:%s"%code)


def check_right(objectid,right):
    name = "Security:rights:%s"%objectid
    return RedisCli.hget(name, right)
 
def get_rights(objectid):
    """
    return:rights
    [{"name":"value(0:allow|1:deny|Otherwise:inherits)"},....]
    e.g.
    [{"set_password_others":"0"}]
    """
    return RedisCli.hgetall("Security:rights:%s"%objectid)
def set_right(objectid,rights):
    """
    set list
    [{"name":"value(0:allow|1:deny|Otherwise:inherits)"},....]
    """
    name = "Security:rights:%s"%objectid
    for i in rights:
        RedisCli.hset(name, i["name"], i["value"])

def clear_right(objectid):
    name = "Security:rights:%s"%objectid
    RedisCli.hdel(name)
    

