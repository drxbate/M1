#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月7日

@author: ruixidong


Adpater(object):
    __init__(self) 初始化对象
    __parse__(self,object) 转换方法
'''

class DataAdapter(object):
    def __init__(self,data={}):
        object.__init__(self)
        object.__setattr__(self,"__data__",data)
    def __parse__(self,data={}):
        __data__=object.__getattribute__(self,"__data__")
        __data__.update(data)
    def __getattribute__(self,name):
        if name!="__data__" and self.__data__.has_key(name):
            return self.__data__[name]
        else:
            return object.__getattribute__(self,name)
    def __setattr__(self, name,value):
        if name!="__data__" and self.__data__.has_key(name):
            self.__data__[name]=value
        else:
            object.__setattr__(self,name,value)
            
if __name__=="__main__":
    a=DataAdapter({'a':1})
    print a