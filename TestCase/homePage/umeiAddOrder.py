#-*-coding:utf-8 -*-
from appium import webdriver
from  time import  sleep
import unittest
import traceback
from  TestCase.common import umeiInitialize
from  TestCase.common import umeiCutScreenShot

class umeiAddOrder(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***************addOrder test************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_addOrder(self):
        sleep(3)
        try:
            '''缺少选择顾客的操作'''
            btn_adOr = self.driver.find_element_by_id("com.staff:id/iv4")
            btn_adOr.click()
            sleep(3)
            selectProject = self.driver.find_element_by_id("com.staff:id/ll_select_pro")
            selectProject.click()
            sleep(5)
            selPro = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]")
            selPro.click()
            checkBox = self.driver.find_element_by_id("com.staff:id/smoothCheckBoxOne")
            checkBox.click()
            sel_tomor  = self.driver.find_element_by_name("明天")
            sel_tomor.click()
            sel_time = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
            sel_time.click()
            umeiCutScreenShot.cutScreenShot()
            sleep(2)
            btn_submit = self.driver.find_element_by_id("android.widget.RelativeLayout")
            btn_submit.click()
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite
    suite.addTest(umeiAddOrder("test_addOrder"))
    runner = unittest.TextTestRunner()
    runner.run(suite)