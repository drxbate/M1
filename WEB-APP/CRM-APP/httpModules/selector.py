#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,request
from ObjectModules import MetaData,Profile
import json

selector = Blueprint("selector",__name__)

@selector.route("/district")
def __district__():
    return render_template("/selector/district.html",citys=MetaData.ZoneInfo.getCitys())

@selector.route("/city")
def __city__():
    return render_template("/selector/city.html",citys=MetaData.ZoneInfo.getCitys())

@selector.route("/businessdistrict")
def __businessdistrict__():
    return render_template("/selector/businessdistrict.html",citys=MetaData.ZoneInfo.getCitys())

@selector.route("/mark")
def __mark__():
    return render_template("/selector/mark.html",marks=Profile.Marks())

@selector.route("/mark/add",methods=["POST"])
def __add_mark__():
    icon,iconColor,style,text=request.form.get("icon"),request.form.get("iconColor"),request.form.get("style"),request.form.get("text")
    m=Profile.Mark.newMark()
    m.icon = icon
    m.iconColor=iconColor
    m.style= style
    m.text=text
    Profile.Marks().append(m)
    return json.dumps(dict(state=0,id=m.__id__))

@selector.route("/mark/del/<id>",methods=["POST"])
def __del_mark__(id):
    Profile.Marks().remove(id)
    return json.dumps(dict(state=0,id=id))
    

