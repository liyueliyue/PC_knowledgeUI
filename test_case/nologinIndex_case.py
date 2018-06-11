import unittest
from models.function import insert_img
from models.driver import browser
from page_obj.indexPage import Index
from time import sleep

class nologinndexTest(unittest.TestCase):
    """未登录-首页"""
    def setUp(self):
        self.driver = browser()
        self.index = Index(self.driver)
        self.index.openNologin()
    def tearDown(self):
        self.driver.quit()
    def test_click_relayManage(self):
        '''未登录点击转载管理'''
        self.index.click_relayManage()
        insert_img(self.driver,"1.未登录点击转载管理按钮.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_click_myDraw(self):
        '''未登录点击我的画像'''
        self.index.click_myDraw()
        insert_img(self.driver,"2.未登录点击我的画像按钮.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_click_login(self):
        '''未登录点击登录按钮'''
        self.index.click_login()
        insert_img(self.driver,"3.未登录点击登录按钮.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_click_saleBack(self):
        '''未登录点击导航栏分销后台'''
        self.index.click_salesBack()
        insert_img(self.driver,"4.未登录点击导航栏分销后台.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_click_norelay(self):
        '''未登录点击全部tab的只看转载课按钮'''
        self.index.click_norelay()
        insert_img(self.driver,"5.未登录点击全部tab的只看未转载课按钮.jpg")
        sleep(1)
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_click_norelay_(self):
        '''未登录点击个人提升tab的只看转载课按钮'''
        self.index.click_norelay_()
        insert_img(self.driver,"6.未登录点击个人提升tab的只看转载课按钮.jpg")
        # 断言
        self.assertEqual(self.index.get_codeText(),"微信登录")
    def test_nologinBooleanRecommand(self):
        '''未登录不显示“精品推荐”或“专属推荐模块”'''
        insert_img(self.driver,"7.未登录首页.jpg")
        sleep(1)
        self.assertEqual(self.index.boolean(),False)
if __name__ == "__main__":
    unittest.main()