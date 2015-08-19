#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月17日

@author: ruixidong
'''

from DataAccess import Profile
import json
from HttpContext import Context
from bson import ObjectId

class __profile__:
    def __init__(self):
        self.session=Context.CurrentSession
        self.uid=self.session.userid
    

class Mark:
    def __init__(self):
        self.__id__,self.icon,self.iconColor,self.style,self.text="","","","",""
    @classmethod
    def newMark(cls):
        m=Mark()
        m.__id__=str(ObjectId())
        return m
    @classmethod
    def serialize(cls,mark):
        return json.dumps(
                          dict(
                               __id__=mark.__id__,
                               icon=mark.icon,
                               iconColor=mark.iconColor,
                               style=mark.style,
                               text=mark.text,
                               )
                          )
    @classmethod
    def descerialize(cls,text):
        d=dict(__id__="",icon="",iconColor="",style="",text="",)
        d.update(json.loads(text))
        m=Mark()
        m.__id__,m.icon,m.iconColor,m.style,m.text=d["__id__"],d["icon"],d["iconColor"],d["style"],d["text"]
        return m
    def __eq__(self,obj):
        if type(obj)==str or type(obj)==unicode:
            return self.__id__==obj
        elif type(obj)==Mark:
            return self.__id__ == obj.__id__
        else:
            return False
    
class Marks(__profile__):
    def __init__(self,cls):
        __profile__.__init__(self)
        self.__items__=[]
        self.cls=cls
    @property
    def items(self):
        if len(self.__items__)<=0:
            l=Profile.getHashTable("__global__", "%s:mark"%self.cls)
            for k,i in l.items():
                m=Mark.descerialize(i)
                m.__lock__=True
                self.__items__.append(m)
                
            l=Profile.getHashTable(self.uid, "%s:mark"%self.cls)
            for k,i in l.items():
                self.__items__.append(Mark.descerialize(i))
        return self.__items__
    def __iter__(self):
        for i in self.items:
            yield i
    def append(self,*items):
        for i in items:
            Profile.updateHashTable(self.uid, "%s:mark"%self.cls, i.__id__,Mark.serialize(i))
    def remove(self,mark):
        _id=""
        if type(mark)==Mark:
            _id = mark.__id__
        else:
            _id = mark
        Profile.removeHashTable(self.uid,"%s:mark"%self.cls,_id)
        self.items.remove(mark)


        