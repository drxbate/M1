#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from base import SecurityHandler
from common import utility

class Registion(object):
    @classmethod
    def generateCode(cls,username):
        cd = ""
        while SecurityHandler.exists(cd) or cd=="":
            cd = utility.generateCode(6)
        SecurityHandler.bindCode(cd,info = dict(username=username),expire= 24*60)
        return cd
    @classmethod
    def validCode(cls,username,code):
        cdinfo = SecurityHandler.loadCode(code,keepAlive=True)
        return cdinfo and cdinfo["username"]==username