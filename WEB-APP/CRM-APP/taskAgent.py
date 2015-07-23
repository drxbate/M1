#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月23日

@author: ruixidong
'''
import TaskModules,time
import sys
from common import daemon

@daemon.Daemon("TaskDaemon")
def run():
    TaskModules.run_tasks()
    while True:
        time.sleep(100)

if __name__=='__main__':
    daemon.process(len(sys.argv)<2 and 'run' or sys.argv[1])