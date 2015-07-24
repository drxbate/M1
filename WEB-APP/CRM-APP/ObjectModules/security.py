#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
import md5,base64
from DataAccess import User as UserHandler,Session as SessionHandler

def md5code(s):
    m = md5.new()
    m.update(s)
    return m.hexdigest()

class User(object):
    @classmethod
    def createUser(cls,username,password,info={}):
        UserHandler.pushRegistQueue(username, password, info)
    @classmethod
    def updateUserInfo(cls,username,info={}):
        pass
    @classmethod
    def valid(cls,username,password):
        pwd = UserHandler.getPassword(username)
        return pwd==password
    @classmethod
    def exists(cls,username):
        return UserHandler.existsUser(username)
    def __init__(self,username):
        self.username = username
        userinfo = UserHandler.getUserInfo(username)
        self.userid = str(userinfo["_id"])
        
class Session(object):
    @classmethod
    def CreateSession(cls,username):
        user = User(username)
        _id = user.userinfo["_id"]
        ssid = SessionHandler.createSession(_id)
        s=Session(ssid)
        s.update()
    @classmethod
    def LoadSession(cls,ssid):
        s=Session(ssid)
        s.load()
    def __init__(self,ssid):
        self.ssid=None
        self.data={}
    def load(self):
        self.data = SessionHandler.loadSession(self.ssid)
    def update(self):
        SessionHandler.updateSession(self.ssid, self.data)
    
        
        