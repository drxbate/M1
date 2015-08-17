#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
import sys
reload(sys)

setdefaultencoding = getattr(sys, "setdefaultencoding")

if setdefaultencoding:
    setdefaultencoding("utf8")

#init flask app ---begin
    
from flask import Flask, g, request,Response,url_for,redirect
import os
 
from flask.ext.bootstrap import Bootstrap
from common import cacheManager

app = Flask(__name__,template_folder="templates",static_folder="static")
app.config['SECRET_KEY'] = '123456'
app.debug = True

from htmlPlugins import FragmentPluginExtension
app.jinja_env.add_extension(FragmentPluginExtension)

bootstrap = Bootstrap(app)
cacheManager.init_cache(app)

#init flask app ---end

#load http modules for flask app --begin
from httpModules import *

app.register_blueprint(homePage,url_prefix= "/")
app.register_blueprint(extjs,url_prefix= "/js")
app.register_blueprint(securityPages,url_prefix="/security")
app.register_blueprint(profile,url_prefix="/cmo")
app.register_blueprint(demo,url_prefix="/demo")
app.register_blueprint(cust,url_prefix="/cust")
app.register_blueprint(metadata,url_prefix="/metadata")
app.register_blueprint(selector,url_prefix="/selector")
app.register_blueprint(admin,url_prefix="/admin")
#app.jinja_env.add_extension('jinja2.ext.i18n')

#load http modules for flask app --end

def run():
    print "run httpd"
    app.run(host="0.0.0.0",port=9910,debug=True)
    
    
if __name__=="__main__":
    run()