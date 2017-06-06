#-*-coding:utf-8-*-
from  appium import webdriver
from TestCase.common import  umeiInitialize
from  TestCase.common import  umeiInitLogin
from TestCase.common import  umeiCutScreenShot
import  traceback
import unittest
from  time import sleep
#滑动查看banner
class umeiCheckHomePageBanner(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "*************************************checkHomePageBanner test********************************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkHomePageBanner(self):
        try:
            print  "start test_checkHomePageBanner test..."
            sleep(3)
            #获取banner元素
            banner = self.driver.find_element_by_id("com.staff:id/cbLoopViewPager")
            width = self.driver.get_window_size().get('width')
            height = self.driver.get_window_size().get("height")
            x_start = 540*width/720
            x_end = 160*width/720
            y = 450*height/1280
            for i in range(0,1):
                self.driver.swipe(x_start,y,x_end,y)
                sleep(2)
                print "swiping..."
            # #向左滑动
            # for i in  range(0,1):
            #     self.driver.swipe(x_start,y,x_end,y)
            sleep(3)
            banner.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckHomePageBanner("test_checkHomePageBanner"))
    runner = unittest.TextTestRunner
    runner.run(suite)