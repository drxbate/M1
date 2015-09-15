#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月25日

@author: ruixidong
'''
import random
import md5,base64
from bson import ObjectId

def generateCode(bits):
    ran = random.Random()
    ss=""
    for i in range(0,bits):
        ss+="%d"%ran.randint(0, 9) 
    return ss

def md5code(s):
    m = md5.new()
    m.update(s)
    return m.hexdigest()

def is_validId(oid):
    return ObjectId.is_valid(oid)