#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月27日

@author: ruixidong
'''

from flask import render_template
from jinja2 import ext,Environment,Template

'''
plugins:
{name1:tuple(func,template),name2:tuple(func,template)}
'''
plugins={}


def Plugin(name,template=None):
    def func(f):
        plugins[name]=(f,template if template!=None else name,)
    return func

def __rend_plugin__(name):
    global plugins
    if plugins.has_key(name):
        func,template=plugins[name]
        context=func()
        if context.has_key("__template__"):
            template=context["__template__"]
        else:
            context["__template__"]=template
        return render_template(template,**context)
    else:
        return {}
        


from jinja2 import nodes
from jinja2.ext import Extension


class FragmentPluginExtension(Extension):
    # a set of names that trigger the extension.
    tags = set(['plugin'])

    def __init__(self, environment):
        super(FragmentPluginExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            fragment_cache_prefix='',
            fragment_cache=None,
        )

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        args = [parser.parse_expression()]
        body = parser.parse_statements(['name:endplugin'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_render_plugin', args),
                               [], [], body).set_lineno(lineno)

    def _render_plugin(self, name, caller):
        rv = __rend_plugin__(name)
        return rv
