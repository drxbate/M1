#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月24日

@author: ruixidong
'''
from Handler import RedisCli
import time,uuid

def loadSession(ssid):
    return RedisCli.hgetall("sessions:%s"%ssid)

def updateSession(ssid,dict={}):
    RedisCli.expire("sessions:%s"%ssid, time+120*60)#2小时超时
    for k,v in dict.items():
        RedisCli.hset("sessions:%s"%ssid, k, v)

def createSession(userid):
    ssid=uuid.uuid1()
    RedisCli.hset("user:sessions:%s"%userid, ssid)
    return ssid
