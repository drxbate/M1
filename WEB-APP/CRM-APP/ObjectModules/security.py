#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
''' 
import md5,base64
from DataAccess import User as UserHandler,Session as SessionHandler,Registion as RegistionHandler,Security as SecurityHandler
from common import utility

def md5code(s):
    m = md5.new()
    m.update(s)
    return m.hexdigest()

class User(object):
    @classmethod
    def createUser(cls,username,password,info={}):
        RegistionHandler.pushRegistQueue(username, password, info)
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
        self.userinfo = UserHandler.getUserInfo(username)
        self.userid = str(self.userinfo["_id"])
        
class Session(object):
    @classmethod
    def CreateSession(cls,username):
        user = User(username)
        _id = user.userinfo["_id"]
        ssid = SessionHandler.createSession(_id)
        s=Session(ssid)
        s.data["user"]=user
        s.update()
        return s
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
    def __getattribute__(self, *args, **kwargs):
        name=args[0]
        if self.data.has_key(name):
            return self.data[name]
        else:
            return object.__getattribute__(self, *args, **kwargs) 
     
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
        
        
            
        