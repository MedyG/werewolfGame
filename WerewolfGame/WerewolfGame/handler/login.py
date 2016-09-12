#!/usr/bin/env python
#coding:utf-8

import tornado.web
from optsql.dbconn import DatabaseConnection

class LoginHandler(tornado.web.RequestHandler):
    """ 登陆处理类 """
    def get(self):
        self.render("login.html")
    def post(self):
        #dbconn = DatabaseConnection()
        #dbconn.connect("138.68.12.224", "werewolfgame")
        self.set_secure_cookie("username", self.get_argument("username"))
        print(self.get_argument("username") + " login success")
        self.redirect("/")