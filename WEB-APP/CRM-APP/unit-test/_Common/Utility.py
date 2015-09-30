#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月25日

@author: ruixidong
'''
import unittest
from common import utility 

class Test(unittest.TestCase):


    def testGenerateCode(self):
        code = utility.generateCode(6)
        self.assertTrue(True, code)
        


if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testGenerateCode']
    unittest.main()