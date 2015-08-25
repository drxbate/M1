#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: ruixidong
'''
from flask import render_template,request,render_template_string
from jinja2 import ext,Environment,Template

from jinja2 import nodes
from jinja2.ext import Extension
from ObjectModules.HttpContext import Context


class RolePluginExtension(Extension):
    # a set of names that trigger the extension.
    tags = set(['role'])

    def __init__(self, environment):
        super(RolePluginExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            fragment_cache_prefix='',
            fragment_cache=None,
        )

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        args = [parser.parse_expression()]
        #allow = Context.CurrentSession.allow(args.value)
        self.bodys=[]
        end_tokens=['name:noright','name:endrole']
        while 1:
            body = parser.parse_statements(end_tokens, drop_needle=False)
            self.bodys.append(body)
            
            token = parser.stream.next()
            if token.test("name:noright"):
                
                end_tokens.pop(0)
                continue
            elif token.test("name:endrole"):
                break
        
        result = nodes.If(
                          self.call_method('check_allow',args), #Expression
                          self.bodys[0], #True
                          None if len(self.bodys)<2 else self.bodys[1] #Else
                          ).set_lineno(lineno)
        return result
    def check_allow(self,role):
        allow = Context.CurrentSession.allow(role)
        return allow==1
    def _render_plugin(self, caller):
        return caller()  
        
    
