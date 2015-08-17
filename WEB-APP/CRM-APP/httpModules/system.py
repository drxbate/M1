#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template
from common import cacheManager
import json

admin = Blueprint("system",__name__)

@admin.route("/clear-cache")
def __clearCache__():
    cacheManager.clear()
    return json.dumps(dict(state=0))
