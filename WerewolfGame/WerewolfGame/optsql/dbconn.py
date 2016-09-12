#!/usr/bin/env python
#coding:utf-8

import tornado.web
import tornado.gen

from tornado_mysql import pools

class DatabaseConnection:
    """ 数据库连接 """
    def connect(self, host, dbname):
        self.mysql_pool = pools.Pool(dict(host = host, port = 3306, user = "root", passwd="19931122", db=dbname), 
            max_idle_connections=5,
            max_open_connections=10,
            max_recycle_sec=5)
        print(self.mysql_pool._get_conn())