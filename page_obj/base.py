from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support.select import Select

class Page():
    """基础类，用于所有页面的继承"""
    topicUrl = r'https://m.qlchat.com/wechat/page/topic-intro?topicId=2000001368645697'
    pcknowledgeUrl = r'https://m.qlchat.com/pc/knowledge-mall/index'
    def __init__(self,driver,base_url=pcknowledgeUrl):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
    # def on_page(self):
    #     return self.driver.current_url == (self.base_url + self.url)
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        self.driver.maximize_window()
    # 打开PC知识通商城（未登录状态）
    def openNologin(self):
        self._open()
    def _openPc(self):
        self.driver.get(self.topicUrl)
        cookies = {'name': 'userId', 'value': '270000127243445'}
        cookies1 = {'name': 'QLZB_SESSIONID',
                    'value': '4B6250526A505A5A2F3532506F6446537552357167336276646C79537151536631673449674E51637832413D'}
        self.driver.add_cookie(cookie_dict=cookies)
        self.driver.add_cookie(cookie_dict=cookies1)
        self.driver.refresh()
        self.openNologin()
        self.driver.maximize_window()
    # 打开知识通商城（已登录）
    def openLogin(self):
        self._openPc()
    def find_element(self,*args):
        return self.driver.find_element(*args)
    def find_elements(self,*args):
        return self.driver.find_elements(*args)
    # 使用显示等待定位元素
    def wait_element(self,*args):
        return WebDriverWait(self.driver,10,0.5).until(lambda driver:self.find_element(*args))
    def wait_elements(self,*args):
        return WebDriverWait(self.driver,10,0.5).until(lambda driver:self.find_elements(*args))
    # 执行js
    def execute_js(self,src):
        return self.driver.execute_script(src)
    # 处理下拉框
    def select(self,e,number):
        return Select(e).select_by_index(number)
    # 获取警告框text
    def switch_alert(self):
        return self.driver.switch_to_alert().text
    # 多表单切换（src指定位后元素）
    def switch_frame(self,src):
        return self.driver.switch_to.frame(src)