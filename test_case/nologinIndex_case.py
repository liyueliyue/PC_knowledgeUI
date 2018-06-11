import unittest
from models.function import insert_img
from models.driver import browser
from page_obj.indexPage import Index
from time import sleep

class indexTest(unittest.TestCase):
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
        sleep(1)
if __name__ == "__main__":
    unittest.main()