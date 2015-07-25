#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月23日

@author: ruixidong
'''
from Task import Task
from DataAccess import Registion,User,Security as SecurityHandler
from ObjectModules import security as SecurityModule
from common import sms
import sys



@Task("CreateUser")
def createUser():
    try:
        rInfo=Registion.popRegistQueue()
        if rInfo==None:
            return True
        #{"username":username,"password":password,"info":info}
        cellphone = rInfo["username"]
        objectId=User.createUser(cellphone, rInfo["password"], rInfo["info"])
        code = SecurityModule.Registion.generateCode(cellphone)
        sms.send(cellphone, "［C.M.O］动态六位编码 %s"%code)
    except:
        print sys.exc_info()
    return True