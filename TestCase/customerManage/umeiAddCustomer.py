#-*-coding:utf-8 -*-
from appium import webdriver
from  time import  sleep
import unittest
import traceback
from  TestCase.common import umeiInitialize
from  TestCase.common import umeiCutScreenShot


class umeiAddCustomer(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***************AddCustomer test************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_addCustomer(self):
        sleep(2)
        try:
            btn_customer = self.driver.find_element_by_name("顾客管理")
            btn_customer.click()
            sleep(3)

            btn_add =  self.driver.find_element_by_id("com.staff:id/tv_right")
            btn_add.click()
            sleep(2)
            # 上传头像
            btn_head = self.driver.find_element_by_id("com.staff:id/rl_head")
            btn_head.click()
            btn_album = self.driver.find_element_by_name("从图库选择...")
            btn_album.click()
            sleep(2)
            select_photo = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.view.View[1]")
            select_photo.click()
            comlete_selected = self.driver.find_element_by_id("com.staff:id/tv_right")
            comlete_selected.click()
            btn_ok_photo =self.driver.find_element_by_id("com.staff:id/id_action_clip")
            btn_ok_photo.click()
            sleep(2)
            #编辑姓名
            btn_name = self.driver.find_element_by_id("com.staff:id/tv_name_buttom")
            btn_name.click()
            btn_name.send_keys(u"哇塞")
            #编辑手机号
            btn_phone = self.driver.find_element_by_id("com.staff:id/tv_phone_buttom")
            btn_phone.click()
            btn_phone.send_keys("12345678900")
            #生日
            select_birth = self.driver.find_element_by_id("com.staff:id/tv_brithday_buttom")
            select_birth.click()
            select_birth_ok = self.driver.find_element_by_id("android:id/button1")
            select_birth_ok.click()
            #分类
            btn_fenlei = self.driver.find_element_by_id("com.staff:id/tv_fenlei_buttom")
            btn_fenlei.click()
            select_fenlei = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
            select_fenlei.click()
            select_fenlei_ok = self.driver.find_element_by_id("com.staff:id/tv_sure")
            select_fenlei_ok.click()
            #备注
            txt_remark = self.driver.find_element_by_id("com.staff:id/et_remark")
            txt_remark.click()
            txt_remark.send_keys(u"一只程序猿")
            umeiCutScreenShot.cutScreenShot()
            #确认添加
            btn_add_save = self.driver.find_element_by_id("com.staff:id/btn_save")
            btn_add_save.click()
            sleep(3)
            print "Add Customer Successful"
        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite
    suite.addTest(umeiAddCustomer("test_addCustomer"))
    runner = unittest.TextTestRunner()
    runner.run(suite)