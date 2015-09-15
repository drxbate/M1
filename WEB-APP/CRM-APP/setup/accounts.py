#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月25日

@author: ruixidong
'''
from DataAccess import User,Security
from ObjectModules import security
from common import Settings


def create_domains():
    objid = User.add_root_domain(domain="<root>")
    Settings.accounts["root_domain_id"] = str(objid)
    Settings.save()
    
def create_users():
    objid = User.createUser("admin", "admin")
    Security.set_right(objid, [security.Role("admin",1)])
    
def main():
    objid = User.createUser("admin", "admin")
    Security.set_right(objid, [security.Role("admin",1)])

if __name__=="__main__":
    create_domains()
    create_users()