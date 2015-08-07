#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月28日

@author: ruixidong

Customer结构
{
'__owner__':ObjectId(owner), ＃所属用户ID,userid
'type':str(type), #客户类型 PERSON 个人/LEGALENTITY 法人／公司 
'cellphone':str(cellPhone), ＃主要联系手机号
'dispName':str(dispName) ＃显示名称,
'__exinfo__':{}, ＃ 客户扩展信息
'__tags__':[], ＃标签
'__req__':[], #需求列表
'__lmtime__:datetime.strftime("%Y/%m/%d"), #最近经营日期
'__fav__':0|1,#是否收藏
'__vip__':0|1#是否VIP客户
} 

'''
from Handler import MongoCli
from bson import ObjectId
from datetime import datetime,timedelta

def QueryCustomer(owner="",filter={},fields=[],sortby=[]):
    '''
    sortby=[('field1','asc'),('field2','desc')]
    options={
    pageSize:10,
    page:1
    }
    '''
    sorts={"asc":1,"desc":-1}
    filter.update(dict(__owner__=owner))
#     
#     items = []
#     for f in fields:
#         items.append({f:1})
    if len(fields)>0:
        custs=MongoCli.Customer["custinfo"].find(filter,fields)
    else:
        custs=MongoCli.Customer["custinfo"].find(filter)
    if len(sortby)>0:
        sEx=[]
        for f,s in sortby:
            sEx.append((f,sorts[s],))
        custs.sort(sEx)
    return custs

def count(owner,filter):
    custs=MongoCli.Customer["custinfo"].find(filter)
    return custs.count()

def saveCustomer(owner="",custid="",cellPhone="",dispName="",type="PERSON",exinfo={},tags=[],requirements=[]):
    #custid=None while creating a customer
    
    custinfo={}
    custinfo.update(dict(__owner__=owner,type=type,cellphone=cellPhone,dispName=dispName,__exinfo__=exinfo,__tags__=tags,__req__=requirements))
    if custid!=None:
        cust = MongoCli.Customer["custinfo"].find_one({'_id':ObjectId(custid)},{"__owner__":1})
        if cust["__owner__"]!=owner:
            raise Exception("非当前用户客户，不可进行修改")
        else:
            MongoCli.Customer["custinfo"].update({'_id':ObjectId(custid)},custinfo)
    else:
        ts = datetime.now()
        ts = ts.strftime("%Y/%m/%d")
        custinfo.update(dict(__new_time__=ts))
        custid = MongoCli.Customer["custinfo"].save(custinfo)
    return custid
    