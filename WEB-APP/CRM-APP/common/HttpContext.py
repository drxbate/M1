#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''

from flask import session
from ObjectModules import security



class __context__(object): 
    @property
    def CurrentSession(self):
        if not hasattr(self,"__session__"):
            self.__session__=security.Session.LoadSession(session["ssid"])
        return self.__session__
    
Context=__context__()