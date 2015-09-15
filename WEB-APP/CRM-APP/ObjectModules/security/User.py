#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from base import SecurityObject,RegistionHandler,UserHandler
from common import ItemsCollection,DataAdapter
import Domain,Group

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
class UserAdapter(DataAdapter):
    @property
    def User(self):
        return User(self.username,self)
    @property
    def id(self):
        return str(self._id)
class UserCollection(ItemsCollection):
    @classmethod
    def queryUsers(cls,domain,groups=[]):
        return UserCollection(UserHandler.getUsers(domain=domain, groups=groups))
    @classmethod
    def getUser(cls,domain,id):
        for i in UserCollection(UserHandler.getUsers(domain, id=id)):
            return i
    @classmethod
    def addDomain(cls,domain,parent):
        objid=UserHandler.update_domain(name=domain, parent=parent)
        return objid
    @classmethod
    def saveDomain(cls,id,domain,parent):
        objid=UserHandler.update_domain(id=id,name=domain, parent=parent)
        return objid
    def __init__(self,cursor):
        ItemsCollection.__init__(self, cursor, UserAdapter)
    def __iter__(self):
        for i in ItemsCollection.__iter__(self):
            yield i.User