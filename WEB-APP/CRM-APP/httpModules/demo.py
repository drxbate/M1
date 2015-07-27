#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for

demo=Blueprint("demo",__name__)

@demo.route("/<page>.html",methods=["GET"])
def showDemoPage(page):
    return render_template("demo/%s.html"%page)
