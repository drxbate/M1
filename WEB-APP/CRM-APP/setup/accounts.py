#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月25日

@author: ruixidong
'''
from DataAccess import User,Security
from ObjectModules import security


def main():
    objid = User.createUser("admin", "admin")
    Security.set_right(objid, [security.Role("admin",1)])

if __name__=="__main__":
    main()