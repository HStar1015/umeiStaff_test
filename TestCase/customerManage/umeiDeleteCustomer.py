#-*-coding:utf-8 -*-
from appium import webdriver
from  time import  sleep
import unittest
import traceback
from  TestCase.common import umeiInitialize
from  TestCase.common import umeiCutScreenShot


class umeiDeleteCustomer(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***************DeleteCustomer test************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_deleteCustomer(self):
        sleep(2)
        try:
            btn_customer = self.driver.find_element_by_name("顾客管理")
            btn_customer.click()
            sleep(3)
            #选择顾客
            select_customer = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]")
            select_customer.click()
            #删除
            btn_delete = self.driver.find_element_by_id("com.staff:id/tv_delete")
            btn_delete.click()
            sleep(2)
            btn_delete_ok = self.driver.find_element_by_id("android:id/button1")
            btn_delete_ok.click()
            sleep(3)
            print "Delete Customer Successful"
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite
    suite.addTest(umeiDeleteCustomer("test_deleteCustomer"))
    runner = unittest.TextTestRunner()
    runner.run(suite)