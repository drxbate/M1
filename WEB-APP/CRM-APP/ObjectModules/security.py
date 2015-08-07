#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
''' 
import md5,base64
from DataAccess import User as UserHandler,Session as SessionHandler,Registion as RegistionHandler,Security as SecurityHandler
from common import utility
import json

def md5code(s):
    m = md5.new()
    m.update(s)
    return m.hexdigest()

class User(dict):
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
    def __init__(self,username,data=None):
        dict.__init__(self)
        if data==None:
            self['username'] = username
            self['userinfo'] = UserHandler.getUserInfo(username)
            self['userinfo']["_id"]=str(self.userinfo["_id"])
            self['userid'] = self.userinfo["_id"]
        else:
            self.update(data)
    @property
    def username(self):
        return self["username"]
    @username.setter
    def username(self,value):
        self["username"]=value
    @property
    def userid(self):
        return self["userid"]
    @userid.setter
    def userid(self,value):
        self["userid"]=value
    @property
    def userinfo(self):
        return self["userinfo"]
    @userinfo.setter
    def userinfo(self,value):
        self["userinfo"]=value
    
class Session(object):
    @classmethod
    def CreateSession(cls,username):
        user = User(username)
        _id = user.userid
        ssid = SessionHandler.createSession(_id)
        s=Session(ssid)
        s.data["user"]=user
        s.update()
        return s
    @classmethod
    def LoadSession(cls,ssid):
        s=Session(ssid)
        s.load()
        return s
    def __init__(self,ssid):
        self.ssid=ssid
        self.data={}
    def load(self):
        data = SessionHandler.loadSession(self.ssid)
        data["user"]=json.loads(data["user"])
        self.data = User("",data=data)
    def update(self):
        SessionHandler.updateSession(self.ssid, self.data)
    @property
    def userid(self):
        return str(self.data["user"]["userid"])


     
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
        
        
            
        