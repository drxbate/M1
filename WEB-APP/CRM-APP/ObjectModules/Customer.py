#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月28日

@author: ruixidong
'''
from DataAccess import Customer as CustomerHandler
 
class MyCustomer(object):
    def __init__(self,uid):
        self.uid = uid
    @property
    def count(self,*kinds):
        return CustomerHandler.Count(self.uid, {"kinds":{"$IN":kinds}})
    
    def query(self,filter={},fields=[],sortby=[]):
        return CustomerHandler.QueryCustomer(self.uid, filter,fields,sortby)
    
    