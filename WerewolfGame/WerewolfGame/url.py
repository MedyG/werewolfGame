#!/usr/bin/env python
#coding:utf-8

#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')

from handler.index import MainHandler
from handler.login import LoginHandler
from handler.logout import LogoutHandler


url=[
    (r'/', MainHandler),                    # handle index.html
    (r'/login', LoginHandler),              # handle login.html
    (r'/logout', LogoutHandler),

    ]