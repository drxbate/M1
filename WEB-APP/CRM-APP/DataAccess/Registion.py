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
    lsn = RedisCli.get("registion:lsn")
    if lsn is None:
        lsn=1
    RedisCli.set("registion:lsn",lsn)
    return "%s%s-%06d"%(CD,monthcode,lsn)

def pushRegistQueue(username,password,info=[]):
    e = {"username":username,"password":password,"info":info}
    RedisCli.rpush("registion:queue",json.dumps(e))

def popRegistQueue():
    e = RedisCli.lpop("registion:queue")
    return None if e==None else json.loads(e)

