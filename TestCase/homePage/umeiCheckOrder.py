#-*- coding:utf-8 -*-
from appium import webdriver
from  TestCase.common import umeiInitialize
from  TestCase.common import  umeiInitLogin
from  TestCase.common import  umeiCutScreenShot
from  time import  sleep
import  traceback
import  unittest
#查看待操作订单
class umeiCheckOrder(unittest.TestCase):

    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "*************************************checkOrder test********************************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)


    def test_checkOder(self):
        try:
            print "start test_checkOrder test..."
            sleep(3)
            btn_oder = self.driver.find_element_by_id("com.staff:id/iv1")
            btn_oder.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()
            btn_complete_order = self.driver.find_element_by_name("已完成订单")
            btn_complete_order.click()
            umeiCutScreenShot.cutScreenShot()
            sleep(2)
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckOrder("test_checkOrder"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


