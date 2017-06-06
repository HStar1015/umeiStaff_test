#-*-coding:utf-8-*-
import unittest
import traceback
from time import  sleep
from  TestCase.common import  umeiInitialize
from  TestCase.common import  umeiInitLogin
from  TestCase.common import  umeiCutScreenShot

class umeiCheckProject(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***********************umeiCheckProject test****************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkProject(self):
        sleep(2)
