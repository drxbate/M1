#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from Handler import RedisCli,MongoCli
import time
import json

def calcUserCode(CD):
    monthcode="%4d%2d"%time.localtime()
    lsn = RedisCli.get("security:lsn")
    if lsn is None:
        lsn=1
    RedisCli.set("security:lsn",lsn)
    return "%s%s-%06d"%(CD,monthcode,lsn)

def pushRegistQueue(username,password,info=[]):
    e = {"username":username,"password":password,"info":info}
    RedisCli.rpush("security:register",json.dumps(e))

def popRegistQueue():
    e = RedisCli.lpop("security:register")
    return None if e==None else json.loads(e)

def createUser(username,password,info=[]):
    return MongoCli.User["authinfo"].save({"username":username,"password":password,"info":info})

def getPassword(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"passowrd":1})
    return None if auth == None else auth["passowrd"]

def getUserInfo(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"username":1})
    return auth

def existsUser(username):
    return getPassword(username)!=None
