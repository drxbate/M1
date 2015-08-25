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
        body = parser.parse_statements(['noright','name:endplugin'], drop_needle=True)
        body_0 = parser.parse_statements(['name:endplugin'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_render_plugin', args),
                               [], [], body).set_lineno(lineno)

    def _render_plugin(self, role, caller):
        
        return caller()
