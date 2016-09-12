#!/usr/bin/env python
#coding:utf-8

import tornado.web
from handler.basehandler import BaseHandler

class MainHandler(BaseHandler):
    """ 渲染index.html """
    @tornado.web.authenticated
    def get(self):
        #self.write("Hello, world")
        self.render("index.html", user=self.current_user)