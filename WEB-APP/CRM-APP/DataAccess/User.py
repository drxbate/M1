#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from Handler import MongoCli
import time
import json

def createUser(username,password,info=[]):
    return MongoCli.User["authinfo"].save({"username":username,"password":password,"info":info})

def getPassword(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"password":1})
    return None if auth == None else auth["password"]

def getUserInfo(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"username":1})
    return auth

def existsUser(username):
    return getPassword(username)!=None
