#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from base import SessionHandler
from User import User
import json
from common import Logger

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
        self.data = SessionHandler.loadSession(self.ssid)
        self.data["user"] = User("",data=self.data["user"])
    def update(self):
        SessionHandler.updateSession(self.ssid, self.data)
    @property
    def userid(self):
        return str(self.user.userid)
    @property
    def user(self):
        return self.data["user"]
    @property
    def groups(self):
        return str(self.user.groups)
    @property
    def domain(self):
        return str(self.user.domain)
    
    def allow(self,right):
        return self.user.allow(right)