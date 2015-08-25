#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
''' 
from base import SecurityObject,SecurityHandler,UserHandler

class Domain(SecurityObject):
    def __init__(self,domainName,parents=[]):
        SecurityObject.__init__(self)
        self.name=domainName
        self.__parents__=parents
    @classmethod
    def createDomain(cls,domain,parentDomain):
        UserHandler.update_domain(domain, parentDomain)