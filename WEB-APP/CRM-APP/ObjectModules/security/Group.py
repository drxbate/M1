#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from ObjectModules.security.base import SecurityObject,UserHandler
from common import DataAdapter,ItemsCollection

class Group(SecurityObject):
    def __init__(self,groupname,parents=[]):
        SecurityObject.__init__(self)
        self.name=groupname
        self.__parents__=parents
    @property
    def parents(self):
        __group__=""
        def __get_group__(_id):
            e = UserHandler.find_group(id=_id)
            if e==None:
                return False
            else:
                __group__=e["name"]
                return True
        ps = [__group__ for _id in self.__parents__ if __get_group__(_id)]
        return ",".join(ps)

class GroupAdapter(DataAdapter):
    pass

class GroupCollection(ItemsCollection):
    @classmethod
    def querySubGroup(cls,domain,parent=None):
        if parent!=None:
            return GroupCollection(UserHandler.find_groups(domain,parents=[parent]))
        else:
            return GroupCollection(UserHandler.find_groups(domain,parents=[]))
    @classmethod
    def getGroup(self,domain,id):
        for i in GroupCollection(UserHandler.find_group(domain=domain,id=id)):
            return i
    @classmethod
    def addGroup(cls,domain,group,parents=[]):
        objid=UserHandler.update_group(domain=domain,newgroupname=group, parents=parents)
        return objid
    @classmethod
    def saveGroup(cls,domain,newgroup="",parents=[]):
        objid=UserHandler.update_group(id=id,domain=domain,newgroupname=newgroup, parent=parents)
        return objid        
    def __init__(self,cursor):
        ItemsCollection.__init__(self, cursor, GroupAdapter)
    pass