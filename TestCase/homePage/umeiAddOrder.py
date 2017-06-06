#-*-coding:utf-8-*-
from  appium import  webdriver
from  TestCase.common import umeiInitLogin
from TestCase.common import umeiCutScreenShot
from  TestCase.common import umeiInitialize
from time import  sleep
import  traceback
import  unittest
import umeiCheckOrder
class umeiAddOrder(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "**********************************addOrder test******************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_addOrder(self):
        try:
            print "start test_addOrder test..."
            sleep(2)
            btn_order = self.driver.find_element_by_id("com.staff:id/iv4")
            btn_order.click()
            sleep(2)
            txt_name = self.driver.find_element_by_id("com.staff:id/et_customer_name")
            txt_name.click()
            txt_name.send_keys("Test")
            txt_phone = self.driver.find_element_by_id("com.staff:id/et_customer_phone")
            txt_phone.click()
            txt_phone.send_keys("15651966757")
            btn_select = self.driver.find_element_by_name("选择项目")
            btn_select.click()
            sleep(5)
            btn_ok = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]")
            btn_ok.click()
            sleep(2)
            btn_fee = self.driver.find_element_by_id("com.staff:id/smoothCheckBoxOne")
            btn_fee.click()
            sleep(2)
            btn_time = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
            btn_time.click()
            btn_submit = self.driver.find_element_by_id("com.staff:id/btn_submit")
            btn_submit.click()
            sleep(2)
            btn_sure = self.driver.find_element_by_id("android:id/button1")
            btn_sure.click()
            sleep(2)
            umeiCutScreenShot.cutScreenShot()
        except Exception,e:
            print traceback.format_exc()
def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiAddOrder("test_addOrder"))
    runner = unittest.TextTestRunner
    runner.run(suite)