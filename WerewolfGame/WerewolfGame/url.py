#!/usr/bin/env python
#coding:utf-8

#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')

from handler.index import MainHandler

url=[
    (r'/', MainHandler),                    # handle index.html

    ]