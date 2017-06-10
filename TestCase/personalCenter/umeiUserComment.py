#coding:utf-8

from appium import webdriver
from  TestCase.common import umeiInitialize
from  TestCase.common import  umeiCutScreenShot
import  unittest
from  time import  sleep
import traceback

class umeiUserComment(unittest.TestCase):
    def __init__(self,mehodName):
        unittest.TestCase.__init__(self,mehodName)
        print "***********************umeiUserComment test****************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_umeiUserComment(self):
        sleep(2)
        try:
            btn_me = self.driver.find_element_by_name("我的")
            btn_me.click()
            sleep(2)

            #全部评价
            btn_comment = self.driver.find_element_by_id("com.staff:id/linear_one")
            btn_comment.click()
            umeiCutScreenShot.cutScreenShot()

            #好评
            btn_good = self.driver.find_element_by_id("com.staff:id/tv_good")
            btn_good.click()
            umeiCutScreenShot.cutScreenShot()

            #中评
            btn_middle = self.driver.find_element_by_id("com.staff:id/tv_middle")
            btn_middle.click()
            umeiCutScreenShot.cutScreenShot()

            #差评
            btn_bad = self.driver.find_element_by_id("com.staff:id/tv_bad")
            btn_bad.click()
            umeiCutScreenShot.cutScreenShot()

        except Exception,e:
            print  traceback.format_exc()
def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiUserComment("test_umeiUserComment"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
