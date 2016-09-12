#!/usr/bin/env python
#coding:utf-8

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    """ 登陆处理类 """
    def get(self):
        self.render("login.html")
    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        print(self.get_argument("username") + " login success")
        self.redirect("/")