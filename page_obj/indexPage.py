import sys
sys.path.append('./page_obj')
from page_obj.base import Page
from selenium.webdriver.common.by import By

class Index(Page):
    """商城首页"""
    relayManage_loc = (By.XPATH,'//*[@id="top"]/div[1]/div/div[2]/div[1]/a[2]')  # 转载管理按钮
    myDraw_loc = (By.XPATH,'//*[@id="top"]/div[1]/div/div[2]/div[1]/a[3]')       # 我的画像
    login_loc = (By.XPATH,'//*[@id="top"]/div[1]/div/div[2]/div[2]')              # 登录按钮
    salesBack_loc = (By.XPATH,'//*[@id="top"]/div[7]/div[4]')                      # 分销后台
    allTab_loc = (By.XPATH,'//*[@id="top"]/div[3]/div/ul/li[2]')                   # 全部tab
    norelay_loc = (By.XPATH,'//*[@id="top"]/div[3]/div[2]/div/span[5]/span[1]')  # 只看未转载课程
    thirdTab_loc = (By.XPATH,'//*[@id="top"]/div[3]/div[1]/ul/li[3]')              # 个人提升tab
    iframe_loc = (By.XPATH,'//*[@id="modal-content"]/span[8]/div/div[1]/div/div/div/iframe')  # 登录二维码iframe
    codeText_loc = (By.XPATH,'/html/body/div/div/div[1]')                            # 微信登录文本

    # 未登录点击转载管理
    def click_relayManage(self):
        self.wait_element(*self.relayManage_loc).click()
    # 未登录点击我的画像
    def click_myDraw(self):
        self.wait_element(*self.myDraw_loc).click()
    # 点击登录按钮
    def click_login(self):
        self.wait_element(*self.login_loc).click()
    # 点击分销后台
    def click_salesBack(self):
        self.wait_element(*self.salesBack_loc).click()
    # 点击全部tab的只看转载课按钮
    def click_norelay(self):
        self.wait_element(*self.allTab_loc).click()
        self.wait_element(*self.norelay_loc).click()
    # 点击个人提升tab的只看转载课按钮
    def click_norelay_(self):
        self.wait_element(*self.thirdTab_loc).click()
        self.wait_element(*self.norelay_loc).click()

    # 切换到iframe窗口,获取二维码的文案text，用于断言
    def get_codeText(self):
        self.switch_frame(self.wait_element(*self.iframe_loc))
        codeText = self.wait_element(*self.codeText_loc).text
        return codeText

