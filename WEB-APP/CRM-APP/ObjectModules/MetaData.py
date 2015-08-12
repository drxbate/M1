#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''

from DataAccess.MetaData import *

def getCitys():
    for city in getKeys("district","???"):
        cd = city.split(":")[-1]
        name = getData("district", cd)
        yield cd,name
        
def getDistrict(city):
    for district in getKeys("district",city,"???"):
        cd = district.split(":")[-1]
        name = getData("district",city, cd)
        yield cd,name.strip()

def getBusinessDistrict(city,district):
    if city!=None:
        district = city + ":" + district
    for bd in getKeys("district",district,"???"):
        cd = bd.split(":")[-1]
        name = getData("district",district,cd)
        yield cd,name.strip() 
        
class ZoneInfo(object):
    @classmethod
    def getCitys(cls):
        z=ZoneInfo()
        def __items__():
            return getCitys()
        z.__items__=__items__
        z.__parent__ = None
        return z
    @property
    def districts(self):
        z = ZoneInfo()
        def __items__():
            return getDistrict(self.cd)
        z.__items__=__items__
        z.__parent__=self
        return z
    @property
    def businessDistricts(self):
        z = ZoneInfo()
        def __items__():
            return getBusinessDistrict(self.__parent__.cd,self.cd)
        z.__items__=__items__
        z.__parent__=self
        return z
    def __iter__(self):
        for cd,name in self.__items__():
            self.cd = cd
            self.name = name
            yield self