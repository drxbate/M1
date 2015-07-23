#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月23日

@author: ruixidong

守护进程定义

定义守护进程
@daemon.Daemon("TaskDaemon")
def run():
    TaskModules.run_tasks()
    while True:
        time.sleep(100)
        
启动守护进程
daemon.process()
'''

from multiprocessing import Process
import sys
from time import sleep

__Task_list__={}

def Task(name,intterupt=1):
    def func(f):
        __Task_list__[name]=dict(func=f,intterupt=intterupt)
    return func


def __roll__(func,intterupt):
    while func():
        sleep(intterupt)


def run_tasks():
    for k,t in __Task_list__.items():
        func = t["func"]    
        intterupt=t["intterupt"]
        p=Process(target=__roll__,args=(func,intterupt))
        p.name=k
        p.daemon=True
        p.start()
        t["Process"]=p
        
        

def stop_task(name):
    try:
        t = __Task_list__[name]
        t.terminate()
    except:
        print sys.exc_info()