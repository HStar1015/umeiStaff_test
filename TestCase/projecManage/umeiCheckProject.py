#-*-coding:utf-8-*-
import unittest
import traceback
from time import  sleep
from  TestCase.common import  umeiInitialize
from  TestCase.common import  umeiInitLogin
from  TestCase.common import  umeiCutScreenShot

class umeiCheckProject(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self,methodName)
        print "***********************umeiCheckProject test****************************"

    def setUp(self):
        umeiInitialize.setUp(self)

    def tearDown(self):
        umeiInitialize.tearDown(self)

    def test_checkProject(self):
        sleep(2)
        try:
            project = self.driver.find_element_by_name("项目管理")
            project.click()
            umeiCutScreenShot.cutScreenShot()

            #有项目时删除一项
            pro_detail = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]")
            pro_detail.click()
            sleep(2)
            btn_delete = self.driver.find_element_by_id("com.staff:id/tv_delete")
            btn_delete.click()
            btn_ok = self.driver.find_element_by_id("com.staff:id/btn_ok")
            btn_ok.click()
            sleep(3)

            #添加项目
            btn_add = self.driver.find_element_by_id("com.staff:id/tv_right")
            btn_add.click()
            sleep(4)
            sel_pro = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]")
            sel_pro.click()
            btn_tianjia = self.driver.find_element_by_id("com.staff:id/btn_tianjia")
            btn_tianjia.click()
            umeiCutScreenShot.cutScreenShot()
        except Exception,e:
            print  traceback.format_exc()

def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(umeiCheckProject("test_umeiCheckProject"))
    runner = unittest.TextTestRunner()
    runner.run(suite)