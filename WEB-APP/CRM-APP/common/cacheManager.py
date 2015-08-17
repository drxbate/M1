#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月13日

@author: ruixidong
'''
from flask.ext.cache import Cache

cache=None

def init_cache(app):
    global cache
    cache = Cache(app,config={'CACHE_TYPE': 'simple'})
    
def clear():
    cache.clear()