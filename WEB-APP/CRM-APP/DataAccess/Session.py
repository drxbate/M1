#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月24日

@author: ruixidong
'''
from Handler import RedisCli
import time,uuid,json

def loadSession(ssid):
    dict = RedisCli.hgetall("sessions:data:%s"%ssid)
    ss={}
    for k,v in dict.items():
        try:
            ss[k] = json.loads(v)
        except:
            ss[k] = v
    return ss

def updateSession(ssid,dict={}):
    RedisCli.expire("sessions:data:%s"%ssid, 120*60)#2小时超时
    RedisCli.hmset("sessions:data:%s"%ssid, dict)

def clearSession(ssid):
    RedisCli.delete("sessions:data:%s"%ssid)#2小时超时

def createSession(userid):
    ssid = RedisCli.hget("sessions:users",userid)
    if ssid==None or ssid=="":
        clearSession(ssid)
    ssid=uuid.uuid1()
    RedisCli.hset("sessions:users",userid, ssid)
    return ssid
