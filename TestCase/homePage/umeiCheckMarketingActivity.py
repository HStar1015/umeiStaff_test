#-*- coding:utf-8 -*-
from appium import webdriver
from  TestCase.common import umeiInitialize
from  TestCase.common import  umeiCutScreenShot
from  time import  sleep
import  traceback
import  unittest
#查看营销活动
class umeiCheckMarketingActivity(unittest.TestCase):

    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "*************************************checkMarketingActivity test********************************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkMarketingActivity(self):
        try:
            print "start chekcMarktingActivity test..."
            sleep(2)
            btn_activity = self.driver.find_element_by_id("com.staff:id/iv3")
            btn_activity.click()
            sleep(5)
            umeiCutScreenShot.cutScreenShot()
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckMarketingActivity("test_checkMarketingActivity"))
    runner = unittest.TextTestRunner()
    runner.run(suite)