#!/usr/bin/python
# -*- coding: utf8 -*-

#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8') 

class Actor:
    """ 身份基类 """
    def __init__(self):
        self.role = 0
        self.isOut = False
        self.canVote = True
    def vote(self, num):
        """ vote someone """