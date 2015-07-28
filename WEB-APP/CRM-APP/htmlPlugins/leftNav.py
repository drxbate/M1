#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''
from flask import render_template
from common.HttpContext import Context
from plugin import Plugin

@Plugin("leftNav",template="plugin/leftnav.html")
def leftNav():
    #user = Context.getCurrentSession().data["user"]
    return dict(user="user")
