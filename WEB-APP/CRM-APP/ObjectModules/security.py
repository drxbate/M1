#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
import md5,base64

def md5code(s):
    m = md5.new()
    m.update(s)
    return m.hexdigest()

class User(object):
    @classmethod
    def createUser(cls,username,password):
        pass
    @classmethod
    def updateUserInfo(cls,username,info={}):
        pass
    def __init__(self,username):
        self.username=username
    def auth(self,Password):
        if User.valid(self.username, self.password):
            return True
        else:
            return False