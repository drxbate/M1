#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Flask, g, request,Response,url_for,redirect
import os
from httpModules import *
 
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__,template_folder="templates",static_folder="static")
app.debug = True
app.register_blueprint(homePage,url_prefix= "/")
app.register_blueprint(securityPages,url_prefix="/security")
app.register_blueprint(profile,url_prefix="/cmo")

bootstrap = Bootstrap(app)

def run():
    print "run httpd"
    app.run(host="0.0.0.0",port=9910,debug=True)
    
    
if __name__=="__main__":
    run()