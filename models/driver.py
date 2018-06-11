from selenium import webdriver
from time import sleep

def browser():
    driver = webdriver.Chrome()
    return driver
if __name__ == "__main__":
    driver = browser()
    driver.get(r'https://m.qlchat.com/wechat/page/topic-intro?topicId=2000001368645697')
    driver.implicitly_wait(5)
    cookies = {'name':'userId','value':'270000127243445'}
    cookies1 = {'name':'QLZB_SESSIONID','value':'4B6250526A505A5A2F3532506F6446537552357167336276646C79537151536631673449674E51637832413D'}

    driver.add_cookie(cookie_dict=cookies)
    driver.add_cookie(cookie_dict=cookies1)
    driver.refresh()
    sleep(1)
    driver.get(r'https://m.qlchat.com/pc/knowledge-mall/index')
    driver.maximize_window()
    sleep(1)
    driver.quit()