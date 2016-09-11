#!/usr/bin/python
# -*- coding: utf8 -*-

import Actor

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("index.html", list_info = [11, 22, 33])

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

''' settings
'''
settings = {
    "debug" : True,
    "template_path" :"views" ,            # html文件
    "static_path": "static" ,              # 静态文件路径（css，js，img）
    "static_url_prefix" : "/static/",     # 静态文件前缀
    "login_url" : "/login"
}

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
