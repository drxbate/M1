#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from DataAccess import User as UserHandler,Session as SessionHandler,Registion as RegistionHandler,Security as SecurityHandler
import json

class SecurityObject(dict):
    def __init__(self):
        self.__obj_id__=None
        self.__parents__=[]
    def get_parents(self):
        return self.__parents__
    @property
    def rights(self):
        return SecurityHandler.get_rights(self.__obj_id__)
    def allow(self,right):
        rv = SecurityHandler.check_right(self.__obj_id__, right)
        if rv==0:
            return 0
        elif rv==1:
            return 1
        
        rv = -1
        for i in self.get_parents():
            if i.allow==0:
                return 0
            elif i.allow==1:
                rv = 1
            
        return rv
    def __str__(self):
        return json.dumps(self)