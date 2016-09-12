#!/usr/bin/python
# -*- coding: utf8 -*-

from url import url

import tornado.web
import os

''' settings
'''
settings = {
    "debug" : True,
    "template_path" :"views" ,            # html文件
    "static_path": "static" ,              # 静态文件路径（css，js，img）
    "static_url_prefix" : "/static/",     # 静态文件前缀
    "login_url" : "/login",
    "cookie_secret" : "IsCc9w+yQmCngmk2Yg5VwiWoqYA7Sk5inYr+F44r4mQ="
}

def make_app():
    return tornado.web.Application(
        handlers=url,
        **settings)
