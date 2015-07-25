#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月25日

@author: ruixidong
'''
import random

def generateCode(bits):
    ran = random.Random()
    ss=""
    for i in range(0,bits):
        ss+="%d"%ran.randint(0, 9) 
    return ss
