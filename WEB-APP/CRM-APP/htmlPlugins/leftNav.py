#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''
from flask import render_template,request
from ObjectModules.HttpContext import Context
from plugin import Plugin
from ObjectModules.Customer import MyCustomer


@Plugin("leftNav",template="plugin/leftnav.html")
def leftNav():
    if request.path.startswith(u"/admin/"):
    #user = Context.getCurrentSession().data["user"]
        return dict(user="user",cust=MyCustomer(),__template__="plugin/adminnav.html")
    else:
        return dict(user="user",cust=MyCustomer())

    