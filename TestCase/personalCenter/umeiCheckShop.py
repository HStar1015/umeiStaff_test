#-*-coding:utf-8-*-
from  appium import webdriver
from time import  sleep
import unittest
from TestCase.common import  umeiInitialize
from  TestCase.common import  umeiCutScreenShot
import  traceback

class umeiCheckShop(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_umeiCheckShop(self):

        try:
            btn_me = self.driver.find_element_by_name("我的")
            btn_me.click()
            sleep(2)

            #查看所属门店
            btn_shop = self.driver.find_element_by_id("com.staff:id/linear_two")
            btn_shop.click()
            sleep(2)
            umeiCutScreenShot.cutScreenShot()

        except Exception,e:
            print traceback.format_exc()
def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckShop("test_umeiCheckShop"))
    runner = unittest.TextTestRunner()
    runner.run(suite)