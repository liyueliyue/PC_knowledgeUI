from selenium import webdriver
from time import sleep

def browser():
    driver = webdriver.Chrome()
    return driver
if __name__ == "__main__":
    driver = browser()
    driver.get(r'https://m.qlchat.com/pc/knowledge-mall/index')
    # 右右小号cookies
    cookies = {'name': 'userId', 'value': '120000175327591'}
    cookies1 = {'name': 'QLZB_SESSIONID',
                'value': '46715072626C6A764D7631686F683641616E54472B2F6A3563657864626C652F6B73426D74544E2B504E413D'}
    driver.add_cookie(cookie_dict=cookies)
    driver.add_cookie(cookie_dict=cookies1)
    driver.refresh()
    driver.maximize_window()
    sleep(1)
    driver.close()