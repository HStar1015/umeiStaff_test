#-*- coding:utf-8 -*-
import  unittest
import  traceback
from  time import  sleep
from TestCase.common import  umeiCutScreenShot
from  TestCase.common import  umeiInitialize

class umeiCheckDayOrder(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print  "**********************start umeiCheckDayOrder test********************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkDayOrder(self):
        sleep(2)
        try:
            #查看今日预约
            btn_today = self.driver.find_element_by_id("com.staff:id/ll_today_appointment")
            btn_today.click()
            sleep(5)
            umeiCutScreenShot.cutScreenShot()
            #查看当月其它日期订单数量
            btn_cal =  self.driver.find_element_by_id("com.staff:id/tv_right")
            btn_cal.click()
            sleep(3)
            umeiCutScreenShot.cutScreenShot()
        except Exception, e:
            print traceback.format_exc()

def suite(self):

    suite = unittest.TestSuite()
    suite.addTest(umeiCheckDayOrder("test_checkDayOrder"))
    runner = unittest.TextTestRunner
    runner.run(suite)