#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from ObjectModules.security.base import SecurityObject

class Group(SecurityObject):
    def __init__(self,groupname,parents=[]):
        SecurityObject.__init__(self)
        self.name=groupname
        self.__parents__=parents