#!/usr/bin/python
# -*- coding: utf8 -*-

import Actor
import application

import tornado.ioloop

#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8') 





if __name__ == "__main__":
    app = application.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
