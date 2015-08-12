#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月30日

@author: ruixidong
'''
import unittest
from DataAccess import Customer


class Test(unittest.TestCase):


    def testNewCustomer(self):
        obj = Customer.saveCustomer("uid",None, "cellPhone", "legalName", "type", exinfo=dict(exinfo=1), tags=["buyer"], requirements=[1,2])
        print obj
        self.assertTrue(True, "创建客户资料测试成功")
        
    def testUpdateOwnerCustomer(self):
        self.assertTrue(True, "更新客户资料测试成功")
        obj = Customer.saveCustomer("uid",'55b9dd82cb5f8f2600f06b54',"cellPhone", "legalName", "type", exinfo=dict(exinfo=2), tags=["buyer"], requirements=[1,2])
        print obj
        self.assertTrue(True, obj)

    def testUpdateOthersCustomer(self):
        obj = Customer.saveCustomer("uid1",'55b9dd82cb5f8f2600f06b54',"cellPhone", "legalName", "type", exinfo=dict(exinfo=3), tags=["buyer"], requirements=[1,2])
        print obj
        self.assertTrue(True, "更新其他人的客户资料测试成功")
    
    def testQueryCustomer(self):
        cus = Customer.QueryCustomer("uid",sortby=[("type","desc",)])
        for i in cus:
            print i
        self.assertTrue(True, "查询客户资料成功")

if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testQueryCustomer']
    unittest.main()