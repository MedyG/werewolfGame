#!/usr/bin/env python
#coding:utf-8

import tornado.web
from handler.basehandler import BaseHandler

class LogoutHandler(BaseHandler):
    """ 登出处理类 """
    def post(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            print("logout success")
        self.redirect("/")