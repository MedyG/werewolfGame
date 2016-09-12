#!/usr/bin/python
# -*- coding: utf8 -*-

from Actor import Actor
import application

import tornado.ioloop

if __name__ == "__main__":
    app = application.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
