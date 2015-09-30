#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from ObjectModules.security.base import SecurityObject,UserHandler
import Domain,User

from common import DataAdapter,ItemsCollection,utility

class Group(SecurityObject):
    def __init__(self,domain,id,groupname,parents=[]):
        SecurityObject.__init__(self)
        self.__domain__=domain
        self.__id__=id
        self.name=groupname
        self.__parents__=parents
    @property
    def id(self):
        return self.__id__
    @property
    def parents(self):
        def __get_group__(_id):
            if not utility.is_validId(_id):
                return ""
            e = GroupCollection.getGroup(domain=self.__domain__,id=_id)
            if e==None:
                return ""
            else:
                return e.name
                
        ps = [__get_group__(_id) for _id in self.__parents__]
        ps = [v for v in ps if v!=""]
        return ",".join(ps)
    @property
    def domain(self):
        return Domain.DomainCollection.getDomain(self.__domain__)
    @property
    def group(self):
        return self.name
    @property
    def subgroups(self):
        return GroupCollection.querySubGroup(self.__domain__, self.__id__)
    @property
    def members(self):
        return User.UserCollection.queryUsers(domain=self.__domain__, groups=[self.__id__])
    
class GroupAdapter(DataAdapter):
    @property
    def Group(self):
        return Group(self.__domain__,self._id,self.name,self.__parents__)
    @property
    def id(self):
        return str(self._id)

class GroupCollection(ItemsCollection):
    @classmethod
    def querySubGroup(cls,domain,parent=None):
        if parent!=None:
            return GroupCollection(UserHandler.find_groups(domain,parents=[parent]))
        else:
            return GroupCollection(UserHandler.find_groups(domain,parents=[]))
    @classmethod
    def getGroup(cls,domain,id):
        for i in GroupCollection(UserHandler.find_group(domain=domain,id=id)):
            return i
    @classmethod
    def addGroup(cls,domain,group,parents=[]):
        objid=UserHandler.add_group(domain=domain,groupname=group, parents=parents)
        return objid
    @classmethod
    def saveGroup(cls,domain,id,newgroup="",parents=[]):
        objid=UserHandler.update_group(id=id,domain=domain,newgroupname=newgroup, parents=parents)
        return objid        
    def __init__(self,cursor):
        ItemsCollection.__init__(self, cursor, GroupAdapter)
    def __iter__(self):
        for i in ItemsCollection.__iter__(self):
            yield i.Group
