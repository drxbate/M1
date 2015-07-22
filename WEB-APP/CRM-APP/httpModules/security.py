#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for



securityPages=Blueprint("security",__name__)

@securityPages.route("/login",methods=["GET"])
def showLoginForm():
    return render_template("security/login.html",title="title",nickname="nickname")

@securityPages.route("/login",methods=["POST"])
def valid():
    user,pwd=request.form.get("user"),request.form.get("password")
    return redirect("../cmo/{0}/index.html".format(user))