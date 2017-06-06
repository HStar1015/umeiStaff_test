#-*-coding:utf-8 -*-
from appium import  webdriver
import time
import  os


def init_case(opt):
    pass

def setUp(self):
    #执行用例前卸载Appium相关apk，防止出现apk安装失败的情况，在7.0系统机型上出现的问题
    try:
        os.popen("adb uninstall io.appium.android.ime")
        os.popen("adb uninstall io.appium.unlock")
        os.popen("adb uninstall io.appium.settings")
        print "Succeed to unistall apk... "
    except Exception, e:
        e.message
    desire_caps = {}
    desire_caps["deviceName"] = "PBV0216526002577"
    desire_caps["platformName"] = "Android"
    desire_caps["platformVersion"] = "7.0"
    desire_caps["appPackage"] = "com.staff"
    desire_caps["appActivity"] = "com.staff.ui.user.guide.StartAvtivity"
    desire_caps["unicodeKeyboard"] = True
    desire_caps["resetKeyboard"] = True
    self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
    time.sleep(5)

def tearDown(self):
    self.driver.quit()
