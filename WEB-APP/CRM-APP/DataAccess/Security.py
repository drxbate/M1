#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月25日

@author: ruixidong
'''
from Handler import RedisCli
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