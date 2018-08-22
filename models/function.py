import sys, os
sys.path.append(r'./models')

def insert_img(driver,filename):
    # base_dir = os.path.abspath('.') 这个方法只适合在当前脚本使用，
    # 通过import 该方法需要使用下面的方法使用绝对路径否则截不了图片
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split(r'/models')[0]
    file_path = base + r'/test_report/image/' + filename
    driver.get_screenshot_as_file(file_path)

if __name__ == "__main__":
    from models.driver import browser
    from time import sleep

    driver = browser()
    driver.get(r'https://www.baidu.com/')
    sleep(1)
    insert_img(driver,'test.jpg')
    sleep(1)
    driver.quit()