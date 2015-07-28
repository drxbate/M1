#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,redirect

homePage = Blueprint("app",__name__)

@homePage.route("")
@homePage.route("index.html")
def __homePage__():
    return redirect("security/login")