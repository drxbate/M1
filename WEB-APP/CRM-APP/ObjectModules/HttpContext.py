#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''

from flask import session
from ObjectModules import security



class __context__(object): 
    def createSession(self,user):
        ss=security.Session.CreateSession(user)
        session["session"]=dict(id=ss.ssid)
    
    @property
    def CurrentSession(self):
        if not hasattr(self,"__session__") or getattr(self, "__session__")==None:
            self.__session__=security.Session.LoadSession(session["session"]["id"])
        return self.__session__
    @property
    def Roles(self):
        sess = self.CurrentSession.roles
        
Context=__context__()