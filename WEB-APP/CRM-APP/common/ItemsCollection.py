#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月30日

@author: ruixidong
'''

class ItemsCollection(object):
    def __init__(self,cursor,adapterClass=None):
        self._pageSize=-1
        self._page=-1
        self.__cur__=cursor
        self.__count__ = self.__cur__.count()
        self.adapterClass = adapterClass
        self.__filters__=[]
        
    def count(self):
        return self.__count__

    @property
    def pageSize(self):
        return self._pageSize
    @pageSize.setter
    def pageSize(self,pageSize=1):
        self._pageSize=pageSize
        
    @property
    def page(self):
        return self._page
    @page.setter
    def page(self,pageNumber=1):
        self._page=pageNumber
        self.__cur__.limit(self._pageSize).skip(self._page*self._pageSize)
    def __iter__(self):
        #yield self.__cur__.next()
        for i in self.__cur__:
            if self.adapterClass==None:
                r = i
            else:
                r = self.adapterClass(i)
            
            ex = [1 for reference,comparater in self.__filters__ if not comparater(reference,r)]
            if len(ex)==0:
                yield r

    def addFilter(self,reference,comparater):
        '''
        comparater=lambda reference,cur:reference==cur
        '''
        self.__filters__.append((reference,comparater,))