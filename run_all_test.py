import sys,time,unittest,smtplib,os
sys.path.append('./test_case')
sys.path.append('./models')
from models.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

# #定义邮件发送
# def send_mail(file_new):
#     f = open(file_new,'rb')
#     mail_body = f.read()
#     f.close()
#
#     msg = MIMEText(mail_body,'html','utf-8')
#     msg['Subject'] = Header('web自动化测试报告','utf-8')
#
#     msg['from'] = 'test0_test1@126.com'
#     msg['to'] = 'yue.li@qlchat.com'
#     smtp = smtplib.SMTP()
#     smtp.connect('smtp.126.com')
#     smtp.login('test0_test1@126.com','Li123456')
#     smtp.sendmail('test0_test1@126.com','yue.li@qlchat.com',msg.as_string())
#     smtp.quit()
#     print('web自动化测试报告已经发送到你的邮箱，请注意查收。')
#
# def new_report(testreport):
#     lists = os.listdir(testreport)
#     lists.sort(key=lambda fn : os.path.getmtime(testreport + '\\' + fn))
#     file_new = os.path.join(testreport,lists[-1])
#     print(file_new)
#     return file_new
#
# if __name__ == "__main__":
#     now = time.strftime('%Y-%m-%d_%H-%M-%S')
#     filename = r'./test_report/' + now + '_result.html'
#     fp = open(filename,'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title='web自动化测试报告',
#         description = 'chrome 67'
#     )
#     test_dir = r'./test_case'
#     discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
#     runner.run(discover)
#     fp.close()
#     file_path = new_report('./test_report/')
#     send_mail(file_path)

test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*_case.py")
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "./test_report/" + now + "result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="《知识通商城》测试用例统计报告",
        description="环境：mac 浏览器：chrome"
    )
    runner.run(discover)
    fp.close()