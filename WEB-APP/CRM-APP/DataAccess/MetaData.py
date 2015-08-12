#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''
from DataAccess.Handler import RedisCli

def getData(name,*args):
    tag = "metadata:%s"%name
    if type(args)==str:
        tag+=":"+args
    else:
        for i in args:
            tag+=":"+i
    return RedisCli.get(tag)
def getKeys(name,*filters):
    tag = "metadata:%s"%name
    if type(filters)==str:
        tag+=":"+filters
    else:
        for i in filters:
            tag+=":"+i
    return RedisCli.keys(tag)