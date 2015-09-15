#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''

from flask import session

from Session import Session


class __context__(object): 
    def createSession(self,user):
        ss=Session.CreateSession(user)
        session["session"]=dict(id=ss.ssid)
    
    @property
    def CurrentSession(self):
        if not hasattr(self,"__session__") or getattr(self, "__session__")==None:
            self.__session__=Session.LoadSession(session["session"]["id"])
        return self.__session__
    @property
    def Roles(self):
        sess = self.CurrentSession.roles
        
Context=__context__()