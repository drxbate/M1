#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from base import SecurityObject,RegistionHandler,UserHandler

class User(SecurityObject):
    @classmethod
    def createUser(cls,username,password,info={}):
        RegistionHandler.pushRegistQueue(username, password, info)
    @classmethod
    def changePassword(cls,username,password):
        UserHandler.changePassword(username, password)
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
        SecurityObject.__init__(self)
        if data==None:
            self['username'] = username
            self['userinfo'] = UserHandler.getUserInfo(username)
            self['userinfo']["_id"]=str(self.userinfo["_id"])
        else:
            self.update(data)
        self.__obj_id__=self['userinfo']["_id"]
    @property
    def username(self):
        return self["username"]
    @username.setter
    def username(self,value):
        self["username"]=value
    @property
    def userid(self):
        return self.__obj_id__
    @userid.setter
    def userid(self,value):
        self.__obj_id__=value
    @property
    def userinfo(self):
        return self["userinfo"]
    @userinfo.setter
    def userinfo(self,value):
        self["userinfo"]=value
    @property
    def groups(self):
        return []
    @property
    def domain(self):
        return None
    def get(self,k):
        if k=="userid":
            return self.__obj_id__
        return SecurityObject.get(self,k)
    def get_parents(self):
        parents=[]
        parents.extend(self.groups)
        parents.append(self.domain)
        return parents
