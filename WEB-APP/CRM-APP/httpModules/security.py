#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for
from ObjectModules import security
import json,time


securityPages=Blueprint("security",__name__)

@securityPages.route("/login",methods=["GET"])
def showLoginForm():
    return render_template("security/login.html",title="title",nickname="nickname")

@securityPages.route("/login",methods=["POST"])
def valid():
    user,pwd=request.form.get("user"),request.form.get("password")
    return redirect("../cmo/{0}/index.html".format(user))

@securityPages.route("/registion",methods=["GET"])
def registion():
    return render_template("security/registion.html")

@securityPages.route("/registion",methods=["POST"])
def regist_user():
    user,pwd=request.form.get("user"),request.form.get("password")
    security.User.createUser(user, pwd, {})
    
@securityPages.route("/exists",methods=["GET"])
def exists_user():
    user=request.args.get("user")
    if security.User.exists(user):
        return json.dumps(dict(state=1))
    else:
        return json.dumps(dict(state=0))