#-*- coding:utf-8 -*-

from  appium import webdriver
import  os
import time


#处理未登录状况
def init_login(self):
    time.sleep(3)
    txt_phone = self.driver.find_element_by_id("com.staff:id/et_phone")
    txt_phone.click()
    txt_phone.send_keys("15850766382")

    txt_pwd = self.driver.find_element_by_id("com.staff:id/et_password")
    txt_pwd.click()
    txt_pwd.send_keys("123456")
    btn_login = self.driver.find_element_by_id("com.staff:id/btn_login")
    btn_login.click()

#处理已登录要退出状况，前提在应用的一级界面
def init_logout(self):
    time.sleep(5)
    btn_me = self.driver.find_element_by_name("我的")
    btn_me.click()
    time.sleep(2)
    btn_setting = self.driver.find_element_by_name("设置")
    btn_setting.click()
    time.sleep(3)
    btn_logout = self.driver.find_element_by_id("com.staff:id/btn_exit")
    btn_logout.click()
    time.sleep(2)
    btn_ok = self.driver.find_element_by_id("android:id/button1")
    btn_ok.click()





