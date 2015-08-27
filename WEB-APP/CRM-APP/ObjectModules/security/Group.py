#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from ObjectModules.security.base import SecurityObject,UserHandler

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