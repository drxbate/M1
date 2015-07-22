#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint

homePage = Blueprint("app",__name__)

@homePage.route("/app")
def __homePage__():
    return "Hello"