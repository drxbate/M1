#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''
from flask import Blueprint,send_file,Response
from common.cacheManager import cache
from os.path import exists
ext=Blueprint("js",__name__)

@cache.cached(timeout=10*60*60)
@ext.route("/ext.js",methods=["GET"])
def extjs():
    def response_scripts():
        with open("static/js/ext.js") as f:
            yield "//readfile..."
            for l in f:
                l=l.strip("\n")
                if l.startswith("#"):
                    continue
                js = "static/js/%s"%l
                if not exists(js):
                    continue
                
                with open(js) as sf:
                    yield sf.read()
                    sf.close()
            f.close();
    return Response(response_scripts(), content_type='text/javascript')