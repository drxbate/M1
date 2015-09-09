#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,request,redirect
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

@selector.route("/mark/<cls>")
def __mark__(cls):
    return render_template("/selector/mark.html",cls=cls,marks=Profile.Marks(cls))

@selector.route("/mark/<cls>/query",methods=["POST"])
def __query_mark__(cls):
    ids = request.form.get("ids")
    if ids==None:
        return json.dumps(dict(state=0,data=[]))
    m = Profile.Marks(cls)
    l=ids.split(",")
    ll = [i.__dict__ for i in m if i.__id__ in l]
    
    return json.dumps(dict(state=0,data=ll))

@selector.route("/mark/<cls>/add",methods=["POST"])
def __add_mark__(cls):
    icon,iconColor,style,text=request.form.get("icon"),request.form.get("iconColor"),request.form.get("style"),request.form.get("text")
    m=Profile.Mark.newMark()
    m.icon = icon
    m.iconColor=iconColor
    m.style= style
    m.text=text
    Profile.Marks(cls).append(m)
    return json.dumps(dict(state=0,id=m.__id__))

@selector.route("/mark/<cls>/del/<id>",methods=["POST"])
def __del_mark__(cls,id):
    Profile.Marks(cls).remove(id)
    return json.dumps(dict(state=0,id=id))

@selector.route("/domain")
def __domain__():
    return redirect("/admin/domain-selector?ex=%s"%request.args.get("ex"))
    
@selector.route("/group")
def __group__():
    return redirect("/admin/group-selector?ex=%s"%request.args.get("ex"))

