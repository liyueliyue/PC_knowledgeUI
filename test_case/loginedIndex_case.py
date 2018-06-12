import unittest
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
        insert_img(self.driver,"1搜索不存在课程.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_searchText(),"没有更多了")
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
        self.assertEqual(self.index.get_currentUrl(),'https://m.qlchat.com/pc/knowledge-mall'
                                                     '/manage?selectedLiveId=310000108181722')

if __name__ == "__main__":
    unittest.main()