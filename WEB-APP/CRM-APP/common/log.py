#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-9-17

@author: Rich
'''
import logging,os
DEBUG,INFO,WARN=logging.INFO,logging.DEBUG,logging.INFO
'''
set config LOG_PATH and APP_NAME(Default logfile prefix)
'''
BASIC_LOG_PATH="log"
APP_NAME="ayi"

'''
Extend config-info
e.g.
{
"new1": {"file":"new1","level":DEBUG},
"new2": {"file":"new2","level":DEBUG},
:
:
}
'''
EXTEND_CONFIG={
               "WWW": {"file":"www","level":DEBUG},
               }



from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler,Logger as _Logger



BASIC_LOG_PATH="{0}{1}{2}".format(os.getcwd(),os.sep,BASIC_LOG_PATH)



LOG_CONFIG={"default": {"file":APP_NAME,"level":DEBUG}}

LOG_CONFIG.update(EXTEND_CONFIG)

class Logger(_Logger):
    DEBUG,INFO,WARN=logging.INFO,logging.DEBUG,logging.INFO
    @classmethod
    def __init_logger__(cls):
        if not hasattr(cls,"__inited__"):
            cls.__inited__=True
            
            if not os.path.exists(BASIC_LOG_PATH):
                os.mkdir(BASIC_LOG_PATH)
    
            for k,d in LOG_CONFIG.items():
                cls.regist(k,d)
    @classmethod
    def regist(cls,key,config):
        '''
        Usesage:
        key:str
        config:dict,e.g. {"file":"PLUGIN","level":logging.INFO}
        '''
        if not hasattr(cls,"logger"):
            cls.logger={}        
        if not cls.logger.has_key(key):
            cls.logger[key]=Logger(config["file"],level=config["level"])
        return cls.get(key)
    @classmethod
    def get(cls,name="default"):
        cls.__init_logger__()
        if not cls.logger.has_key(name):
            name="default"
        return cls.logger[name]
    @classmethod
    def Warn(cls,name="default",message="",*args,**kwargs):
        cls.get(name).warn(message,*args,**kwargs)
    @classmethod
    def Error(cls,name="default",message="",*args,**kwargs):
        cls.get(name).error(message,*args,**kwargs)
    @classmethod
    def Info(cls,name="default",message="",*args,**kwargs):
        cls.get(name).info(message,*args,**kwargs)
    @classmethod
    def Debug(cls,name="default",message="",*args,**kwargs):
        cls.get(name).debug(message,*args,**kwargs)        
    @classmethod
    def Exception(cls,name="default",message="",*args,**kwargs):
        cls.get(name).exception(message,*args,**kwargs)
                      
    def __init__(self,filename,level=logging.INFO):
        _Logger.__init__(self,filename,level)
        formatter=logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d \n%(message)s\n--end--')
        
        fileTimeHandler = TimedRotatingFileHandler("{0}{1}{2}".format(BASIC_LOG_PATH ,os.sep, filename), "H", 1, 10,encoding="utf-8")
        fileTimeHandler.suffix = "%Y%m%d%H.log" 
        fileTimeHandler.setFormatter(formatter)
        fileTimeHandler.setLevel(level)
        self.addHandler(fileTimeHandler)
        
        console=StreamHandler()
        console.setLevel(level)
        console.setFormatter(formatter)
        self.addHandler(console)
        
        self.handler=fileTimeHandler      
    @property
    def Loghandler(self):
        return self.handler
    def __del__(self):
        self.removeHandler(self.handler)
    

Logger.__init_logger__()


     