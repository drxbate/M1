#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for
from common import Logger
profile=Blueprint("cmo",__name__)

@profile.route("/index.html",methods=["GET"])
def showHomePage():
    Logger.Info("www", "cmo..index")
    return render_template("cmo/index.html")


@profile.route("/leftnav.html")
def leftnav():
    return render_template("cmo/index.html",title="hhhh")