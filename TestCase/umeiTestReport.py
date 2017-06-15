#-*-coding:utf-8 -*-
import HTMLTestRunner
import unittest
import time
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from login import umeiLogin
from homePage import umeiCheckHomePageBanner
from homePage import umeiCheckWorkPlan
from homePage import umeiCheckMarketingActivity
from homePage import umeiCheckOrder
from homePage import  umeiAddOrder
from projecManage import umeiCheckProject
from  personalCenter import  umeiChangePersonalInfo
from  personalCenter import  umeiCheckShop
from  personalCenter import  umeiUserComment

reload(sys)
sys.setdefaultencoding('utf8')


def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    #    print u'打印'
    #    print mail_body
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码
    user = '15651966757@163.com'
    password = 'hx258000'
    # 发送邮箱
    sender = '15651966757@163.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['15651966757@163.com']
    # 发送邮件主题
    subject = '优美师自动化测试报告'

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    #    msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    #    msg_plain = MIMEText(text,'plain', 'utf-8')
    #    msg.attach(msg_plain)

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 以附件的方式发送：但是会报554，倍163退信。--此路不通。
    #    msg_html = MIMEText(mail_body,'base64','utf-8')
    #    msg_html["Content-Type"] = 'application/octet-stream'
    #    msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
    #    msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163设置授权码（即客户端的密码），否则会报535
    msg['From'] = '15651966757@163.com'
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__=="__main__":
    print '=====AutoTest Start======'
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    #    test_dir='./test_case'
    # Windows的cmd执行：python "D:\system files\workspace\selenium\test_project\runtest_htmltestrunner_autosendemail.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    test_dir = 'D:\\hanxing\\study\umeiStaff_test\\TestCase'
    # 知道测试报告的路径
    test_report_dir = 'D:\\hanxing\\study\\umeiStaff_test\\TestCase\\report'


    # 包装测试用例
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(umeiLogin.umeiLogin))
    suite.addTest(unittest.makeSuite(umeiCheckHomePageBanner.umeiCheckHomePageBanner))
    suite.addTest(unittest.makeSuite(umeiCheckOrder.umeiCheckOrder))
    suite.addTest(unittest.makeSuite(umeiCheckWorkPlan.umeiCheckWorkPlan))
    suite.addTest(unittest.makeSuite(umeiCheckMarketingActivity.umeiCheckMarketingActivity))
    suite.addTest(unittest.makeSuite(umeiAddOrder.umeiAddOrder))
    suite.addTest(unittest.makeSuite(umeiCheckProject.umeiCheckProject))
    suite.addTest(unittest.makeSuite(umeiChangePersonalInfo.umeiChangePersonalInfo))
    suite.addTest(unittest.makeSuite(umeiUserComment.umeiUserComment))
    suite.addTest(unittest.makeSuite(umeiCheckShop.umeiCheckShop))
    #生成与执行时间相同的测试报告


    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    # 需屏蔽fp中的中文文字说明。否则在windows下执行会报：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 553: ordinal not in range(128)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(suite)
    # 注意：调用函数一定要加括号，一个括号害死个人，哎，查了几天的问题，才发现导致html文件始终显示空白，就是因为close函数调用不正确，漏了括号。
    fp.close()

    # 2.取最新测试报告
    new_report = new_file(test_report_dir)
    # 调试用的
    #    print new_report

    # 3.发送邮件，发送最新测试报告html
    send_email(new_report)
    print '=====AutoTest Over======'