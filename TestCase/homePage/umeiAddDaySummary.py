#-*-coding:utf-8-*-
from appium import  webdriver
from time import  sleep
import  unittest
import traceback
from TestCase.common import umeiInitLogin
from  TestCase.common import umeiInitialize
from  TestCase.common import umeiCutScreenShot

class umeiAddDaySummary(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "**********************addDaySummary test*********************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)


    def test_addDaySummary(self):
        print "start test_addDaySummary test..."
        try:
            sleep(2)
            btn_summary = self.driver.find_element_by_id("com.staff:id/iv5")
            btn_summary.click()
            sleep(2)
            sel_data = self.driver.find_element_by_id("com.staff:id/tv_one")
            sel_data.click()

            sel_day = self.driver.find_element_by_xpath("//android.widget.DatePicker[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.NumberPicker[3]/android.widget.Button[1]")
            sel_day.click()
            sleep(2)
            btn_submit = self.driver.find_element_by_id("android:id/button1")
            btn_submit.click()
            sleep(2)

            dayRes = self.driver.find_element_by_id("com.staff:id/tv_two")
            dayRes.click()
            sleep(5)
            customerRes = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
            customerRes.click()
            sleep(2)
            txt_money = self.driver.find_element_by_id("com.staff:id/et_money")
            txt_money.click()
            txt_money.send_keys("100")
            sleep(2)
            btn_ok = self.driver.find_element_by_id("com.staff:id/btn_ok")
            btn_ok.click()
            sleep(3)
            self.driver.tap([(720,1650),(1080,1794)],500)
            sleep(2)


            dayExp = self.driver.find_element_by_id("com.staff:id/tv_three")
            dayExp.click()
            sleep(5)
            customerExp = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
            customerExp.click()
            sleep(2)
            txt_money = self.driver.find_element_by_id("com.staff:id/et_money")
            txt_money.click()
            txt_money.send_keys("100")
            sleep(2)
            btn_ok = self.driver.find_element_by_id("com.staff:id/btn_ok")
            btn_ok.click()
            sleep(3)
            self.driver.tap([(720, 1650), (1080, 1794)], 500)
            sleep(2)

            dayOrder = self.driver.find_element_by_id("com.staff:id/tv_four")
            dayOrder.click()
            sleep(3)
            btn_back = self.driver.find_element_by_id("com.staff:id/linear_back")
            btn_back.click()
            sleep(2)

            txt_1 = self.driver.find_element_by_id("com.staff:id/et_one")
            txt_1.click()
            txt_1.send_keys("1")
            txt_2 = self.driver.find_element_by_id("com.staff:id/et_two")
            txt_2.click()
            txt_2.send_keys("2")
            txt_3 = self.driver.find_element_by_id("com.staff:id/et_three")
            txt_3.click()
            txt_3.send_keys("3")
            txt_4 = self.driver.find_element_by_id("com.staff:id/et_four")
            txt_4.click()
            txt_4.send_keys("4")
            txt_5 = self.driver.find_element_by_id("com.staff:id/et_five")
            txt_5.click()
            txt_5.send_keys("12345")
            btn_save = self.driver.find_element_by_id("com.staff:id/btn")
            btn_save.click()

        except Exception ,e:
            print traceback.format_exc()
def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiAddDaySummary("test_addDaySummary"))
    runner = unittest.TextTestRunner()
    runner.run(suite)