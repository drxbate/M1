#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月17日

@author: ruixidong
'''

from ObjectModules.Profile import Mark,Marks
from DataAccess.Handler import RedisCli
from DataAccess import Profile

tags=[dict(__id__="cs01",text="诚意客户",style="mark-style-1",icon="flag",iconColor="red"),
      dict(__id__="cs02",text="独家委托",style="mark-style-1",icon="flag",iconColor="red"),
      dict(__id__="cs03",text="多次带看",style="mark-style-1",icon="flag",iconColor="red"),
      dict(__id__="cs04",text="老客户",style="mark-style-1",icon="flag",iconColor="red"),
      ]

if __name__=="__main__":
    RedisCli.delete("profile:__global__:cust:mark")
    
    for i in tags:
        m = Mark()
        m.__id__=i["__id__"]
        m.icon = i["icon"]
        m.iconColor = i["iconColor"]
        m.style = i["style"]
        m.text = i["text"]
        Profile.updateHashTable("__global__", "mark", m.__id__,Mark.serialize(m))