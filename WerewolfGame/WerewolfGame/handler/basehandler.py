#!/usr/bin/env python
#coding:utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """ 继承这个类以用于登陆验证 """
    def get_current_user(self):
        return self.get_secure_cookie("username")