#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年9月30日

@author: ruixidong
'''
def func(name):
    class c:
        def __init__(self,func):
            self.func=func
        def __call__(self,*args,**params):    
            print "func"
            print args
            print "params"
            print params        
            return self.func(*args,**params)
            print "a"
    def _c(func):
        return c(func)
    return _c


@func("abc")
def dd(a,b):
    print "dd"
    print a,b
    return "result"

print "pre-call"
print dd(1,2)
print "called 0"
print dd(a=1,b=2)
print "called 1"