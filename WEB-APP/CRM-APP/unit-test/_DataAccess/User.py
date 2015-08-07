#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
import unittest
import sys

#sys.path.append("../../")
from DataAccess import Registion,User

class Test(unittest.TestCase):


    def createUser(self):
        objectid= User.createUser("13524157392", "123456")
        print objectid
        self.assertTrue(True, objectid)
        pass
    def registerUser(self):
        objectid= Registion.pushRegistQueue("test", "test", {"infoo":"132"})
        self.assertTrue(True, objectid)
        pass
    def readUserRegistion(self):
        rInfo = Registion.popRegistQueue()
        self.assertTrue(True, rInfo)
    def getUserInfo(self):
        userInfo = User.getUserInfo("test")
        self.assertTrue(True, userInfo)

if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.createUser']
    unittest.main()