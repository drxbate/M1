#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月28日

@author: ruixidong
'''
from DataAccess import Customer as CustomerHandler
from common import ItemsCollection,DataAdapter
from HttpContext import Context
from bson import ObjectId
import time

class Customer(object):
    def __init__(self,owner):
        '''
        {
        owner:用户ID，必须为str或bson.ObjectId类型
        '''
        if type(owner)==str:
            self.owner=ObjectId(owner)
        elif type(owner)!=ObjectId:
            raise Exception("owner is not ObjectId or str")
        else:
            self.owner = owner
  
    def count(self,*kinds):
        return CustomerHandler.count(self.owner, {"kinds":{"$IN":kinds}})
    
    def query(self,filter={},fields=[],sortby=[]):
        return ItemsCollection(CustomerHandler.QueryCustomer(self.owner, filter,fields,sortby),adapterClass=CustomerAdapter)
    

        
    def appedCustomer(self,cellPhone="",dispName="",type="PERSON",exinfo={},tags=[],requirements=[]):
        return CustomerHandler.saveCustomer(owner = self.owner,
                                    custid = None, 
                                    cellPhone = cellPhone, 
                                    dispName = dispName , 
                                    type = type, 
                                    exinfo = exinfo, 
                                    tags = tags, 
                                    requirements = requirements)
        
    def updateCustomer(self,custid,cellPhone="",dispName="",type="PERSON",exinfo={},tags=[],requirements=[]):
        CustomerHandler.saveCustomer(owner = self.owner,
                                    custid = custid, 
                                    cellPhone = cellPhone, 
                                    dispName = dispName , 
                                    type = type, 
                                    exinfo = exinfo, 
                                    tags = tags, 
                                    requirements = requirements)

class MyCustomer(Customer):
    def __init__(self):
        session = Context.CurrentSession
        Customer.__init__(self, session.userid)
    def total(self,key):
        exp="query_%s"%key
        func=getattr(self, exp)
        cur = func()
        return cur.count()
    def query_fav(self):
        return self.query(filter={"__fav__":1})
    def query_l10(self):
        from datetime import datetime,timedelta
        lmtime = datetime.now()-timedelta(days=10)
        lmtime = lmtime.strftime("%Y/%m/%d")
        return self.query(filter={"lmtime":{"$gt":lmtime}})
    def query_vip(self):
        return self.query(filter={"__vip__":1})
    def query_new(self):
        from datetime import datetime,timedelta
        ts = datetime.now()-timedelta(days=10)
        ts = ts.strftime("%Y/%m/%d")
        return self.query(filter={"__new_time__":{"$gt":ts}})
    def query_all(self):
        return self.query()
    def get(self,custid):
        for i in self.query(filter={"_id":ObjectId(custid)}):
            return i

class CustomerAdapter(DataAdapter):
    @property
    def Tags(self):
        tags = self.__tags__
        return tags
    @property
    def work4(self):
        return self.__data__["__exinfo__"]["work4"]
    @property
    def homeAdr(self):
        return self.__data__["__exinfo__"]["homeAdr"]
    @property
    def custid(self):
        return str(self.__data__["_id"])
    @property
    def requirements(self):
        return RequirementCollection(owner=self.__owner__, custid=self.custid)
    
class RequirementCollection(ItemsCollection):
    def __init__(self,owner,custid,):
        ItemsCollection.__init__(self, CustomerHandler.queryRequirement(owner=owner, custid=custid), adapterClass=RequirementAdapter)
        self.__custid__=custid
        self.__owner__=owner
    def save(self,reqid=None,**reqinfo):
        CustomerHandler.saveRequirement(owner=self.__owner__, custid=self.__custid__,reqid=reqid,reqinfo=reqinfo)
    def get(self,reqid):
        return [RequirementAdapter(i) for i in self.__cur__ if str(i["_id"])==reqid]
        
class RequirementAdapter(DataAdapter):
    pass
    
    