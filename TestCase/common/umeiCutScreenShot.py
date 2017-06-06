# coding:utf-8
import os
import time

PATH = lambda p: os.path.abspath(p)
#截图
def cutScreenShot():
    path = PATH(os.path.abspath("..")  + "/screenshot")
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.path.abspath("..") + "/screenshot")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print "Succeed to cutScreen..."


if __name__ == "__main__":
    cutScreenShot()
