import unittest, sys, os
# os.chdir('../')  # 切换工作目录
# fpath = os.getcwd()
# sys.path.append(fpath)  # 加进python 的path
'''
先看报错是哪个模块，然后将换个模块的路径添加到sys，注意例如我有这样一个路径报错

/usr/local/bin/python3.6 /Users/louchengwang/PycharmProjects/Sanjieke/src/utils/config.py

报错是

No module named 'src'

那么首先确定去执行的文件中config.py添加src模块的路径

然后rootpath要确定最终应该append的应该是/Users/louchengwang/PycharmProjects/Sanjieke，而不是到src,这里要注意应该是
'''
curPath = os.path.abspath(os.path.dirname(__file__))  # 获取当前的工作目录
print(curPath)
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(rootPath)
print(sys.path)
from models.function import insert_img
from models.driver import browser
from page_obj.indexPage import Index
from time import sleep

class indexTest(unittest.TestCase):
    """已登录-首页"""
    def setUp(self):
        self.driver = browser()
        self.index = Index(self.driver)
        self.index.openLogin()
    def tearDown(self):
        self.driver.close()
    def test_searchForm_null(self):
        '''输入不存在的课程，点击搜索显示‘没有更多了’'''
        self.index.sendTextTosearchForm(text="jgfkldjasfljas")
        insert_img(self.driver, "1搜索不存在课程.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_searchText(), "没有更多了")
    def test_searchForm(self):
        '''输入存在的课程，点击搜索显示对应数据'''
        self.index.sendTextTosearchForm(text="优惠")
        insert_img(self.driver,"2搜索存在的课程.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_searchResult(),True)
    def test_click_relayManage(self):
        '''已登录点击转载管理按钮'''
        self.index.click_relayManage()
        insert_img(self.driver,'3已登录点击转载管理按钮.jpg')
        sleep(1)
        # 断言
        self.assertIn('/pc/knowledge-mall/manage',self.index.get_currentUrl())
    def test_click_myDraw(self):
        '''已登录点击我的画像按钮'''
        self.index.click_myDraw()
        insert_img(self.driver,'4已登录点击我的画像.jpg')
        sleep(1)
        self.assertIn('/pc/knowledge-mall/user-portrait',self.index.get_currentUrl())
    def test_switchAcount(self):
        '''测试切换直播间'''
        self.index.switchAcount()
        insert_img(self.driver,'5切换直播间.jpg')
        sleep(1)
        # 断言

if __name__ == "__main__":
    unittest.main()