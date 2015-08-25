#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
import json

class Role(dict):
    def __init__(self,name,value):
        dict.__init__(self)
        self["name"],self["value"]=name,value
    def __str__(self):
        return json.dumps(self)
    
        