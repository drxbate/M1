#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from Handler import MongoCli
import time
import json
from bson import ObjectId


def parseUser(username):
    if username.index("@")>0:
        username,domain = tuple(username.split("@",2))
    else:
        domain=""
    return username,domain
    

def createUser(username,password,**options):
    username,domain=parseUser(username)
    data = dict(
                username=username,
                password=password,
                __domain__=domain,
                __groups__=options["groups"]
                )
    return MongoCli.User["authinfo"].save(data)

def addGroup(username,*groups):
    username,domain=parseUser(username)
    filter=dict(username=username,__domain__=domain)
    for group in groups:
        MongoCli.User["authinfo"].update(filter,{"$push":{"__groups__":group}})

def quitGroup(username,group):
    MongoCli.User["authinfo"].update(filter,{"$pop":{"__groups__":group}})

def getPassword(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"password":1})
    return None if auth == None else auth["password"]

def getUserInfo(username):
    auth = MongoCli.User["authinfo"].find_one({"username":username},{"username":1})
    return auth

def existsUser(username):
    return getPassword(username)!=None

def find_domain(**filter): 
    """
    filter:{id:...,parent:...}
    """
    __filters__={}
    
    if filter.has_key("id"):
        __filters__["_id"]=ObjectId(filter["id"])
    if filter.has_key("parent"):
        __filters__["__parent__"]=ObjectId(filter["parent"])
    return MongoCli.User["domain"].find(__filters__)

def update_domain(name,parent,info={}):
    data=dict(__parent__=parent,domain=name,info=info)
    return MongoCli.User["domain"].update({"domain":name},data,True,False)
    
def find_groups(domain,parents=[]):
    __filter__=dict(__domain__=domain)
    if len(parents)>0:
        __filter__["__parent__"]={"$in":parents}
    return MongoCli.User["group"].find(__filter__)

def update_group(domain,groupname,parents=[]):
    data=dict(__domain__=domain,name=groupname,__parents__=parents)
    return MongoCli.User["group"].update({"name":groupname},data,True,False)
