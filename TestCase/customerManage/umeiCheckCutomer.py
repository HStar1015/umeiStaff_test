#-*-coding:utf-8 -*-
from appium import webdriver
from  time import  sleep
import unittest
import traceback
from  TestCase.common import umeiInitialize
from  TestCase.common import umeiCutScreenShot


class umeiCheckCustomer(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***************CheckCustomer test************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkCustomer(self):
        sleep(2)
        try:
            #查看顾客
            btn_customer = self.driver.find_element_by_name("顾客管理")
            btn_customer.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()
            width = self.driver.get_window_size()['width']
            print "width is ", width
            height = self.driver.get_window_size()["height"]
            print "height is ",height
            startx = width/2
            starty = height/2
            endx =   width/2
            endy =   height/5
            self.driver.swipe(startx,starty,endx,endy)
            # umeiCutScreenShot.cutScreenShot()
            #查看高端顾客
            btn_items = self.driver.find_element_by_id("com.staff:id/iv_arrow")
            btn_items.click()
            sleep(2)
            high_expend = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]")
            high_expend.click()
            sleep(2)
            umeiCutScreenShot.cutScreenShot()
        except Exception,e:
            print traceback.format_exc()
def suite(self):
    suite = unittest.TestSuite
    suite.addTest(umeiCheckCustomer("test_checkCustomer"))
    runner = unittest.TextTestRunner()
    runner.run(suite)