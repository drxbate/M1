#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for

profile=Blueprint("cmo",__name__)

@profile.route("/<username>/index.html",methods=["GET"])
def showHomePage(username):
    return "Welcome {0}".format(username)
