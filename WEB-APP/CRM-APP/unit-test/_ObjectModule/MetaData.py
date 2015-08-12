#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''
import unittest

class Test(unittest.TestCase):


    def testCitys(self):
        from ObjectModules.MetaData import getCitys
        for i in getCitys():
            print i
        self.assertTrue(True, "ok")
    def testDistrict(self):
        from ObjectModules.MetaData import getDistrict
        for i in getDistrict("001"):
            print i
        self.assertTrue(True, "ok")
    def testBusinessDistrict(self):
        from ObjectModules.MetaData import getBusinessDistrict
        for i in getBusinessDistrict("001:002"):
            print i
        self.assertTrue(True, "ok")


if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testBusinessDistrict']
    unittest.main()