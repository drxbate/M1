#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''
from flask import Blueprint,redirect
from ObjectModules import MetaData
import json

metadata = Blueprint("meta",__name__)

@metadata.route("/district/")
def __city__():
    citys = {}
    for cd,name in MetaData.getCitys():
        citys[cd] = name
    return json.dumps(citys)

@metadata.route("/district/<city>")
def __district__(city):
    districts = {}
    for cd,name in MetaData.getDistrict(city):
        districts[cd] = name
    return json.dumps(districts)

@metadata.route("/district/<city>/<district>")
def __business_district__(city,district):
    districts = {}
    for cd,name in MetaData.getBusinessDistrict(city,district):
        districts[cd] = name
    return json.dumps(districts)