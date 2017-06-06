#-*- coding:utf-8 -*-
from appium import webdriver
from  TestCase.common import umeiInitialize
from  TestCase.common import  umeiInitLogin
from  TestCase.common import  umeiCutScreenShot
from  time import  sleep
import  traceback
import  unittest
#查看工作计划
class umeiCheckWorkPlan(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "********************************checkWorkPlan test*****************************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkWorkPlan(self):
        sleep(2)
        try:
            print "start test_checkWorkPlan test..."
            btn_plan = self.driver.find_element_by_id("com.staff:id/iv2")
            btn_plan.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()
            area = self.driver.find_element_by_name("2017-05 月度计划")
            area.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()

        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckWorkPlan("test_checkWorkPlan"))
    runner = unittest.TextTestRunner
    runner.run(suite)