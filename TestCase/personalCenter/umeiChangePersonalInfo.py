#-*-coding:utf-8 -*-
import  unittest
from appium import webdriver
from TestCase.common import  umeiInitialize
from  TestCase.common import  umeiCutScreenShot
import  traceback
from time import  sleep

class umeiChangePersonalInfo(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***********************umeiChangePersonalInfo test****************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_changePersonalInfo(self):
        sleep(2)
        try:
            btn_me = self.driver.find_element_by_name("我的")
            btn_me.click()
            sleep(2)

            btn_photo = self.driver.find_element_by_id("com.staff:id/simpleDraweeView")
            btn_photo.click()
            sleep(2)

            #修改头像
            btn_head = self.driver.find_element_by_id("com.staff:id/linear_one")
            btn_head.click()
            sleep(2)
            btn_selPhoto = self.driver.find_element_by_name("从图库选择...")
            btn_selPhoto.click()
            sleep(2)
            #选择图片
            btn_selected = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]")
            btn_selected.click()
            btn_compelte = self.driver.find_element_by_id("com.staff:id/tv_right")
            btn_compelte.click()
            width = self.driver.get_window_size().get('width')
            height = self.driver.get_window_size().get("height")
            self.driver.swipe(width/2,height/2,width/2,height/4)
            btn_ok = self.driver.find_element_by_id("com.staff:id/id_action_clip")
            btn_ok.click()
            sleep(2)

            #修改姓名
            txt_name = self.driver.find_element_by_id("com.staff:id/tv_two")
            txt_name.click()
            edit_name = self.driver.find_element_by_id("com.staff:id/et_name")
            edit_name.clear()
            edit_name.send_keys(u"美容师")
            save_name = self.driver.find_element_by_id("com.staff:id/tv_right")
            save_name.click()


            #修改工作年限
            sel_year = self.driver.find_element_by_id("com.staff:id/tv_seven")
            sel_year.click()
            work_year = self.driver.find_element_by_id("com.staff:id/tv_two_work")
            work_year.click()
            btn_okyear = self.driver.find_element_by_id("com.staff:id/tv_sure")
            btn_okyear.click()
            sleep(2)

            #修改个人介绍
            self.driver.tap([(0,1343),(1080,1659)],500)
            edit_intro = self.driver.find_element_by_id("com.staff:id/et_name")
            edit_intro.click()
            edit_intro.clear()
            edit_intro.send_keys(u"服务天下美业人~")
            btn_save = self.driver.find_element_by_id("com.staff:id/tv_right")
            btn_save.click()
            umeiCutScreenShot.cutScreenShot()

            #保存提交
            btn_submit = self.driver.find_element_by_id("com.staff:id/btn_submit")
            btn_submit.click()
            sleep(2)

        except Exception,e:
            print traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiChangePersonalInfo("test_changePersonalInfo"))
    runner = unittest.TextTestRunner()
    runner.run(suite)