import sys,os
sys.path.append(r'./models')

def insert_img(driver,filename):
    base_dir = os.path.abspath('.')
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split(r'/models')[0]
    file_path = base + r'/test_report/image/' + filename
    driver.get_screenshot_as_file(file_path)

if __name__ == "__main__":
    from models.driver import browser
    from time import sleep
    driver = browser()
    driver.get(r'https://m.qlchat.com/wechat/page/topic-intro?topicId=2000001368645697')
    driver.implicitly_wait(5)
    cookies = {'name':'userId','value':'270000127243445'}
    cookies1 = {'name':'QLZB_SESSIONID','value':'4B6250526A505A5A2F3532506F6446537552357167336276646C79537151536631673449674E51637832413D'}

    driver.add_cookie(cookie_dict=cookies)
    driver.add_cookie(cookie_dict=cookies1)
    driver.refresh()
    sleep(1)
    insert_img(driver,'topicTest.jpg')
    driver.get(r'https://m.qlchat.com/pc/knowledge-mall/index')
    driver.maximize_window()
    sleep(1)
    driver.quit()