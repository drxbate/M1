#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,request
from common import cacheManager,utility
from ObjectModules import security
import json

admin = Blueprint("system",__name__)

@admin.route("/")
def __index__():
    return render_template("admin/index.html")

@admin.route("/clear-cache")
def __clearCache__():
    cacheManager.clear()
    return json.dumps(dict(state=0))

@admin.route("/domain-selector",methods=["GET"])
@admin.route("/domain",methods=["GET"]) 
def __domain__():
    '''
    id 当前域id，获取当前域的子域，如果为空，则获取全部顶层域
    exp 需要排除的，域id
    '''
    
    id,ex = request.args.get("id"),request.args.get("ex")
    if id!="" and id!=None:
        currentDomain=security.DomainCollection.getDomain(id)
        data = security.DomainCollection.querySubDomain(id)
    else:
        currentDomain=None
        data = security.DomainCollection.querySubDomain(TopLevelOnly=True)
    
    
    #def _compare(ref,obj):
    #    return obj.id != ref
    
    if request.path=="/admin/domain-selector":
        #data.addFilter(currentDomain.id,lambda ref,obj: ref.id != obj.id)
        #data.addFilter(ex,_compare)
        return render_template("admin/domain-selector.html", current = currentDomain, data=data,ex=ex)
    else:
        return render_template("admin/domain.html", current = currentDomain, data=data,ex=ex)


@admin.route("/domain/editor",methods=["GET"])
@admin.route("/domain/save",methods=["POST"])
def __domain_editor__():
    if request.path=="/admin/domain/save":
        id,domain,parent=request.form.get("id"),request.form.get("domain"),request.form.get("parent")
        if id==None:
            id=security.DomainCollection.addDomain(domain, parent)
            return json.dumps(dict(state=0,result=dict(id=str(id))))
        else:
            security.DomainCollection.saveDomain(id, domain, parent)
            return json.dumps(dict(state=0,result=dict(id=id)))
    else:
        id,parent = request.args.get("id"),request.args.get("parent")
        pId,pName,data="","",None
        if id==None:
            parent=security.DomainCollection.getDomain(parent)
            if parent!=None:
                pId,pName=parent.id,parent.domain
        else:
            data = security.DomainCollection.getDomain(id)
            if data!=None and data.parent!=None:
                pId,pName = data.parent.id,data.parent.name
                
        return render_template("admin/domain-editor.html",data=data,pId=pId,pName=pName)


@admin.route("/group-selector",methods=["GET"])
@admin.route("/group",methods=["GET"]) 
def __group__():
    '''
    id 当前域id，获取当前域的子域，如果为空，则获取全部顶层域
    exp 需要排除的，域id
    '''
    _domain=security.Context.CurrentSession.domain
    domain,id= request.args.get("domain"),request.args.get("id")
    _domain="%s"%(domain if domain!=None and domain!="" else _domain,)
    
    if id!="" and id!=None:
        data = security.GroupCollection.querySubGroup(_domain,parent=id)
    else:
        data = security.GroupCollection.querySubGroup(_domain)
    
    
    #def _compare(ref,obj):
    #    return obj.id != ref
    
    if request.path=="/admin/group-selector":
        #data.addFilter(currentDomain.id,lambda ref,obj: ref.id != obj.id)
        #data.addFilter(ex,_compare)
        return render_template("admin/group-selector.html",domain=_domain, data=data)
    else:
        return render_template("admin/group.html", domain=_domain, data=data)
    
@admin.route("/group/editor")
@admin.route("/group/save",methods=["POST"])
def __group_editor__():
    if request.path=="/admin/group/save":
        domain,id,group,parents=request.form.get("domain"),request.form.get("id"),request.form.get("group"),request.form.get("parents")
        if id==None or id=="":
            parents=("%s"%parents).split(" ")
            
            id=security.GroupCollection.addGroup(domain, group, parents)
            return json.dumps(dict(state=0,result=dict(id=str(id))))
        else:
            security.GroupCollection.saveGroup(domain=domain, id=id, group=group, parents=parents)
            return json.dumps(dict(state=0,result=dict(id=str(id))))
    else:
        domain,id = request.args.get("domain"),request.args.get("id")
        data=None
        if id!=None:
            data = security.GroupCollection.getGroup(domain,id)
        
        domain = None if not utility.is_validId(domain) else security.DomainCollection.getDomain(domain)
        return render_template("admin/group-editor.html",data=data,domain=domain,id=id)
    