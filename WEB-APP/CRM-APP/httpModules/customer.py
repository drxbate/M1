#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,render_template,session,request,redirect,url_for
from ObjectModules.Customer import MyCustomer
import json

cust=Blueprint("cust",__name__)

@cust.route("/vip",methods=["GET"])
def vip():
    return render_template("customer/custlist.html",NAV_ID="CUST_VIP",cust=MyCustomer().query_vip())

@cust.route("/l10",methods=["GET"])
def l10():
    return render_template("customer/custlist.html",NAV_ID="CUST_L10",cust=MyCustomer().query_l10())

@cust.route("/fav",methods=["GET"])
def fav():
    return render_template("customer/custlist.html",NAV_ID="CUST_FAV",cust=MyCustomer().query_fav())

@cust.route("/newlist",methods=["GET"])
def newlist():
    return render_template("customer/custlist.html",NAV_ID="CUST_NEW_LIST",cust=MyCustomer().query_new())

@cust.route("/all",methods=["GET"])
def allList():
    return render_template("customer/custlist.html",NAV_ID="CUST_ALL",cust=MyCustomer().query_all())


@cust.route("/new",methods=["GET","POST"])
@cust.route("/edit",methods=["GET"])
@cust.route("/view",methods=["GET"])
def _new():
    custid = request.form.get("custid")
    custid = custid if custid!=None else request.args.get("custid")
    tel = request.form.get("cellphone")
    customer=MyCustomer()
    cust = customer.get(custid)
    if request.path=="/cust/new":
        return  render_template("customer/form.html",cust=None)
    else:
        if request.path=="/cust/edit":
            return render_template("customer/form.html",cust=cust)
        else:
            return render_template("customer/view.html",cust=cust)
    

@cust.route("/save",methods=["GET","POST"])
def _save():
    custid = request.form.get("custid")
    dispName = request.form.get("dispName")
    cellphone = request.form.get("cellphone")
    work4 = request.form.get("work4")
    homeAdr = request.form.get("homeAdr")
    c=None
    myCust=MyCustomer()
    try:
        c = myCust.get(custid)
    except:
        pass
    
    if c==None:
        custid=MyCustomer().appedCustomer(cellphone, dispName, "PERSON", {"work4":work4,"homeAdr":homeAdr}, [], [])
    else:
        MyCustomer().updateCustomer(custid,cellphone, dispName, "PERSON", {"work4":work4,"homeAdr":homeAdr}, c.__data__["__tags__"], c.__data__["__req__"])
    return json.dumps(dict(state=0,result=dict(custid=str(custid))))

# @cust.route("/form",methods=["GET"])
# def editor():
#     return render_template("customer/form.html")




@cust.route("/my",methods=["GET"])
def mycust():
    tel = request.args.get("tel")
    info = MyCustomer().query(filter={"cellphone":tel},fields=["cellphone","dispName","_id"])
    l=[]
    for i in info:
        l.append(i)
    return json.dumps(l)

@cust.route("/requirement/new")
@cust.route("/requirement/edit")
def requirement():
    custid = request.args.get("custid")
    reqid = request.args.get("reqid")
    cust = MyCustomer().get(custid)
    req = cust.requirements.get(reqid)
    return render_template("customer/requirement.html",cust=cust,req=req)

@cust.route("/requirement/save",methods=["POST"])
def save_requirement():
    custid = request.form.get("custid")
    reqid = request.form.get("reqid")
    cust = MyCustomer().get(custid)
    
    reqinfo={}
    for k,item in request.form.items():
        if k in ["custid","reqid"]:
            continue
        reqinfo[k]=item
    
    req = cust.requirements
    req.save(reqid=reqid,**reqinfo)
    
    return json.dumps(dict(state=0,data=dict(reqid="")))

@cust.route("/form-template/<name>")
def form_template(name):
    return render_template("customer/form/%s.html"%name)
