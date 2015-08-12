#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template
from ObjectModules import MetaData
selector = Blueprint("selector",__name__)

@selector.route("/district")
def __district__():
    return render_template("/selector/district.html",citys=MetaData.ZoneInfo.getCitys())