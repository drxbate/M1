#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月23日

@author: ruixidong
'''
from Task import Task
from DataAccess import User
import sys


@Task("CreateUser")
def createUser():
    try:
        rInfo=User.popRegistQueue()
        if rInfo==None:
            return True
        #{"username":username,"password":password,"info":info}
        objectId=User.createUser(rInfo["username"], rInfo["password"], rInfo["info"])
    except:
        print sys.exc_info() 
    return True