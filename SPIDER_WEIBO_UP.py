from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def loginWeibo(username, password,url='https://passport.weibo.cn/signin/login',show=False,find_cookie=True):
    #默认展示关，寻找cookie开
    if show : driver = webdriver.Chrome()
    #这里需要更改为你的路径
    else:
        option=webdriver.ChromeOptions()
        option.add_argument('headless') # 设置option
        driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器    
    driver.get(url)
    print('正在加载界面....')
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginAction")))
    finally :
        driver.find_element_by_id("loginName").send_keys('b1821199691@163.com')
        driver.find_element_by_id("loginPassword").send_keys('cptbtptp12')
        driver.find_element_by_id("loginAction").click()
        print('已登录，正在获取cookie....')
    time.sleep(1)
#获取cookie
    if find_cookie:        
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "viewport")))
        finally :
            cookies = driver.get_cookies()
            cookie_list = []
            for dict in cookies:
                cookie = dict['name'] + '=' + dict['value']
                cookie_list.append(cookie)
            cookie = ';'.join(cookie_list)
            print('获取cookie成功')
    else : cookie=False
    driver.close()
    return cookie

if __name__ == '__main__':    
    cookie=loginWeibo('b1821199691@163.com','')
    print(cookie)
