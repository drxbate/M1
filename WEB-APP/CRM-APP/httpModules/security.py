#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template


securityPages=Blueprint("security",__name__)

@securityPages.route("/login",methods=["GET"])
def loginForm():
    return render_template("security/login.html",title="title",nickname="nickname")