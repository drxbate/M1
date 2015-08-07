#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月24日

@author: ruixidong
'''
from Handler import RedisCli
import time,uuid,json

def loadSession(ssid):
    return RedisCli.hgetall("sessions:data:%s"%ssid)

def updateSession(ssid,dict={}):
    RedisCli.expire("sessions:data:%s"%ssid, 120*60)#2小时超时
    for k,v in dict.items():
        RedisCli.hset("sessions:data:%s"%ssid, k, json.dumps(v))

def clearSession(ssid):
    RedisCli.delete("sessions:data:%s"%ssid)#2小时超时

def createSession(userid):
    ssid = RedisCli.hget("sessions:users",userid)
    if ssid==None or ssid=="":
        clearSession(ssid)
    ssid=uuid.uuid1()
    RedisCli.hset("sessions:users",userid, ssid)
    return ssid
