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
    if security.User.valid(user, pwd):
        return redirect("../cmo/index.html")
    else:
        render_template("security/login.html",title="title",nickname="nickname",error="用户名或密码错误...")

@securityPages.route("/registion",methods=["GET"])
def registion():
    return render_template("security/registion.html")

@securityPages.route("/registion",methods=["POST"])
def regist_user():
    user,pwd=request.form.get("user"),request.form.get("password")
    security.User.createUser(user, pwd, {}) 
    return redirect("security/registion-confirm-form?user=%s"%user)

@securityPages.route("/registion-confirm-form",methods=["GET"])
def confirmCodeForm():
    errors={"invalidcode":"无效编码，请重新获取"}
    errcode = request.args.get("error")
    
    user=request.args.get("user")
    
    errormessage="" if errcode==None or errcode=="" else "未知错误" if errors.has_key(errcode) else errors[errcode]
    
    return render_template("security/registion-confirm.html",error=errormessage,username=user)


@securityPages.route("/registion-code-confirm",methods=["POST"])
def confirmCode():
    user,code=request.form.get("user"),request.form.get("code")
    if security.Registion.validCode(user, code):
        ss = security.Session.CreateSession(user)
        session["ssid"]=ss.ssid
        return redirect("../cmo/index.html")
    else:
        return redirect("security/registion-confirm-form?user=%s&error=invalidcode"%user)

@securityPages.route("/exists",methods=["GET"])
def exists_user():
    user=request.args.get("user")
    if security.User.exists(user):
        return json.dumps(dict(state=1))
    else:
        return json.dumps(dict(state=0))