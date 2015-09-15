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
from common import Settings


def parseUser(username):
    
    if username.find("@")>0:
        username,domain = tuple(username.split("@",2))
    else:
        domain=""
    return username,domain
    

def createUser(username,password,**options):
    username,domain=parseUser(username)
    if domain=="":
        _domain=Settings.accounts.root_domain_id
    else:
        for i in find_domain(domain=domain):
            _domain=str(i["_id"])
            
    filter=dict(username=username,__domain__=_domain)
    data = dict(
                username=username,
                password=password,
                __domain__=_domain,
                __groups__=[] if not options.has_key("groups") else options["groups"]
                )
    MongoCli.User["authinfo"].update(filter,data,True,False)
    for i in MongoCli.User["authinfo"].find(filter):
        return str(i["_id"])

def changePassword(username,password):
    username,domain=parseUser(username)
    filter=dict(username=username,__domain__=domain)
    return MongoCli.User["authinfo"].update(filter,{"$set":{"password":password}})

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

def getUsers(domain,id=None,groups=[]):
    filters=dict(__domain__=domain)
    if groups!=None and len(groups)>1:
        filters["__groups__"]={"$all":groups}
    
    return MongoCli.User["authinfo"].find(filters)

def find_domain(**filter): 
    """
    filter:{id:...,parent:...}
    """
    __filters__={}
    
    if filter.has_key("id"):
        __filters__["_id"]=ObjectId(filter["id"])
    if filter.has_key("parent"):
        __filters__["__parent__"]=filter["parent"]
    return MongoCli.User["domain"].find(__filters__)

def add_root_domain(domain,info={}):
    data=dict(__parent__="",domain=domain,info=info)
    return MongoCli.User["domain"].save(data)

def add_domain(domain,parent=None,info={}):
    if parent=="" or parent==None:
        parent=Settings.accounts.root_domain_id
    data=dict(__parent__=parent,domain=domain,info=info)
    return MongoCli.User["domain"].save(data)

def update_domain(name,parent,id=None,info={}):
    data=dict(__parent__=parent,domain=name,info=info)
    if id==None:
        return add_domain(domain=name,parent=parent)
    else:
        MongoCli.User["domain"].update({"_id":ObjectId(id)},data,True,False)
        return id

def find_group(domain,id):
    if domain=="" or domain==None:
        domain = Settings.accounts.root_domain_id
    __filter__=dict(__domain__=domain,_id=ObjectId(id))
    return MongoCli.User["groups"].find(__filter__)

def find_groups(domain,parents=[]):
    if domain=="" or domain==None:
        domain = Settings.accounts.root_domain_id
    __filter__=dict(__domain__=domain)
    if len(parents)>0:
        __filter__["__parent__"]={"$in":parents}
    return MongoCli.User["groups"].find(__filter__)

def add_group(domain,groupname="",parents=None):
    if domain==None or domain=="":
        domain = Settings.accounts.root_domain_id
    data=dict(__domain__=domain,name=groupname,__parents__=parents)
    return MongoCli.User["groups"].save(data)
    

def update_group(domain,id=None,newgroupname="",parents=None):
    if domain=="" or domain==None:
        domain = Settings.accounts.root_domain_id
    data=dict(__domain__={"$set":domain},name={"$set":newgroupname},__parents__={"$set":parents})
    if parents==None:
        data.pop("__parents__")
    if newgroupname!="":
        data.update(dict(name=newgroupname))
    if id==None:
        return MongoCli.User["groups"].save(data)
    else:
        return MongoCli.User["groups"].update({"_id":ObjectId(id)},data,True,False)
