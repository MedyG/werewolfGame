#!/usr/bin/env python
#coding:utf-8

import tornado.web

#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8') 

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("index.html", list_info = [11, 22, 33])