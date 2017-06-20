#-*- coding=utf-8 -*-
from  appium import  webdriver
from TestCase.common import umeiInitialize
from TestCase.common import  umeiInitLogin
from TestCase.common import  umeiCutScreenShot
import unittest
from time import  sleep
import traceback
import sys
class umeiLogin(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print  "*************************************login test********************************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        print  "*************************************login test********************************************"
        umeiInitialize.tearDown(self)


    def test_login(self):
        try:
            print "Start to test_login test....."
            # umeiInitLogin.init_logout(self)
            sleep(5)
            txt_phone = self.driver.find_element_by_id("com.staff:id/et_phone")
            txt_phone.clear()
            txt_phone.send_keys("15850766382")

            sleep(2)
            txt_pwd = self.driver.find_element_by_id("com.staff:id/et_password")
            txt_pwd.click()
            txt_pwd.send_keys("123456")
            sleep(2)
            btn_login = self.driver.find_element_by_id("com.staff:id/btn_login")
            btn_login.click()
            sleep(5)
            umeiCutScreenShot.cutScreenShot()
            print "Succeed to excute this case..."
        except Exception,e:
            print traceback.format_exc()


def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiLogin("test_login"))
    runner = unittest.TextTestRunner
    runner.run(suite)
