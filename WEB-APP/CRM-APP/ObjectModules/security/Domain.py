#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
''' 
from base import SecurityObject,SecurityHandler,UserHandler
from common import DataAdapter,ItemsCollection
import sys

from HttpContext import Context

class Domain(SecurityObject):
    def __init__(self,id,domainName,parent=None):
        SecurityObject.__init__(self)
        self.__id__=str(id)
        self.name=domainName
        self.__parents__.append(parent)
    @classmethod
    def createDomain(cls,domain,parentDomain):
        UserHandler.update_domain(domain, parentDomain)
    @property
    def id(self):
        return self.__id__
    @property
    def domain(self):
        return self.name
    @property
    def parent(self):
        for p in self.__parents__:
            if p!="" and p!=None:
                for i in DomainCollection(UserHandler.find_domain(id=p)):
                    return i
    @property
    def members(self):
        return UserHandler.getUsers(domain=self.domain).count()
    @property
    def subdomains(self):
        return UserHandler.find_domain(parent=self.id).count()
    @property
    def groups(self):
        return UserHandler.find_groups(domain=self.domain).count()
    def fetchPath(self):
        l = []
        p = self
        while p!=None:
            l.append(p)
            p = p.parent
        l.reverse()
        return l
    def __eq__(self, obj):
        if type(obj)==Domain and obj.id == self.id:
            return True
        else:
            return False
class DomainAdapter(DataAdapter):
    @property
    def Domain(self):
        return Domain(self._id,self.domain,self.__parent__)
    @property
    def id(self):
        return str(self._id)
    
class DomainCollection(ItemsCollection):
    @classmethod
    def querySubDomain(cls,parent=None,TopLevelOnly=False):
        if TopLevelOnly==True:
            if Context.CurrentSession.allow("system"):
                return DomainCollection(UserHandler.find_domain(parent=""))
            else:
                return DomainCollection(UserHandler.find_domain(parent=Context.CurrentSession.domain))
        if parent!=None:
            return DomainCollection(UserHandler.find_domain(parent=parent))
#         else:
#             return DomainCollection(UserHandler.find_domain())
    @classmethod
    def getDomain(cls,id):
        for i in DomainCollection(UserHandler.find_domain(id=id)):
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
        ItemsCollection.__init__(self, cursor, DomainAdapter)
    def __iter__(self):
        for i in ItemsCollection.__iter__(self):
            yield i.Domain