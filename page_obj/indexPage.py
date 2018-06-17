import sys
sys.path.append('./page_obj')
from page_obj.base import Page
from selenium.webdriver.common.by import By
from time import sleep

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
    nav_loc = (By.XPATH,'//*[@id="top"]/div[7]')                                     #右侧导航栏

    searchForm_loc = (By.XPATH,'//*[@id="top"]/div[1]/div/div[1]/div[3]/input')   # 搜索框
    click_searchButton_loc = (By.XPATH,'//*[@id="top"]/div[1]/div/div[1]/div[3]/i') # 点击搜索按钮
    get_searchText_loc = (By.XPATH,'//*[@id="main-content"]/div/div[2]')            # 搜索结果不存在文案
    get_searchResult_loc = (By.XPATH,'//*[@id="top"]/div[4]/div[1]/div/section/div[1]/h1') # 搜索结果中第一个课程标题

    # 未登录点击转载管理
    def click_relayManage(self):
        # sleep(1)
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
    # 点击全部tab的只看未转载课按钮
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
    # 是否显示“精品推荐”或“专属推荐模块”
    def boolean(self):
        # 生成一个list首先考虑列表生成式
        l = [i.text for i in self.wait_elements(*self.nav_loc)]
        j = "精品推荐"
        z = "专属推荐"
        return j in l[0] or z in l[0]
    # 搜索框
    def sendTextTosearchForm(self,text):
        self.wait_element(*self.searchForm_loc).clear()
        self.wait_element(*self.searchForm_loc).send_keys(text)
        self.wait_element(*self.click_searchButton_loc).click()
    # 获取搜索内容不存在的text
    def get_searchText(self):
        return self.wait_element(*self.get_searchText_loc).text
    # 判断搜索字段是否存在结果中
    def get_searchResult(self):
        text = self.wait_element(*self.get_searchResult_loc).text
        if '优惠' in text:
            return True
        else:
            return False
